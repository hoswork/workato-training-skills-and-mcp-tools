---
name: the-tape
description: Use at end of a session to record decisions that overrode, extended, questioned, or validated the Standards Desk or any team skill — or when the user commits an override to memory, asks Claude to update a local skill file, or says "run the tape", "tape this", "log this decision". Builds the decision history that evolves team standards over time.
metadata:
  version: "1.0"
---

# The Tape

The Tape is the Workato training team's decision record — every consequential call that overrides, extends, or validates a team standard gets captured here. It is the moat: the accumulated decision history that makes the Standards Desk and team skills improvable over time.

This skill is the first-generation MVP of The Tape. Entries are written locally to your device. Publishing is a separate, explicit opt-in — see `~/code/the-tape/CLAUDE.md`.

## Posture

Three principles behind every interaction:

1. **Never surprised.** The person always knows what's being recorded, when, and why. Automatic offers say in one line why they're firing. Nothing is logged silently.
2. **Always in charge.** "Not this session" means this session. "Never" means never. No re-asking mid-session. Settings can be changed anytime by saying "change my tape settings."
3. **Helpful not annoying.** One-line offers. Short capture form. Only offer when there's something real to capture. If the person says no, move on immediately.

## When to invoke

**Direct (always, regardless of settings):**
- "Run the tape", "tape this", "log this decision", "capture this override", "change my tape settings"

**Automatic (only if `auto_offer: true` in config):**
- At end of session, after `mbo-asset-tracker`, if a Standards Desk skill was used or a skill file was updated
- When the user asks Claude to commit an override or exception to memory

**Re-offer (only if `auto_offer: "not_now"`, only at the START of a new session — never mid-session):**
- At session start: one offer, one line: "Want automatic tape offers this session? You said not now last time."

Never fire automatically if `auto_offer` is `"never"` or `local_tracking` is `false`. If someone says no during a session, do not ask again in that session.

## First use — two-step opt-in

On first invocation, check for `~/code/the-tape/config.json`. If it doesn't exist, walk through two questions in order. Never bundle them — ask one, wait for the answer, then ask the next.

### Step 1 — Local tracking

> "The Tape saves your decisions locally so the team can improve these tools over time. Nothing leaves your device without you choosing to share it. Want to turn it on?"

Options: **Yes** / **Not this session** / **No, don't ask again**

- **Yes** → Step 2
- **Not this session** → `{ "local_tracking": "not_now" }`; skip for this session; offer again at the start of the next
- **No, don't ask again** → `{ "local_tracking": false }`; never auto-trigger again; still responds to "run the tape"

### Step 2 — Automatic offers (only if Step 1 = Yes)

> "Should I offer to capture decisions automatically at the end of sessions, or would you rather trigger it yourself?"

Options: **Automatically** / **I'll trigger it** / **Never ask**

- **Automatically** → `auto_offer: true`
- **I'll trigger it** → `auto_offer: false`
- **Never ask** → `auto_offer: "never"`

### Step 3 — Attribution

> "How should entries show you — your name, just your role, or anonymous?"

Options: **Named** / **Role only** / **Anonymous**

Ask name slug if named. Write final config and confirm: "All set. Say 'change my tape settings' anytime to update these."

```json
{ "local_tracking": true, "auto_offer": true, "user": "your-name", "attribution": "named" }
```

If config exists, skip setup entirely. Check `local_tracking` and `auto_offer` flags before any automatic offer.

## The automatic offer

When firing automatically, use one line — state why, make it easy to decline:

> "Want to tape any decisions from this session? [brief reason: e.g. 'you updated a skill file' or 'the-once-over flagged a few things']"

Options: **Yes** / **No** / **Stop offering automatically**

- **Stop offering automatically** → set `auto_offer: "never"` immediately. Confirm: "Got it, I won't offer again. You can still say 'run the tape' anytime."
- **No** → move on immediately. Do not ask again this session.

## Capture flow

Keep it under 2 minutes. Five questions only:

**1. Which skill or standard?**
`the-once-over` · `wow-plan` · `addie-plan` · `generate-kahoot` · `mbo-asset-tracker` · `calibrate-challenge` · `say-it-plain` · `complete-check` · `fact-check` · `stick-check` · other

**2. What type of artifact?**
Lab guide · slide deck · course plan · Knowledge Check · course abstract · Kahoot quiz · e-learning module · other

**3. What happened?** — one or two sentences: what the rule said, what you did instead (or what pattern you noticed). Skip if already obvious from context.

**4. Why?** — the reasoning that would help decide whether to update the standard. One sentence.

**5. Example** — paste whatever you have; Claude rewrites it into an anonymized pattern:
- Workato customer names never appear — replace with `[customer]`
- All other names/companies/projects → `[company]`, `[project]`, `[person]`
- Keep only the structural wording that makes the decision evaluable

Show the rewrite and ask: "Does this capture it?" Adjust if needed. The rewritten version is stored — not the raw input. Skip if there's nothing concrete to show.

**Promote?** — Offer at the end: "Worth flagging for review?" Yes / Maybe / Just logging. Don't ask if there's no reason to believe this would change anything.

## Output

Append one JSON line to `~/code/the-tape/entries/[user-slug].jsonl` (or `anonymous.jsonl`):

```json
{
  "date": "2026-06-11",
  "quarter": "Q2",
  "fiscal_year": "FY27",
  "user": "your-name",
  "skill": "the-once-over",
  "artifact_type": "lab guide",
  "event_type": "OVERRIDE",
  "rule": "say-it-plain §1.3",
  "what_rule_says": "No telegraphic noun fragments — expand to full sentences",
  "decision": "Kept nav path as telegraphic fragment",
  "why": "UI navigation paths are standard technical writing convention; expanding them harms scannability",
  "example": "Settings → Skills → Add → upload each zip → restart Claude Desktop",
  "promote": "maybe"
}
```

Auto-populate `quarter` and `fiscal_year` from the current date using Workato's fiscal calendar (Feb–Apr = Q1, May–Jul = Q2, Aug–Oct = Q3, Nov–Jan = Q4; FY = calendar year + 1 for Feb–Dec).

Confirm briefly: "Taped — [event_type], [skill], [promote status]." Then move on.

## Privacy guardrails

**Local entries are private.** Entries in `~/code/the-tape/entries/` stay on your device and are visible only to you.

**Published entries contain minimum information, no PII.** When publishing to the Skill Feedback folder or packaging to share, entries are stripped to only what is needed to act on the feedback:

| Kept | Stripped |
|---|---|
| Event type, skill, artifact type | Personal name |
| Rule and section | Customer names, project names, company names |
| Decision and why | Any content identifying a specific person |
| Sanitized example showing the pattern | Raw content from the artifact |
| Role (trainer / education team) | Full name attribution |

**Published attribution is always role-only.** Regardless of local attribution setting, shared entries use role only (`trainer` or `education team`). Names never leave the device.

**Example field — sanitize before publishing.** When capturing an example, replace any identifying details with placeholders: `[customer name]`, `[project name]`, `[person]`. Keep only the structural pattern that illustrates the decision.

> ❌ "Sarah Chen's Genie lab guide said: 'AcmeCorp uses Workato to sync their Salesforce data...'"
> ✅ "Lab guide said: '[Company] uses Workato to sync their [CRM] data...'"

When packaging or publishing, automatically apply this reminder and ask the user to confirm the example is clean before proceeding.

## Generate a tape package

Two modes: **standard** (anonymized patterns, shareable with the team) and **private** (fuller detail for a specific recipient).

**Triggers:** "generate a tape package", "share my tape", "I want to report a problem with [skill]", "export my [skill] overrides"

**Standard package (default):**
1. Ask what to include: a specific skill, a date range, entries marked "promote", or all entries.
2. Read the relevant entries from `~/code/the-tape/entries/[user-slug].jsonl`.
3. Apply the same anonymization reasoning used at capture — confirm patterns are clean.
4. Produce a summary with anonymized entries plus a one-paragraph context note.
5. Save to `~/code/the-tape/published/[date]-team-package.json`.
6. Confirm the path. The team's Skill Feedback folder: https://drive.google.com/drive/folders/1rX5sz9weRJVCjEJhquhUjeL3FZgLR5M-

**Private feedback bundle** (when the user explicitly says "send this to [name]" or "this is a private report"):
1. Ask what happened — the user can provide fuller context including original unedited content.
2. Ask who the recipient is.
3. Preserve fuller context — but **always** strip Workato customer names regardless of mode. Replace with `[customer]`. Other identifying details (internal project names, team member names) may be retained in a private bundle at the user's discretion.
4. Save to `~/code/the-tape/published/[date]-private-[recipient].json`.
5. Remind: "This package contains unanonymized content. Only share it directly with [recipient], not the shared folder."

The package is a JSON file the recipient can read directly or load into a review session. No automatic upload — the user shares it manually.

## Logging

At completion, invoke: `skill-logger the-tape` (if `skill-logger` is available in the current environment; skip silently if not). This collects org-wide usage telemetry for Workato training-team skills.
