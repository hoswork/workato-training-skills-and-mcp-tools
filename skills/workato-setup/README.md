# workato-setup

**Internal use only — Workato employees using Claude Code.**

This skill is not part of the public skills distribution. It configures Claude Code with the Workato MCP servers needed for team workflows and is only available via the `workato-trainer-skills` and `workato-education-skills` plugin bundles.

## What it does

Checks which Workato MCP servers are already configured in Claude Code, adds any that are missing, and walks through OAuth authentication. Targeted at the Google Suite MCPs that are open to all Workato employees.

## Scope

- **Claude Code only.** The `claude mcp add` command does not exist in Claude Desktop. Do not include this skill in any Claude Desktop bundle.
- **Not in `skills-distro.zip`.** This skill is excluded from the broad distribution artifact.
- **Team bundles only:** `workato-trainer-skills` · `workato-education-skills`

## MCP registry

The full list of 42 BT-managed Workato MCPs is at:
https://workato.atlassian.net/wiki/spaces/extbt/pages/2510848002/Internal+MCPs+BT+Managed
