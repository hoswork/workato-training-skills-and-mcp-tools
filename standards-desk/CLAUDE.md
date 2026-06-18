# standards-desk

Three-tool Workato MCP: `list_pillars`, `get_rubrics`, `run_static_checks`.

Python source: `cli/` (source of truth — embed into recipe JSON before pushing).
Recipe JSON: `workato/standards-desk/`.
Pillar rubrics: `~/.claude/skills/the-once-over/pillars/` (canonical source).
Push: `cd workato && workato push --restart-recipes`, then re-assign tools to the MCP server via Dev API.
