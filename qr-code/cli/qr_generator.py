"""QR code generator — local CLI using qrcode[pil] and Pillow.

Usage:
    python qr_generator.py <url> [--color RRGGBB] [--output path.png]

Defaults:
    color  : 000000 (black)
    output : qrcode.png
"""

from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path

import qrcode
from PIL import Image


def generate_qr_bytes(
    url: str,
    color: str = "000000",
    box_size: int = 10,
    border: int = 4,
) -> bytes:
    """Generate a QR code PNG as bytes.

    Args:
        url:      The URL or text to encode.
        color:    Foreground color as a 6-char hex string (no leading #).
        box_size: Pixel size of each module (box).
        border:   Number of module-width quiet-zone boxes around the QR.

    Returns:
        Raw PNG bytes.
    """
    fill_color = f"#{color}"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color="white").convert("RGBA")

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def generate_qr(
    url: str,
    output: Path,
    color: str = "000000",
    box_size: int = 10,
    border: int = 4,
) -> Path:
    """Generate a QR code PNG and write it to disk.

    Args:
        url:      The URL or text to encode.
        output:   Destination file path.
        color:    Foreground color as a 6-char hex string (no leading #).
        box_size: Pixel size of each module.
        border:   Quiet-zone width in modules.

    Returns:
        The resolved output path.
    """
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    png_bytes = generate_qr_bytes(url, color=color, box_size=box_size, border=border)
    output.write_bytes(png_bytes)
    return output


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a QR code PNG from a URL.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  python qr_generator.py https://workato.com
  python qr_generator.py https://workato.com --color 108291 --output workato.png
""",
    )
    parser.add_argument("url", help="URL or text to encode in the QR code")
    parser.add_argument(
        "--color",
        default="000000",
        metavar="RRGGBB",
        help="Foreground color as a 6-char hex string without '#' (default: 000000)",
    )
    parser.add_argument(
        "--output",
        default="qrcode.png",
        metavar="PATH",
        help="Output file path (default: qrcode.png)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)

    # Validate hex color
    color = args.color.lstrip("#")
    if len(color) != 6 or not all(c in "0123456789abcdefABCDEF" for c in color):
        print(f"Error: --color must be a 6-char hex string (e.g. 108291), got: {args.color!r}", file=sys.stderr)
        return 1

    output_path = generate_qr(args.url, Path(args.output), color=color)
    print(f"QR code written to: {output_path.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
