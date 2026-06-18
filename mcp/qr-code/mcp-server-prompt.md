# qr-code MCP — server prompt and tool descriptions

## Server description
> Workato-branded QR code generator. Generates PNG QR codes with the Workato W logo centered. Returns base64-encoded PNG.

## Tool: generate_qr_code
> Generate a Workato-branded QR code as a base64 PNG. EC level H (30% error correction) with centered Workato W logo. fg_color controls both QR modules and logo color — presets: workato (#108291 teal), dark, black, white, or any hex #rrggbb. bg_color presets: white, transparent, or hex. Returns image_base64 (PNG), mime_type, width, height, url.
