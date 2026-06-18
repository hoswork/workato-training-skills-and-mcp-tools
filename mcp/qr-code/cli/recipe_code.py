import io, base64, numpy as np
from PIL import Image

_LOGOS = {
    "workato-w-qr": "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",
}

PRESETS = {
    "workato": "#108291", "teal": "#108291",
    "dark": "#000000",    "black": "#000000",
    "white": "#ffffff",   "transparent": None,
}

def _parse_color(s):
    if s is None or str(s).strip().lower() in ("transparent","none",""): return None
    s = str(s).strip()
    mapped = PRESETS.get(s.lower(), s)
    if s.lower() in PRESETS and mapped is None: return None
    s = (mapped or s).lstrip("#")
    if len(s)==6: return (int(s[0:2],16),int(s[2:4],16),int(s[4:6],16),255)
    if len(s)==8: return (int(s[0:2],16),int(s[2:4],16),int(s[4:6],16),int(s[6:8],16))
    raise ValueError(f"Invalid color: {s!r}")

_EXP=[0]*512;_LOG=[0]*256;_x=1
for _i in range(255):
    _EXP[_i]=_x;_LOG[_x]=_i;_x=(_x<<1)^(0x11d if _x>127 else 0)
for _i in range(255,512): _EXP[_i]=_EXP[_i-255]

def _gf(a,b): return 0 if a==0 or b==0 else _EXP[_LOG[a]+_LOG[b]]
def _poly_mul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,pi in enumerate(p):
        for j,qj in enumerate(q): r[i+j]^=_gf(pi,qj)
    return r
def _rs_gen(n):
    g=[1]
    for i in range(n): g=_poly_mul(g,[1,_EXP[i]])
    return g
def _rs_enc(data,n):
    g=_rs_gen(n);rem=list(data)+[0]*n
    for i in range(len(data)):
        c=rem[i]
        if c:
            for j,gj in enumerate(g): rem[i+j]^=_gf(c,gj)
    return rem[len(data):]

_ECM={
    1:(16,10,1,16,0,0),2:(28,16,1,28,0,0),3:(44,26,1,44,0,0),
    4:(64,18,2,32,0,0),5:(86,24,2,43,0,0),6:(108,16,4,27,0,0),
    7:(124,18,4,31,0,0),8:(154,22,2,38,2,39),9:(182,22,3,36,2,37),
    10:(216,26,4,43,1,44),11:(254,30,1,50,4,51),12:(290,22,6,36,2,37),
    13:(334,22,8,37,1,38),14:(365,24,4,40,5,41),15:(415,24,5,41,5,42),
}
_ECH={
    1:(9,17,1,9,0,0),2:(16,28,1,16,0,0),3:(26,22,2,13,0,0),
    4:(36,16,4,9,0,0),5:(46,22,2,11,2,12),6:(60,28,4,15,0,0),
    7:(66,26,4,13,1,14),8:(86,26,4,14,2,15),9:(100,24,4,12,4,13),
    10:(122,28,6,15,2,16),
}
_ALIGN={
    1:[],2:[6,18],3:[6,22],4:[6,26],5:[6,30],6:[6,34],
    7:[6,22,38],8:[6,24,42],9:[6,26,46],10:[6,28,50],
    11:[6,30,54],12:[6,32,58],13:[6,34,62],14:[6,26,46,66],15:[6,26,48,70],
}
_REM={1:0,2:7,3:7,4:7,5:7,6:7,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:3,15:3}
_FMT_DIV=0b10100110111

def _fmt(mask_id,ec=0b01):
    raw=(ec<<3)|mask_id;rem=raw<<10
    for i in range(4,-1,-1):
        if rem&(1<<(i+10)): rem^=(_FMT_DIV<<i)
    return ((raw<<10)|(rem&0x3ff))^0b101010000010010

def _interleave(blocks):
    out=[];mx=max(len(b) for b in blocks)
    for i in range(mx):
        for b in blocks:
            if i<len(b): out.append(b[i])
    return out

def _encode(url_bytes,v,use_H):
    tbl=_ECH if use_H else _ECM;row=tbl[v];td,ne,bg1,cw1,bg2,cw2=row
    bits=[]
    def ab(val,n):
        for i in range(n-1,-1,-1): bits.append((val>>i)&1)
    ab(0b0100,4);ab(len(url_bytes),8)
    for b in url_bytes: ab(b,8)
    for _ in range(min(4,td*8-len(bits))): bits.append(0)
    while len(bits)%8: bits.append(0)
    pad=[0b11101100,0b00010001];pi=0
    while len(bits)<td*8: ab(pad[pi%2],8);pi+=1
    cws=[int("".join(map(str,bits[i*8:(i+1)*8])),2) for i in range(td)]
    pos=0;db=[];eb=[]
    for _ in range(bg1):
        bl=cws[pos:pos+cw1];pos+=cw1;db.append(bl);eb.append(_rs_enc(bl,ne))
    for _ in range(bg2):
        bl=cws[pos:pos+cw2];pos+=cw2;db.append(bl);eb.append(_rs_enc(bl,ne))
    final=_interleave(db)+_interleave(eb);rbits=[]
    for cw in final:
        for i in range(7,-1,-1): rbits.append((cw>>i)&1)
    rbits+=[0]*_REM.get(v,0);return rbits

def _matrix(v):
    """Return (M, F) where M=modules(-1=unset,0/1=set), F=reserved bool matrix."""
    sz=4*v+17
    M=np.full((sz,sz),-1,dtype=np.int8)
    F=np.zeros((sz,sz),dtype=bool)
    def pf(r,c,val): M[r,c]=val;F[r,c]=True

    # Finder patterns + separators
    def finder(row,col):
        for dr in range(7):
            for dc in range(7):
                pf(row+dr,col+dc,1 if(dr in(0,6) or dc in(0,6) or(1<dr<5 and 1<dc<5)) else 0)
        for i in range(8):
            if 0<=row+i<sz and col+7<sz and not F[row+i,col+7]: pf(row+i,col+7,0)
            if 0<=row+7<sz and col+i<sz and not F[row+7,col+i]: pf(row+7,col+i,0)
    finder(0,0);finder(0,sz-7);finder(sz-7,0)
    # Bottom-left finder TOP separator (row sz-8, cols 0-7)
    for i in range(8):
        if not F[sz-8,i]: pf(sz-8,i,0)
    # Top-right finder LEFT separator (col sz-8, rows 0-7)
    for i in range(8):
        if not F[i,sz-8]: pf(i,sz-8,0)

    # Alignment patterns (BEFORE timing so centers on timing rows/cols get placed correctly)
    als=_ALIGN.get(v,[])
    for ar in als:
        for ac in als:
            if F[ar,ac]: continue
            for dr in range(-2,3):
                for dc in range(-2,3):
                    pf(ar+dr,ac+dc,1 if(abs(dr)==2 or abs(dc)==2 or(dr==0 and dc==0)) else 0)

    # Timing patterns (AFTER alignment — overwrites alignment centers on timing lines)
    for i in range(8,sz-8):
        pf(6,i,1 if i%2==0 else 0)
        pf(i,6,1 if i%2==0 else 0)

    # Dark module
    pf(4*v+9,8,1)

    # Version information (versions 7+)
    if v >= 7:
        def _bch_ver(ver):
            g=0b1111100100101; d=ver<<12
            while d.bit_length()-g.bit_length()>=0: d^=g<<(d.bit_length()-g.bit_length())
            return (ver<<12)|d
        vbits=_bch_ver(v)
        for i in range(18):
            pf(i//3, i%3+(sz-11), (vbits>>i)&1)
            pf(i%3+(sz-11), i//3, (vbits>>i)&1)

    # Reserve format info positions (will be written later)
    fmt_positions_1=[(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,7),(8,8),
                     (7,8),(5,8),(4,8),(3,8),(2,8),(1,8),(0,8)]
    for r,c in fmt_positions_1: F[r,c]=True;M[r,c]=0
    for c in range(sz-8,sz): F[8,c]=True;M[8,c]=0
    for r in range(sz-7,sz): F[r,8]=True;M[r,8]=0
    # Dark module already reserved above
    F[sz-8,8]=True  # reserve dark module position explicitly

    return M,F

def _place_data(M,F,bits):
    sz=M.shape[0];bi=0;col=sz-1;up=True
    while col>=0:
        if col==6: col-=1
        cs=[col,col-1]
        rows=range(sz-1,-1,-1) if up else range(sz)
        for r in rows:
            for c in cs:
                if 0<=c<sz and not F[r,c] and M[r,c]==-1:
                    M[r,c]=bits[bi] if bi<len(bits) else 0;bi+=1
        up=not up;col-=2

_MASKS=[
    lambda r,c:(r+c)%2==0, lambda r,c:r%2==0,
    lambda r,c:c%3==0,     lambda r,c:(r+c)%3==0,
    lambda r,c:(r//2+c//3)%2==0, lambda r,c:(r*c)%2+(r*c)%3==0,
    lambda r,c:((r*c)%2+(r*c)%3)%2==0, lambda r,c:((r+c)%2+(r*c)%3)%2==0,
]

def _apply_mask(M,F,mid):
    fn=_MASKS[mid];sz=M.shape[0]
    for r in range(sz):
        for c in range(sz):
            if not F[r,c] and fn(r,c): M[r,c]^=1

def _write_fmt(M,mid,use_H):
    # EC level bits per QR spec: L=01, M=00, Q=11, H=10
    ec=0b10 if use_H else 0b00
    f=_fmt(mid,ec);sz=M.shape[0]
    fb=[(f>>i)&1 for i in range(14,-1,-1)]  # fb[0]=b14(MSB), fb[14]=b0(LSB)
    # First copy (around top-left finder)
    p1=[(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,7),(8,8),
        (7,8),(5,8),(4,8),(3,8),(2,8),(1,8),(0,8)]
    for i,(r,c) in enumerate(p1): M[r,c]=fb[i]
    # Second copy: upper right (row 8, cols sz-8..sz-1) - bits 7..0 (MSB-to-LSB order)
    for i,c in enumerate(range(sz-8,sz)): M[8,c]=fb[7+i]
    # Second copy: lower left (col 8, rows sz-7..sz-1) - bits 8..14 (MSB-to-LSB order)
    for i,r in enumerate(range(sz-7,sz)): M[r,8]=fb[6-i]

def _penalty(M):
    sz=M.shape[0];p=0
    for row in M:
        run=1
        for i in range(1,sz):
            if row[i]==row[i-1]: run+=1
            else:
                if run>=5: p+=run-2
                run=1
        if run>=5: p+=run-2
    for col in M.T:
        run=1
        for i in range(1,sz):
            if col[i]==col[i-1]: run+=1
            else:
                if run>=5: p+=run-2
                run=1
        if run>=5: p+=run-2
    for r in range(sz-1):
        for c in range(sz-1):
            v=M[r,c]
            if v==M[r+1,c]==M[r,c+1]==M[r+1,c+1]: p+=3
    return p

def _qr_matrix(url,use_H=False):
    data=url.encode("utf-8")
    tbl=_ECH if use_H else _ECM
    v=next((i for i in sorted(tbl) if len(data)<=tbl[i][0]),None)
    if v is None: raise ValueError(f"URL too long ({len(data)} bytes)")
    bits=_encode(data,v,use_H)
    best=None;bp=float("inf")
    for mid in range(8):
        Mt,Ft=_matrix(v)
        _place_data(Mt,Ft,bits)
        _apply_mask(Mt,Ft,mid)   # ← only masks data modules now
        _write_fmt(Mt,mid,use_H)  # ← write format info AFTER masking
        pen=_penalty(Mt)
        if pen<bp: bp=pen;best=Mt.copy()
    return best

def _colorize_logo(logo_bytes,fg,bg):
    img=Image.open(io.BytesIO(logo_bytes)).convert("RGBA")
    arr=np.array(img,dtype=np.uint16)
    r,g,b,a=arr[...,0],arr[...,1],arr[...,2],arr[...,3]
    ink=(a>30)&((r+g+b)<600)
    out=np.zeros_like(arr)
    out[ink,0]=fg[0];out[ink,1]=fg[1];out[ink,2]=fg[2];out[ink,3]=255
    if bg is not None:
        out[~ink,0]=bg[0];out[~ink,1]=bg[1];out[~ink,2]=bg[2]
        out[~ink,3]=bg[3] if len(bg)>3 else 255
    else:
        out[~ink,3]=0
    result=Image.fromarray(out.astype(np.uint8),"RGBA")
    # Crop to active (ink) pixel bounding box so sizing is based on content not canvas
    bbox=result.getbbox()
    if bbox: result=result.crop(bbox)
    return result

def _render(M,fg,bg,logo_bytes=None,module_px=10,border=4):
    sz=M.shape[0];total=(sz+2*border)*module_px
    canvas_bg=bg if bg is not None else (0,0,0,0)
    img=Image.new("RGBA",(total,total),canvas_bg)
    px=img.load()
    for r in range(sz):
        for c in range(sz):
            if M[r,c]==1:
                for dr in range(module_px):
                    for dc in range(module_px):
                        px[(border+c)*module_px+dc,(border+r)*module_px+dr]=fg
    if logo_bytes:
        logo=_colorize_logo(logo_bytes,fg,bg)
        max_l=int(total*0.30);logo.thumbnail((max_l,max_l),Image.LANCZOS)
        lw,lh=logo.size
        mod=module_px;pad=mod
        bw=(-(-(lw+pad*2)//mod))*mod;bh=(-(-(lh+pad*2)//mod))*mod
        bl=((total-bw)//2)//mod*mod;bt=((total-bh)//2)//mod*mod
        bg_c=bg if bg is not None else (255,255,255,255)
        img.paste(Image.new("RGBA",(bw,bh),bg_c),(bl,bt))
        # Center logo within the background patch (not the image)
        lx=bl+(bw-lw)//2;ly=bt+(bh-lh)//2
        img.paste(logo,(lx,ly),logo)
    buf=io.BytesIO();img.save(buf,format="PNG");return buf.getvalue()

def main(input):
    url=(input.get("url") or "").strip()
    if not url: raise ValueError("url is required")
    fg_str=(input.get("fg_color") or "workato").strip()
    bg_str=(input.get("bg_color") or "white").strip()
    fg=_parse_color(fg_str)
    if fg is None: fg=(16,130,145,255)
    bg=_parse_color(bg_str)
    logo_name="workato-w-qr"
    logo_bytes=None
    if logo_name in _LOGOS:
        logo_bytes=base64.b64decode(_LOGOS[logo_name])
    use_H=logo_bytes is not None
    M=_qr_matrix(url,use_H)
    png=_render(M,fg,bg,logo_bytes)
    sz=(M.shape[0]+8)*10
    return {"image_base64":base64.b64encode(png).decode("ascii"),
            "mime_type":"image/png","width":sz,"height":sz,"url":url}
