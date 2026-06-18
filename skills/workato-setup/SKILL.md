---
name: workato-setup
description: Use when the user says "get me set up", "set up my MCPs", "what do I need installed", "get sorted", or "new machine". Checks which Workato MCPs are already configured and adds any that are missing. Claude Code only.
metadata:
  version: "1.0"
---

# Workato Setup

Gets Claude Code configured with the right Workato MCP servers for training and education team work. Checks what's already installed, adds what's missing, and tells you what needs authentication.

The full BT-managed MCP registry (42 connectors) is at:
**https://workato.atlassian.net/wiki/spaces/extbt/pages/2510848002/Internal+MCPs+BT+Managed**

## Trainer + Education role MCPs

These are the MCPs the training and education team needs. All are open to Everyone at Workato.

| Name | URL |
|---|---|
| `gmail-workato` | https://4086.apim.mcp.workato.com/ |
| `google-calendar-workato` | https://3812.apim.mcp.workato.com/ |
| `google-docs-workato` | https://5492.apim.mcp.workato.com/ |
| `google-drive-workato` | https://5491.apim.mcp.workato.com/ |
| `google-sheets-workato` | https://3811.apim.mcp.workato.com/ |

## Setup workflow

### 1. Check what's already installed

Run:
```
claude mcp list
```

Parse the output. For each MCP in the table above, note whether it is:
- **Connected** — already working, skip it
- **Needs authentication** — installed but needs an OAuth flow
- **Missing** — not in the list at all

### 2. Add missing MCPs

For each missing server, run:
```
claude mcp add --scope user <name> --transport http <url>
```

Example:
```
claude mcp add --scope user gmail-workato --transport http https://4086.apim.mcp.workato.com/
```

Add all missing ones, then tell the user: **"Restart Claude Code to activate the new servers."**

### 3. After restart — authenticate

After restart, for any server showing "Needs authentication", invoke its authenticate tool. Each will open a Workato OAuth flow at `https://id.workato.com`. Complete it in the browser. If the redirect page shows a connection error, paste the full URL from the address bar and call `complete_authentication`.

### 4. Confirm

Run `claude mcp list` again and report status. Done when all five show **Connected**.

## Logging

At completion, invoke: `skill-logger workato-setup` (if available; skip silently if not).

## If the registry has changed

If the user asks about other available MCPs (e.g. Salesforce, Confluence, Slack), fetch the registry page via the Atlassian MCP and filter by their role. The full list has 42 connectors — most are role-restricted.
