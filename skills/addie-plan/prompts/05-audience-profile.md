---
title: Audience Profile
addie_phase: Analyze
prompt_order: 5
confluence_page_id: 2529001864
confluence_version: 1
confluence_version_date: 2026-05-06
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2529001864
---

**ADDIE Phase:** Analyze → Design (bridge artifact)

**Position:** Runs after Needs Analysis and Customer Voice Research. Output feeds Learning Objectives, Detailed Outline, Script Drafting, and Knowledge Checks.

## When to use

After your Needs Analysis is complete (or in progress) and you have at least initial Customer Voice research. Use this prompt to generate a standalone audience profile for each persona the course serves. Run once per persona — if your course serves multiple personas, run separately for each.

This prompt produces a **first-class reference artifact** that downstream prompts consume directly. When you move to Learning Objectives, Detailed Outline, or Script Drafting, paste the relevant Audience Profile as structured input rather than summarizing the persona from memory.

### Required upstream artifacts

Before running this prompt, the following deliverables must exist (completed or in progress). Claude will attempt to locate and read them automatically — you just need to tell it where they live.

* **Needs Analysis** — specifically Section 1 (Persona Profile), Section 2 (Performance Gap), and Section 3 (Course-Level Learning Goal). Claude will read the full document and extract the relevant sections.
* **Customer Voice Research Brief** — specifically Section D (Misconception & Confusion Patterns). Claude will read the full document and extract Section D.

These artifacts may be stored as:

* A file in the working folder or Claude Projects directory
* A Confluence page in the ETT space
* A Google Doc (accessible via Drive)

**If Claude can't locate an artifact automatically**, it will ask you to provide the location or paste the relevant section. The prompt is designed to work either way — automated retrieval is preferred, manual paste is the fallback.

### Optional upstream artifacts (use if available)

* **Usage Data Research Brief — Sections B–D** (drop-off points, failure modes, adoption barriers) — grounds the gap analysis in behavioral data
* **Content Audit & Gap Analysis — Section E** (Freshness & Stability Assessment) — helps flag which knowledge areas are stable vs. shifting
* **Existing course completion or assessment data** for this persona (if a predecessor course exists)

If these exist, tell Claude where to find them. If they don't exist yet, the prompt will generate those sections at lower confidence and flag them for future enrichment.

```markdown
You are an instructional designer working on Workato Academy — a technical e-learning curriculum for a SaaS automation platform. You are creating a standalone Audience Profile artifact for a specific learner persona. This profile will be referenced by all downstream deliverables (learning objectives, outline, scripts, assessments, storyboard) — so it must be precise, grounded in data, and explicit about what is known vs. assumed.

**Course or learning path name:** [e.g., Intro to Enterprise MCP]
**Persona name or label:** [e.g., Platform Owner]

### Step 0: Retrieve Upstream Artifacts

Before generating the profile, locate and read the following upstream deliverables. The user will tell you where each one lives — it may be a local file path, a Confluence page (search the ETT space if needed), or a Google Doc.

**Required — read these before proceeding:**

1. **Needs Analysis** for this course. Extract and hold:
   - Section 1 (Persona Profile) — role, responsibilities, prior knowledge, motivations, pain points
   - Section 2 (Performance Gap) — current gaps and their sources
   - Section 3 (Course-Level Learning Goal) — the performance outcome statement
   - Section 8 (Build Risk Assessment) — risks that may affect prerequisite assumptions

2. **Customer Voice Research Brief** for this course. Extract and hold:
   - Section D (Misconception & Confusion Patterns) — the specific misconceptions, confusion points, frequency data, and learning design implications already identified

**Optional — read if the user provides a location:**

3. **Usage Data Research Brief** — Sections B–D (drop-off points, failure modes, adoption barriers, success patterns)
4. **Content Audit & Gap Analysis** — Section E (Freshness & Stability Assessment)

**If you cannot locate a required artifact:** Ask the user for the file path, Confluence page title, or to paste the relevant section. Do not proceed without at least the Needs Analysis Sections 1–3 and Customer Voice Section D — these are required inputs, not nice-to-haves.

**After retrieval, confirm to the user:** List which artifacts you found, which sections you extracted, and any artifacts you couldn't locate. Then proceed to generate the profile.

---

Here are any additional discovery notes, SME interview excerpts, or usage data the user wants to provide beyond the upstream artifacts:
[User provides additional context — or writes "None beyond the above"]

Using the above inputs, generate a **standalone Audience Profile** covering the following sections. For every section, include a confidence rating (High / Medium / Low) with a brief explanation of what the rating is based on and what would change it.

---

### 1. Identity & Role Description
*Carry forward and refine from Needs Analysis Section 1.*

Describe this persona in concrete terms:
- **Role title(s):** What are they typically called? (List 2–3 common titles if the persona spans multiple job titles.)
- **Organizational position:** Where do they sit — team, department, reporting line? How senior are they?
- **Day-to-day responsibilities:** What does a typical week look like for this person? Focus on the tasks and decisions that are relevant to the course topic.
- **Relationship to the product:** How do they interact with Workato today? Are they a builder, a consumer of what others build, an administrator, a decision-maker, or some combination?
- **Estimated audience size:** If knowable — how many people in the customer base roughly match this persona? (This helps prioritize design trade-offs.)

**🔵 Confidence:** [High / Medium / Low] — [What this rating is based on; what would change it]

---

### 2. Current State — What They Bring

#### 2A. Existing Knowledge
What does this persona already know that's relevant to the course topic? Be specific — not "they know some automation" but "they can build basic Workato recipes with triggers and actions; they understand workspace-level permissions."

- **Solid foundations:** Knowledge and skills that are reliable prerequisites — things we can build on without re-teaching.
- **Partial knowledge:** Areas where they have exposure but incomplete or inconsistent understanding. Note the specific gaps.
- **Knowledge they think they have but don't:** Misconceptions or overconfidence areas. (This differs from Section 2C below — this is about knowledge self-assessment, not factual misconceptions.)

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

#### 2B. Transferable Skills
What adjacent skills, mental models, or experiences does this persona have that we can leverage — even if they weren't learned in a Workato context? These represent teaching shortcuts: concepts we can reference or build on rather than teaching from scratch.

For each transferable skill, note:
- What the skill is and where it comes from (e.g., "Familiar with RBAC concepts from managing Azure AD")
- How it maps to the course content (e.g., "Can be leveraged when teaching Workato workspace permissions — the mental model transfers, only the implementation differs")
- What does NOT transfer (e.g., "Azure AD role hierarchy is flat; Workato's is nested — this difference needs to be explicitly taught")

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

#### 2C. Misconceptions & Confusion Patterns
*Use the Customer Voice Section D retrieved in Step 0. Do not re-derive misconceptions from scratch — pull the specific misconceptions already identified in that document and map them to this persona. If additional misconceptions emerge from SME notes or usage data, add them but tag them as "[New — not in Customer Voice brief]" so the source is traceable.*

For each misconception relevant to this persona:
- **The misconception:** What do they believe that is incorrect or incomplete?
- **Why it's wrong:** One or two sentences explaining the correct understanding.
- **Why they hold it:** What experience, analogy, or prior product behavior created this mental model?
- **Instructional implication:** Where in the course should this be addressed, and how? (Direct correction? Comparison activity? Scenario that exposes the gap?)
- **Source:** [Reference the Gong call, Slack thread, or SME interview where this was identified]

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

### 3. Target State — Where They Need to Be

#### 3A. Learning Outcomes Mapped to Bloom's Levels
For each major outcome this persona should achieve by the end of the course, specify:
- **Outcome statement:** Written as an observable performance (what they can DO, not what they will "understand")
- **Bloom's level:** Remember / Understand / Apply / Analyze / Evaluate / Create
- **Why this level:** One sentence justifying why this Bloom's level is right for this persona and this content. (A Governance Lead needs to *Evaluate* policy effectiveness, not just *Remember* policy categories.)

Note: These are persona-specific outcomes, not the course-level learning objectives. A course serving multiple personas may have different target Bloom's levels for the same content area. These outcomes feed the Learning Objectives prompt — they don't replace it.

#### 3B. Performance Gap Summary
*Refine from Needs Analysis Section 2, retrieved in Step 0.*

For each major gap between current state (Section 2) and target state (Section 3A):
- **The gap:** What can't they do now that they need to do?
- **Gap type:** Knowledge gap (don't know it), skill gap (know it but can't do it), mental model gap (have the wrong framework), or practice gap (know how but don't have a habit/process)?
- **Closable by training?** Yes / Partially / No — if partially or no, note what else is needed (tooling, policy, manager support, on-the-job practice)
- **Priority:** High / Medium / Low — based on impact to the learner's performance and the course's learning goal

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

### 4. Motivation & Resistance Factors

#### 4A. What Drives This Persona to Learn
Why would they take this course voluntarily? What's in it for them — career growth, solving a current problem, manager requirement, certification, curiosity? Be specific to the persona, not generic ("wants to learn new skills").

#### 4B. What Might Make Them Resistant or Disengaged
What could cause this persona to drop off, skim, or mentally check out? Common factors:
- Content feels too basic for their experience level
- Content feels too technical for their role (e.g., a governance lead being asked to write code)
- Course doesn't match their immediate job need
- Prior bad experience with e-learning
- Time pressure — they'll skim if the course feels longer than the value it delivers
- Organizational resistance to the product/process the course teaches

For each resistance factor, note a design implication (e.g., "If they feel it's too basic, we need to signal depth early — lead with a non-obvious scenario, not definitions").

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

### 5. Prerequisite Mapping

For each knowledge or skill area that the course assumes as a starting point:
- **Prerequisite:** [What we're assuming they already know/can do]
- **How confident are we they have it?** High (most of this persona has it) / Medium (some do, some don't) / Low (many will lack this)
- **If they don't have it, what happens?** [How does the gap manifest — will they be confused by Module 2? Will they misinterpret the lab? Will they skip the course entirely?]
- **Mitigation:** What's our strategy? Options include:
  - *Assume and reference* — mention it but don't teach it ("As you know from setting up your workspace...")
  - *Brief bridge* — 1–2 minutes of context within the course to level-set
  - *Prerequisite course* — direct them to complete [specific course] first
  - *Self-assessment gate* — let them test whether they need the prerequisite
  - *Standalone bridge module* — build a dedicated short module that multiple courses share

**🔵 Confidence:** [High / Medium / Low] — [Basis and what would change it]

---

### 6. Profile Summary & Downstream Guidance

Close with:
- **One-paragraph persona narrative:** A readable summary of who this person is, what they know, what they need, and what's going to be hard for them. Write this as if briefing a colleague who's picking up the course design.
- **Top 3 design implications:** The three most important things this profile tells us about how to design the course for this persona. (e.g., "Lead with governance scenarios, not builder workflows — this persona will disengage if the first module feels like a recipe tutorial.")
- **Stakeholder validation questions:** 2–3 specific questions to ask stakeholders or SMEs to validate or upgrade the low-confidence sections of this profile.

---

### Document-Level Confidence Statement

Provide an overall confidence assessment for this profile:

> **🔵 Overall Confidence: [High / Medium / Low]**
> [2–3 sentences: What data sources informed this profile. Which sections are strongest. Which sections most need validation. What would increase overall confidence — e.g., "Conducting 2–3 learner interviews would upgrade Sections 2B and 4 from Medium to High."]

---

Write in clear, professional prose. Use the section headers exactly as specified above — downstream prompts will reference sections by number. Flag any section where input is insufficient to answer fully — mark these **[NEEDS INPUT]** and explain what's missing.
```
