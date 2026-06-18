---
title: Usage Data-Informed Design Decisions
addie_phase: Project Prep
prompt_order: 3
confluence_page_id: 2446033027
confluence_version: 3
confluence_version_date: 2026-05-06
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2446033027
---

**ADDIE Phase:** Project Prep (Pre-Analyze) runs early — parallel with or shortly after Customer Voice

**Purpose:** Use actual product usage patterns, adoption metrics, and behavioral data to prioritize learning content, identify where users struggle, and sequence instruction based on real-world workflows instead of assumptions. This prompt ensures learning design aligns with how customers actually use the product.

**Position:** Runs at the start of a new course or learning path, alongside Customer Voice and Content Audit. Can run independently, but produces stronger findings when cross-referenced with Customer Voice data (what customers _say_ vs. what they actually _do_). Its output feeds Audience Profile, Needs Analysis, Learning Objectives, Detailed Outline, Script Drafting, and Knowledge Checks.

### When to use

* **After Customer Voice (preferred) or in parallel.** If Customer Voice has already run, this prompt cross-references reported pain points and misconceptions with actual behavioral data. If Customer Voice hasn't run yet, this prompt still works — it just can't validate whether what customers say matches what they do.
* **During Needs Analysis** to prioritize which capabilities to teach based on real adoption and struggle data, not assumptions.
* **When sequencing learning objectives** — teach high-impact, high-struggle workflows first.
* **When designing knowledge checks** — focus assessments on real drop-off points and failure modes.

### Optional upstream artifact

* **Customer Voice Research Brief** — specifically Section A (Pain Points) and Section D (Misconception Inventory). If available, Usage Data cross-references behavioral data against reported pain points and misconceptions. Findings that confirm (or contradict) Customer Voice data are tagged for traceability.

````markdown
You are analyzing product usage data for **[product/feature]** to inform instructional design priorities for Workato Academy. Your goal is to identify high-impact workflows, understand where users struggle or abandon features, and correlate usage patterns with customer success outcomes. Use these insights to ground learning objectives, module sequencing, and assessment design in real user behavior.

This usage data brief is an **early-pipeline deliverable** — its output will be retrieved and consumed by Audience Profile, Needs Analysis, Learning Objectives, Outline, Scripts, and Knowledge Checks. Structure your output precisely as specified below so downstream prompts can reference sections by letter.

### Step 0: Retrieve Upstream Artifacts (if available)

Before beginning the usage analysis, check whether a **Customer Voice Research Brief** exists for this course. The user will tell you where it lives (file path, Confluence page, or Google Doc).

**If available, retrieve and hold:**
- Section A (Pain Point Summary) — the 3–5 pain themes customers express
- Section D (Misconception Inventory) — the numbered misconceptions with frequency and severity

**How to use these during analysis:**
- When identifying struggle points (Step 2) and failure modes (Step 5), check whether they correlate with reported pain points or misconceptions. Tag correlations:
  - "[Confirms CV-A#]" — behavioral data confirms a pain point from Customer Voice Section A
  - "[Confirms CV-D#]" — behavioral data confirms a misconception from Customer Voice Section D
  - "[Contradicts CV-A#]" — customers report a pain point but usage data doesn't show it as a real struggle (or vice versa)
  - "[New — not in CV]" — usage data reveals a struggle point that customers didn't report in calls
- These tags help downstream prompts (especially Audience Profile and Needs Analysis) distinguish between validated findings (confirmed by both voice and data) and single-source findings.

**If the Customer Voice brief doesn't exist yet:** Proceed with the analysis — usage data stands on its own. Note in Section B that cross-referencing with Customer Voice would strengthen the findings.

---

#### Step 1: Query Adoption Metrics

Using Workato's data warehouse, query usage data for **[product/feature]**:

**Basic adoption metrics to pull:**
- **Overall adoption rate:** What % of customers with access to **[feature]** have activated it?
- **Active user rate:** Of those who activated, what % use it regularly (e.g., weekly/monthly)?
- **Feature engagement:** Which specific capabilities within **[feature]** see the most usage?
- **Workflow completion rate:** What % of users who start a workflow complete it successfully?

**Cohort breakdowns (if data allows):**
- Adoption by customer segment (Enterprise vs. SMB, industry verticals)
- Adoption by user role (Admin, Builder, End User)
- Time-to-first-value: How long from account creation to first meaningful use of **[feature]**?

#### Step 2: Identify Drop-Off Points

Analyze usage funnels to find where users abandon workflows or stop using features:

**Look for:**
- **Activation drop-off:** Users enable **[feature]** but never configure it or create their first object
- **Configuration drop-off:** Users start setup but don't complete all required steps
- **First-use drop-off:** Users complete setup but never run a real workflow
- **Sustained-use drop-off:** Users try the feature once or twice, then stop

**For each drop-off point, document:**
- Stage in the user journey where drop-off occurs
- Percentage of users who drop off at this stage
- Hypothesis: Why might users abandon at this point? (complexity? unclear value? missing prerequisite knowledge?)

#### Step 3: Compare Power Users vs. Low Adopters

Identify behavioral differences between successful users and struggling users:

**Segment users into cohorts:**
- **Power users:** Top 10–20% by usage volume or workflow complexity
- **Moderate users:** Middle 60–70%, consistent but basic usage
- **Low adopters:** Bottom 10–20%, minimal or abandoned usage

**For each cohort, analyze:**
- What capabilities do they use differently?
- Do power users follow specific setup patterns that low adopters skip?
- Do power users combine **[feature]** with other Workato products more often?
- What's the time gap between first use and reaching "power user" status?

#### Step 4: Correlate Usage with Business Outcomes

If possible, correlate **[feature]** usage with customer health and business metrics:

**Queries to run:**
- Does adoption of **[feature]** correlate with higher customer health scores?
- Do customers who use **[feature]** have higher ARR or lower churn?
- Do customers who adopt **[feature]** expand to other Workato products more often?
- Are there "leading indicator" behaviors (e.g., completing specific workflows) that predict long-term success?

**Document:**
- Features/workflows that correlate with customer success (prioritize teaching these)
- Features/workflows that don't correlate with value (consider de-emphasizing in training)
- Minimum viable usage patterns: "What's the threshold of usage that predicts sticky adoption?"

#### Step 5: Identify Common Failure Modes

Review error logs, failed workflows, or support tickets related to **[feature]**:

**Look for:**
- Most common error messages users encounter
- Workflows that fail frequently (due to misconfiguration, missing data, etc.)
- Support tickets that reveal knowledge gaps ("How do I...?" questions)

**For each failure mode, document:**
- What error or failure occurs?
- What % of users encounter this?
- What's the root cause? (User error? Product limitation? Unclear documentation?)
- Implication for learning: What should we teach differently to prevent this?

#### Step 6: Synthesize for Instructional Design

Consolidate all research into the structured output sections below. **Use the exact section letters and headers** — downstream prompts reference them by letter.

---

### Output Deliverable: Usage Data-Informed Design Brief

Begin the document with this metadata header:

```
---
Document: Usage Data-Informed Design Brief
Course/Path: [name]
Topic: [product/feature]
Date: [date generated]
Upstream artifacts used: [e.g., "Customer Voice Research Brief (dated [X])" or "None — Customer Voice not yet available"]
Data sources queried: [list — e.g., Data warehouse (adoption metrics, funnel data), Support tickets (Zendesk/Slack), Error logs]
Data timeframe: [e.g., "Last 90 days" or "Jan–Apr 2026"]
Recommended refresh: [date + 3 months — usage data goes stale faster than customer voice]
---
```

---

#### Section A: Priority Workflow Ranking

Ranked list of workflows to teach, ordered by instructional priority. This directly informs module sequencing and lesson emphasis.

For each workflow:

```
A[#]. [Workflow name]

Usage frequency: [High / Medium / Low] — [metric: e.g., "Used by 72% of active accounts"]
Success correlation: [High / Medium / Low] — [metric: e.g., "Accounts that complete this have 2.3x higher health scores"]
Drop-off risk: [High / Medium / Low] — [metric: e.g., "38% of users who start this workflow abandon before completion"]
Teaching priority: [1–5 ranking, with 1 = highest]
Rationale: [1 sentence — why this ranking, based on the combination of frequency, correlation, and risk]
CV cross-reference: [Confirms CV-A# / Contradicts CV-A# / New — not in CV / Not evaluated]
```

**Downstream use:** Needs Analysis consumes this to inform module scope and sequencing priority. Detailed Outline uses the ranking to order lessons — high-priority workflows get earlier and deeper coverage. Learning Objectives uses success correlation to determine which outcomes matter most.

**🔵 Confidence:** [High / Medium / Low] — [Basis: data completeness, sample size, timeframe. What would change it — e.g., "Adoption data is strong (full customer base), but success correlation is based on health scores which may lag real outcomes by 60+ days."]

---

#### Section B: Struggle Point Inventory

Top 3–5 points where users struggle, structured as numbered items for downstream reference.

For each struggle point:

```
B[#]. [Descriptive label]

What happens: [Observable behavior — e.g., "60% of users abandon during initial configuration of [feature]"]
Where in the journey: [Stage — activation / configuration / first use / sustained use]
Metric: [Quantified — % of users affected, error frequency, etc.]
Hypothesized cause: [Why users struggle — complexity, missing prerequisite, unclear value, UX issue]
CV cross-reference: [Confirms CV-A# / Confirms CV-D# / New — not in CV / Not evaluated]
Design implication: [What to do about it in the course]
Scaffolding needed: [Specific support — e.g., "Guided setup walkthrough in Module X; configuration checklist job aid"]
```

**Downstream use:** Audience Profile consumes these for Section 2A (existing knowledge gaps) and Section 3B (performance gap summary). Needs Analysis uses them to ground the performance gap analysis in behavioral data, not assumptions. Detailed Outline uses them to place scaffolding at the right point in the sequence. Knowledge Checks uses struggle points as scenario stems.

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

#### Section C: Adoption Barrier Analysis

Gaps between what users need to know and what they arrive with — structured as barriers the course must address.

For each barrier:

```
C[#]. [Barrier label]

Barrier: [What prevents successful adoption — e.g., "Users don't understand prerequisite concept [X] before attempting to use [feature]"]
Evidence: [Usage data supporting this — e.g., "80% of failed workflows trace back to misconfigured [X]"]
Affected cohort: [Which user segment — all users, specific persona, specific segment]
CV cross-reference: [Confirms CV-D# / New — not in CV / Not evaluated]
Design implication: [What the course must do — e.g., "Add prerequisite module or lesson explicitly teaching [X] before introducing [feature]"]
```

**Downstream use:** Audience Profile consumes these for Section 5 (prerequisite mapping) — adoption barriers often reveal missing prerequisites. Needs Analysis uses them to distinguish between gaps training can close and gaps that require other interventions. Knowledge Checks uses barriers as realistic scenario contexts.

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

#### Section D: Success Pattern Insights

What power users do that others don't — these become the "target behaviors" the course teaches toward.

For each pattern:

```
D[#]. [Pattern label]

What successful users do: [Specific behavior — e.g., "Complete [specific workflow] within their first week"]
What others do instead: [Contrasting behavior of low adopters]
Impact: [Quantified difference — e.g., "Users who do this are 3x more likely to reach active user status"]
Time dimension: [When in the user journey this pattern matters — e.g., "First 7 days", "After first 3 workflows"]
Design implication: [How to use this in the course — e.g., "Emphasize this workflow early in the learning path; make it a capstone activity for Module X"]
Proof point for narration: [A stats-ready sentence for Script Drafting — e.g., "Customers who complete [workflow] in their first week are 3x more likely to become active long-term users."]
```

**Downstream use:** Audience Profile consumes these for Section 4A (motivation — what success looks like) and Section 3A (target state — what we're teaching toward). Script Drafting uses the proof points and success examples in narration. Detailed Outline uses patterns to design capstone activities and success milestones.

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

#### Section E: Business Outcome Correlations

Quantified connections between feature usage and business metrics — these serve as proof points in narration and strategic context for Needs Analysis.

For each correlation:

```
E[#]. [Correlation label]

Finding: [e.g., "Accounts with active [feature] usage have 1.4x higher NRR than accounts without"]
Metric: [Specific numbers]
Causation caveat: [Is this causal or just correlated? Be honest — e.g., "Correlation — accounts that adopt [feature] may already be healthier"]
Source: [Data warehouse query / Salesforce report]
Use in narration: [A ready-to-use proof point sentence — e.g., "Organizations using [feature] see 40% higher net revenue retention."]
Use in strategic context: [How this supports MBO or business case — e.g., "Supports M5: 15% product adoption rate target"]
```

**Downstream use:** Script Drafting uses narration-ready proof points. Needs Analysis uses strategic context to justify course priority and investment. Storyboarding uses metrics for on-screen data callouts.

**🔵 Confidence:** [High / Medium / Low] — [Basis: sample size, timeframe, causation vs. correlation. What would change it.]

---

### Cross-Reference Summary (if Customer Voice was available)

If Customer Voice data was retrieved in Step 0, close with a cross-reference summary:

| Customer Voice Finding | Usage Data Confirmation | Status |
|---|---|---|
| CV-A1: [Pain point] | [Corresponding usage finding, or "No behavioral signal found"] | Confirmed / Contradicted / Unvalidated |
| CV-D1: [Misconception] | [Corresponding failure mode or drop-off, or "No behavioral signal found"] | Confirmed / Contradicted / Unvalidated |

**Key insight from cross-referencing:** [1–2 sentences — what did comparing voice data to behavioral data reveal? e.g., "Pain point A2 (configuration complexity) is strongly confirmed by usage data — it's the #1 drop-off point. However, misconception D3 (confusing MCP with standard API access) doesn't show up in failure modes, suggesting customers recognize the distinction once they're in the product even if they describe it incorrectly in calls."]

---

### Document-Level Confidence Statement

> **🔵 Overall Confidence: [High / Medium / Low]**
> [2–3 sentences: Data completeness (were all relevant metrics accessible?). Sample size and timeframe. Which sections are strongest. Which sections have data gaps — e.g., "Adoption metrics (Section A) are strong — full customer base, 90-day window. Success patterns (Section D) are Medium confidence — based on a smaller cohort of 50 power users. Business outcome correlations (Section E) are Low confidence — health score data lags by 60+ days and may not reflect recent product changes."]

---

### Appendix: Query Log

| Query | Data Source | Timeframe | Result Summary | Section(s) Informed |
|---|---|---|---|---|
| [Query description] | [Data warehouse / Salesforce / Support] | [Date range] | [Brief — e.g., "72% adoption rate, 38% config drop-off"] | A, B |

---

Write in clear, professional prose. Use the section headers and letters exactly as specified — downstream prompts reference sections by letter (e.g., "retrieve Usage Data Section B"). Flag any section where data is unavailable or insufficient with **[LOW DATA — needs additional sources]** and explain what's missing.
````
