---
title: Content Audit & Gap Analysis
addie_phase: Project Prep
prompt_order: 2
confluence_page_id: 2467004727
confluence_version: 4
confluence_version_date: 2026-05-06
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2467004727
---

**ADDIE Phase:** Project Prep (Pre-Analyze) runs early — parallel with or shortly after Customer Voice

**Purpose:** Prevent redundancy, identify reusable content, understand what already exists, and surface gaps before investing in new content creation. This prompt maps the existing knowledge ecosystem so instructional design decisions are informed by what's already available.

**Position:** Runs at the start of a new course or learning path, alongside Customer Voice and Usage Data. Can run independently, but produces a stronger gap analysis if Customer Voice has already been completed (pain points and use cases help evaluate whether existing content addresses the right problems). Its output feeds Needs Analysis, Audience Profile, Detailed Outline, Script Drafting, and Storyboarding.

### When to use

* **After Customer Voice (preferred) or in parallel.** If Customer Voice has already run, this prompt retrieves pain points and use cases to evaluate existing content against real customer needs — not just topic coverage. If Customer Voice hasn't run yet, this prompt still works, just with a less targeted gap analysis.
* **Before Needs Analysis.** The content inventory and stability assessment feed directly into the Needs Analysis Module Scope Map (content status and stability ratings).
* **Before Detailed Outline.** Reuse opportunities and stability flags inform which lessons can leverage existing content and which topics need careful handling.
* **When consolidating or sunsetting old content.** The redundancy assessment identifies what to deprecate when new content launches.

### Optional upstream artifact

* **Customer Voice Research Brief** — specifically Section A (Pain Points) and Section C2 (Use Case Inventory). If available, Content Audit uses these to evaluate whether existing content addresses the problems and workflows customers actually care about. If not available, Content Audit evaluates content by topic coverage only.

````
You are conducting a comprehensive content audit for **[product/feature/topic]** to inform instructional design decisions for Workato Academy content. Your goal is to map what content already exists across all organizational repositories, assess its quality and relevance, identify gaps, and recommend what to reuse vs. create from scratch.

This content audit is an **early-pipeline deliverable** — its output will be retrieved and consumed by Needs Analysis, Detailed Outline, Script Drafting, and Storyboarding. Structure your output precisely as specified below so downstream prompts can reference sections by letter.

### Step 0: Retrieve Upstream Artifacts (if available)

Before beginning the audit, check whether a **Customer Voice Research Brief** exists for this course. The user will tell you where it lives (file path, Confluence page, or Google Doc).

**If available, retrieve and hold:**
- Section A (Pain Point Summary) — the 3–5 pain themes customers express
- Section C2 (Use Case Inventory) — the 5–7 real customer workflows

**How to use these during the audit:**
- When evaluating existing content (Steps 1–5), assess not just "does content on this topic exist?" but "does existing content address the pain points and use cases customers actually have?"
- In the Gap Analysis (Section B), flag gaps where existing content covers the topic but misses the customer's actual problem or workflow
- Tag any gap analysis finding that was informed by Customer Voice data as "[CV-informed]" for traceability

**If the Customer Voice brief doesn't exist yet:** Proceed with the audit — evaluate content by topic coverage. Note in Section B that gap analysis could be strengthened by running Customer Voice research.

---

#### Step 1: Search Internal Documentation (Google Drive)

Search Drive for existing documentation on **[product/feature/topic]**:
- **Query terms:** "[feature] guide", "[feature] documentation", "[feature] how-to", "[feature] training", "[product] setup", "[product] best practices"
- **File types:** Docs, Slides, PDFs, Sheets (for matrices or decision frameworks)
- **Folders to check:** Product documentation, Solutions Engineering, Customer Success, Academy archives

**For each relevant document found, record:**
- Title and Drive link
- Owner/author
- Last updated date
- Content summary (2–3 sentences: what does it cover?)
- Target audience (internal/external, persona, skill level)
- Format (long-form doc, quick reference, video walkthrough, diagram)
- Quality assessment (accurate? current? well-structured? or outdated/incomplete?)

#### Step 2: Search Sales/Marketing Content (Highspot)

Search Highspot for customer-facing or sales enablement content:
- **Query terms:** Same as Step 1, plus "[feature] pitch", "[product] demo", "[feature] competitive"
- **Content types:** Pitch decks, product sheets, demo videos, battle cards, customer decks

**For each relevant asset found, record:**
- Title and Highspot link
- Content type (pitch, demo, one-pager, etc.)
- Last updated date
- What positioning/messaging does it use? (how is the feature framed for customers?)
- What proof points or examples does it include?
- Quality assessment (approved? current? or needs refresh?)

#### Step 3: Search Internal Discussions (Slack)

Search relevant Slack channels for recent discussions about **[product/feature]**:
- **Channels to check:** #product-[name], #solutions-engineering, #customer-success, #academy-internal, #enablement
- **Query terms:** "[feature]", "[product] release", "[feature] update", "[feature] issue", "[feature] question"
- **Timeframe:** Last 6 months

**Document:**
- Threads discussing **product updates** (new capabilities, deprecations, breaking changes)
- Threads discussing **known issues** or **workarounds**
- Threads where **SMEs answer technical questions** (reveals what's confusing)
- Threads showing **customer feedback** or requests for better documentation/training

**Key insights to extract:**
- Is the product stable or rapidly evolving?
- What are recent changes that existing content may not reflect?
- What do internal teams wish was documented better?
- What technical nuances or edge cases are commonly discussed?

#### Step 4: Review Existing Academy Modules

Start with the **Education Content Inventory** spreadsheet as the primary source of existing Academy courses and modules:
- **Location:** [Google Sheets — Education Content Inventory](https://docs.google.com/spreadsheets/d/1rFV2drpfTBI8JfkSluKKET_GMsQPM-fC2g4_vKf-6Tc/edit?gid=170263460#gid=170263460)
- Read the spreadsheet via Google Drive and filter for courses related to **[product/feature/topic]** — check course titles, descriptions, and topic tags.

**Important:** This inventory may not be fully up to date. After reviewing it, cross-check by searching Confluence (ETT space) and Google Drive for any recently launched or in-development courses that may not have been added to the inventory yet. If you find courses missing from the inventory, flag them in your output so the inventory can be updated.

**For any related modules found (from the inventory or other sources):**
- Module title and link (Docebo link if available, or Confluence project page)
- What learning objectives does it cover?
- What overlap exists with the new module being planned?
- What prerequisite knowledge does it establish that the new module can build on?
- What content could be cross-referenced vs. duplicated?
- **Inventory status:** [In inventory / Missing from inventory — flag for update]

#### Step 5: Assess External Workato Resources

Check public-facing resources:
- **Workato Docs** (docs.workato.com): Official product documentation
- **Community** (community.workato.com): User discussions, troubleshooting threads
- **Blog** (workato.com/the-connector): Thought leadership, use case articles

**Document:**
- What official documentation exists? Is it comprehensive or sparse?
- What community questions/threads show user confusion?
- What blog content could be repurposed or linked?

#### Step 6: Synthesize Findings

Consolidate all research into the structured output sections below. **Use the exact section letters and headers** — downstream prompts reference them by letter.

---

### Output Deliverable: Content Audit & Gap Analysis Report

Begin the document with this metadata header:

```
---
Document: Content Audit & Gap Analysis Report
Course/Path: [name]
Topic: [product/feature]
Date: [date generated]
Upstream artifacts used: [e.g., "Customer Voice Research Brief (dated [X])" or "None — Customer Voice not yet available"]
Sources searched: [list — e.g., Google Drive, Highspot, Slack (#solutions-engineering, #product-x), Academy catalog, Workato Docs, Community]
Recommended refresh: [date + 6 months, or sooner if product is rapidly evolving]
---
```

---

#### Section A: Content Inventory

Full table of all existing assets found across all sources.

| # | Content Asset | Type | Location | Owner | Last Updated | Target Audience | Quality | Pain Points Addressed | Reusable? |
|---|---|---|---|---|---|---|---|---|---|
| A1 | [Title] | [Doc/Deck/Video/etc.] | [Link] | [Author] | [Date] | [Persona / skill level] | [Current / Outdated / Incomplete] | [List pain point themes from CV Section A this addresses, or "Not evaluated" if CV not available] | [Yes / Partial / No] |

**Downstream use:** Needs Analysis consumes this to set "Content status" per module (Exists / Adapt / Net-new). Detailed Outline references specific assets for reuse per lesson.

**🔵 Confidence:** [High / Medium / Low] — [Basis: how thoroughly each source was searched, whether all relevant repositories were accessible. What would change it.]

---

#### Section B: Gap Analysis

For the planned course/module, map what's covered vs. what's missing.

##### B1: Topics with existing coverage
For each topic/objective that existing content addresses:
- **Topic:** [What's covered]
- **Covered by:** [Asset # from Section A]
- **Coverage quality:** Complete / Partial / Outdated
- **Customer relevance:** [If CV available: Does this content address the pain points and use cases customers actually have? Or does it cover the topic from a different angle?] [CV-informed] or [Topic-only assessment]

##### B2: Gaps — topics with no existing coverage
For each topic/objective that no existing content covers:
- **Gap:** [What's missing]
- **Why it matters:** [Impact on learning if this gap isn't filled]
- **Customer relevance:** [If CV available: Does this gap align with a documented pain point or use case?] [CV-informed] or [Not evaluated]
- **Build priority:** High / Medium / Low

##### B3: Gaps — existing content that's outdated or misleading
For each piece of existing content that's no longer accurate:
- **Asset:** [Reference from Section A]
- **What's wrong:** [Outdated info, incorrect procedures, deprecated features]
- **Risk if not addressed:** [What happens if a learner or colleague encounters this?]
- **Recommended action:** Update / Deprecate / Replace with new module

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

#### Section C: Redundancy Risk Assessment

Identify overlap that could cause confusion or duplicate effort.

For each redundancy found:
- **Redundancy type:** Direct overlap / Partial overlap / Conflicting framing
- **Assets involved:** [References from Section A]
- **Risk:** [What goes wrong if both exist — e.g., "Learners encounter conflicting instructions on configuring X"]
- **Recommended resolution:** Consolidate / Deprecate one / Scope boundaries clearly / Cross-reference

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

#### Section D: Reuse Opportunities

Categorize existing assets by recommended action.

##### D1: Reuse as-is
Assets that can be linked or embedded directly without modification.
- **Asset:** [Reference from Section A]
- **Use in new course:** [Where/how — e.g., "Link as prerequisite reading before Module 2"]

##### D2: Adapt / Update
Assets that are 80%+ there but need refresh or reframing.
- **Asset:** [Reference from Section A]
- **What needs changing:** [Specific updates needed]
- **Estimated effort:** Low / Medium
- **Use in new course:** [Where/how]

##### D3: Repurpose
Assets where specific elements (diagrams, examples, proof points, screenshots) can be extracted.
- **Asset:** [Reference from Section A]
- **Element to extract:** [What specifically]
- **Use in new course:** [Where/how]

##### D4: Replace / Deprecate
Assets that should be sunset when the new course launches.
- **Asset:** [Reference from Section A]
- **Why:** [Outdated / superseded / causing confusion]
- **Deprecation plan:** [Archive? Redirect? Delete?]

**Downstream use:** Detailed Outline references D1–D3 when specifying reusable assets per lesson. Storyboarding uses D3 for existing visual assets.

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

#### Section E: Freshness & Stability Assessment

**This section is consumed by every downstream prompt that produces content.** Structure it as a per-topic stability profile so downstream prompts can apply the right flag to each lesson or script section.

##### E1: Overall Product Stability
- **Product/feature:** [Name]
- **Stability status:** Stable / Actively evolving / In beta / Undergoing major redesign
- **Recent changes (last 6 months):** [List significant updates, releases, or deprecations found in Slack and docs]
- **Upcoming changes (if known):** [Roadmap items mentioned in Slack or SME conversations]
- **Documentation currency:** [Is official documentation keeping pace with product changes?]

##### E2: Per-Topic Stability Ratings

For each major topic or capability the course will cover:

```
E2.[#]. [Topic/capability name]

Stability rating: [Evergreen / Moderately Stable / High Maintenance]
  - Evergreen: Core concept unlikely to change. Safe to teach definitively.
  - Moderately Stable: Implementation details may shift, but concepts hold.
    Teach concepts; be cautious with specific UI steps.
  - High Maintenance: Actively changing. Screenshots will go stale.
    Teach principles and patterns; flag specific steps as version-sensitive.

Last verified: [Date of most recent source confirming current state]
Evidence: [What sources inform this rating — Slack threads, release notes, doc update dates]
Known upcoming changes: [If any — "None known" is a valid answer]
Downstream flags:
  - Outline: [Should this topic carry a ⚠️ stability flag in the lesson?]
  - Script: [Should the script prefer concepts over specific UI steps?]
  - Storyboard: [Should screenshots carry version-sensitivity flags in production notes?]
```

##### E3: Maintenance Burden Forecast
- **Estimated update frequency:** [How often will this course need content refreshes — quarterly? Biannually? Only on major releases?]
- **Highest-risk sections:** [Which topics/modules will need updates most frequently?]
- **Maintenance trigger:** [What event should prompt a content review — e.g., "Any release note mentioning [feature]"]

**Downstream use:** Needs Analysis consumes E2 ratings for the Module Scope Map stability column. Detailed Outline applies ⚠️ stability flags to lessons covering Moderately Stable or High Maintenance topics. Script Drafting uses E2 downstream flags to decide whether to write concept-focused or procedure-focused narration. Storyboarding uses E2 downstream flags to set version-sensitivity on screenshots. The future Course Maintenance Genie inherits E2 and E3 for post-publication drift detection.

**🔵 Confidence:** [High / Medium / Low] — [Basis: How many sources confirm each stability rating. How recent is the evidence. What would change it — e.g., "Stability rating for [topic] is Medium confidence — based on Slack discussion from 3 months ago. A quick check with SME would confirm whether the Q3 release changed this."]

---

### Document-Level Confidence Statement

> **🔵 Overall Confidence: [High / Medium / Low]**
> [2–3 sentences: How thoroughly sources were searched. Whether any major repositories were inaccessible. Which sections are strongest. Which sections have gaps — e.g., "Academy catalog search was comprehensive but Highspot returned sparse results — Sales may have content in a different location. Section E stability ratings for [topics X and Y] need SME confirmation."]

---

### Appendix: Source Log

| Source Type | Source / Link | Date Accessed | What was found | Section(s) it informed |
|---|---|---|---|---|
| Google Drive | [Doc title / link] | [Date] | [Brief note] | A, B, D |
| Highspot | [Asset title / link] | [Date] | [Brief note] | A, B, E |
| Slack | [Channel + thread] | [Date] | [Brief note] | E |
| Academy | [Module title] | [Date] | [Brief note] | A, B, C |
| Workato Docs | [Page / section] | [Date] | [Brief note] | B, E |
| Community | [Thread / topic] | [Date] | [Brief note] | B |

---

Write in clear, professional prose. Use the section headers and letters exactly as specified — downstream prompts reference sections by letter (e.g., "retrieve Content Audit Section E2"). Flag any section where data is thin with **[LOW DATA — needs additional sources]** and explain what's missing.
````

## How this prompt connects to the pipeline

| Upstream Source | What Content Audit retrieves | How it's used |
| --- | --- | --- |
| **Customer Voice Section A** (Pain Points) | Optional — retrieved in Step 0 | Evaluates whether existing content addresses real customer pain points, not just topic coverage |
| **Customer Voice Section C2** (Use Cases) | Optional — retrieved in Step 0 | Evaluates whether existing content covers real customer workflows |

### Downstream consumers

| Consumer | What it retrieves | Which section(s) |
| --- | --- | --- |
| **Needs Analysis** | Content status per module, stability ratings, existing content gaps | Sections A, B, E |
| **Audience Profile** | Stability data for prerequisite confidence assessment | Section E |
| **Detailed Outline** | Reuse opportunities per lesson, stability flags per topic | Sections D, E |
| **Script Drafting** | Stability flags — scripts for unstable topics prefer concepts over specific UI steps | Section E |
| **Storyboarding** | Stability flags → version sensitivity on screenshots | Section E |
