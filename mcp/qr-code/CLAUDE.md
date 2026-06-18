# qr-code

Single-tool Workato MCP: `generate_qr_code`.

Python source: `cli/recipe_code.py` (source of truth — embed into recipe JSON before pushing).
Recipe JSON: `workato/workato-qr/`.
Push: `cd workato && workato push --restart-recipes`, then re-assign tools to the MCP server via Dev API.
