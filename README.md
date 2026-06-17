# workato-qr

QR code generator with two deployment targets:

## cli/ — local Python CLI

Uses `qrcode[pil]` + `Pillow`. Generates QR codes locally.

```bash
pip install -r cli/requirements.txt
python cli/qr_generator.py <url> [--color RRGGBB] [--output path.png]
```

## workato/ — Workato RCLM project

Skill recipe + MCP server hosted on Workato trial workspace.

- **Skill**: `generate_qr_code` (url, optional color → base64 PNG)
- **MCP server**: `workato-qr-mcp`
- Uses `api.qrserver.com` via `urllib` (stdlib only — no Pillow needed)

### MCP usage

Connect to: `https://2581.apim.mcp.trial.workato.com?wkt_token=<token>`

**Tool**: `generate_qr_code`

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `url` | string | yes | URL or text to encode |
| `color` | string | no | Hex color without `#` (default: `000000`) |

**Returns**: JSON text with `image_base64`, `mime_type`, `width`, `height`, `url`

> Note: result is nested as `content[0].text` → `JSON.parse` → `.result.image_base64`
