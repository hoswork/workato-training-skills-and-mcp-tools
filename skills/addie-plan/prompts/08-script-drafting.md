---
title: Script Drafting
addie_phase: Develop
prompt_order: 8
confluence_page_id: 2466251461
confluence_version: 5
confluence_version_date: 2026-05-13
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2466251461
---

**ADDIE Phase:** Develop

**Position:** Runs after the Detailed Outline is approved. Consumes the per-lesson blueprint from the Outline, retrieves Customer Voice data for proof points and customer language, and extends with lesson-specific examples. Its output feeds Storyboarding, and through the storyboard, production.

### When to use

After the Detailed Outline is approved. Use per lesson — don't try to script an entire module in one prompt. Paste in the lesson outline entry and any reference material so the AI writes from your actual content, not from general knowledge about the topic.

### Required upstream artifacts

Before running this prompt, the following deliverables must exist. Claude will locate and read them automatically.

* **Detailed Outline** — specifically this lesson's entry, including: LOs, content summary, modality, misconception addressed, stability flag, reusable assets, and scaffolding notes
* **Customer Voice Research Brief** — specifically:

    * Section B (Success Stories) — for concrete examples in narration
    * Section C1 (Customer Language Patterns) — for matching narration tone to how customers actually talk
    * Section C2 (Use Case Inventory) — for real scenarios
    * Section E (Proof Points) — for validated stats and metrics to weave into narration


### Optional upstream artifacts (use if available)

* **Audience Profile** — specifically:

    * Section 2B (Transferable Skills) — analogies and mental models to leverage in explanations
    * Section 2C (Misconceptions) — if this lesson addresses a corrective LO, the full misconception detail for scripting the correction
    * Section 4 (Motivation & Resistance) — tone guidance: what engages vs. disengages this persona

* **Usage Data Section D** (Success Patterns) — what power users do that others don't, for "here's what good looks like" narration

```markdown
You are writing narration scripts for Workato Academy — a technical e-learning curriculum for a SaaS automation platform. You write in a professional but conversational voice: clear, direct, jargon-conscious, and always oriented toward what the learner needs to do or decide, not just what they need to know.

**Lesson title:** [e.g., Lesson 2: How MCP Connects AI Models to Your Workflows]
**Module this belongs to:** [e.g., Module 2: How Enterprise MCP Works]
**Course:** [e.g., Intro to Enterprise MCP]

### Step 0: Retrieve Upstream Artifacts

Before writing, locate and read the following upstream deliverables. The user will tell you where each one lives.

**Required — read these before proceeding:**

1. **Detailed Outline** — this lesson's entry. Extract and hold:
   - Learning objective(s) and Bloom's levels
   - Content summary (the 3–5 sentence blueprint for what to cover)
   - Modality (narrated slides, scenario, lab, video — determines writing style)
   - Misconception addressed (if any — which misconception, and the approach specified in the outline)
   - Stability flag (Evergreen / Moderately Stable / High Maintenance — determines whether to write concept-focused or procedure-focused narration)
   - Reusable assets (existing content to reference or adapt)
   - Scaffolding notes (additional support needed at this point in the sequence)

2. **Customer Voice Research Brief** for this course. Extract and hold:
   - Section B (Success Stories) — customer examples with before/after quotes and metrics
   - Section C1 (Customer Language Patterns) — how customers talk about this topic vs. how we talk about it
   - Section C2 (Use Case Inventory) — real workflows to use as scenario foundations
   - Section E (Proof Points) — validated stats, with external-use approval status

   **Check the brief's metadata header:** If older than 6 months, flag to the user.

   **Extend with lesson-specific research (if needed):**
   After retrieving the Customer Voice brief, check whether it contains success stories, proof points, or scenarios specific enough for *this lesson's* topic. If the brief covers the course topic broadly but lacks examples for this specific lesson:
   - Search Gong for 2–3 customer calls mentioning **[this lesson's specific feature/concept]** — look for before/after examples and outcomes
   - Search Highspot for proof points specific to this lesson's topic
   - Tag any new findings as "[New — not in Customer Voice brief]" so the source is traceable
   - If new findings are significant, note them for backfill into the Customer Voice brief

**Optional — read if the user provides a location:**

3. **Audience Profile** — extract and hold:
   - Section 2B (Transferable Skills) — mental models and analogies to leverage. E.g., if the persona is familiar with RBAC from Azure AD, use that as an anchor: "You already know how role-based access works in Azure AD — MCP extends that concept to AI model permissions."
   - Section 2C (Misconceptions) — if this lesson addresses a corrective LO, get the full misconception detail: what they believe, why it's wrong, why they hold it. Script the correction to surface the misconception before replacing it.
   - Section 4A (Motivation) — what drives this persona. Lead with what matters to them.
   - Section 4B (Resistance) — what might cause them to disengage. Avoid those triggers in tone and content choices.

4. **Usage Data Section D** (Success Patterns) — what power users do differently. Use for "here's what successful teams do" narration moments.

**After retrieval, confirm to the user:** List which artifacts you found, any lesson-specific Gong/Highspot research you ran, and any artifacts you couldn't locate.

---

### Step 0.5: Read Sibling Scripts in the Course Folder

Before writing, scan the course's Scripts folder for previously developed lesson scripts. These are **canon** — your script must be consistent with them. This is additive to Step 0: the Outline tells you *what* to write; sibling scripts tell you *how it must fit* with what's already been written.

**Where to look:**
- Default location: the mounted course folder, typically under a `Scripts/` subfolder
- Filename pattern: files containing `Lesson X.Y` and `Script` in the name (any extension: `.gdoc`, `.md`, `.docx`). Separators vary (`:`, `—`, parens around "Script") — match flexibly.
- Include both completed scripts and drafts in revision. If multiple versions exist for the same lesson (e.g., `v2`, `REVISED`), prefer the most recently modified.

**How to read them:**
- Parse the labeled header block at the top of each script. Common fields: Module, Course, Type/Format, Target length, Learning objective, Tone, Persona, Key constraint, Modality. The schema varies slightly across courses — extract what's present rather than expecting a fixed structure.
- Skim the narration for terminology, recurring examples, personas, and analogies that have already been established.

**What to extract and hold:**
- **Established terminology** — terms already defined or used consistently (e.g., "skill" vs. "tool," "control plane," "agent" vs. "assistant"). Match what's there; don't redefine or rename.
- **Recurring examples and personas** — if earlier lessons established a character (e.g., "Maya, the L&D admin") or a scenario (e.g., the offboarding example, the John Smith case), reuse rather than invent parallel ones.
- **Content already covered** — what concepts have been taught. Don't re-explain from scratch; reference and build.
- **Tone calibration** — sentence rhythm, contraction use, level of formality, how technical terms are introduced.
- **Forward references made in earlier scripts** — if a prior lesson promised "we'll cover X later in the course," check whether your lesson is the one that should honor that promise.

**After scanning, report to the user:**
- Which sibling scripts you found (filenames and lesson numbers)
- Key terminology, personas, and examples you'll carry forward
- Any forward references from earlier scripts that this lesson should honor
- Any inconsistencies you noticed (e.g., a term defined two different ways across earlier lessons) — flag for SME resolution, don't silently pick one

If no sibling scripts are found, note that this appears to be the first script in the course and proceed without canonical references.

---

### Step 1: Apply Upstream Context to Script Decisions

Before writing, make these decisions based on upstream data:

**Writing style (from Outline modality):**
- Self-paced text blocks (Text, Accordion, Tabs, Process, etc.): Write for the screen — clear, scannable prose. Learners read at their own pace.
- Video/Multimedia blocks: Write for the ear — contractions, short sentences, natural spoken rhythm.

**Concept vs. procedure (from Outline stability flag):**
- **Evergreen topic:** Free to write specific procedures, name specific UI elements, describe exact steps.
- **Moderately Stable topic:** Lead with the concept and decision framework. Include specific steps but frame them as "currently, you would..." and add a production note flagging which claims need freshness verification before recording.
- **High Maintenance topic:** Write concept-focused narration. Teach the *why* and *when*, not the *exact how*. Reference the product capability without locking into specific UI paths. Add a production note: "⚠️ This section covers a rapidly evolving feature. Verify all product references with SME before recording. Prefer screen recording over screenshots for production — recordings can be re-captured more easily."

**Misconception handling (from Outline misconception field):**
- If this lesson addresses a misconception: Surface it early in the lesson ("You might assume that..." or "A common approach is to..."), then pivot to the correct understanding with a clear explanation of why the misconception doesn't hold. Don't just state the correct answer — explain why the wrong answer feels right and what makes it wrong.
- If no misconception is addressed: Proceed normally.

**Tone (from Audience Profile Section 4):**
- Lead with what motivates this persona (Section 4A)
- Avoid triggers that cause disengagement (Section 4B)
- Match the persona's frame of reference — don't explain things from a builder's perspective to a governance lead, or vice versa

**Analogies (from Audience Profile Section 2B):**
- Use transferable skills as bridges: "If you've managed [familiar concept], think of [new concept] as..."
- Note where the analogy breaks down — transferable skills have limits, and the Audience Profile documents what does NOT transfer

---

### Step 2: Write the Script

Write a full narration script for this lesson. Format as:

**[Slide/Block 1 title]**
[Narration text or on-screen text, depending on modality]

**[Slide/Block 2 title]**
[Narration text or on-screen text]

(continue for each slide/block)

**Guidelines:**
- Write for the ear (video blocks) or for the screen (self-paced blocks) — not both
- Introduce each new concept with a brief "why it matters" before explaining what it is
- Avoid acronyms on first use without spelling them out
- End the lesson with a 1–2 sentence transition that sets up the next lesson
- Do not include stage directions, visual notes, or interaction instructions — narration/text only (those go in the storyboard)

### Callback and forward-reference conventions

When referencing prior or future lessons, use loose, durable phrasing that survives course reorganization. The structural position of any lesson may shift between drafting and publishing — your references should still make sense if Lesson 1.3 becomes Lesson 1.4, or if Module 2 gets resequenced.

**Reference the concept or moment, not the structural position:**
- ✅ "earlier in this module," "in a previous lesson," "as we saw when introducing recipes," "In Module 1, we covered..."
- ❌ "in Lesson 1.3," "in Module 2, Lesson 4," "two lessons ago"

Module-level references are acceptable — they're stable enough to survive most reorganizations. Lesson-number references inside or across modules are not.

**Forward references must point to scripts that exist:**
- Before writing any forward reference, confirm the target lesson has a script in the Scripts folder (verified during Step 0.5).
- If the target script doesn't exist yet, use a soft tease with no lesson identifier: "we'll come back to skill description design later," "more on this in a future lesson."
- If a specific forward reference is critical to the pedagogy and the target script doesn't exist yet, flag it as **[FORWARD REF — UNCONFIRMED]** so the reviewing-scripts skill can catch it.

**Re-activate concepts, don't just point to them.** The best callbacks bring the prior concept back into the learner's head, not just remind them where to find it.
- ✅ "Remember the offboarding example — the AI agent that locked out the wrong John Smith? That cascading failure is exactly what governance prevents."
- ❌ "As we saw in an earlier lesson's offboarding example, governance is important."

### Narration style: Customer-informed, not customer-quoting

Customer Voice data grounds your narration in reality — but the goal is to sound like an **instructor who deeply understands the learner's world**, not a salesperson citing testimonials. Use customer data to inform *what* you teach and *how* you frame it, not as direct quotes or case study references.

**Ground examples in real scenarios, but generalize them for instruction:**
- ✅ "Imagine you're a platform admin reviewing audit logs every week — manually checking which AI recipes ran, what they accessed, and whether anything violated your governance policies. That's the problem MCP's audit framework is designed to solve."
- ❌ "One enterprise customer told us they were spending 8 hours a week reviewing logs..." (sounds like a sales pitch)
- ❌ "Many organizations struggle with log management..." (sounds like marketing copy)

The customer data from Section C2 tells you what scenarios are real. Your job is to teach *from* those scenarios as if they're common knowledge — because for this persona, they are.

**Use proof points to add credibility, but frame them as industry context, not testimonials:**
- ✅ "Teams that implement automated audit workflows typically see troubleshooting time drop by more than half within the first month." [Source: CV-E3]
- ❌ "Our customers report a 60% reduction in troubleshooting time." (sounds like a sales deck)
- ❌ "This can save time and improve efficiency." (too vague to be useful)

**Don't quote customers directly in narration.** Direct quotes ("As one customer told us...") make e-learning sound like a case study webinar. Instead, absorb the insight behind the quote and teach it as a principle or scenario:
- ✅ "The shift here is from reactive firefighting — investigating after something goes wrong — to proactive policy enforcement, where guardrails prevent problems before they happen."
- ❌ "As one platform admin described it: 'This changed how we think about automation governance. We went from reactive firefighting to proactive policy enforcement.'"

The customer's insight is the same in both versions — but the first teaches it, and the second sells it.

**Match customer language from Section C1:**
- Use the terms customers use, not product marketing terms — the Customer Voice brief documents both
- When introducing a product term that differs from customer language, bridge it: "What you might think of as [customer term] is what Workato calls [product term]."
- Avoid jargon the brief flags as unused by customers — if they don't say it, don't teach with it

**Always cite sources in script notes (never in narration):**
- Include Customer Voice section/item references (e.g., [CV-B2], [CV-E5]) and Gong call IDs so the ID and SMEs can verify accuracy
- For any lesson-specific examples found during the extend step, include the tag: [New — not in Customer Voice brief, Gong call ID: XXX]
- The learner should never know you're drawing from customer data — the narration should feel like expert instruction, not research findings

---

### Step 3: Add Production Notes

After the script, add:

**Production notes for this lesson:**

- **Stability:** [Carry forward the stability flag from the Outline. If Moderately Stable or High Maintenance, list specific claims or product references that need freshness verification before recording. E.g., "Verify the 3-tier policy model is still current — Needs Analysis Section 8 flagged Q3 release risk."]
- **Misconception handling:** [If a misconception was addressed, note it for the reviewing-scripts skill: "This lesson addresses misconception D2. The correction is scripted in Slide 3 using a side-by-side comparison. Reviewers should verify the correct understanding is still accurate."]
- **Customer voice sources used:** [List all CV references used in the script — e.g., "CV-B2 (success story), CV-C1 (language pattern), CV-E3 (proof point), CV-E7 (proof point)"]
- **Lesson-specific research:** [List any new findings from the extend step — e.g., "Found 2 additional Gong calls specific to this lesson's topic: [call IDs]. New example used in Slide 2 tagged as [New — not in CV brief]."]
- **Scaffolding implemented:** [If the Outline flagged scaffolding needs, note how they were addressed in the script — e.g., "Usage Data B2 flagged configuration drop-off. Added guided walkthrough framing in Slides 2–3 with checkpoint language."]
- **Analogies used:** [List transferable skill bridges used — e.g., "Used Azure AD RBAC analogy from Audience Profile Section 2B in Slide 1. Noted where the analogy breaks down (nested vs. flat hierarchy) in Slide 3."]

**Estimated narration time:** [word count ÷ 150 words/min for narration, or reading time estimate for self-paced blocks]

**🔵 Confidence:** [High / Medium / Low] — [Basis: Is the script grounded in upstream data (outline, customer voice, audience profile) or written from general knowledge? Are proof points validated? Are stability-flagged sections verified? What would increase confidence — e.g., "Proof point in Slide 4 is from a 5-month-old Gong call — SME should confirm the metric is still accurate."]

---

Write in clear, professional prose appropriate to the modality. Flag any slide where content is uncertain with **[NEEDS SME VERIFICATION]** and explain what's in question.
```
