# workato-qr CLI

Local Python CLI for generating QR code PNGs. Uses `qrcode[pil]` and `Pillow` — no external API calls, no stdlib-only constraints.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```
python qr_generator.py <url> [--color RRGGBB] [--output path.png]
```

| Argument | Default | Description |
|----------|---------|-------------|
| `url` | _(required)_ | URL or text to encode |
| `--color` | `000000` | Foreground color as a 6-char hex string (no `#`) |
| `--output` | `qrcode.png` | Output file path |

## Examples

```bash
# Black QR code (default)
python qr_generator.py https://workato.com

# Workato teal
python qr_generator.py https://workato.com --color 108291 --output workato.png

# Custom color + output path
python qr_generator.py https://example.com --color ff6600 --output /tmp/orange.png
```

## Notes

- Output is always PNG.
- Uses `ERROR_CORRECT_M` (15% redundancy), suitable for clean prints without a center logo.
- For the Workato-hosted version (no local dependencies), see `../workato/`.
