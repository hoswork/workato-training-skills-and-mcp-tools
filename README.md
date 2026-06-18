# workato-training-skills-and-mcp-tools

Workato training team's Claude skills and MCP servers.

## Skills (`skills/`)

Claude Code/Desktop skills distributed as zips. Install via Claude Desktop → Plugins, or via `workato-setup` skill in Claude Code.

| Skill | Audience |
|---|---|
| the-once-over | Trainer + Education |
| wow-plan | Trainer |
| addie-plan | Education |
| mbo-asset-tracker | Trainer + Education |
| the-tape | Trainer + Education |
| generate-kahoot | Trainer |
| file-workato-product-bug | Trainer + Education + All Workato |
| workato-setup | Trainer + Education |

Distribution: https://workato.atlassian.net/wiki/spaces/ETT/pages/2604859430/AI+Initiatives+Shared+Skills

## MCP servers (`mcp/`)

Workato-hosted tools accessible from Claude Code and Claude Desktop.

| Server | Tools |
|---|---|
| standards-desk | `list_pillars` · `get_rubrics` · `run_static_checks` |
| kahoot-generator | `get_kahoot_constraints` · `format_kahoot` |
| qr-code | `generate_qr_code` |

## Pillar rubrics (`pillars/`)

Canonical source for all Standards Desk pillar content. Changes here propagate to skills and MCP via `make sync`.

## Internal MCP registry

Full list of 42 BT-managed Workato MCPs: https://workato.atlassian.net/wiki/spaces/extbt/pages/2510848002/Internal+MCPs+BT+Managed
