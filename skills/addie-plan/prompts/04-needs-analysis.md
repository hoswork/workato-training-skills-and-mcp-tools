---
title: Needs Analysis / Scoping
addie_phase: Analyze
prompt_order: 4
confluence_page_id: 2433515899
confluence_version: 5
confluence_version_date: 2026-05-06
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2433515899
---

**ADDIE Phase:** Analyze (runs after Customer Voice, Content Audit, and Usage Data)

**Position:** This is the **synthesis prompt** — it consumes the three upstream Analyze-phase deliverables (Customer Voice, Content Audit, Usage Data) and produces the course-level scoping document that governs all downstream work for a single course. Its output feeds the Audience Profile, Learning Objectives, Detailed Outline, and project planning (JIRA/ADDIE checklist).

## When to use

At the start of a new course, after the upstream research briefs are complete (or at least in progress). Use after initial SME discovery interviews and stakeholder alignment. This prompt produces a course-level scoping document that governs all modules within the course.

**Note:** This prompt scopes a single course. For learning path-level planning (sequencing multiple courses, identifying shared modules, defining persona tracks), use the Curriculum Design prompt (To Come) which sits above individual course needs analyses.

### Required upstream artifacts

Before running this prompt, the following deliverables should exist. Claude will locate and read them automatically — you just need to tell it where they live.

* **Customer Voice Research Brief** — pain points (Section A), use cases (Section C2), misconceptions (Section D), proof points (Section E)
* **Content Audit & Gap Analysis Report** — content inventory (Section A), gaps (Section B), stability assessments (Section E2)
* **Usage Data-Informed Design Brief** — priority workflows (Section A), struggle points (Section B), adoption barriers (Section C), success patterns (Section D), business outcome correlations (Section E)

These artifacts may be stored as files in the working folder, Confluence pages in the ETT space, or Google Docs.

**If any upstream artifact doesn't exist yet:** The prompt will still work, but sections that depend on missing data will be flagged with lower confidence ratings and "\[NEEDS UPSTREAM DATA\]" markers. The prompt will run targeted queries to partially fill gaps, following the refresh-and-extend pattern — but a full upstream brief will always produce stronger results.

### Required user inputs

In addition to the upstream artifacts, you'll need to provide:

* SME discovery interview notes or transcripts
* Stakeholder alignment context (MBOs, strategic goals)
* Module list with titles and brief descriptions (if already scoped)
* Existing content identified for reuse (or "None identified")

## Prompt

````markdown
You are an instructional designer working on Workato Academy — a technical e-learning curriculum for a SaaS automation platform. You are drafting a course-level needs analysis to scope and plan a single course before module development begins.

This needs analysis is a **synthesis deliverable** — it consumes three upstream research briefs (Customer Voice, Content Audit, Usage Data) and produces the strategic scoping document that governs all downstream design and development. Structure your output precisely as specified below so downstream prompts can reference sections by number.

**Course name:** [e.g., Intro to Enterprise MCP]
**Target persona:** [e.g., Integration developers and platform admins who build and manage automations on Workato; familiar with recipes and connectors but new to MCP and agentic AI capabilities]
**Course goal:** [e.g., Learners can explain what Enterprise MCP is, how it fits into Workato's agentic AI architecture, and when to use it in their automation workflows]
**Prerequisite course(s):** [e.g., AI Essentials recommended; Workato Foundations I required]
**Number of modules planned:** [e.g., 4 modules]
**Estimated total learning time:** [e.g., ~30 minutes]
**Target launch quarter:** [e.g., Q2 FY27]
**Primary MBO or strategic goal this course supports:** [e.g., M1: 25+ AI-focused courses published; M5: 15% product adoption rate for academy accounts]

Here is a summary of the modules currently scoped for this course:
[Paste the module list with titles and brief descriptions. This typically comes from your kickoff or discovery meeting with stakeholders and SMEs — the initial "here's what we think this course should cover" conversation. It may also come from a higher-level planning document like the Modular Learning Architecture. Note: the upstream research briefs (Customer Voice, Content Audit, Usage Data) don't generate this list — they help you evaluate whether it's the right list. If you ran the upstream prompts before your kickoff, use their findings to sharpen the conversation and refine the module list before pasting it here.]

Here are my raw discovery notes from SME interviews and stakeholder conversations for this course:
[Paste your notes here — bullet points, transcript excerpts, rough observations are fine. These are your unstructured notes from SME discovery interviews, kickoff meetings, Slack threads with SMEs, or any other context you've gathered through conversation. The upstream research briefs (retrieved in Step 0) provide complementary data from systems (Gong, data warehouse, Highspot); these notes capture what you've learned from people.]

### Step 0: Retrieve Upstream Artifacts

Before beginning the needs analysis, locate and read the following upstream deliverables. The user will tell you where each one lives — it may be a local file path, a Confluence page (search the ETT space if needed), or a Google Doc.

**Required — read these before proceeding:**

1. **Customer Voice Research Brief** for this course. Extract and hold:
   - Section A (Pain Point Summary) — the 3–5 ranked pain themes with quotes and business impact
   - Section C2 (Use Case Inventory) — the 5–7 real customer workflows
   - Section D (Misconception Inventory) — the numbered misconceptions with severity and persona relevance
   - Section E (Proof Point Quick Reference) — validated stats and metrics

2. **Content Audit & Gap Analysis Report** for this course. Extract and hold:
   - Section A (Content Inventory) — existing assets with quality and reusability ratings
   - Section B (Gap Analysis) — what's covered, missing, and outdated
   - Section D (Reuse Opportunities) — assets categorized by reuse action
   - Section E2 (Per-Topic Stability Ratings) — Evergreen / Moderately Stable / High Maintenance per topic

3. **Usage Data-Informed Design Brief** for this course. Extract and hold:
   - Section A (Priority Workflow Ranking) — workflows ranked by teaching priority
   - Section B (Struggle Point Inventory) — where users struggle, with design implications
   - Section C (Adoption Barrier Analysis) — prerequisite gaps revealed by behavioral data
   - Section D (Success Pattern Insights) — what power users do that others don't
   - Section E (Business Outcome Correlations) — usage-to-business-value connections

**After retrieval, confirm to the user:** List which artifacts you found, which sections you extracted, and any artifacts you couldn't locate.

**If an upstream artifact is missing:** Note it in the metadata header. For each section of the needs analysis that depends on missing upstream data:
- Run a targeted query to partially fill the gap (following the refresh-and-extend pattern)
- Flag the section with "[NEEDS UPSTREAM DATA — [which brief]]" so the ID knows to circle back
- Lower the confidence rating for affected sections

**Extend with scoping-specific context:**
After retrieving the upstream briefs, run any additional queries needed for scoping decisions that the upstream prompts don't cover:
- **Strategic alignment:** Query Salesforce for opportunity/account data that connects this course to specific business outcomes or pipeline targets — if not already covered by Usage Data Section E
- **Stakeholder context:** Check Slack or Confluence for recent stakeholder discussions about this course's priority, timeline, or scope changes
- Tag any new findings as "[Scoping-specific — not in upstream briefs]"

---

Using the upstream artifacts, SME discovery notes, and any additional context gathered above, draft a **Course Strategy Document** covering the following sections. The first section (Course Strategy) frames the strategic rationale; the remaining sections (1–10) provide the detailed scoping analysis.

---

### Course Strategy

This section frames the strategic purpose of the course. It should be decided during kickoff and validated with stakeholders before detailed design begins. Ground it in upstream data where available.

#### Vision Statement
How will the business leverage this course to achieve its goals? Write 2–3 sentences connecting the course to the business outcome it serves. Reference Usage Data Section E (business outcome correlations) and the MBO/strategic goal from the course metadata above.

#### Audience Segments
Who is this course for? List the primary audience segment and any secondary segments. Be specific — not just "customers" but which customers (e.g., new customers in onboarding, enterprise platform admins, partner implementers). If Usage Data provides cohort breakdowns (segment, role, adoption level), reference them here.

#### Business Problems / Opportunities
What business problem does this course address, or what opportunity does it unlock? Examples: customer retention, churn reduction, feature adoption, partner enablement, market expansion. Ground in:
- Customer Voice Section A (pain points — what problems are customers describing?)
- Usage Data Section A (priority workflows — what high-impact capabilities are underadopted?)
- Usage Data Section E (business outcome correlations — what's the business case?)

#### Project Strategy Statement
Summarize the course's purpose in one sentence using this format (per ETT standard):

> This program helps **[primary target audience]**
> learn how to **[competency]**
> so they can **[behavior change]**,
> which will result in **[improved / increased / decreased] [business impact]**.

Example: *This program helps integration developers and platform admins learn how to evaluate and apply Enterprise MCP capabilities so they can build agentic AI workflows with proper governance, which will result in increased product adoption and reduced time-to-value.*

**🔵 Confidence:** [High / Medium / Low] — [Basis: Is the strategic framing validated with stakeholders, or inferred from upstream data? What would change it — e.g., "Strategy statement is drafted from upstream data but needs stakeholder sign-off at kickoff."]

---

### Section 1: Persona Profile

*This section is the seed for the standalone Audience Profile prompt. Write it with enough structure that the Audience Profile can consume and expand it.*

Who is this learner? Describe:
- **Role and titles:** What are they typically called? List 2–3 common job titles.
- **Day-to-day responsibilities:** Focus on tasks relevant to the course topic.
- **Prior knowledge:** What do they already know? What adjacent skills do they bring? Ground this in Usage Data Section D (success patterns) if available — what do successful users in this role already do?
- **Motivations:** Why would they take this course? Ground in Customer Voice Section A (pain points) — what real problems are they trying to solve?
- **Pain points:** What frustrates them? Use customer language from Customer Voice Section A, not product marketing language.
- **Relationship to the product:** Builder? Consumer? Administrator? Decision-maker?

**🔵 Confidence:** [High / Medium / Low] — [Basis: SME interviews, Customer Voice data, usage data. What would change it.]

**Downstream note:** The Audience Profile prompt will consume this section and expand it into a full per-persona profile with transferable skills, misconception mapping, Bloom's-level target state, and prerequisite mapping.

---

### Section 2: Performance Gap

What is the learner currently unable to do that this course will address?

For each major gap:
- **The gap:** What can't they do?
- **Gap source:** Lack of knowledge? Lack of a mental model? No established practice? Wrong mental model (misconception)?
- **Evidence:** Ground in upstream data where possible:
  - Usage Data Section B (struggle points) — behavioral evidence of the gap
  - Customer Voice Section A (pain points) — how customers describe the gap
  - Customer Voice Section D (misconceptions) — wrong mental models that create the gap
- **Training-closable?** Yes / Partially / No — if partially or no, note what else is needed (tooling, policy, manager support)
- **Source tag:** [CV-confirmed] / [UD-confirmed] / [SME-reported] / [Assumed — needs validation]

**🔵 Confidence:** [High / Medium / Low] — [Basis: How many upstream sources confirm each gap. Gaps confirmed by both Customer Voice and Usage Data are high confidence. Gaps from SME interviews alone are medium. Gaps inferred without data are low.]

---

### Section 3: Course-Level Learning Goal

In one or two sentences: what should learners be able to do by the end of this course that they cannot do today? Write this as a performance outcome, not a content summary.

Ground the goal in:
- The highest-priority gaps from Section 2
- The highest-priority workflows from Usage Data Section A
- The success patterns from Usage Data Section D (what does "good" look like for this persona?)

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

### Section 4: Module Scope Map

For each module in the course, provide:

```
Module [#]: [Title]

Learning goal: [One sentence — what the learner can do after this module]
Content status: [Exists / Adapt / Net-new] — reference Content Audit Section B/D:
  - If Exists: cite the asset from Content Audit Section A [asset #]
  - If Adapt: cite the asset and note what needs updating from Content Audit Section D2
  - If Net-new: note what Content Audit Section B2 identified as the gap
Stability rating: [Evergreen / Moderately Stable / High Maintenance] — carry forward from Content Audit Section E2:
  - Cite the E2 item number and last-verified date
  - If the topic isn't covered in E2, derive a rating from Slack/SME notes and tag as [Derived — not in Content Audit]
Key SME dependency: [Name — subject area]
Build complexity: [Low / Medium / High] — one-line rationale
Priority: [Informed by Usage Data Section A workflow ranking — higher-priority workflows = higher-priority modules]
Known risks: [Carry forward any relevant risks from upstream — e.g., stability concerns, missing SME availability]
```

**🔵 Confidence:** [High / Medium / Low] — [Basis: How much of the scope map is grounded in upstream data vs. assumptions. Flag any module where the scope is uncertain.]

---

### Section 5: Sequencing Rationale

Why are the modules in this order?

- Identify prerequisite dependencies between modules (where Module X must precede Module Y)
- Reference Usage Data Section A (priority workflow ranking) — are high-priority workflows taught early enough?
- Reference Usage Data Section B (struggle points) — are scaffolding needs addressed before the modules that need them?
- Flag any modules that could be reordered or delivered in parallel if timeline pressure requires it
- Note any sequencing decisions that depend on assumptions about learner prerequisites

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

### Section 6: Shared Dependencies and Cross-Course Connections

Identify any content that this course shares with other existing or planned courses. This section surfaces coordination needs — it does not design the learning path (that's the Curriculum Design prompt's job).

- Modules or topics in this course that overlap with other courses — reference Content Audit Section C (redundancy risk assessment)
- Assets that could be shared across courses and built once — reference Content Audit Section D1 (reuse as-is)
- Concepts where this course and another course could end up framing things differently — flag for coordination
- Prerequisite relationships with other courses (e.g., "This course assumes learners have completed AI Essentials")

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

### Section 7: SME Requirements

List the SMEs needed to develop and review this course.

For each SME:
- **Name and subject area**
- **Modules they're needed for:** [Reference Module Scope Map items]
- **Estimated review time commitment**
- **Earliest engagement phase:** [Which ADDIE phase — e.g., "Analysis for scope validation" or "Design for technical review"]
- **Availability risks:** [If known — e.g., "On leave in July" or "Split across 3 projects"]

---

### Section 8: Build Risk Assessment

Identify the top 3–5 risks that could delay or compromise this course's quality or timeline.

For each risk:

```
Risk [#]: [Label]

What: [Description]
Why it matters: [Impact if not mitigated]
Likelihood: [High / Medium / Low]
Upstream evidence: [Reference specific upstream findings — e.g., "Content Audit E2.3 rates [topic] as High Maintenance — content may change before launch" or "Usage Data confidence is Low for Section D — success patterns may not hold"]
Mitigation: [Proposed action]
Owner: [Who needs to act]
Inherited downstream: [Yes / No — will this risk affect Audience Profile, Outline, Scripts, etc.?]
```

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

**Downstream note:** The Audience Profile prompt inherits risks tagged as "inherited downstream = Yes" and factors them into prerequisite confidence and design implications. Downstream reviewing skills check whether inherited risks have been addressed.

---

### Section 9: Success Metrics

How will we know this course is working?

- **Completion rate target:** [e.g., 70%+]
- **CSAT target:** [e.g., 4.2+ / 5.0]
- **Behavioral or business outcome indicator:** Ground in Usage Data Section E (business outcome correlations) — what usage behavior should increase post-course? [e.g., "15% increase in [feature] activation rate among course completers within 30 days"]
- **How and when measured:** [Post-launch measurement plan]

**🔵 Confidence:** [High / Medium / Low] — [Basis: Are the success metrics measurable with current instrumentation? Are baseline metrics available from Usage Data?]

---

### Section 10: Open Questions

List anything that cannot be resolved without additional SME input, stakeholder decision, or product clarity.

For each:
- **Question:** [What needs to be answered]
- **Why it matters:** [What's blocked until this is resolved — reference specific module or section]
- **Action needed:** [SME review / Stakeholder decision / Product clarity / Additional research]
- **Owner:** [Who needs to act]
- **Urgency:** [Blocks next phase / Should resolve before [specific phase] / Nice-to-have]

---

### Document-Level Confidence Statement

> **🔵 Overall Confidence: [High / Medium / Low]**
> [2–3 sentences: Which upstream artifacts were available and consumed. Which were missing. How much of the needs analysis is grounded in multi-source validated data vs. single-source or assumed. Which sections most need stakeholder validation. What would increase confidence — e.g., "Sections 1 and 2 are high confidence (grounded in all three upstream briefs + SME interviews). Section 4 stability ratings for Modules 5–7 are Medium — Content Audit rated these topics but the ratings are 4 months old. A quick SME check would confirm whether Q3 releases changed anything."]

---

Write in clear, professional prose. Use the section numbers exactly as specified — downstream prompts reference sections by number (e.g., "retrieve Needs Analysis Section 4"). Flag any section where input is insufficient to answer fully — mark these **[NEEDS INPUT]** and explain what's missing.
````
