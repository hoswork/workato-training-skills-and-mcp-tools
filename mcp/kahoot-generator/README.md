# kahoot-generator

Kahoot quiz generator MCP — Claude generates questions client-side; this MCP handles constraint validation and XLSX formatting.

## Tools

- `get_kahoot_constraints` — returns field limits (question/answer lengths, points values, time ranges)
- `format_kahoot` — validates and formats a question set into Kahoot-importable XLSX

## Developing

1. Edit `cli/format_kahoot.py`
2. Embed into recipe JSON and push: `cd workato && workato push --restart-recipes`
3. Re-assign tools to MCP server via Dev API (see `mcp-server-prompt.md` for tool descriptions)
