"""
fact-check — snippet 1 (rules + rubric).
Applies to training and education audiences. Not applicable to workato general audience.
Most checks are LLM reasoning — only mechanical patterns included here.
"""

RUBRIC = ""
---
name: fact-check
description: Use when shipping or reviewing Workato training content (labs, slide decks, course plans, abstracts, Knowledge Checks, demos) to verify technical claims against the current Workato product surface — feature availability, action/connector names, UI labels, limits, pricing, deprecations. Frame the pillar of Accuracy under The Standards Desk.
---

# Fact Check

A pass that verifies training content against **the current Workato product surface**. Every technical claim, every named feature, every UI label, every limit, every screenshot — checked against what's actually true in the product *today*, not what was true when the content was authored.

The hardest pillar to keep evergreen, because the product moves. The skill encodes verification *protocol* (how to check) and *patterns* (what tends to drift) rather than a fixed list of facts.

## When to invoke

Invoke before:

- **Shipping** any training artifact (lab guide, slide deck, course plan, Knowledge Check, course abstract) to customers or to WoW
- **Republishing** an artifact >90 days after its last verification
- **Citing** a Workato feature, limit, or pricing tier in any external-facing copy
- **Embedding** a screenshot in content that will ship in the next 90 days
- **Designing** a lab around a feature in development (where availability may shift before delivery)

Skip on: internal drafts before content review; experimental material flagged as "not for delivery."

## Posture

Three rules of taste behind the checks:

1. **Verify, don't trust.** Author memory + 6-month-old screenshots are the most reliable source of drift. Re-check against the live product even when "you just checked last week."
2. **Cite or strip.** Every technical claim either has a source you can re-verify (Workato docs URL, Confluence page, run-through date), or it doesn't belong in the content. No claim should live on "I'm pretty sure."
3. **Drift is not a failure — it's a feature of an active product.** When you find drift, the artifact gets a fresh `verified-on:` date, not a blame label. The job is to keep content current, not to keep it pristine.

## Check classification

**Static checks** — a small but high-value set that can run without accessing the live product:
- `feature_ga_dependency` field presence: is the field present on each module? (§1.1)
- GA date vs. delivery date: is every listed feature's GA target ≥2 months before the course delivery date? (§1.1 — date arithmetic, no judgment)
- Screenshot freshness: is the `verified-on` date >90 days old? (§5 — date comparison)
- Required spellings: pattern match against the §7 required-spelling list (Workato, recipe, connector, Datapill, etc.)
- External link resolution: does every URL in the content resolve with a non-error status? (§6)
- `verified-on` field presence: is it present in the artifact's header/frontmatter? (§5)

**Reasoning checks** — everything else. Fact-checking is inherently a live-product verification task:
- Feature availability: is the feature actually GA in the form the content claims? Requires checking release notes, Confluence PRDs, and the live workspace.
- UI label accuracy: do the button names, field labels, and action names in the content match the current live UI? Requires walking the workspace.
- Limits, quotas, and pricing: do the numbers stated in content match current Workato docs? Requires checking docs.workato.com and Confluence.
- Code/API block correctness: does the code actually run and return what the lab claims? Requires execution.
- Screenshot content accuracy: does the screenshot show the correct current UI? Requires visual comparison.
- Customer attribution: is the claim sourced and approved? Requires checking Highspot and sign-off status.
- PM lookup (§1.1.1): requires reading the Confluence PMO page body and querying the Atlassian user lookup API.

## How to apply

Walk the seven check categories in order. Each maps to a common drift pattern.

## §1. Feature availability (does the feature exist in the form claimed?)

Workato ships rapidly. A feature claimed by a lab may be:

- **GA** — broadly available in customer workspaces. Safe to use.
- **In Testing / Private Beta** — available behind a flag or to selected customers. Risky for cross-customer training; lab may fail for some learners.
- **Draft / In Development** — announced but not yet shipping. Cannot be exercised in a lab.
- **Deprecated / Sunset** — was available; removed or replaced. Lab will break.
- **Renamed** — same capability, new name (e.g., *Compose* → *Generate text*). Lab text references the old name.

**Verification protocol:**

1. **Check Workato product release notes** (`docs.workato.com` → release notes) for any feature mentioned in the content.
2. **Check Confluence PRDs / PMO tickets** if available — gives release-state and tier-availability beyond what docs.workato.com surfaces.
3. **Check the WoW workspace** (or whatever training workspace the lab targets) — features may be flagged for some workspaces and not others.
4. **For features in development:** confirm the delivery date is *before* the content's delivery date. If the delivery date moves, the lab needs to move.

**Common feature-availability drift patterns:**

- Lab claims a feature is "new" — feature has shipped to GA and the framing is now stale.
- Lab uses a feature still in private beta — works in author's workspace, fails for half the learners.
- Lab uses *Compose* — feature is now *Generate text*; the UI labels and walkthrough need updating.

### §1.1 Course-module GA dependency tagging (the GA-2-months rule)

For course plans (especially WoW-style instructor-led courses), every module must declare a **`feature_ga_dependency`** field listing which features must be GA before the module can run. This is the Ryan Koh GA-2-months rule, named for the team feedback that established it (WoW 2026 build):

> *"For every module we tag the feature that needs to be GA - 2 months."*

**fact-check verification per module:**

1. The module's `feature_ga_dependency` list is present and accurate (every feature actually needed for the lab/session is listed).
2. **Every listed feature has a confirmed GA date ≥2 months before the course delivery date.** This buffer gives time for: feature stabilization, content updates if the feature ships differently than planned, screenshot refresh, and trainer dry-runs.
3. If any feature is GA-1-month or closer, flag as ⚠️ and note the specific module/lab that breaks if the feature slips.
4. If any feature won't be GA before delivery, flag as 🔴 and require a fallback (different lab, different feature, different module).

**Course-level Roadmap Dependencies table.** Each course's `feature_ga_dependency` entries roll up into a per-course Roadmap Dependencies table at the end of the course plan:

| Feature | PMO | PM | Current status | GA target | WoW-ready? | Impact if delayed |
|---|---|---|---|---|---|---|

WoW-ready values:
- ✅ Yes — GA confirmed with ≥2 months lead time
- ⚠️ Needs confirmation — target date exists but is close or uncertain
- 🔜 Not yet — dependent on other features or no confirmed date

**Impact if delayed** must name the specific module/lab that breaks, not "this course is affected." If the impact note is generic, the entry isn't actionable.

### §1.1.1 PM-lookup protocol (Confluence PMO pages → PM name)

When you need to populate a PM column (or any DRI field) for a feature documented on a Confluence PMO page, walk this protocol in order. **The lookup runs dynamically against whichever PMOs surface during research** — there's no hardcoded list. Phase 0 roadmap research (in workflows like `wow-plan`) produces a set of relevant PMOs based on the course topic; this protocol turns each of those PMOs into a PM attribution.

It works for *any* course topic — Agent Studio, MCP, recipe-building, integration courses, future ADDIE pipelines — because every Workato product feature gets a PMO page with the same authorship metadata.

**Step 1 — Explicit DRI in the page body.** Read the PMO page via `mcp__atlassian__getConfluencePage`. Scan the body for:
- A field labeled `**Author:** <name>` or `**DRI:** <name>` (often in a metadata table near the top, or in a "Document Status" header block)
- A "Revision History" table that names the original author
- A byline below the title

If a DRI is explicitly named, use that name and stop. This is the most-authoritative signal.

**Step 2 — Page metadata `authorId` → user lookup.** If the body has no explicit Author/DRI field, fall back to the page metadata. The `getConfluencePage` response includes `authorId` (the page creator) and `ownerId`. Use the `authorId`:

```
mcp__atlassian__lookupJiraAccountId(
  cloudId: <your workato cloud ID>,
  searchString: "<the full authorId, e.g. 712020:2f7afb5c-4df1-4964-988b-83f48952c340 or 5de63fe422389c0d118c581e>"
)
```

The tool accepts a full Atlassian account ID as the search string (not just a name fragment). It returns `displayName` and email. Record the `displayName` as the PM.

**Step 3 — Fall back to TBD.** If neither the body nor the user lookup yields a name, record `TBD — check with product team` in the PM column.

**Heuristic for default DRI when a page genuinely has no explicit DRI:** If the same person authors multiple adjacent PMO pages in the same product area (e.g., Bennett Goh authors PMO-2078 Guardrails, PMO-2555 Native Channel, PMO-2893 Evals Phase 1 — all under Agent Studio), they're a strong default-DRI signal for related features that don't have their own DRI lines. Note this signal in the table as `<name> (inferred — adjacent-page DRI signal)` so the inference is auditable.

### §1.1.2 PM lookup applied — keep one home, not many

The protocol above lives in `fact-check` so every workflow that needs PM attribution (wow-plan, addie-plan, and any future course-planning skill) calls into the same routine instead of restating it. When the protocol updates (e.g., a new MCP tool replaces `lookupJiraAccountId`), updating fact-check is the only change needed.

---

**PM lookup (one-line summary for workflows that cite this protocol):** The PM column is populated from the Confluence PMO page for each feature via `fact-check §1.1.1` — explicit DRI in body → page-creator account ID → user lookup → TBD if all fail.

### §1.2 Cross-cutting Workato platform changes

Some roadmap items affect every course regardless of topic — they change how the Workato platform works for builders rather than being features being taught. fact-check verifies that these are tracked in a separate **Platform Changes** table that appears once in the course-plan Overview (not per-course):

| Change | Status | Courses affected | Training impact |
|---|---|---|---|

Examples to look for: RBAC 2.0, Decision Models, Workato Expression Language (WEL), Canvas UX redesign. When platform changes land, instructions and screenshots across multiple courses may drift — fact-check catches the drift before delivery.

## §2. UI labels and action/connector names

Workato UI labels drift more often than feature shape. A button renamed, a tab moved, an action reordered.

**Verification protocol:**

1. **Open the Workato workspace** the lab targets.
2. **Walk the lab steps** — every UI label the content mentions, check against the live UI.
3. **Compare against any screenshots** — UI labels visible in the screenshot must match the prose.

**Common UI-label drift:**

- Button or action renamed (*Compose* → *Generate text*).
- Field label renamed (*Source content* → *Inputs*).
- Action reordered within a connector menu (the lab says "third action under Salesforce" — it's now fifth).
- Connector renamed or re-categorized.
- Setting moved between settings panels (e.g., from Account → Workspace).

**The Ghost verification cycle (per `GHOST_CONTRACT §10`)** is the operational form of this check: Ghost runs each task against the live product, captures real screenshots, and files inline `<!-- ghost-note: -->` corrections when reality and the spec disagree. For non-lab artifacts (decks, course plans), the same protocol applies: walk the live product, compare against the content.

## §3. Limits, quotas, and pricing tiers

Workato platform limits change as the product scales. Pricing tiers and feature gating change as packaging evolves. Any number stated in content is a drift candidate.

**Verification protocol:**

1. **Check the current limit/quota** in Workato docs (e.g., 16MB per file, KB ingestion limits, action execution timeouts).
2. **Check pricing tier availability** in the current packaging (e.g., "Agent Studio is available in the Enterprise tier" — was that true 6 months ago? Is it true now?).
3. **For PRD-referenced limits** (not yet in docs), confirm the limit is the current decision, not a draft proposal.

**Common limits/pricing drift:**

- KB file size limit (was X MB; now Y MB).
- Concurrency limits on a Genie's tool calls.
- Feature gating moved between tiers (Genie X is now available in tier Y where it wasn't before).
- Action execution timeouts (e.g., HTTP connector timeout default).

**Anti-pattern:** *quoting a limit from a draft PRD as if it were live policy*. PRDs change; cite a doc, not a draft.

## §4. Code, configuration, and API blocks

Code blocks in labs and decks must compile or execute against the current platform.

**Verification protocol:**

1. **Run every code block** in the target Workato workspace (or sandbox).
2. **For API blocks** (Workato Developer API, third-party APIs): run the actual call, confirm the response shape matches the lab's claim.
3. **For formula-mode expressions:** evaluate against a real datapill or test value.
4. **For deprecated APIs:** check the Workato API changelog / Confluence for any deprecation notes.

**Common code-block drift:**

- Connector action signature changed (input/output field renamed or removed).
- Formula function renamed or signature changed.
- API endpoint deprecated; new endpoint required.
- Third-party connector version updated, breaking field paths.

**For non-Workato code** (Python, Mustache, SQL, JSON examples): drift is rarer but possible. Re-run before publishing.

## §5. Screenshot freshness

Screenshots drift the moment the UI updates. Old screenshots are the #1 trust erosion in training content.

**Rule:** screenshots ≤90 days old. Re-capture against the live workspace if older.

**Verification protocol:**

1. **Check the screenshot file timestamp** or the `verified-on:` date in `decisions.yaml`.
2. **If >90 days:** re-walk the lab against the live UI and capture fresh.
3. **For each screenshot:** verify UI matches the surrounding prose. Caption must match what's actually visible.

**Anti-patterns:**

- Annotating an old screenshot with new labels (the underlying UI is wrong; annotation lies).
- Using a "representative" screenshot from a different feature ("close enough").
- Photoshop / image-edit fixes to UI elements (always lies).

## §6. External links

Every URL in content must resolve. Workato docs URLs drift; third-party URLs go 404; Confluence pages move.

**Verification protocol:**

1. **Curl or browse every URL** in the content.
2. **Check redirect chains:** a 301 to a different topic is broken even if the page loads.
3. **Check Confluence URLs:** they're internal; some learners won't have access.

**Common link drift:**

- Workato docs URL — page moved or renamed.
- Confluence URL — page moved between spaces; access changed.
- Third-party doc URL — vendor restructured (Salesforce, Jira, Slack all do this).
- API reference URLs — versioned URLs may sunset.

## §7. Workato-specific terminology and required spellings

The Workato product surface has specific spellings that drift in author memory.

**Verification protocol:**

Cross-reference content against the **Workato Education and Training wordlist** (Confluence: `ETT/758775978`) and the **Workato product stylization** guide (Confluence: `PPD/347407142`). When in doubt, the docs.workato.com spelling wins.

**Required spellings** (commonly missed):

- `Workato` (never `WorkAto`, `workato`, `Workato.com` mid-sentence)
- `recipe` (lowercase — the product noun)
- `connector` (lowercase)
- `Connection` (capitalized when it is the UI noun for an established auth)
- `Recipe Lifecycle Management` (no abbreviation in content; *RLCM* may be used in dev-facing copy only)
- `Datapill`, `Datapills`, `Datatree` — each one word, no spaces
- `Knowledge Checks` — always full term ([[feedback_knowledge_checks_naming]])

**Never:** abbreviated forms in customer-facing content unless explicitly approved (see [[feedback_omnifocus_naming]] for the same principle applied to OmniFocus).

## §8. Customer attribution and privacy

When training content references customer data — anonymized or named, in narration or scenarios — the same verification discipline applies as for product facts. Attribution and privacy are factual claims about the customer; they need cite-or-strip handling.

**Verification protocol:**

1. **Anonymize by default.** Industry + size + role beats company name. *"A mid-market SaaS customer"* is verifiable from a description; *"Acme Corp"* needs explicit approval.
2. **Cite attribution only with explicit approval.** Named customers, named individuals, named accounts — only with Marketing/Sales sign-off, and ideally cross-referenced against the approved-for-external-use catalog in Highspot.
3. **Verify metrics at source.** Quantified outcomes (*"40% reduction in..."*) need a traceable source (Gong call ID, Salesforce report, Highspot case study). Author memory is not a source.
4. **Don't expose internal customer data.** ARR, pipeline, churn risk, health scores, and similar fields don't appear in customer-facing content even when anonymized.
5. **Document data lineage during authoring.** When a proof point or scenario draws on customer data, track the source in author/review notes (not in learner-facing content) so the claim can be re-verified during the next freshness pass.

**Common attribution drift:**

- Customer name in content that was approved 18 months ago — re-verify; permissions may have lapsed.
- Anonymized scenario that's re-identifiable from the detail combination (industry + region + size + use case can triangulate).
- Quantified outcome cited in narration with no source in author notes — the claim is unverifiable; strip or re-source.
- Internal data field (health score, expansion ARR) used as a proof point — never appropriate in customer-facing content even with consent.

**Source:** ADDIE pipeline Customer Privacy & Ethics guidelines (Workato Academy ETT, 2026). The check is a peer to product fact-checking — customer attribution is a factual claim, and it drifts the same way product references drift.

## Verification cadence

| Artifact type | Default verification interval | Re-verify trigger |
|---|---|---|
| Lab guide (active delivery) | 90 days | Major Workato release; feature deprecation; UI redesign |
| Slide deck (active delivery) | 90 days | Same |
| Course plan / abstract | At authoring + 30 days before delivery | Feature roadmap shift |
| Knowledge Check | Same as parent lab/module | When parent lab is re-verified |
| Course bundle (in WoW workspace) | 30 days before each delivery date | Workspace reset; new tenant config |

After re-verification, update the `verified-on:` field in the artifact's `decisions.yaml` (per `GHOST_CONTRACT §10`) or equivalent header field.

## What this skill is NOT

- **Not authoritative on Workato product behavior** — that's the live product + Workato docs + the product team. This skill is a *protocol* for checking against those sources, not a replacement for them.
- **Not a stylistic editor** — fact-check verifies *correctness*, not *quality*. Style is `say-it-plain` + `team-style-guide`.
- **Not a completeness check** — fact-check verifies *what's there is true*; complete-check verifies *the right things are there*.
- **Not for non-Workato content** — the skill is Workato-product-specific. Other content has its own source-of-truth checking.

## Source priority

When fact-checking, resolve conflicts in this order:

1. **The live Workato product surface** (the running UI in the target workspace)
2. **docs.workato.com** (official product documentation)
3. **Confluence PRDs / PMO tickets** (forward-looking; useful for features pre-GA)
4. **Workato Education and Training wordlist + style guides** (terminology)
5. **Product team / engineering Slack channels** (for behavior the docs haven't caught up to)
6. **Author memory** (only as a starting hypothesis to verify)

When the live product disagrees with the docs, the live product wins — and the docs get a bug report.
\
"""

SPELLING_PATTERNS = [
    {
        "pattern": r"\bData[Pp]ill\b|\bdata pill\b|\bdata-pill\b",
        "message": "Spelling: use 'Datapill' (one word)",
        "ignore_case": False,
    },
    {
        "pattern": r"\bData[Tt]ree\b|\bdata tree\b|\bdata-tree\b",
        "message": "Spelling: use 'Datatree' (one word)",
        "ignore_case": False,
    },
    {
        "pattern": r"\bKnowledge [Cc]heck(?!s)\b",
        "message": "Use 'Knowledge Checks' (plural, full term — never abbreviated)",
        "ignore_case": False,
    },
    {
        "pattern": r"\bRecipe [Ll]ifecycle [Mm]anagement\b",
        "message": "Spelling: 'Recipe Lifecycle Management' (verify exact casing)",
        "ignore_case": False,
    },
]

PRESENCE_CHECKS_TRAINING = [
    {
        "pattern": r"feature_ga_dependency",
        "message": "Course plan missing 'feature_ga_dependency' field on module(s) — required for GA tracking",
    },
]

PRESENCE_CHECKS_EDUCATION = [
    {
        "pattern": r"verified.on",
        "message": "Screenshot block missing 'verified-on' date — required for freshness tracking",
    },
]


def _rules(audience):
    if audience == "workato":
        return {
            "applicable": False,
            "note": "fact-check applies to training and education content only",
            "banned_phrases": [],
            "regex_patterns": [],
        }

    presence = (
        PRESENCE_CHECKS_TRAINING if audience == "training"
        else PRESENCE_CHECKS_EDUCATION
    )

    return {
        "applicable": True,
        "banned_phrases": [],
        "regex_patterns": SPELLING_PATTERNS,
        "presence_checks": presence,
    }


def main(input):
    audience = input.get("audience", "workato")
    return {
        "rubric": RUBRIC,
        "rules": _rules(audience),
    }
