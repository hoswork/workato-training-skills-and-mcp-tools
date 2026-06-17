# workato-qr

QR code generator with Workato W logo. Two deployment targets:

## Architecture

```
URL + color params
      ↓
generate_qr_code (Workato Skill)
      ↓
  py_eval step: pure Python QR matrix generation
  - GF(256) Reed-Solomon error correction
  - EC level H (30% redundancy) when logo is present
  - Workato W logo embedded as base64, colorized to match fg_color
  - Pillow (v11.3.0, available in Workato Python sandbox) for rendering
  - No external API calls — fully self-contained
      ↓
  Returns: { image_base64, mime_type, width, height, url }
      ↓
workato-qr-mcp (Workato MCP Server)
  Exposes generate_qr_code as an MCP tool
  Returns: content[0].text → JSON.parse → .result.image_base64
```

## Deployments

### cli/ — local Python CLI
Uses `qrcode[pil]` + Pillow for local generation (libraries not available in Workato sandbox).

```bash
cd cli
pip install -r requirements.txt
python qr_generator.py https://workato.com
python qr_generator.py https://workato.com --color 108291 --output my-qr.png
```

### workato/ — Workato RCLM project
Workato Skill + MCP Server on trial workspace. Pure Python implementation using only libraries available in Workato's `py_eval` step: `numpy`, `Pillow`.

**Key design choices:**
- No external QR API — generates matrix using pure Python + numpy (Reed-Solomon, alignment, timing, version info)
- Logo registry in Python dict — add logos by updating the `_LOGOS` dict in the recipe and pushing via CLI
- EC level H with logo (30% error correction) — allows ~25% logo coverage
- `workato push` is authoritative over cloud — always edit JSON locally, push, then pull to verify

## Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `url` | string | required | URL to encode |
| `fg_color` | string | `"workato"` | Foreground color. Presets: `workato` (#108291), `dark`/`black`, `white`. Or any hex (`#ff6600`). |
| `bg_color` | string | `"white"` | Background color. Same presets + `"transparent"`. |

## MCP usage

```
Endpoint: https://2581.apim.mcp.trial.workato.com?wkt_token=<token>
Tool: generate_qr_code
Response: content[0].text → JSON.parse → .result
```

Token is in the Workato MCP server settings. The result is double-wrapped (Workato MCP behavior): `JSON.parse(content[0].text).result.image_base64`.

## Reliability

Tested against 27 combinations (9 URLs × 3 colors) using `zbarimg`. All pass. URL coverage: v3 through v8 EC-H (19-71 bytes). See `cli/recipe_code.py` for the full test suite.

## Operations

```bash
# Deploy
cd workato/ && workato push --restart-recipes

# Sync after UI changes  
cd workato/ && workato pull

# Add a logo
# 1. Add base64 PNG to _LOGOS dict in cli/recipe_code.py
# 2. Copy code to recipe JSON: python3 -c "import json; ..."
# 3. workato push --restart-recipes
```
