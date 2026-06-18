"""
team-style-guide — snippet 1 (rules + rubric).
Applies to training and education audiences only. Not applicable to workato general audience.
"""

RUBRIC = ""
---
name: team-style-guide
description: Use when authoring or reviewing Workato training content (lab guides, slide decks, course bundles, Knowledge Checks) for surface-level style — typography, color, casing, punctuation conventions, brand, required spellings, banned terms. Peer to say-it-plain under the Style pillar; say-it-plain handles prose, this handles everything else.
---

# Team Style Guide

The Workato training team's surface-style pass. Covers typography, color, casing, punctuation conventions, imagery, layout, brand, required spellings, and banned terms. Peer skill to `say-it-plain` (which handles sentence-level prose) under the Style pillar of The Standards Desk.

## When to invoke

Before publishing any Workato training artifact:

- Lab guides (HTML — Standard or Print)
- Slide decks (training, customer-facing)
- Course bundles, module pages
- Knowledge Check screens
- Internal-team training materials that will travel

Skip on: code, private notes, chat messages, drafts that haven't reached coherent shape yet (run `say-it-plain` first).

## Check classification

**Static checks** — the overwhelming majority of this pillar. Nearly everything is a threshold, a count, a spelling, or a pattern match:
- §1 Typography: font size floors and ceilings, max families per slide, max font sizes per slide, casing rules (Title Case vs. sentence case), ALL CAPS detection, semantic formatting presence
- §2 Color: WCAG contrast ratio (≥4.5:1 normal / ≥3:1 large text), max color count per artifact, palette compliance (approved colors only), color-only meaning detection
- §3 Punctuation: bullet terminal punctuation per surface, heading terminal punctuation ban, step terminal punctuation (`.?!:;…`), exclamation mark count (max 1)
- §4 Imagery: DPI floor (≥150), format check (png/jpg/svg only), max count per slide (3), size percentage check (10–70% of slide area), alt text presence
- §5 Layout: margin floor (0.5"), max text boxes per slide (4), content height ceiling (4.2"), element overlap detection
- §6 Content density: all word/bullet/sentence count limits
- §7 Brand: logo presence on bookend slides, slide numbers on non-title slides
- §8 Required spellings: exact pattern match
- §9 Banned terms: exact pattern match
- §10 Callout vocabulary: valid class name check (note/tip/warning/pitfall/key-insight)

**Reasoning checks** — a small set where judgment is unavoidable:
- §4 Image content relevance: "content-relevant, no stock clichés" — requires evaluating whether the image strengthens the surrounding content. A DPI check doesn't tell you if it's a hand-shake-on-a-laptop stock photo.
- §11 Allowed exceptions: "Workato magic" staying in-bounds, other team-specific carve-outs — requires understanding context and intent, not just pattern matching.
- Surface mismatch evaluation: when a rule conflict exists between surfaces, determining which profile applies requires reading the artifact and understanding its context.

## Source authorities

Order of precedence when this skill doesn't cover a specific case:

1. **AP Stylebook** — general written conventions.
2. **Conscious Language guidelines** — inclusive vocabulary.
3. **Google Developer Documentation Style Guide** — technical-writing conventions.
4. **Microsoft Writing Style Guide** — UI-facing conventions.
5. **This skill** — Workato-specific consolidations and overrides.

For Workato product terminology: the Workato Documentation style guide and Education and Training wordlist (internal Confluence pages) override the external references.

## Surface profile

This skill applies across surfaces, but five rules **diverge by surface** — labs and slides intentionally part ways. The surface itself sets the choice; this skill carries both profiles.

| Rule | Slide deck | Lab guide |
|---|---|---|
| Heading/title case | Title case | Sentence case |
| Bullet terminal punctuation | No period | Period (AP) |
| Emphasis weight | Poppins SemiBold (never bold) | Bold |
| Body font floor | 14pt absolute, 16pt operational | 12pt floor |
| Contrast | Floor only — projection eats softness | Floor + near-black/near-white for long-form |

Outside these five, surfaces align.

When invoked, **determine the surface first** and apply the matching profile.

## 1. Typography

**Font sizes:**

| Element | Slide deck | Lab guide |
|---|---|---|
| Body | 16pt operational, 14pt floor | 12pt floor |
| Bullets | 16pt | 12pt floor |
| Slide / page headers | 24pt | 24–28pt |
| Section headers | 24–28pt | body + 1–2pt, bold |
| Title slide / lab title | 36pt / lab `<h1>` | n/a / `<h1>` |
| Absolute floor | 14pt anywhere | 12pt anywhere |

**Weights:**

- Slides: **Poppins SemiBold** for all emphasis. **Never bold.**
- Lab guides: **bold** for emphasis.

**Font families:**

- Max 2 families per slide or page.
- Max 3 font sizes per slide (title, subtitle/header, body).

**Casing:**

- Slides: **title case** for titles (`Build a Customer Onboarding Recipe`).
- Lab guides: **sentence case** for all headings, including the lab title and Task titles (`Lab 2: Build a customer onboarding recipe`, `2.3 Configure the Salesforce trigger`).
- **No ALL CAPS** in body text on either surface — reduces readability.

**Semantic formatting:**

- Use the template's heading and body styles. Don't manually resize.
- HTML labs: `<h1>`, `<h2>`, `<h3>`, `<strong>`, `<em>`, `<code>` carry structure. No deeper than `<h3>`.
- Slides: use named layouts. No ad-hoc layouts.

**Text formatting conventions (labs):**

- **boldface** — GUI elements associated with action (`Click Save`); terms defined inline.
- *italic* — book titles; emphasis (sparingly); placeholder variables (`<your-account-name>`).
- `monospace` — commands inline; URLs; code blocks; text on screen; text the learner types.

## 2. Color

**Palette:**

- 3–5 brand palette colors per artifact.
- Approved Workato brand colors only.
- **Teal accent (`#108291` dark teal):** bullets, blockquotes, key takeaways. Chosen for WCAG AA compliance.

**Color usage:**

- **One meaning per color.** Don't use red for both errors and emphasis.
- **Never color-only meaning.** Pair color with icons, labels, or patterns.
- Lab guides (long-form): prefer near-black (`#1a1a1a`) on near-white (`#fafafa`) over pure `#000` on `#fff`. Long dwell time benefits from softened contrast.
- Slides: no softness ceiling. Projection eats contrast.

**Floor (both surfaces):** WCAG 2.1 AA — ≥4.5:1 for normal text (<18pt), ≥3:1 for large text (≥18pt, or ≥14pt bold).

## 3. Punctuation

**Bullets:**

- **Slide decks:** no terminal period. Bullets are scannable phrases.
- **Lab guides:** AP-style period. Capitalize the first letter, end every bullet with a period.

**Headings:**

- Never end in terminal punctuation on either surface.

**Lab Steps:**

- Every Step ends with `.`, `?`, `!`, `:`, `;`, or `…`.

**Exclamation marks:**

- Default zero per artifact. Absolute ceiling: one per deck or lab. Excitement-performance erodes trust.

## 4. Imagery

- **Content-relevant.** Image strengthens the text. No stock clichés.
- **Attribution.** Source in the image title field (`![alt](path "Photo by Jane Doe, Unsplash")`) or visible caption when required.
- **Internal-only artifacts:** real Workato team-member photos when a person is depicted.
- **Quality:** ≥150 DPI. Formats: png, jpg, svg.
- **Quantity (slides):** max 3 images per slide.
- **Size (slides):** max 70% slide area, min 10%.

**Lab screenshots:**

- Inline captions state the action (`Setup menu with API highlighted`), not the element identity.
- Tight crop carries the targeting. No bounding boxes, arrows, or overlays unless explicitly requested.
- Alt text equals caption.

**Picture Superiority guard (slides):** no more than 3 consecutive text-only slides. Break up runs with a relevant visual.

## 5. Layout

**Single-column flow:**

- Top-left for the title (eye-entry point).
- Bottom-right for navigation or key takeaway (eye-exit).
- Body text left-aligned (natural reading direction).

**White space:**

- Slide margin: minimum 0.5".
- No overlapping elements.
- Slides: max 4 text boxes per slide. Prefer single-column flow.

**Slide content safety:**

- Usable content height ≤4.2".
- Safe bottom at 5.0". Content below may overlap logo or slide number.
- Vertical flow — elements stack top-to-bottom, no horizontal sprawls.

**Image handling:**

- Aspect ratio preserved. Fit within bounding box; no stretching.

**Slide title position consistent:** top-left, same position across every slide in the deck.

**Lab chunking:**

- ~120 words per visible page-section.
- 1–3 sentence chunks.
- Pages under ~120 words get read at ~50%; pages much longer get read at ~20%. Cut ruthlessly; front-load value.
- Optimize for scanning: headings, lists, breaks, callouts.

## 6. Content density (slides)

Slides are scanned, not read.

- **Max words per slide: 120.** Hard ceiling.
- **Max words per split-layout slide: 50.** Image + text shares space.
- **Max bullets per slide: 6.** Keep lists scannable.
- **Max words per bullet: 25.** Phrases, not sentences.
- **Max nested bullet depth: 2.**
- **Max sentences per paragraph: 3.**
- **Key takeaway supporting text: max 15 words.**
- **No blank slides.**
- **No dangling words.** Single-word widows on the last line trigger a rewrite or size override.

## 7. Brand

**Logo:**

- Workato logo present on bookend slides (title and final).
- Workato logo present bottom-left on all non-title slides.

**Slide numbers:**

- Slide number bottom-right on all non-title slides.

## 8. Required spellings

- `Workato` (never `WorkAto`, `workato`, `Workato.com` mid-sentence)
- `recipe` (lowercase, the product noun)
- `connector` (lowercase)
- `Connection` (capitalized when it is the UI noun for an established auth)
- `Recipe Lifecycle Management`
- `Datapill`, `Datapills`, `Datatree` — each one word, no spaces
- `Knowledge Checks` — always full term

## 9. Banned terms

**Never write "pedagogy"** — including `pedagogical` and `pedagogically`. The word means "leading children" and is off-register for adult enterprise learners. Substitute: `adult learning`, `andragogy`, `instructional approach`, `learning effectiveness`. Banned in both artifacts and conversation.

**Never abbreviate Knowledge Checks** — never `KC` or `KCs` in any context (prose, slides, code symbols, filenames).

**Never abbreviate OmniFocus** (if referenced) — never `OF`.

**Never frame Workato as "hard."** Complexity belongs to the problem domain (enterprise integration) or the depth of the capability ("with great power comes real depth"). Never Workato itself.

**Banned verb "fire" in Tinsel Town copy.** Use `emit` (events), `runs`/`triggers` (animations), `issue`/`send` (HTTP). Especially HR-adjacent contexts.

**Don't use "spine" as a metaphor.** Skip "content spine," "lab spine." Use "match list" or name the fields directly.

**Never name a customer in learner-facing content without explicit approval.** Even anonymized references (industry + role + size) should pass a re-identification check before publishing. Named customers, named individuals, or named accounts require Marketing/Sales sign-off cross-referenced against Highspot's approved-for-external-use catalog. See `fact-check §8` for the verification protocol.

## 10. Callout vocabulary

Authoring vocabulary uses six branded boxes:

- **Notes** — supplementary context.
- **Info** — background information; non-blocking.
- **Success** — confirmation a step worked correctly.
- **Warning** — be careful here; non-blocking.
- **Error** — what to do when something breaks.
- **Tip** — optional efficiency or insight.

Operational HTML rendering compresses these to five classes — `note`, `tip`, `warning`, `pitfall`, `key-insight` — with Success rendered via `note` and Error via `warning`. The six are the authoring vocabulary; the five are the runtime classes.

## 11. Allowed exceptions

**Workato magic.** `Workato magic` and `magic` (when describing the customer experience of Workato) stay in-bounds. Training team motto: "allow the world to experience the Workato magic." Other superlatives still get cut.

**Audit case as data, not opinion.** Run mechanical checks where possible (font size, weight, hex, contrast ratio, terminal punctuation, banned-term substrings). Reserve judgment for cases where the rule has a "prefer" or "default."

## Edit pattern

When a check fires:

1. **Surface mismatch?** Apply the correct surface profile.
2. **Banned term?** Substitute from the list.
3. **Contrast / size below floor?** Raise to the floor; document if exceeding the operational target.
4. **Color carries meaning alone?** Pair with icon, label, or pattern.
5. **Casing inconsistent?** Apply the surface's casing rule across all headings.

If a rule conflicts with a surface-specific decision logged in `Lab Guide Standards.md §0` or `Presentation Content Standards.md §0` override log, the override wins. This skill is upstream; the surface override log carries the locked downstream choice.

## Downstream consumers

- `Lab Guide Standards.md` §6 — composes this skill into the lab surface.
- `Presentation Content Standards.md` §§4, 6, 9, 11 — composes this skill into the slide surface.
- `HTML Lab Style Guide.md` + `html-lab-rules.yaml` — Lab Buddy's operational kit; mirrors the lab-surface rules from this skill.
- DoubleChecker (Bakery), Gatekeeper, Coach — consume directly when reasoning about Style at the surface layer.
\
"""

BANNED_TERMS = [
    "pedagogy", "pedagogical", "pedagogically",
    "KC", "KCs",
]

REQUIRED_SPELLINGS_PATTERNS = [
    {
        "pattern": r"\bWorkAto\b|\bworkato\b(?<!\bWorkato\b)",
        "message": "Spelling: use 'Workato' (capital W, lowercase rest)",
        "ignore_case": False,
    },
    {
        "pattern": r"\bKnowledge Check[^s]",
        "message": "Use 'Knowledge Checks' (plural, full term — never 'KC')",
        "ignore_case": True,
    },
    {
        "pattern": r"\bOmniFocus\b",
        "message": "Spelling check: ensure 'OmniFocus' is written in full, never 'OF'",
        "ignore_case": False,
    },
    {
        "pattern": r"\bData pill\b|\bdata pill\b|\bdata-pill\b",
        "message": "Spelling: use 'Datapill' (one word, capital D)",
        "ignore_case": False,
    },
    {
        "pattern": r"\bData tree\b|\bdata tree\b|\bdata-tree\b",
        "message": "Spelling: use 'Datatree' (one word, capital D)",
        "ignore_case": False,
    },
]

BANNED_VERBS = [
    {
        "pattern": r"\bfires?\b(?!\s+up)",
        "message": "Banned verb 'fire' — use 'emit' (events), 'runs/triggers' (animations), 'send/issue' (HTTP)",
        "ignore_case": True,
    },
]

BANNED_METAPHORS = [
    {
        "pattern": r"\b(content spine|lab spine|course spine)\b",
        "message": "Banned metaphor 'spine' — use 'match list' or name the fields directly",
        "ignore_case": True,
    },
]

COMPLEXITY_FRAMING = [
    {
        "pattern": r"\bWorkato is (hard|difficult|complex|complicated)\b",
        "message": "Don't frame Workato as hard — complexity belongs to the domain, not the tool",
        "ignore_case": True,
    },
]


def _rules(audience):
    if audience == "workato":
        return {
            "applicable": False,
            "note": "team-style-guide applies to training and education team content only",
            "banned_phrases": [],
            "regex_patterns": [],
        }

    return {
        "applicable": True,
        "banned_phrases": BANNED_TERMS,
        "regex_patterns": (
            REQUIRED_SPELLINGS_PATTERNS
            + BANNED_VERBS
            + BANNED_METAPHORS
            + COMPLEXITY_FRAMING
        ),
    }


def main(input):
    audience = input.get("audience", "workato")
    return {
        "rubric": RUBRIC,
        "rules": _rules(audience),
    }
