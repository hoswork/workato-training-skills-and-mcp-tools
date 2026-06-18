---
name: file-workato-product-bug
description: Use when filing a product bug on Workato's CCE Jira Service Desk — or when the user says "file a bug", "report a Workato bug", "raise a PSM ticket", or describes a diagnosed Workato product issue ready to escalate. Redirects SDK Connector bugs to their separate portal.
metadata:
  version: "1.0"
---

# file-workato-product-bug

A workflow skill for filing a Product Bug ticket on Workato's CCE Jira Service Desk. Handles the full motion: portal selection → form inspection → draft → review → fill → hand to user for submit.

**Sources:**

- CCE "How to submit an ideal ticket": `https://workato.atlassian.net/wiki/spaces/CCE/pages/177078428`
- Product Bug form: `https://workato.atlassian.net/servicedesk/customer/portal/4/group/99/create/117`
- SDK Connector Bug form (different portal): `https://workato.atlassian.net/servicedesk/customer/portal/4/group/1531/create/4063`
- The iteration that codified these rules (2026-06-05; first run filed a Workato Dev API MCP schema bug)

## When to invoke

- The user says they want to "file a bug," "report a bug to CCE," "report a Workato product bug," "raise a PSM ticket," or similar.
- The user has diagnosed a Workato product issue and is ready to escalate to engineering.
- The user is filing on behalf of a customer ticket escalating from Freshdesk to Jira.

Skip when:

- The bug is an SDK Connector bug — those go to a different portal (see §"SDK Connector bugs" below). Redirect, don't draft.
- The user is still in diagnosis mode (no diagnosed cause yet). Help them diagnose first; file once they know what's broken.
- The bug is a one-off internal note that won't travel.

## Posture

Bug reports are triage artifacts. Composing `the-once-over` on the draft enforces the general posture — matter-of-fact register, no speculation, no teaching content (see `say-it-plain` §3 and `complete-check` §1.6 inside the-once-over). This skill adds the Workato-specific layer on top.

Three Workato-specific rules of taste:

1. **The form is opinionated.** The CCE Product Bug form has 5 required fields and ~10 optional ones. Each field expects a specific shape; the helper text on the form matters. Always inspect the form before drafting so the draft matches.
2. **Customer vs non-customer changes the metadata.** Two metadata profiles with different defaults. Set the metadata first; it changes what other fields need.
3. **Two-portal awareness.** Product/platform/API/MCP/AIRO bugs go on the Product Bug form. SDK Connector bugs go elsewhere. AIRO bugs share the Product Bug form but require an AIRO marker.

## Workflow

### Step 1 — Confirm portal

Before drafting anything, confirm the bug belongs on the Product Bug form:

- **Product Bug form** (`portal/4/group/99/create/117`) — platform, REST API, MCP server, Genie, Workato Cloud, recipe engine, the Connector SDK gem itself, AIRO, identity, embed, etc.
- **SDK Connector Bug form** (`portal/4/group/1531/create/4063`) — bugs in a *custom* connector built using the Connector SDK. The Product Bug form has a banner pointing to this portal.

If it's an SDK Connector bug, **stop and point the user to the other portal.** Do not draft on the Product Bug form.

### Step 2 — Determine customer vs non-customer

Set the metadata profile up front:

**Non-customer-driven** (internal tooling, AI integrations, developer-experience, bugs the user discovered themselves):
- Customer Company = `Workato`
- Customer Support Plan = `Not Defined`
- top100 = `No`
- Customer at Risk = blank
- Customer Name = blank

**Customer-driven** (Freshdesk → Jira escalation, PSM ticket, named customer report):
- Customer Company = customer org name
- Customer Support Plan = customer's plan tier
- top100 = `Yes` if the customer is a Flagship account
- Customer at Risk = per the customer's account-health signal
- Customer Name = contact name at the company

### Step 3 — Inspect the form

Use Chrome DevTools (or equivalent browser-control tooling) to navigate to the Product Bug form, take a snapshot, and confirm the field names, required-vs-optional flags, and the current `uid` mapping. Form structure can shift over time; inspection is the source of truth at fill time.

Expected required fields (as of 2026-06-04 — verify on inspect):

- Raise this request on behalf of (combobox; auto-filled to reporter)
- Summary (text)
- Severity (combobox, default `Severity 3`)
- Bug Description (rich text)
- Expected Behavior (rich text)
- Steps To Reproduce (rich text)
- Customer Company (text)

Expected optional fields: Identifiers, Datacenter, Recipe URL, Customer Name, Customer Support Plan, top100, Customer at Risk, Connector Name, Attachment, Log details.

### Step 4 — Draft Summary

One line. Leads with impact + names the affected component. No *"X is broken"* generics.

Format: `<area>: <component name> <verb-phrase impact>` or similar.

Example: `Workato Dev API MCP: post_api_collections_api_endpoints has invalid JSON Schema (draft 2020-12) — poisons Claude Code sessions`

If the bug is AIRO-related: **include "AIRO" in the Summary** (or in the Connector Name field). The form helper text requires it. CCE uses this for triage routing.

### Step 5 — Draft Bug Description (four labeled subsections)

Order: **IMPACT → DIAGNOSED CAUSE → ERROR → SCOPE.**

See `complete-check` §1.6 (inside the-once-over) for the per-subsection content checklist. See `say-it-plain` §3 for the register rules (no speculation, matter-of-fact, first-person attribution, load-bearing word reuse, literal error quotes, involuntariness explicit, named-component-in-IMPACT).

### Step 6 — Draft Expected Behavior

What the affected component should do. ≤2 sentences. Do not restate IMPACT in inverse.

### Step 7 — Draft Steps to Reproduce (two paths)

```
For CCE (observable in <user-facing client>):

1. <Step 1 — copy-pasteable>
2. <Step 2>
3. <Observed result — what the CCE engineer sees>

For engineering (direct):

<One-line pointer to the underlying-layer repro — e.g., "Validate the input_schema against draft 2020-12">
```

The CCE path lets a triage engineer confirm the bug from the user-facing surface (Claude Code, the Workato UI, a customer recipe). The engineering path lets the implementing team test the fix at the layer they control (schema validator, unit test, integration test on the raw artifact).

### Step 8 — Set Severity

Default is Severity 3. Calibrate by blast radius:

| Sev | When |
|---|---|
| **1** | Paid customer workloads taken down; data loss; security. |
| **2** | One bug wedges a session-wide or pipeline-wide failure (not a single call). |
| **3** | Single-call failure, intermittent, or in-session workaround exists. |
| **4** | Cosmetic or minor. |

Don't leave it at the form default unless the default genuinely matches the bug. Default Sev 3 is usually too low for session-wedging bugs.

### Step 9 — Draft Identifiers

Tool name, error path, ID-shaped identifiers only. Quote literal values; don't speculate on mappings.

For Workato-specific bug shapes, also surface (when applicable):

- **Job Handle** — `j-YYYYYYYY-ZZZZZZ` format; for recipe-execution bugs
- **Webhook link** — full webhook URL when the trigger is a webhook
- **X-Request-id** — when the bug is browser-side, from the Network tab
- **MCP tool name** — full `mcp__server__toolname` shape
- **Recipe ID** — numeric, e.g., from `app.workato.com/recipes/<id>`

### Step 10 — Draft Log details

Use for evidence that doesn't fit Bug Description's tight four-section shape:

- Probe / sweep tables establishing scope (e.g., "213 of 214 tools pass")
- Session-impact lists with first-person attribution and timestamps
- Brief interim mitigation suggestion (one short paragraph, no rationale tree)

For browser-side bugs: attach the HAR file (Network tab → Export HAR) instead of inlining the requests.

**Do NOT** use Log details for: speculation, *"where to look"* guesses, mechanism walkthroughs beyond the 1–2-sentence DIAGNOSED CAUSE.

### Step 11 — Set Customer Company, Customer Support Plan, top100

Per the profile chosen in Step 2.

For non-customer-driven: Customer Company = `Workato`, Customer Support Plan = `Not Defined`, top100 = `No`.

For customer-driven: fill per the customer's account record.

### Step 12 — Recipe URL (recipe bugs only)

If the bug is reproducible via a specific Workato recipe, paste the recipe URL with sharing token:

`https://app.workato.com/recipes/<id>?st=<token>`

Generate the token via: Recipe → Settings → Sharing → Generate link → Copy.

For non-recipe bugs (MCP, SDK, platform, AIRO, identity): leave blank.

### Step 13 — Run the-once-over (if available)

Invoke `the-once-over` on the draft. It routes the bug report through `fact-check` + `say-it-plain` (§1 + §2 + §3) + `complete-check` §1.6. Address any pillar fails before filling the form.

**Degraded mode** (the-once-over unavailable): apply the rules in `say-it-plain` §3 and `complete-check` §1.6 manually. The bug-filing rules in those pillar sections are self-contained.

### Step 14 — Fill the form

Fill each field via Chrome DevTools (`fill_form` for batch text inputs; `fill` + `press_key` for the combobox or for rich-text fields that need to be cleared first). Take a snapshot afterward to confirm the result.

Rich-text editor gotcha: the Bug Description / Expected Behavior / Steps to Reproduce / Identifiers / Log details fields are ProseMirror-based and don't accept markdown formatting via `fill`. Send plain text; the user can apply formatting (bold, code blocks) manually before submit if desired.

To replace existing content in a rich-text field (not append): `click` the field → `press_key Meta+A` → `press_key Backspace` → `fill` with new content.

### Step 15 — User reviews and submits

The user does the final visual review (formatting, severity choice, any custom bolding) and clicks `Send`. **This skill does not auto-submit.** The user is the final gate.

## Workato-specific carve-outs

### AIRO

For AIRO-related bugs (the AIRO connector, AIRO actions, AIRO triggers): include `AIRO` in the Summary, or in the Connector Name field. The Product Bug form has a banner saying so. CCE uses this for triage routing.

### SDK Connector bugs (separate portal)

Bugs in a *custom* connector built using the Connector SDK go to a different portal: `portal/4/group/1531/create/4063`. The Product Bug form has a banner pointing there. If the user describes a custom-connector bug, stop and redirect.

This carve-out does NOT apply to bugs in the Connector SDK gem *itself* — those are Product Bug.

### Recipe URL with sharing token

For recipe bugs: the URL must include the sharing token (`?st=<token>`). Without the token, CCE can't open the recipe and will request it. Generate the token via Settings → Sharing → Generate link → Copy.

### HAR file / X-Request-id (browser-side bugs)

For browser-side bugs (Workato UI, JavaScript errors, slow page loads), CCE expects either:

- A HAR file (Network tab → Export HAR), attached to the ticket
- An X-Request-id from a specific failing Network-tab request, in the Identifiers field

Both are documented in the CCE "How to submit an ideal ticket" Confluence page.

### Job Handle / Webhook link

For recipe-execution bugs: the Job Handle (`j-YYYYYYYY-ZZZZZZ`) goes in Identifiers or Summary. The Workato logs are massive; without the Job Handle, CCE can't search Kibana for the failure.

For webhook-triggered recipe bugs: include the webhook URL (`https://www.workato.com/webhooks/rest/<UUID>/<event>`). If the customer shared a recipe *copy* instead of the original, the webhook URL is the only way to identify the failing trigger.

## Bug report quality checklist (standalone)

Use this checklist at Step 13 when `the-once-over` is not available. When `the-once-over` IS available, invoke it instead — it runs these checks plus `fact-check` and the full `say-it-plain` pass.

**Bug Description — four labeled subsections, in order:**
- [ ] IMPACT present and named first
- [ ] DIAGNOSED CAUSE present, ≤3 sentences (cause + mechanism)
- [ ] ERROR present
- [ ] SCOPE present

**IMPACT:** names the component by name (no "a tool" / "the system" generics); first-person for reporter observations; involuntariness explicit; one-line in-the-wild impact if available.

**DIAGNOSED CAUSE:** cause in 1 sentence; mechanism in 1–2 sentences; reuses the load-bearing word from IMPACT; no speculation (no "probable," "likely," "common causes include").

**ERROR:** literal error string, not paraphrased.

**SCOPE:** numeric ratio (e.g., "1 of 214 tools," "3 of 50 customers").

**Steps to Reproduce:** two paths — (A) observable from user-facing client, (B) direct at the layer engineering fixes; each step copy-pasteable; each path names its audience.

**Severity:** calibrated by blast radius, not frequency; not left at form default unless it genuinely matches.

**Speculation / teaching ban:**
- [ ] No "probable" / "likely" in fact-claiming positions
- [ ] No "where to look" / "common causes include" / "things to check" guesses
- [ ] No mechanism-walk paragraphs beyond the 1–2-sentence DIAGNOSED CAUSE
- [ ] No platform-overview / "how it normally works" preambles

Source: `complete-check §1.6`. The register rules (matter-of-fact, no speculation, first-person) are in `say-it-plain §3` — apply those too.

## Composition with the-once-over

This skill assumes `the-once-over` exists and can be invoked at Step 13. If unavailable, use the **Bug report quality checklist** section above plus `say-it-plain §3`.

If you're filing on a non-Workato system, the general rubric still applies but the form URLs, customer metadata, and AIRO carve-out don't. Run `the-once-over` directly on the draft.

## What this skill is NOT

- **Not for SDK Connector bugs** — those go to a different portal. Redirect.
- **Not for general bug-filing on non-Workato systems** — the workflow is Workato-CCE-specific. The general rubric (`say-it-plain` §3 + `complete-check` §1.6) transfers; the form / portal / metadata specifics don't.
- **Not an auto-submitter** — fills the form for user review; the user submits.
- **Not a bug diagnoser** — the user comes in with a diagnosed cause. This skill helps file the report, not figure out the cause.

## Logging

At completion, invoke: `skill-logger file-workato-product-bug` (if `skill-logger` is available in the current environment; skip silently if not). This collects org-wide usage telemetry.

## Tape

At the end of a session where this skill was used, if any decisions were made that overrode, extended, or notably validated these rules — or if the bug report revealed a gap in the CCE form field knowledge — offer to run `the-tape` to capture the decision. Skip silently if `the-tape` is not installed.
