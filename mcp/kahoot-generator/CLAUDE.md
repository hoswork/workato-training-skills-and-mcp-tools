# kahoot-generator

Two-tool Workato MCP: `get_kahoot_constraints` and `format_kahoot`.

Python source: `cli/format_kahoot.py` (source of truth — embed into recipe JSON before pushing).
Recipe JSON: `workato/kahoot-generator/`.
Push: `cd workato && workato push --restart-recipes`, then re-assign tools to the MCP server via Dev API.
