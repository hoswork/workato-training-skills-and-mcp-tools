# workato-qr — Claude context

QR code generator: Workato Skill + MCP Server on the trial workspace, plus a local Python CLI.

## Repo structure

```
workato-qr/
  cli/
    qr_generator.py     — standalone CLI (uses qrcode[pil] + Pillow, local only)
    recipe_code.py      — THE SOURCE OF TRUTH for the Workato Python implementation
    requirements.txt
  workato/              — RCLM project (push/pull via Workato platform CLI)
    workato-qr/
      generate_qr_code.recipe.json
      generate_qr_code.agentic_skill.json
      workato_qr_mcp.mcp_server.json
      project.json
```

## Authoritative facts

| Resource | Value |
|---|---|
| Trial workspace | id `2100000234` |
| Project | `workato-qr` id `28820`, folder `42011` |
| Recipe | `generate_qr_code` id `277230` |
| Skill | id `skl-AaXQmwN6-MBemcL-AB` |
| MCP server | id `mcps-AaXQnHFM-aLA-AB` |
| MCP URL | `https://2581.apim.mcp.trial.workato.com` |
| Dev API auth | `jq -r '.mcpServers["workato-dev-api"].env.AUTH_HEADER' ~/.mcp.json` |

The MCP server `wkt_token` is NOT in the local JSON — fetch it via:
```bash
AUTH=$(jq -r '.mcpServers["workato-dev-api"].env.AUTH_HEADER' ~/.mcp.json)
curl -s -H "Authorization: $AUTH" \
  "https://app.trial.workato.com/api/mcp/mcp_servers/mcps-AaXQnHFM-aLA-AB" | jq -r '.data.mcp_url'
```

## Infra-as-code rule

**`workato push` is authoritative.** It overwrites cloud with local file values. Always:
1. Edit local files
2. `workato push --restart-recipes`
3. `workato pull` to verify sync

## Full push workflow (step by step)

### When you change the Python QR code

1. Edit `cli/recipe_code.py` — this is the source of truth
2. Copy the Python code into the recipe JSON:
```bash
python3 << 'EOF'
import json
with open('cli/recipe_code.py') as f:
    code = f.read()
with open('workato/workato-qr/generate_qr_code.recipe.json') as f:
    r = json.load(f)
for step in r['code']['block']:
    if step.get('provider') == 'py_eval':
        step['input']['code'] = code
        break
with open('workato/workato-qr/generate_qr_code.recipe.json', 'w') as f:
    json.dump(r, f, indent=2)
print("Updated")
EOF
```
3. Push:
```bash
cd workato && workato push --restart-recipes
```
4. Pull to sync:
```bash
workato pull
```
5. **Re-assign the skill to the MCP server** (see below — required after every push)

### When you change the skill schema (parameters)

Edit `parameters_schema_json` in the recipe trigger AND the corresponding `code_input.schema` in the Python step. Both must stay in sync.

### When you change the MCP server description or tool description

The platform CLI does NOT apply `tools[].description` changes from `workato_qr_mcp.mcp_server.json`. You must update via Dev API after every push.

## Post-push: re-assign skill to MCP server

**This must be run after every `workato push`.** The push updates the recipe and skill but does NOT maintain the tool assignment or description on the MCP server.

```bash
AUTH=$(jq -r '.mcpServers["workato-dev-api"].env.AUTH_HEADER' ~/.mcp.json)

TOOL_DESC="Generate a Workato-branded QR code as a base64 PNG. EC level H (30% error correction) with centered Workato W logo. fg_color controls both QR modules and logo color — presets: workato (#108291 teal), dark, black, white, or any hex #rrggbb. bg_color presets: white, transparent, or hex. Returns image_base64 (PNG), mime_type, width, height, url."

curl -s -X POST -H "Authorization: $AUTH" \
  -H "Content-Type: application/json" \
  -d "{
    \"tools\": [{
      \"id\": \"skl-AaXQmwN6-MBemcL-AB\",
      \"trigger_application\": \"workato_skill\",
      \"description\": \"${TOOL_DESC}\"
    }]
  }" \
  "https://app.trial.workato.com/api/mcp/mcp_servers/mcps-AaXQnHFM-aLA-AB/assign_tools" | jq '.data.tools_count'
# Should return 1
```

## Testing the MCP server

```bash
# Get the current wkt_token
TOKEN=$(curl -s -H "Authorization: $AUTH" \
  "https://app.trial.workato.com/api/mcp/mcp_servers/mcps-AaXQnHFM-aLA-AB" | jq -r '.data.mcp_url | split("wkt_token=")[1]')

# List tools (verify description is set)
curl -sk -X POST "https://2581.apim.mcp.trial.workato.com?wkt_token=${TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}' | jq '.result.tools[] | {name, description}'

# Generate a QR code
curl -sk -X POST "https://2581.apim.mcp.trial.workato.com?wkt_token=${TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"generate_qr_code","arguments":{"url":"https://workato.com","fg_color":"workato","bg_color":"white"}}}' \
  | python3 -c "
import sys,json,base64
d=json.load(sys.stdin)
r=json.loads(d['result']['content'][0]['text'])['result']
print('size:', r['width'],'x', r['height'], '| PNG bytes:', len(base64.b64decode(r['image_base64'])))
"
```

Note: the MCP response is double-wrapped. To get the image:
```python
data = json.loads(response['result']['content'][0]['text'])['result']
image_bytes = base64.b64decode(data['image_base64'])
```

## Adding a logo

To add a new logo variant to the `_LOGOS` dict:
1. Encode the PNG: `python3 -c "import base64; print(base64.b64encode(open('logo.png','rb').read()).decode())"`
2. Add to `_LOGOS` in `cli/recipe_code.py`: `"my-logo": "<base64 string>"`
3. In `main()`, change `logo_name = "workato-w-qr"` to `"my-logo"` (or accept it as a parameter)
4. Follow the full push workflow above

## Required tools for managing this project

Both of these must be available:

1. **Workato platform CLI** (`workato`) — push/pull the RCLM project (recipes, skills, MCP server config)
2. **Workato Dev API MCP** (`mcp__workato-dev-api__*`) — set MCP tool descriptions, re-assign skills, check recipe status, manage the MCP server post-push

The platform CLI handles the code (recipe, skill schema, Python). The Dev API MCP handles the operational wiring that the CLI doesn't fully manage (tool assignment, tool descriptions on the live MCP server).

Dev API auth is always: `jq -r '.mcpServers["workato-dev-api"].env.AUTH_HEADER' ~/.mcp.json`

**AVOID** `mcp__workato-dev-api__post_api_collections_api_endpoints` — it has a broken JSON Schema that poisons the MCP tool list for the entire session. Other tools in that namespace are safe.

## Known platform CLI gaps

- **`workato push` does NOT apply `tools[].description`** in `workato_qr_mcp.mcp_server.json`. The tool description must be set via Dev API after every push.
- **`workato push` does NOT maintain MCP tool assignments** across pushes. After a push, the tools_count in the MCP server may drop to 0. Always run the re-assign command above.
- **The `wkt_token` is not stored in the local JSON** — it's managed by Workato and retrieved via Dev API. Never hardcode it; always fetch dynamically.
- **Recipe must be running** before the MCP tool can be invoked. Check: `curl -s -H "Authorization: $AUTH" "https://app.trial.workato.com/api/recipes/277230" | jq .running`
- **`workato push` without `--restart-recipes` fails** if any recipe in the project is running. Always use `--restart-recipes` for this project.

## Reliability verification

Run this locally to verify correctness across URL lengths and colors:
```bash
cd cli
python3 << 'EOF'
import base64, subprocess, tempfile, os
exec(open('recipe_code.py').read())
urls = ["https://workato.com", "https://app.workato.com/recipes/new?template=genie",
        "https://academy.workato.com/learn/course/view/elearning/123456"]
passed = failed = 0
for url in urls:
    for fg, bg in [('workato','white'), ('dark','white')]:
        r = main({'url':url,'fg_color':fg,'bg_color':bg})
        png = base64.b64decode(r['image_base64'])
        with tempfile.NamedTemporaryFile(suffix='.png',delete=False) as tf:
            tf.write(png); fname=tf.name
        res = subprocess.run(['zbarimg','--quiet',fname],capture_output=True,text=True)
        os.unlink(fname)
        got = res.stdout.strip().replace('QR-Code:','').strip()
        if got == url: passed += 1
        else: print(f"FAIL {fg}: {url}"); failed += 1
print(f"{passed} passed, {failed} failed")
EOF
```
Requires `brew install zbar` for `zbarimg`.
