---
name: presentation-content-standards
description: Surface reference for slide deck reviews — content density, instructional design, voice, and accessibility. Format-agnostic (PPTX, Google Slides, Keynote, harness-generated). Loaded alongside the standard routing pillars when the-once-over evaluates a slide deck; not a standalone pillar.
metadata:
  version: "1.0"
---

# Presentation Content Standards

A surface reference for slide deck evaluation. Slides are not documents — different density limits, different hierarchy rules, different voice register, and an additional instructional layer (speaker notes, pacing, memorability). Load this alongside the standard routing pillars when reviewing any slide deck; it doesn't replace them, it calibrates their checks for the slide medium.

Format-agnostic: applies to PPTX, Google Slides, Keynote, harness-generated decks, or any other format.

---

## Check classification

**Static checks** — the majority of this reference. Counts, thresholds, presence, and pattern matches:
- §1 Deck structure: slide count vs. deck-type limit, required slides detection (title/objectives/summary by layout name or title text), no blank slides, one concept per slide (heading count), consecutive text-only slide count, consecutive same-layout count, engagement pacing (activity/question within 10 slides)
- §2 Content density: all word limits (body, split-layout, takeaway, bullet), bullet count (top-level max 6, nesting max 2), Miller's Law total item count (max 7), bullet period check, bullet word count (max 25)
- §3 Typography: font size floors (14pt body, 24pt title), max font families (2), max font sizes per slide (3), ALL CAPS body text detection, no periods on titles
- §5 Voice/tone — word lists only: prohibited term list match, superlative count per slide (max 1), sales urgency phrase list, second-person hype patterns, confidentiality marker match, filler word count, passive voice regex
- §5 Readability: Flesch-Kincaid grade level (body ≤10, notes ≤12)
- §6 Accessibility: contrast ratio check (4.5:1 normal text, 3:1 large/UI elements), alt text presence, font floor (14pt)
- §7 Brand: color palette compliance, logo placement, slide numbers on non-title slides

**Reasoning checks** — the instructional and quality judgment layer:
- §4 Instructional design: speaker notes *quality* (does KEY POINT name the actual core takeaway, or just describe the slide? does TALK TRACK give useful presenter cues or just say "discuss this"?), memorability element *authenticity* (is it genuine to the material and audience, or decoration?), objectives coverage *quality* (do content slides actually develop the stated capability, or just mention it?)
- §5 Voice calibration: tone appropriateness for the audience (technical builders vs. marketing register) — word-list catches the obvious jargon, but misregister between overall voice and audience requires judgment
- Deck narrative arc: does the deck have a beginning/middle/end structure, or is it a flat list of topics? (structural reasoning, not countable)
- Slide titles as headlines: are titles naming the takeaway ("Genies fail silently in async sync") or labeling the topic ("Async Sync Failure Modes")? Requires reading intent, not matching patterns.

---

## § 1 — Deck structure

### Required elements (training decks)

| Element | Rule |
|---|---|
| Opening / title slide | Deck opens with a clear title slide |
| Learning objectives slide | Required for all training/educational decks. Frame objectives as outcomes: "You will be able to…" — not topics ("We will cover…") |
| Summary / recap slide | Required at close. Every stated takeaway must appear on the summary. |

Non-training deck types (product demo, pitch, quarterly review) may omit objectives; summary is still expected unless the deck type explicitly doesn't need it.

### Deck-level constraints

| Check | Limit | Notes |
|---|---|---|
| Max slides | 40 (training), 20 (demo), 15 (pitch), 18 (problem/solution) | Break longer decks into modules |
| Objectives coverage | Every stated learning objective must be covered by ≥1 content slide | Flag any objective with no corresponding slide |
| One concept per slide | Max 1 main heading/concept per slide | Exception: comparison or two-column layouts |
| No blank slides | Every slide must have reviewable content | |

### Engagement pacing

- **Activity or question every 10 slides** — passive consumption sets in without it
- **Max 3 consecutive text-only slides** — break with image, diagram, or activity (Picture Superiority Effect: learners retain visuals better than text)
- **Max 5 consecutive same-layout slides** — layout variety sustains attention
- **≥15% of content slides should be engagement/memorability elements** — see § 4

---

## § 2 — Content density

### Word limits

| Context | Limit | Reason |
|---|---|---|
| Standard slide body | 120 words max | Above this, the slide reads as a document |
| Image + text slide | 50 words max | Text shares space; less real estate |
| Key takeaway callout | 15 words max | The callout is the hero; supporting text stays minimal |
| Bullet item | 25 words max | Fragments, not sentences |
| Speaker notes | 10 words min / 100 words max | KEY POINT + brief TALK TRACK only |

### Bullet rules

- **Max 6 top-level bullets per slide** — more overwhelms
- **Max 2 levels of nesting** — deeper nesting belongs in a document
- **Min 3 items for a list** — fewer items may work better as prose
- **Max 7 total processable items per slide** (bullets at all levels + table rows combined) — Miller's Law: working memory holds 7±2 chunks
- **Parallel structure** — all bullets start with the same part of speech
- **No periods on bullets** — they're fragments

### Tables

- Max 30 cells per table (unreadable at slide scale above this)
- Recommended: 3–5 columns, 5–6 rows

### Dense slides

Slides with 80+ words must use bold, headings, or numbered lists to guide the eye. A wall of unformatted body text at that density is a flag.

Max 3 consecutive bullet-heavy slides — break with a visual, activity, or takeaway.

---

## § 3 — Typography & visual hierarchy

### Font sizes

| Context | Rule |
|---|---|
| Body text | 14pt minimum (16pt preferred) |
| Title / header | 24pt minimum |
| Absolute floor | Nothing smaller than 14pt anywhere |

### Style rules

- **Max 2 font families per slide** — consistency
- **Max 3 distinct font sizes per slide** — clear hierarchy: title / sub-header / body
- **No ALL CAPS body text** — use a SemiBold weight for emphasis
- **Titles use Title Case** — not sentence case, not ALL CAPS
- **No periods on slide titles**
- **Body text left-aligned** — natural reading direction

### Title vs. body overlap

Slide title should not be >80% repeated in body text. Title is a distinct headline; body expands on it. A title that restates the body adds no navigational value.

---

## § 4 — Instructional design

### Speaker notes

**When to write them:** Slides with terse bullets, technical content, demo steps, audience interaction cues.

**When to skip:** Title/opener, section headers, objectives, summary, full-bleed images.

**Required structure:**
```
KEY POINT: One sentence — the slide's core takeaway.
TALK TRACK: Brief guidance — demos, audience questions, transitions.
```

Notes must not duplicate the body — if notes are >60% word-overlap with on-screen text they add no value. Notes add context; the slide carries the content.

### Memorability elements

At least 15% of content slides should include one of:

| Type | Description |
|---|---|
| Mnemonic device | Acronym, acrostic, or pattern for recall |
| Numbered framework | 3–7 numbered steps that chunk knowledge |
| Humor / dad joke | Clean, topic-related; max 1 per 10 slides |
| Themed break | Mental reset at chapter boundaries |
| Poll question | Show of hands to gauge understanding |
| Recap question | Retrieval every 10–15 slides — ask learners to fill in gaps, don't just re-read bullets (testing effect) |
| Analogy / metaphor | Map unfamiliar concept to something the audience already knows |

### Objectives & takeaways

- Objectives slide uses "You will be able to…" — outcome framing, not topic framing
- Every stated objective should have a corresponding content slide
- Every stated takeaway should appear on the summary slide

---

## § 5 — Voice & tone

These checks overlap with `say-it-plain` — defer to say-it-plain for form-level and word-level prose rules. These are slide-specific calibrations.

### Hype language

- **No unsubstantiated superlatives**: "the only," "the first," "the fastest," "the most" — cite a source or soften
- **Max 1 superlative per slide** — flag when exceeded
- **No sales urgency**: "act now," "don't miss," "limited time"
- **No second-person hype**: "you need this," "you won't believe," "you'll love"

### Corporate jargon (flag, suggest plain alternative)

| Banned | Use instead |
|---|---|
| leverage / utilize | use |
| synergy | collaboration |
| best-in-class | leading |
| deep dive | detailed look |
| game-changer | improvement |
| unlock | enable (unless literal) |
| seamless / frictionless | smooth / simple |
| robust | reliable |
| world-class | (remove — show, don't tell) |
| cutting-edge / next-gen | modern / new |
| enterprise-grade | (remove) |
| rockstar / ninja / guru | expert / specialist |
| empower | enable |
| democratize | make accessible |

### Prohibited phrases

Flag and remove before any external sharing:
- "Proprietary and Confidential"
- "Internal Use Only"
- "Do Not Distribute"
- "NDA Required"
- "Draft — Not for Distribution"

### Readability

- **Max reading grade level: 10** (Flesch-Kincaid) — accessible for adult learners at varying levels
- **Speaker notes max grade level: 12** — easy to scan while presenting
- **Prefer active voice** — "the team built X" over "X was built"
- **Avoid filler words** — very, really, just, basically, actually, simply, obviously

---

## § 6 — Accessibility (WCAG 2.1 AA)

| Check | Requirement |
|---|---|
| Text-to-background contrast | 4.5:1 minimum for normal text (<18pt) |
| Large text contrast | 3.0:1 minimum for text ≥18pt or ≥14pt bold |
| Non-text elements | 3.0:1 minimum for bullets, icons, UI elements |
| No color-only meaning | Information conveyed by color must also use icons, labels, or patterns |
| Alt text | All images require alt text |
| Min font size | Nothing below 14pt anywhere |

---

## § 7 — Brand & consistency (Workato)

These are Workato-specific and should be stripped from any external distribution of this document.

### Terminology capitalization

- **Workato** — not "workato" or "WORKATO"
- **Agent Studio** — not "agent studio" or "AgentStudio"
- **Recipe** — capitalized when referring to a Workato Recipe
- **Connector** — capitalized for Workato Connector
- **Trigger, Action** — capitalized for Workato concepts
- **Data pill** — sentence case (not "Data Pill")
- **OPA** — always uppercase
- **Workbot** — not "workbot" or "Work Bot"

### Color palette

Max 5 unique colors per slide. Allowed backgrounds: `#FFFFFF`, `#F5F6F8`, `#EDEEF1`, `#1C1B1B`, `#111010`, `#F8FFFE`, `#E1FFFC`. Flag slides using colors outside the approved palette.

Note: Workato teal #67EADD fails contrast at 1.46:1 on white — use dark teal #108291 (4.54:1) for text over light backgrounds.

### Logo

- Present on first and last slides (bookends)
- Position: bottom-left on standard content slides
- Absent on: section headers, full-bleed layouts

---

## Deck-type calibration

Apply the appropriate profile before running checks. If deck type is not stated, default to **Training module** (most strict).

| Deck type | Objectives req? | Summary req? | Activity pacing | Hype limit | Max slides | Speaker notes |
|---|---|---|---|---|---|---|
| Training module | ✅ | ✅ | Every 10 slides | Standard | 40 | Required format |
| Training intro | ✅ | ✗ | Not required | Standard | 40 | Relaxed |
| Training closing | ✗ | ✅ | Not required | Standard | 40 | Relaxed |
| Product demo | ✗ | ✗ | Not required | Relaxed (3/slide) | 20 | Not required |
| Pitch | ✗ | ✅ | Not required | Relaxed (3/slide) | 15 | Not required |
| Problem/solution | ✗ | ✅ | Not required | Standard | 18 | Not required |
| Quarterly review | ✗ | ✗ | Not required | Standard | 25 | Not required |
| Onboarding | ✅ | ✅ | Every 15 slides | Standard | 40 | Required format |
