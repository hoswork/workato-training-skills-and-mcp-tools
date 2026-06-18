---
name: mbo-asset-tracker
description: Use when a teammate finishes or substantially advances a deliverable with Claude and wants it logged, or when they say "log this session", "log this asset", "track this", "I forgot to log", "show my logs", or "my MBO assets". Built from the Academy AI Tracking team rules.
metadata:
  version: "2.0"
---

# MBO Asset Tracker

Logs how teammates use AI in daily work so it rolls up to their quarterly MBO. Every trackable session writes immediately to a local JSONL queue and to the team's MBO Google Sheet. Slack announcements are batched — the trainer reviews and publishes on their own cadence.

This skill is shared and team-wide. It is not tied to any one person: it reads the per-user config on first use and remembers the answer.

## Shared resources

- **MBO Tracking Drive folder** (where each person's sheet lives): https://drive.google.com/drive/folders/1I7jaNu7YSYn-MR1ZM0iDXIVkHNQ5RsII
- **Slack channel**: `#academy-ai-log` (channel ID `C0B4HS015JQ`). Never post to `#academy-internal`.
- **Per-user config**: `~/code/mbo-logger/mbo-tracker-config.json`
- **Per-user JSONL queue**: `~/code/mbo-logger/[name_slug]-asset-log.jsonl`

## Prerequisites — getting Claude Code set up

This skill requires the Google Sheets Workato MCP. If the trainer is setting up a new machine or the MCP isn't available:

1. **Add the MCP server** (one-time, global):
   ```
   claude mcp add --scope user google-sheets-workato --transport http https://3811.apim.mcp.workato.com/
   ```
2. **Restart Claude Code** so the server is active.
3. **Authenticate** — on first use Claude Code will open a Workato OAuth flow at `https://id.workato.com`. Complete it in the browser.

The full list of BT-managed Workato MCPs (including Google Suite, Salesforce, Slack, and more) is at:
**https://workato.atlassian.net/wiki/spaces/extbt/pages/2510848002/Internal+MCPs+BT+Managed**

All five Google Suite MCPs (Gmail, Calendar, Docs, Drive, Sheets) are open to Everyone at Workato.

## First-time setup

Check for `~/code/mbo-logger/mbo-tracker-config.json`. If it exists, read it silently. If not, ask:

1. **Full name** (e.g. `Sarah Chen`) — used to name the sheet and attribute Slack posts.
2. **Reminder cadence** — how often to be nudged to review and publish the Slack batch:
   - **Weekly** — Friday at 4:00 PM (recommended)
   - **Daily** — weekdays at 5:00 PM

Write the config, then create the CronCreate reminder (see Publish flow below).

Config schema:

```json
{
  "name": "Heiwad Osman",
  "name_slug": "heiwad-osman",
  "reminder_cadence": "weekly",
  "last_slack_post": ""
}
```

## When to offer logging

Offer once per session, only when a real artifact was produced or substantially advanced:

- After a review or QA pass on a near-finished asset
- After 3+ rounds of iteration on a single asset
- When the person signals completion — "done", "ship it", "let's call this final" — or moves on after sustained work
- At session end if substantial work happened but none of the above triggered

## When NOT to offer logging

- Purely conversational, exploratory, or brainstorming with no artifact
- Tooling, prompt engineering, or skill setup
- A review concluded "needs major rework" — wait until the rework lands
- Already logged this session

When in doubt, steer toward skipping — better to under-log than inflate.

## How to prompt

Use AskUserQuestion:

- Question: "Want me to log this session to your AI asset tracker?"
- Options: **Yes** / **Not yet (still iterating)** / **Skip (not a trackable asset)**

If **Yes**, propose values and ask the person to confirm or adjust:

- **Title** — propose one from context; confirm explicitly. This same title appears in both the Sheet and any Slack post.
- **Category** — see Categories below
- **Stage** — see Stages below
- **Time spent** — offer ~15m / ~30m / ~1h / ~2h+
- **One-line note** (optional)

## Writing the entry

When confirmed, write in this order:

### 1. JSONL queue first (always)

Append to `~/code/mbo-logger/[name_slug]-asset-log.jsonl`:

```json
{
  "date": "2026-06-16",
  "quarter": "Q2",
  "fiscal_year": "FY27",
  "title": "Workato Admin Onboarding Module v1",
  "category": "Content",
  "stage": "Develop",
  "duration_minutes": 45,
  "notes": "first draft, needs SME review"
}
```

JSONL is the write-ahead buffer and the Slack staging queue. Write here first — it always succeeds locally even if the Sheet call fails.

### 2. Sheet second (authoritative record)

The Sheet is named `[name_slug]-mbo-log` inside the MBO Tracking Drive folder (ID `1I7jaNu7YSYn-MR1ZM0iDXIVkHNQ5RsII`). Append one row:

```
date | quarter | fiscal_year | title | category | stage | duration_minutes | notes
```

If the sheet doesn't exist yet, create it with the header row first. The Sheet is the authoritative record — "show my logs" reads from here.

If the Sheet write fails, report the error. The entry is safe in JSONL and can be retried.

### Fiscal calendar (FY starts February)

- Feb–Apr = Q1 · May–Jul = Q2 · Aug–Oct = Q3 · Nov–Jan = Q4
- FY = calendar year + 1 (except January: FY = calendar year)
- Today (June 2026) → Q2 FY27. Always recompute from the actual date.

## Publish flow (editorial → Slack)

The trainer reviews and publishes the Slack batch on their own cadence. Slack is not authoritative and does not need completeness — only what the trainer chooses to highlight gets posted.

### Reminder (CronCreate)

On first setup, create a CronCreate reminder:

- Weekly: `0 16 * * 5` (Friday 4 PM)
- Daily: `0 17 * * 1-5` (weekdays 5 PM)

Prompt: `Run the MBO asset tracker publish reminder for [Name]. Read ~/code/mbo-logger/mbo-tracker-config.json and ~/code/mbo-logger/[name_slug]-asset-log.jsonl. If the JSONL has entries, show them as a numbered list and ask: "Ready to review and post your Slack digest?"`

### Publish session

When the trainer triggers a publish (from the reminder or manually):

1. **Show pending entries** — display each JSONL entry as a numbered list with title, category, stage, duration
2. **Editorial** — trainer can:
   - Rename any entry title (updates both the Slack post AND the Sheet row to keep them in sync)
   - Remove any entry from the batch (it stays in the Sheet; it just won't go to Slack)
3. **Confirm** — post one squashed message to `#academy-ai-log`:

```
📝 [Name] — AI assets logged [this week / today / date range]
• *[Title]* · [Category] · [Stage] · ~[X]min
• *[Title]* · [Category] · [Stage] · ~[X]min
Total: N assets · ~[sum]min
[notes on any entry, if present]
```

4. **Clear** — remove published entries from JSONL. Entries the trainer excluded stay in JSONL for the next cycle.
5. **Advance** — set `last_slack_post` in config to today's date.

## Other commands

- **"Show my logs / MBO assets this quarter"** — read the Sheet and summarize: counts by category and stage, total time, recent entries.
- **"I forgot to log [asset] yesterday for ~[time]"** — walk through the fields, write a backdated entry (use the stated date for `date`, `quarter`, `fiscal_year`).
- **"What category is this?"** — suggest category and stage; don't log unless confirmed.
- **"Post my digest now"** — trigger the publish flow immediately without waiting for the cron.
- **"Change my reminder cadence to ..."** — update config and recreate the CronCreate task.

## Categories

- **Curriculum** — course outlines, learning paths, program frameworks
- **Content** — scripts, storyboards, slides, e-learning modules, job aids
- **Assessment** — quizzes, certification exams, rubrics, scenario banks
- **Customer Training** — customer-facing ILT sessions and supporting materials
- **Partner Training** — partner-facing ILT sessions and supporting materials
- **Program** — certification programs, Token Time sessions, community initiatives
- **People Ops** — JDs, performance reviews, promotion rationale, career frameworks
- **Strategy** — V2MOMs, OKRs, QBR decks, business cases, headcount justifications
- **Ops** — LMS configs, SOPs, process docs, templates
- **Research** — customer research, competitive analysis, vendor evaluations

## Stages

- **Strategy** — defining goals, scope, stakeholder alignment
- **Design** — structuring the approach, outlining, frameworks
- **Develop** — drafting, building, iterating
- **Review** — QA, SME feedback, stakeholder input
- **Launch** — finalizing, publishing, delivering
- **Ops** — maintenance, updates, admin work

## Logging

At completion, invoke: `skill-logger mbo-asset-tracker` (if available; skip silently if not).

## Tape

If any decisions were made that overrode or notably extended these standards, offer to run `the-tape`. Skip silently if not installed.
