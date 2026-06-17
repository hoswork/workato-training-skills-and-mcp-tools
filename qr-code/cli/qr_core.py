"""
Pure Python QR code generator for Workato py_eval.
Dependencies: numpy, Pillow (both available in Workato Python action).
No external libraries or network calls.
"""
from __future__ import annotations
import io, base64, struct
import numpy as np
from PIL import Image

# ─── Color presets ─────────────────────────────────────────────────────────
PRESETS = {
    'workato': '#108291', 'teal': '#108291',
    'dark': '#000000',    'black': '#000000',
    'white': '#ffffff',   'transparent': None,
}

def parse_color(s):
    """Return RGBA tuple or None (transparent)."""
    if s is None or str(s).strip().lower() in ('transparent', 'none', ''):
        return None
    s = str(s).strip()
    mapped = PRESETS.get(s.lower())
    if mapped is None and s.lower() in PRESETS:
        return None  # preset explicitly maps to transparent
    s = mapped if mapped is not None else s
    s = s.lstrip('#')
    if len(s) == 6:
        return (int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16), 255)
    if len(s) == 8:
        return (int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16), int(s[6:8], 16))
    raise ValueError(f'Invalid color: {s!r}')

# ─── GF(256) for Reed-Solomon ──────────────────────────────────────────────
_EXP = [0] * 512
_LOG = [0] * 256
_x = 1
for _i in range(255):
    _EXP[_i] = _x
    _LOG[_x] = _i
    _x = (_x << 1) ^ (0x11d if _x > 127 else 0)
for _i in range(255, 512):
    _EXP[_i] = _EXP[_i - 255]

def _gf_mul(a, b):
    return 0 if (a == 0 or b == 0) else _EXP[_LOG[a] + _LOG[b]]

def _gf_poly_mul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, pi in enumerate(p):
        for j, qj in enumerate(q):
            r[i + j] ^= _gf_mul(pi, qj)
    return r

def _rs_generator(n):
    g = [1]
    for i in range(n):
        g = _gf_poly_mul(g, [1, _EXP[i]])
    return g

def _rs_encode(data, n_ec):
    gen = _rs_generator(n_ec)
    rem = list(data) + [0] * n_ec
    for i in range(len(data)):
        c = rem[i]
        if c:
            for j, g in enumerate(gen):
                rem[i + j] ^= _gf_mul(c, g)
    return rem[len(data):]

# ─── QR version tables (EC level M) ──────────────────────────────────────
# Format: [(data_bytes, ec_cw, blocks_g1, cw_g1, blocks_g2, cw_g2)]
# ec_cw = EC codewords per block
_EC_M = {
    1:  (16,  10, 1, 16, 0,  0),
    2:  (28,  16, 1, 28, 0,  0),
    3:  (44,  26, 2, 22, 0,  0),
    4:  (64,  18, 2, 32, 0,  0),
    5:  (86,  24, 2, 43, 0,  0),
    6:  (108, 16, 4, 27, 0,  0),
    7:  (124, 18, 4, 31, 0,  0),
    8:  (154, 22, 2, 38, 2, 39),
    9:  (182, 22, 3, 36, 2, 37),
    10: (216, 26, 4, 43, 1, 44),
    11: (254, 30, 1, 50, 4, 51),
    12: (290, 22, 6, 36, 2, 37),
    13: (334, 22, 8, 37, 1, 38),
    14: (365, 24, 4, 40, 5, 41),
    15: (415, 24, 5, 41, 5, 42),
}
# EC level H (for when logo is present — 30% redundancy)
_EC_H = {
    1:  (7,   17, 1,  7, 0,  0),
    2:  (14,  28, 1, 14, 0,  0),
    3:  (11,  22, 2, 11, 0,  0),
    4:  (25,  16, 4,  9, 0,  0),  # actually 4 blocks
    5:  (25,  22, 2, 11, 2, 12),
    6:  (36,  28, 4,  9, 0,  0),
    7:  (46,  26, 4, 10, 1, 11),
    8:  (60,  26, 4, 10, 2, 11),
    9:  (74,  24, 4, 10, 4, 11),  # adjusted
    10: (85,  28, 6, 10, 2, 11),
}

_ALIGNMENT = {
    1: [], 2: [6,18], 3: [6,22], 4: [6,26], 5: [6,30],
    6: [6,34], 7: [6,22,38], 8: [6,24,42], 9: [6,26,46], 10: [6,28,50],
    11:[6,30,54], 12:[6,32,58], 13:[6,34,62], 14:[6,26,46,66],
    15:[6,26,48,70],
}

_FORMAT_DIVISOR = 0b10100110111

def _format_string(data_mask, ec_indicator=0b01):  # 01 = level M
    raw = (ec_indicator << 3) | data_mask
    rem = raw << 10
    for _ in range(10):
        if rem & (1 << (14 - _)):
            rem ^= (_FORMAT_DIVISOR << (4 - _))
    masked = (raw << 10 | (rem & 0x3ff)) ^ 0b101010000010010
    return masked


def _interleave(blocks):
    result = []
    max_len = max(len(b) for b in blocks)
    for i in range(max_len):
        for b in blocks:
            if i < len(b):
                result.append(b[i])
    return result


def _encode_data(url_bytes, version, use_H=False):
    """Encode data codewords for given version."""
    tbl = _EC_H if use_H else _EC_M
    row = tbl[version]
    total_data = row[0]
    n_ec = row[1]
    bg1, cw1, bg2, cw2 = row[2], row[3], row[4], row[5]

    # Build data bitstream: byte mode
    bits = []
    def add_bits(val, n):
        for i in range(n-1, -1, -1):
            bits.append((val >> i) & 1)

    add_bits(0b0100, 4)          # byte mode indicator
    add_bits(len(url_bytes), 8)  # character count
    for b in url_bytes:
        add_bits(b, 8)

    # Terminator
    for _ in range(min(4, total_data * 8 - len(bits))):
        bits.append(0)
    # Byte-align
    while len(bits) % 8:
        bits.append(0)
    # Pad codewords
    pad = [0b11101100, 0b00010001]
    pi = 0
    while len(bits) < total_data * 8:
        add_bits(pad[pi % 2], 8)
        pi += 1

    data_cw = [int(''.join(map(str, bits[i*8:(i+1)*8])), 2) for i in range(total_data)]

    # Split into blocks and apply RS
    pos = 0
    data_blocks, ec_blocks = [], []
    for _ in range(bg1):
        block = data_cw[pos:pos+cw1]; pos += cw1
        data_blocks.append(block)
        ec_blocks.append(_rs_encode(block, n_ec))
    for _ in range(bg2):
        block = data_cw[pos:pos+cw2]; pos += cw2
        data_blocks.append(block)
        ec_blocks.append(_rs_encode(block, n_ec))

    final = _interleave(data_blocks) + _interleave(ec_blocks)
    # Add remainder bits
    rem = {1:0,2:7,3:7,4:7,5:7,6:7,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:3,15:3}
    result_bits = []
    for cw in final:
        for i in range(7,-1,-1):
            result_bits.append((cw >> i) & 1)
    result_bits += [0] * rem.get(version, 0)
    return result_bits


def _build_matrix(version):
    size = 4 * version + 17
    M = np.full((size, size), -1, dtype=np.int8)  # -1 = unset

    def place(r, c, v):
        M[r, c] = v

    # Finder patterns + separators
    def finder(row, col):
        for dr in range(7):
            for dc in range(7):
                on = (dr in (0,6) or dc in (0,6) or (1<dr<5 and 1<dc<5))
                place(row+dr, col+dc, 1 if on else 0)
        # Separator
        for i in range(8):
            if 0 <= row+i < size and col+7 < size:
                if M[row+i, col+7] == -1: place(row+i, col+7, 0)
            if 0 <= row+7 < size and col+i < size:
                if M[row+7, col+i] == -1: place(row+7, col+i, 0)

    finder(0, 0); finder(0, size-7); finder(size-7, 0)
    # Bottom-left separator extra
    for i in range(8):
        if M[size-8, i] == -1: place(size-8, i, 0)

    # Timing
    for i in range(8, size-8):
        if M[6,i] == -1: place(6, i, 1 if i%2==0 else 0)
        if M[i,6] == -1: place(i, 6, 1 if i%2==0 else 0)

    # Dark module
    place(4*version+9, 8, 1)

    # Alignment patterns
    aligns = _ALIGNMENT.get(version, [])
    for ar in aligns:
        for ac in aligns:
            if M[ar,ac] != -1: continue
            for dr in range(-2,3):
                for dc in range(-2,3):
                    on = (abs(dr)==2 or abs(dc)==2 or (dr==0 and dc==0))
                    place(ar+dr, ac+dc, 1 if on else 0)

    # Format info placeholders (set to 0 for now)
    fmt_pos = [(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,7),(8,8),
               (7,8),(5,8),(4,8),(3,8),(2,8),(1,8),(0,8)]
    for r,c in fmt_pos:
        if M[r,c] == -1: place(r,c,0)
    for i,c in enumerate(range(size-8,size)):
        if M[8,c] == -1: place(8,c,0)
    for i,r in enumerate(range(size-7,size)):
        if M[r,8] == -1: place(r,8,0)

    return M


def _place_data(M, bits):
    size = M.shape[0]
    bit_idx = 0
    col = size - 1
    going_up = True
    while col >= 0:
        if col == 6: col -= 1
        cols = [col, col-1]
        rows = range(size-1, -1, -1) if going_up else range(size)
        for r in rows:
            for c in cols:
                if 0 <= c < size and M[r,c] == -1:
                    if bit_idx < len(bits):
                        M[r,c] = bits[bit_idx]
                        bit_idx += 1
                    else:
                        M[r,c] = 0
        going_up = not going_up
        col -= 2


def _apply_mask(M, mask_id):
    size = M.shape[0]
    masks = [
        lambda r,c: (r+c)%2==0,
        lambda r,c: r%2==0,
        lambda r,c: c%3==0,
        lambda r,c: (r+c)%3==0,
        lambda r,c: (r//2+c//3)%2==0,
        lambda r,c: (r*c)%2+(r*c)%3==0,
        lambda r,c: ((r*c)%2+(r*c)%3)%2==0,
        lambda r,c: ((r+c)%2+(r*c)%3)%2==0,
    ]
    fn = masks[mask_id]
    for r in range(size):
        for c in range(size):
            if M[r,c] in (0,1):  # data module (not reserved)
                if fn(r,c):
                    M[r,c] ^= 1


def _write_format(M, mask_id, ec='M'):
    ec_bits = {'M': 0b01, 'H': 0b10}[ec]
    fmt = _format_string(mask_id, ec_bits)
    size = M.shape[0]
    fmt_bits = [(fmt >> i) & 1 for i in range(14,-1,-1)]
    pos1 = [(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,7),(8,8),
            (7,8),(5,8),(4,8),(3,8),(2,8),(1,8),(0,8)]
    for i,(r,c) in enumerate(pos1):
        M[r,c] = fmt_bits[i]
    pos2_r = [(8,size-1),(8,size-2),(8,size-3),(8,size-4),(8,size-5),
              (8,size-6),(8,size-7),(size-8,8)]
    pos2_c = [(size-7,8),(size-6,8),(size-5,8),(size-4,8),(size-3,8),
              (size-2,8),(size-1,8)]
    for i,(r,c) in enumerate(pos2_r[:8]):
        M[r,c] = fmt_bits[i]
    for i,(r,c) in enumerate(pos2_c):
        M[r,c] = fmt_bits[8+i]


def _penalty(M):
    size = M.shape[0]
    p = 0
    # Rule 1: 5+ same in a row/col
    for row in range(size):
        for start in range(size-4):
            run = 1
            while start+run < size and M[row,start+run]==M[row,start]: run+=1
            if run >= 5: p += run-2
    for col in range(size):
        for start in range(size-4):
            run = 1
            while start+run < size and M[start+run,col]==M[start,col]: run+=1
            if run >= 5: p += run-2
    # Rule 2: 2x2 blocks
    for r in range(size-1):
        for c in range(size-1):
            v = M[r,c]
            if v==M[r+1,c]==M[r,c+1]==M[r+1,c+1]: p += 3
    return p


def generate_qr_matrix(url: str, with_logo: bool = False):
    """Return QR matrix (numpy array, 1=dark, 0=light) for given URL."""
    data = url.encode('utf-8')
    use_H = with_logo

    # Find minimum version
    tbl = _EC_H if use_H else _EC_M
    version = None
    for v in sorted(tbl.keys()):
        if len(data) <= tbl[v][0]:
            version = v
            break
    if version is None:
        raise ValueError(f'URL too long ({len(data)} bytes) for supported versions')

    bits = _encode_data(data, version, use_H)

    # Try all 8 masks, pick best
    best_M, best_pen = None, float('inf')
    for mask_id in range(8):
        M = _build_matrix(version)
        _place_data(M, bits)
        _apply_mask(M, mask_id)
        _write_format(M, mask_id, 'H' if use_H else 'M')
        pen = _penalty(M)
        if pen < best_pen:
            best_pen = pen
            best_M = M.copy()

    return best_M


def colorize_logo(logo_bytes: bytes, fg_color: tuple, bg_color: tuple | None) -> Image.Image:
    """Recolor logo: transparent/white pixels → bg, colored pixels → fg."""
    img = Image.open(io.BytesIO(logo_bytes)).convert('RGBA')
    data = np.array(img, dtype=np.uint16)
    r, g, b, a = data[...,0], data[...,1], data[...,2], data[...,3]

    # Determine which pixels are "ink" (dark, non-transparent)
    is_ink = (a > 30) & ((r + g + b) < 600)

    out = np.zeros_like(data)
    # Ink pixels → fg_color
    out[is_ink, 0] = fg_color[0]
    out[is_ink, 1] = fg_color[1]
    out[is_ink, 2] = fg_color[2]
    out[is_ink, 3] = 255
    # Non-ink pixels
    if bg_color is not None:
        out[~is_ink, 0] = bg_color[0]
        out[~is_ink, 1] = bg_color[1]
        out[~is_ink, 2] = bg_color[2]
        out[~is_ink, 3] = bg_color[3] if len(bg_color) > 3 else 255
    else:
        out[~is_ink, 3] = 0  # transparent

    return Image.fromarray(out.astype(np.uint8), 'RGBA')


def render_qr(matrix, fg_color_rgba, bg_color_rgba, logo_bytes=None, module_px=10, border=4):
    """Render QR matrix to PNG bytes using Pillow."""
    size = matrix.shape[0]
    total = (size + 2 * border) * module_px
    mode = 'RGBA' if (bg_color_rgba is None or (len(bg_color_rgba) > 3 and bg_color_rgba[3] < 255)) else 'RGBA'
    bg = bg_color_rgba if bg_color_rgba is not None else (0, 0, 0, 0)
    img = Image.new('RGBA', (total, total), bg)
    pixels = img.load()

    for r in range(size):
        for c in range(size):
            if matrix[r, c] == 1:
                for dr in range(module_px):
                    for dc in range(module_px):
                        px = (border + c) * module_px + dc
                        py = (border + r) * module_px + dr
                        pixels[px, py] = fg_color_rgba

    if logo_bytes is not None:
        logo = colorize_logo(logo_bytes, fg_color_rgba, bg_color_rgba)
        max_logo = int(total * 0.25)
        logo.thumbnail((max_logo, max_logo), Image.LANCZOS)
        lw, lh = logo.size
        lx = (total - lw) // 2
        ly = (total - lh) // 2
        # White/bg clearance behind logo
        module = module_px
        pad = module
        bg_w = -(-(lw + pad*2) // module) * module
        bg_h = -(-(lh + pad*2) // module) * module
        bl = ((total - bg_w) // 2) // module * module
        bt = ((total - bg_h) // 2) // module * module
        bg_patch = Image.new('RGBA', (bg_w, bg_h), bg if bg_color_rgba is not None else (255,255,255,255))
        img.paste(bg_patch, (bl, bt))
        img.paste(logo, (lx, ly), logo)

    buf = io.BytesIO()
    img.save(buf, format='PNG')
    return buf.getvalue()
