---
title: Customer Voice & Proof Point Research
addie_phase: Project Prep
prompt_order: 1
confluence_page_id: 2434007423
confluence_version: 3
confluence_version_date: 2026-05-06
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2434007423
---

**ADDIE Phase:** Project Prep (Pre-Analyze)

**Purpose:** Ground instructional content in authentic customer language, pain points, success stories, and quantifiable outcomes. This prompt transforms abstract learning goals into customer-informed design decisions.

**Position:** This is the **first deliverable** in the ADDIE pipeline. It has no upstream dependencies — run it at the very start of a new course or learning path. Its output feeds directly into Audience Profile, Needs Analysis, Learning Objectives, Detailed Outline, Script Drafting, Knowledge Checks, and Storyboarding.

## When to use:

* **Before everything else.** Run this prompt at the start of a new course or learning path, before Needs Analysis, before Audience Profile, before anything. It produces the customer data foundation that every downstream deliverable builds on.
* **Before Design:** Downstream prompts (Script Drafting, Knowledge Checks) will retrieve this brief and extend it with lesson-specific research. Running Customer Voice first means those prompts start from real data instead of re-running broad research from scratch.
* **Review with SMEs:** Share findings with product team SMEs to validate interpretations before the data flows downstream.
* **Before Knowledge Check generation:** Use confusion patterns and real scenarios to create authentic assessment questions
* **Privacy:** Always anonymize customer details in learning content unless explicitly approved for external use
* **Refresh cadence:** Re-run this research every 6 months or when major product updates occur

### No upstream inputs required

This prompt queries data sources directly. You just need:

* The course/feature topic
* Access to Gong, Salesforce, Highspot, Google Drive, and Slack (via Otto/MCP)

## Prompt

````markdown
You are researching customer perspectives on **[product/feature/capability]** to inform instructional design for Workato Academy. Your goal is to extract authentic customer voice, identify real pain points, document success patterns, and gather quantifiable proof points that will ground learning content in actual business value.

This research brief is the **first deliverable in the ADDIE pipeline** — its output will be retrieved and consumed by every downstream prompt (Audience Profile, Needs Analysis, Learning Objectives, Outline, Scripts, Assessments, Storyboard). Structure your output precisely as specified below so downstream prompts can reference sections by letter.

#### Step 1: Search Customer Conversations

Using Gong, search for customer calls that mention **[product/feature]** from the past 6 months. Look for:
- Discovery calls where customers describe their problems before considering Workato
- Implementation calls where customers work through configuration or adoption challenges
- Success calls where customers describe outcomes and value realized
- Troubleshooting calls that reveal common confusion points or misunderstandings

**Search parameters:**
- Keywords: [product/feature name], [related capabilities], [use case terms]
- Timeframe: Last 6 months (or specify custom range)
- Call types: Discovery, implementation, QBR, troubleshooting
- Target: 10-15 calls minimum for pattern recognition

#### Step 2: Extract Pain Points (Pre-Adoption)

For each relevant call, document:
- **Customer's exact language** describing their problem (use direct quotes)
- **Business impact** they describe (time wasted, errors, manual work, compliance risk)
- **What they tried before** (workarounds, competitor tools, manual processes)
- **Trigger event** that made them seek a solution (new regulation, growth, acquisition, incident)

**Output format:**
```
Pain Point Theme: [Descriptive label]
Customer Quote: "[Exact words from call]"
Business Impact: [Quantified when possible]
Context: [Company size, industry, use case]
Source: [Gong call ID and date]
```

#### Step 3: Extract Success Stories (Post-Adoption)

For customers who successfully adopted the feature, document:
- **Value realized** in their own words (direct quotes)
- **Quantifiable outcomes** (time saved, error reduction, cost savings, speed improvement)
- **Before/after workflows** they describe
- **Surprising benefits** they mention (unintended positive outcomes)
- **What made it successful** (their perspective on why it worked)

**Output format:**
```
Success Story: [Customer name/segment]
Outcome Quote: "[Exact words describing value]"
Metrics: [Quantified improvements]
Use Case: [Specific workflow or business process]
Success Factors: [What made this work]
Source: [Gong call ID and date]
```

#### Step 4: Identify Common Confusion Points

Analyze troubleshooting and implementation calls to find:
- **Concepts customers misunderstand** (what do they think it does vs. what it actually does?)
- **Configuration mistakes** they commonly make
- **Questions they repeatedly ask** across multiple calls
- **Gaps between expectation and reality**

**Output format:**
```
Confusion Pattern: [What customers misunderstand]
Evidence: [Quotes or call references]
Frequency: [How often this appears across calls]
Implication for learning design: [What this means for how we teach]
```

#### Step 5: Query Salesforce for Adoption Metrics

Search Salesforce for accounts with strong adoption of **[feature]**. Pull:
- **Account names** (for potential reference with permission)
- **Industry and size** (for persona relevance)
- **ARR growth** correlated with feature adoption
- **Time-to-value metrics** (days from activation to first meaningful usage)
- **Expansion opportunities** enabled by the feature

**If specific metrics fields exist, query for:**
- Tasks automated per week
- Hours saved per user per month
- Error rate reduction percentages
- Workflow completion time improvements

#### Step 6: Review Existing Proof Points in Highspot

Search Highspot for:
- Customer success stories already documented
- Case studies featuring **[product/feature]**
- Sales deck proof points and statistics
- Competitive win stories mentioning this capability

**Document:**
- What proof points already exist and are approved for external use
- What customer names/logos can be referenced
- What metrics are already validated by Marketing/Sales
- Gaps between what Sales needs and what exists

#### Step 7: Synthesize for Instructional Design

Consolidate all research into the structured output sections below. **Use the exact section letters and headers** — downstream prompts reference them by letter.

---

### Output Deliverable: Customer Voice Research Brief

Begin the document with this metadata header:

```
---
Document: Customer Voice Research Brief
Course/Path: [name]
Topic: [product/feature]
Date: [date generated]
Data sources queried: [list — e.g., Gong (12 calls), Salesforce (account data), Highspot (3 case studies), Slack (#solutions-engineering, #product-x)]
Recommended refresh: [date + 6 months]
---
```

---

#### Section A: Pain Point Summary

3–5 primary pain themes customers express, ranked by frequency.

For each pain point:
- **Theme label:** [Descriptive name]
- **Frequency:** [How many calls/sources mention this — e.g., "7 of 12 calls"]
- **Representative quote:** "[Exact customer words]" — Source: [Gong call ID]
- **Business impact:** [Quantified when possible]
- **Persona relevance:** [Which persona(s) this pain point most affects, if distinguishable]

**Downstream use:** Needs Analysis consumes these to ground the performance gap analysis. Script Drafting uses quotes to open lessons with real customer language. Detailed Outline uses pain themes to sequence content around real problems.

**🔵 Confidence:** [High / Medium / Low] — [Basis: number of sources, consistency of pattern, recency of data. What would change it.]

---

#### Section B: Success Story Library

3–5 compelling customer examples with metrics.

For each story:
- **Label:** [Customer segment or anonymized reference]
- **Before state:** "[Customer's own words describing the problem]" — Source: [ID]
- **After state:** "[Customer's own words describing value realized]" — Source: [ID]
- **Metrics:** [Quantified improvements — time, cost, error rate, etc.]
- **Use case:** [Specific workflow or business process]
- **Success factors:** [What made this work, from the customer's perspective]
- **Approved for external use?** Yes / No / Needs approval — [note any Highspot case study match]

**Downstream use:** Script Drafting uses these as concrete examples in narration. Storyboarding uses them for scenario blocks. Proof points flow into Knowledge Check scenario stems.

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

#### Section C: Customer Language & Use Case Inventory

##### C1: Language Patterns
How customers naturally talk about this topic.

- **Terms they use:** [Customer language] vs. **terms we use:** [Product/marketing language]
- **Metaphors and analogies they make:** [How they explain it to their own teams]
- **How they describe the value:** [Common phrases]
- **Jargon they don't use:** [Product terms that don't resonate or confuse]

##### C2: Use Case Inventory
5–7 real customer workflows or use cases.

For each:
- **Use case label:** [Brief title]
- **Workflow description:** [What the customer actually does]
- **Business value:** [Why it matters to them]
- **Persona type:** [Which persona this represents]
- **Source:** [Gong call ID, Salesforce account, or Highspot asset]

**Downstream use:** Script Drafting uses C1 to match narration tone to how customers actually talk. C2 provides real scenarios for Outline, Scripts, and Knowledge Checks. Audience Profile uses C1 to validate persona descriptions.

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

#### Section D: Misconception & Confusion Inventory

**This is the most heavily consumed section in the pipeline.** Structure each misconception as a discrete, numbered item — downstream prompts (Audience Profile, Learning Objectives, Detailed Outline, Knowledge Checks) each pull from this inventory for different purposes.

For each misconception:

```
D[#]. [Short label]

Misconception: [What customers believe that is incorrect or incomplete]
Correct understanding: [What is actually true — 1-2 sentences]
Why they hold it: [What experience, analogy, or prior product behavior created this mental model]
Frequency: [How often this appears — e.g., "5 of 12 calls", "recurring in #solutions-engineering"]
Severity: [How much damage does this misconception cause if unaddressed? High = blocks task completion or causes errors. Medium = leads to suboptimal usage. Low = minor misunderstanding with limited impact]
Persona relevance: [Which persona(s) most commonly hold this misconception, if distinguishable]
Evidence: [Gong call ID, Slack thread, or SME interview reference]
Learning design implication: [What this means for how we teach — e.g., "Must be addressed before teaching X because the misconception will interfere with learning Y"]
```

After listing all misconceptions, add:

**Misconception threading guide:** For each misconception, note where in the pipeline it should be addressed:
- **Audience Profile:** Mapped to persona in Section 2C
- **Learning Objectives:** Generates a corrective learning objective
- **Detailed Outline:** Placed in a specific lesson/section at the right point in the sequence
- **Knowledge Checks:** Used as a realistic distractor with rationale

**🔵 Confidence:** [High / Medium / Low] — [Basis: number of independent sources per misconception, consistency across calls, SME validation status. Note: flag any misconception supported by fewer than 2 sources as "low confidence — verify with SME."]

---

#### Section E: Proof Point Quick Reference

10–15 validated statistics, metrics, and quotable data points for use in narration, on-screen text, and assessments.

For each proof point:
- **Stat or quote:** [The proof point as it would appear in content]
- **Source:** [Salesforce report / Highspot case study / Gong call ID]
- **Approved for external use?** Yes / No / Needs approval
- **Recency:** [Date of source data]
- **Context needed:** [Any caveats — e.g., "specific to Enterprise segment", "based on self-reported data"]

**Downstream use:** Script Drafting incorporates these into narration. Storyboarding uses them for on-screen text and data callouts. Knowledge Checks use metrics in scenario stems.

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

### Document-Level Confidence Statement

> **🔵 Overall Confidence: [High / Medium / Low]**
> [2–3 sentences: How many data sources were queried. How many calls/accounts/assets were reviewed. Which sections are strongest. Which sections have thin data and need SME validation or additional research. What would increase confidence — e.g., "Section D has only 2 supporting sources for misconceptions D3 and D5 — additional Gong calls or a Slack search in #customer-success would strengthen these."]

---

### Appendix: Source Log

List every data source reviewed with enough detail for downstream prompts and SMEs to verify:

| Source Type | Source ID / Link | Date | What was extracted | Section(s) it informed |
|---|---|---|---|---|
| Gong call | [Call ID] | [Date] | [Brief note — e.g., "Discovery call — pain points, misconceptions"] | A, D |
| Salesforce | [Report/Account] | [Date] | [Brief note] | B, E |
| Highspot | [Asset title] | [Date] | [Brief note] | B, E |
| Slack | [Channel + thread link] | [Date] | [Brief note] | D |
| Drive | [Doc title] | [Date] | [Brief note] | C |

---

Write in clear, professional prose. Use the section headers and letters exactly as specified — downstream prompts reference sections by letter (e.g., "retrieve Customer Voice Section D"). Flag any section where data is thin with **[LOW DATA — needs additional sources]** and explain what's missing.
````

### Downstream consumers

| Consumer | What it retrieves | Which section(s) |
| --- | --- | --- |
| **Audience Profile** | Misconceptions mapped to persona | Section D |
| **Needs Analysis** | Pain point themes, usage baseline, existing content, strategic context | Sections A, E + extends with scoping-specific queries |
| **Learning Objectives** | Misconceptions → corrective objectives | Section D |
| **Detailed Outline** | Misconception placement, pain points for scenario design | Sections A, D |
| **Script Drafting** | Success stories, proof points, customer language, real scenarios | Sections B, C, E + extends with lesson-specific examples |
| **Knowledge Checks** | Misconceptions as distractors, real failure scenarios | Section D + extends with lesson-specific failure modes |
| **Storyboarding** | Proof points for on-screen text, real scenarios for scenario blocks | Sections B, C, E |
