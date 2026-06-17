# workato-training-mcp — Claude context

Monorepo for Workato training team MCP servers. Each subdirectory is a self-contained MCP project with its own Workato RCLM project, skill, and MCP server.

## MCP projects

| Directory | MCP server | What it does |
|---|---|---|
| `qr-code/` | Workato-branded QR code generator | Generates PNG QR codes via Python snippet |
| `kahoot-generator/` | Kahoot quiz generator | Generates Kahoot-importable CSV from any learning artifact |

## Shared infrastructure patterns

### Auth

Dev API auth token (all projects use the same pattern):
```bash
AUTH=$(jq -r '.mcpServers["workato-dev-api"].env.AUTH_HEADER' ~/.mcp.json)
```

### Push workflow (per project)

Each project has its own `workato/` directory with its own `.workatoenv`. Always push from inside that directory:

```bash
cd <project>/workato && workato push --restart-recipes
```

After every push, re-assign the skill to the MCP server — the platform CLI does NOT maintain tool assignments across pushes. See each project's `CLAUDE.md` for the specific re-assign command.

### Known platform CLI gaps (apply to all projects)

- `workato push` does NOT apply `tools[].description` in MCP server JSON — set via Dev API after push
- `workato push` does NOT maintain MCP tool assignments — always re-assign after push
- The `wkt_token` is not stored in local JSON — fetch via Dev API dynamically, never hardcode
- Recipe must be running before the MCP tool can be invoked

### Adding a new MCP project

1. Create `<project-name>/` directory
2. Add `<project-name>/workato/` with a `.workatoenv` pointing to the right Workato workspace + project
3. Add `<project-name>/CLAUDE.md` with project-specific IDs, endpoints, and test commands
4. Add `<project-name>/README.md` for humans
5. Update the projects table in this file

## AVOID

`mcp__workato-dev-api__post_api_collections_api_endpoints` — broken JSON Schema poisons the MCP tool list for the entire session. All other Dev API tools are safe.
