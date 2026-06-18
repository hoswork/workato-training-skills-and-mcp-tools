---
title: Storyboarding
addie_phase: Develop
prompt_order: 10
confluence_page_id: 2510192874
confluence_version: 8
confluence_version_date: 2026-05-28
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2510192874
---

**ADDIE Stage**: Develop

**Position:** Runs after Script Drafting (and optionally after Knowledge Checks, if assessment blocks are included in the storyboard). Consumes the lesson's script and production notes, Detailed Outline per-lesson metadata, and Learning Objectives. Its output is the final production blueprint — the handoff to Content Development for Rise 360 build, and (for lessons with Video / Multimedia / Custom Needed visuals) the source for the **Mockup Companion** prompt that produces a visual reference deck for the video editor.

### When to use

After a lesson script is approved (or after both the script and knowledge checks are approved, if the lesson includes assessment blocks). This prompt translates approved content into a block-by-block production blueprint that a Content Developer can use to build the lesson in Rise 360. Use per lesson — don't try to storyboard an entire module in one prompt.

Once the storyboard is approved, if the lesson contains Video / Multimedia / Custom Needed blocks, run the **Mockup Companion** prompt as a follow-up to produce a visual reference deck for the video editor. The companion is optional — Rise-only lessons with no video or custom graphics don't need it.

This prompt works with two Claude skills that handle the heavy lifting:

* **storyboarding** — Structures slides, selects Rise 360 block types, writes accessibility notes, and generates production specs. Includes a Rise 360 block catalog (`references/rise-blocks.md`) so block selection is consistent across the team.
* **resolving-assets** — Automatically maps each visual slot to a concrete asset from our three libraries (see below), or flags slots that need product screenshots, screen recordings, or custom graphics. No more vague "relevant diagram" descriptions.

### Asset libraries available

The resolving-assets skill draws from three sources. These are documented inside the skill's reference files, so you don't need to memorize them — but knowing what's available helps you write better visual descriptions in your outlines and scripts.

| Library | What's in it | When it gets used | Where it lives |
| --- | --- | --- | --- |
| **Workato Icon Library** (Frontify) | 200 branded SVG icons — platform concepts, connectors, business metaphors, celebrations, etc. | First choice for conceptual visuals, section headers, slide accents. The skill references icons by exact name (e.g., `recipe`, `shield`, `neural brain`). | Frontify · Full catalog in skill: `references/frontify-catalog.md` |
| **Streamline Milano** | Conceptual SVG illustrations — AI/robots, education, teamwork, data, professional scenarios | Broader themes where an icon is too small. Think intro slides, section openers, and conceptual topics (e.g., "human-AI collaboration"). | Google Drive (file ID TBD — confirm with Kenneth) · Full catalog in skill: `references/streamline-catalog.md` |
| **Figma Storyboard Template** | Branded layout frames, cover page, section components | Reusable structural elements — title slides, section dividers, branded containers. | Figma |

If none of these fit, the skill flags the slot as `[Screenshot]`, `[Screen Recording]`, or `[Custom needed]` so the CD knows exactly what to create.

### Required upstream artifacts

Before running this prompt, the following deliverables must exist. Claude will locate and read them automatically.

* **Script Drafting output** — specifically:

    * Narration/on-screen text per slide (the content to storyboard)
    * Production notes: stability flags, misconception handling notes, customer voice sources, scaffolding implemented, analogies used
    * Estimated narration time

* **Detailed Outline** — this lesson's entry, specifically:

    * Modality (determines block type selection and writing style)
    * Stability flag (determines screenshot vs. concept visual decisions)
    * Reusable assets (from Content Audit Section D — assets to pull vs. create)
    * Scaffolding notes (additional support that should be reflected in block choices)
    * Misconception addressed (if any — the storyboard should support the correction approach)


### Optional upstream artifacts (use if available)

* **Knowledge Check questions** (if this lesson includes assessment blocks) — question stems, options, rationales, and interaction specs for knowledge check blocks
* **Learning Objectives** — the LOs for this lesson, for objectives coverage mapping in the storyboard summary
* **Content Audit Section E2** (Per-Topic Stability Ratings) — if the Detailed Outline's stability flag needs more detail on specific topics within the lesson

## Prompt

`````markdown
````
You are an instructional designer creating visual storyboards for Workato Academy — a technical e-learning curriculum for a SaaS automation platform. You are translating approved course content into a block-by-block production blueprint that a Content Developer will use to build the lesson in Rise 360. Most blocks are self-paced (learners read on-screen text); Video and Multimedia blocks are the exception and need narration scripts written for the ear.

Use the **storyboarding** skill for block structure, Rise 360 block selection, and production specs. Use the **resolving-assets** skill to populate every visual slot with concrete asset references from the Workato Icon Library (Frontify), Streamline Milano illustrations, and Figma storyboard template — or flag slots requiring product screenshots/screen recordings.

**Lesson title:** [e.g., Lesson 2: How MCP Connects AI Models to Your Workflows]
**Module this belongs to:** [e.g., Module 2: How Enterprise MCP Works]
**Course:** [e.g., Intro to Enterprise MCP]

### Step 0: Retrieve Upstream Artifacts

Before building the storyboard, locate and read the following upstream deliverables. The user will tell you where each one lives.

**Required — read these before proceeding:**

1. **Script Drafting output** for this lesson. Extract and hold:
   - Narration/on-screen text per slide (the content you're storyboarding)
   - Production notes — carry these forward into block-level production notes:
     - **Stability flag** (from the Outline, inherited through the script) — determines visual approach: Evergreen topics can use specific screenshots; Moderately Stable/High Maintenance topics should prefer concept visuals, diagrams, or screen recordings over screenshots
     - **Misconception handling** — which misconception is addressed and how (side-by-side comparison, before/after, etc.) — the storyboard must support this approach with appropriate block types and visuals
     - **Customer voice sources** — the CV references used in the script, for traceability
     - **Scaffolding implemented** — what additional support was scripted, so the storyboard can reinforce it with interaction design
     - **Analogies used** — transferable skill bridges, so visuals can reinforce the analogy
   - Estimated narration time — use as the time budget for the storyboard

2. **Detailed Outline** — this lesson's entry. Extract and hold:
   - Learning objective(s) — for objectives coverage mapping
   - Modality — determines block type selection:
     - Self-paced text blocks (Text, Accordion, Tabs, Process, etc.): Content text is `[On-screen text]` — clear, scannable prose
     - Video/Multimedia blocks: Content text is `[Narration script]` — conversational, spoken rhythm. Supporting on-screen text reinforces but never duplicates narration.
   - Stability flag — use this for visual decisions (see guidelines below)
   - Reusable assets — pull these from the Content Audit rather than creating duplicates:
     - "Reuse as-is" assets → reference directly in the Visual column
     - "Adapt" assets → note the adaptation needed in Production Notes
     - "Repurpose element" assets → describe which element to extract
   - Scaffolding notes — translate into interaction design (guided walkthroughs, checkpoint moments, progressive disclosure)
   - Misconception addressed — ensure the storyboard's block sequence and visual design support the correction approach specified in the outline

**Optional — read if the user provides a location:**

3. **Knowledge Check questions** for this lesson (if assessment blocks are included). Extract:
   - Question stems and options (for Knowledge Check blocks)
   - Interaction type (multiple choice, sorting, scenario branch, etc.)
   - Rationales (for feedback text in the interaction)

4. **Learning Objectives** for this module — for the objectives coverage matrix in the storyboard summary.

5. **Content Audit Section E2** — per-topic stability ratings, if more detail is needed beyond the lesson-level flag from the Outline.

**After retrieval, confirm to the user:** List which artifacts you found, which stability flag applies, any reusable assets identified, and any artifacts you couldn't locate.

---

### Step 1: Plan the Block Sequence

Before writing individual blocks, plan the overall sequence:

**Block sequence plan:**

| Block # | Purpose | Block Type | Content Source | Stability Concern? |
|---|---|---|---|---|
| 1 | Lesson opener — hook + LO | Statement | Script Slide 1 | — |
| 2 | Core concept | Text + Media | Script Slide 2 | ⚠️ Moderately Stable |
| 3 | Misconception correction | Tabs (side-by-side) | Script Slide 3 | — |
| ... | ... | ... | ... | ... |

**Rules for block planning:**
- Map each script slide/section to one or more blocks — one concept per block
- Place interaction blocks at least every 4–5 content blocks
- If the script includes a misconception correction, choose a block type that supports the correction approach (Tabs for side-by-side comparison, Accordion for reveal-the-truth, Scenario for misconception-as-option)
- If scaffolding notes call for guided walkthroughs, use Process blocks or stepped interactions
- Flag any block covering a Moderately Stable or High Maintenance topic — these affect visual decisions in Step 2

---

### Step 2: Write Each Block

For each block, provide:

**Block [#]: [Block title]**

| Element | Details |
|---------|---------|
| **Content text** | The primary text content for this block. Prefix with `[On-screen text]` for self-paced blocks (Text, Text + Media, Statement, Accordion, Tabs, Process, Timeline, etc.) or `[Narration script]` for Video/Multimedia blocks. On-screen text should be clear, scannable prose — learners read at their own pace. Narration scripts should be conversational and natural — this text will be spoken aloud. |
| **Supporting on-screen text** | For Video/Multimedia blocks only: key text that appears on screen alongside the narration — headlines, labels, callouts. This reinforces the narration without duplicating it word-for-word. If the video block has multiple slides, detail the supporting text per slide. Write "N/A — self-paced block" for non-video blocks (the content text row already covers what learners see). |
| **Visual / Media** | Resolved asset reference(s) from the resolving-assets skill. Every slot must resolve to one of: `[Frontify] icon-name`, `[Streamline] Filename--Streamline-Milano.svg`, `[Figma] component-name (node: id)`, `[Screenshot] specific capture description`, `[Screen Recording] specific interaction description`, or `[Custom needed] description`. Be concrete — "Screenshot of the Audit Trail panel with the filter set to 'Last 7 days'" not "screenshot of the product." For conceptual visuals, Frontify icons are the first choice; Streamline Milano illustrations work for broader themes (AI, teamwork, learning). |
| **Interaction** | If applicable: click-to-reveal, labeled graphic, sorting activity, scenario branch, accordion, etc. Specify what the learner does, what feedback they receive, and the default/fallback state. Write "None — passive block" if no interaction. |
| **Rise 360 block type** | Use the storyboarding skill's block selection decision tree. Be realistic — don't force complex interactions where a simple block works. |
| **Accessibility notes** | Alt text for every image/illustration. Caption/transcript flag for video/multimedia. Reading order if layout is non-linear. Color contrast notes if custom colors are used. Write "Standard" only if the block is plain text with no media. |
| **Production notes** | See guidelines below. |

### Production notes guidelines

Production notes connect the storyboard to upstream pipeline data. For each block, include relevant items:

- **Stability:** Carry forward from the Script's production notes and the Outline's stability flag. Do NOT independently assess stability — use what upstream already determined.
  - **Evergreen:** "No version sensitivity — screenshot is safe for long-term use."
  - **Moderately Stable:** "⚠️ Version-sensitive screenshot — verify UI matches current release before capture. Consider screen recording for easier refresh." Note which specific element is at risk (e.g., "The policy configuration panel layout may change — verify with SME before capturing").
  - **High Maintenance:** "⚠️ Rapidly evolving feature — use concept diagram or screen recording instead of screenshot. Screen recording can be re-captured more easily when UI changes." Do not use static screenshots for High Maintenance topics unless no alternative exists.
- **Reusable assets:** If the Outline flagged a reusable asset for this content, reference it: "Reuse: [Asset ID from Content Audit D1/D2/D3] — [description]. [Adaptation needed / Use as-is]."
- **Misconception support:** If this block supports a misconception correction, note the approach: "Supports misconception D2 correction — side-by-side comparison. Left tab shows the misconception (what learners typically assume); right tab shows the correct model."
- **Scaffolding:** If this block implements scaffolding from Usage Data: "Scaffolding: Implements guided walkthrough for Usage Data B2 struggle point — progressive disclosure with checkpoint before next section."
- **Analogy reinforcement:** If this block visualizes an analogy from the script: "Visual reinforces Azure AD RBAC analogy from Audience Profile Section 2B — side-by-side showing familiar RBAC model and new MCP permission model."
- **Environment/data for screenshots:** When a screenshot is needed, specify: product environment, test data required, account permissions needed, and any UI state (filters, panels open, etc.).
- **Animation direction:** If applicable — appear, fade-in, none.

Mark any block where you're unsure about the best visual approach with **[VISUAL TBD — CD INPUT NEEDED]** so it gets flagged in review.

---

### Step 3: Resolve Visuals

After completing all blocks, invoke the **resolving-assets** skill to populate visual slots. Pass each block's visual concept and content context to the resolver. Merge resolved asset references back into the Visual/Media column.

**Visual decision tree (informed by upstream stability data):**

1. **Is the content about a specific product UI?**
   - Yes + Evergreen topic → `[Screenshot]` with specific capture description
   - Yes + Moderately Stable → `[Screen Recording]` preferred, or `[Screenshot]` with version-sensitivity flag
   - Yes + High Maintenance → `[Screen Recording]` or `[Custom needed]` concept diagram — avoid static screenshots
   - No → proceed to step 2

2. **Is the content a Workato platform concept?**
   - Yes → `[Frontify]` icon (first choice) or `[Custom needed]` diagram
   - No → proceed to step 3

3. **Is the content a broader theme (AI, collaboration, learning)?**
   - Yes → `[Streamline]` illustration
   - No → `[Figma]` structural component or `[Custom needed]`

4. **Was a reusable asset flagged in the Outline?**
   - Yes → reference it directly, noting any adaptation needed
   - No → proceed through steps 1–3

If none of these fit, flag the slot as `[Custom needed]` with a specific description so the CD knows exactly what to create.

---

### Step 4: Validate and Summarize

**After the final block:**

**Transition note:** How this lesson connects to the next — what the learner should expect and any visual continuity to maintain.

**Storyboard summary:**

- Total blocks: [N]
- Estimated duration: [X] minutes (cross-check against Script's estimated narration time)
- Interaction ratio: [N] interactive blocks / [N] total = [X]% (target: ≥20%)
- Objectives coverage: [map each learning objective → block #s]

**Assets needed (summary):**

- Frontify icons: [list each icon by exact library name]
- Streamline illustrations: [list each SVG filename used]
- Screenshots: [list each with capture description + version sensitivity flag]
- Screen recordings: [list each with interaction description, or "None"]
- Figma components: [list each with node ID, or "None"]
- Custom graphics/diagrams: [list net-new assets needed, or "None"]
- Reusable assets from Content Audit: [list each with asset ID and adaptation status]
- Blocks queued for Mockup Companion: [list of block #s with Video / Multimedia / Custom Needed visuals, or "None — this lesson does not need a mockup companion"]

**Validation checks:**

- [ ] Every block maps back to a learning objective — no decorative blocks without a purpose
- [ ] Every learning objective is covered by at least one block
- [ ] On video blocks, supporting on-screen text reinforces (not repeats) the narration
- [ ] On self-paced blocks, on-screen text is clear and scannable as standalone content
- [ ] Interactions require the learner to think, not just click
- [ ] Interaction blocks appear at least every 4–5 content blocks
- [ ] Rise 360 block types are realistic for the content
- [ ] Each visual is resolved to a specific asset reference (not a vague description)
- [ ] Every Video/Multimedia block has `[Narration script]` prefix; all other blocks have `[On-screen text]` prefix
- [ ] Frontify icons are referenced by exact library name
- [ ] Streamline illustrations are referenced by exact filename
- [ ] No visual slot is left unresolved without a `[VISUAL TBD]` or `[Custom needed]` flag
- [ ] Alt text direction is included for every image and diagram
- [ ] Video/Multimedia blocks are flagged for caption/transcript
- [ ] Stability flags from upstream are carried through — no Evergreen screenshots on High Maintenance topics
- [ ] Reusable assets from Content Audit are referenced where the Outline specified — no redundant creation
- [ ] Scaffolding from Usage Data is reflected in interaction design
- [ ] Misconception correction blocks use the approach specified in the Outline and Script
- [ ] Asset summary is complete — CD can pull a production task list directly from it
- [ ] No content gaps — every block has text content appropriate to its block type

**Open questions for CD review:**
Flag 1–3 specific production decisions — e.g., "Would a labeled graphic or a process block work better for the 3-step flow on Block 4?" or "Is the sorting interaction on Block 6 feasible in Rise 360 without custom development?"

**🔵 Confidence:** [High / Medium / Low] — [Basis: Is the storyboard grounded in approved script and upstream metadata (high), or were blocks improvised beyond the script (medium), or written without an approved script (low)? Are stability flags consistently applied? Are reusable assets identified? What would increase confidence — e.g., "Blocks 5–7 use screenshots for a Moderately Stable topic — SME should confirm UI hasn't changed since the script was written."]

---

Write clearly and precisely — this is a production spec, not a creative brief. Be specific enough that the CD can build without guessing your intent. Flag any block where content is uncertain with **[CONTENT TBD — NEEDS INPUT]** and explain what's missing.
````
`````
