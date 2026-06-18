# kahoot-generator — Claude context

Kahoot quiz formatter. Claude generates questions client-side using LLM reasoning; this MCP handles constraint validation and XLSX formatting for Kahoot import.

## Tools

### 1. `get_kahoot_constraints()`
Returns Kahoot's field limits and format requirements. Call this before generating questions so Claude can produce valid input on the first try.

```
get_kahoot_constraints() → {
  question_max_chars: 120,
  answer_max_chars: 75,
  distractors_required: 3,
  questions_min: 1,
  questions_max: 300,
  time_limit_range: [5, 120],
  valid_points: [0, 1000, 2000],
  supported_formats: ["xlsx"]
}
```

### 2. `format_kahoot(questions: Question[])`
Validates and formats the question set into a Kahoot-importable XLSX file. Returns errors instead of file if validation fails — Claude fixes and retries.

```
format_kahoot(questions: Question[]) →
  { valid: true, file_base64: string, mime_type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename: string }
  { valid: false, errors: [{ question_index: int, field: string, message: string }] }
```

**Question schema:**
```json
{
  "question": "string (max 120 chars)",
  "correct_answer": "string (max 75 chars)",
  "distractor_1": "string (max 75 chars)",
  "distractor_2": "string (max 75 chars)",
  "distractor_3": "string (max 75 chars)",
  "time_limit": 20,
  "points": 1000
}
```

## Typical agent flow

```
1. get_kahoot_constraints()              → learn limits before generating
2. Claude reads artifact, reasons        → generates questions[] client-side
   (concepts, distractors, difficulty)
3. format_kahoot(questions[])            → validate + produce XLSX
4. If errors returned → Claude fixes     → retry format_kahoot
5. Return file_base64 to user
```

## Recipe architecture

```
kahoot-generator Workato project
  ├── get_kahoot_constraints.recipe     → returns hardcoded constraints dict (Python snippet)
  ├── format_kahoot.recipe
  │     ├── Snippet 1: validate questions (re + string checks, returns errors[] or ok)
  │     └── Snippet 2: generate XLSX via openpyxl, return base64
  └── kahoot_generator.mcp_server
```

## Snippet pattern

**get_kahoot_constraints — single snippet:**
```python
def main(input):
    return {
        "question_max_chars": 120,
        "answer_max_chars": 75,
        "distractors_required": 3,
        "questions_min": 1,
        "questions_max": 300,
        "time_limit_range": [5, 120],
        "valid_points": [0, 1000, 2000],
        "supported_formats": ["xlsx"]
    }
```

**format_kahoot — Snippet 1 (validator):**
```python
def main(input):
    questions = input["questions"]
    errors = []
    seen = set()
    for i, q in enumerate(questions):
        if len(q.get("question", "")) > 120:
            errors.append({"question_index": i, "field": "question", "message": "Exceeds 120 chars"})
        for field in ["correct_answer", "distractor_1", "distractor_2", "distractor_3"]:
            if len(q.get(field, "")) > 75:
                errors.append({"question_index": i, "field": field, "message": "Exceeds 75 chars"})
        if q.get("question") in seen:
            errors.append({"question_index": i, "field": "question", "message": "Duplicate question"})
        seen.add(q.get("question"))
        if q.get("points") not in [0, 1000, 2000]:
            errors.append({"question_index": i, "field": "points", "message": "Must be 0, 1000, or 2000"})
    return {"valid": len(errors) == 0, "errors": errors}
```

**format_kahoot — Snippet 2 (XLSX generator, runs only if Snippet 1 passes):**
```python
import io, base64, openpyxl

def main(input):
    questions = input["questions"]
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Question", "Answer 1", "Answer 2", "Answer 3", "Answer 4",
               "Time limit", "Correct answer", "Question type"])
    for q in questions:
        ws.append([
            q["question"],
            q["correct_answer"], q["distractor_1"], q["distractor_2"], q["distractor_3"],
            q.get("time_limit", 20),
            1,  # Correct answer is always column 1 (Answer 1)
            "Quiz"
        ])
    buf = io.BytesIO()
    wb.save(buf)
    return {
        "valid": True,
        "file_base64": base64.b64encode(buf.getvalue()).decode("ascii"),
        "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "filename": "kahoot-quiz.xlsx"
    }
```

**Note:** Validate `openpyxl` availability in Workato's Python environment before building. QR code project confirmed `numpy` and `PIL` — `openpyxl` is likely available but needs a test.

## Workato project IDs (trial workspace)

| Resource | Value |
|---|---|
| Workspace | id `2100000234` (trial) |
| Project | `workato-qr` id `28820`, folder `42011` |
| Recipe: get_kahoot_constraints | id `277619` |
| Skill: get_kahoot_constraints | `skl-AaXspNnE-9FW8bP-AB` |
| Recipe: format_kahoot | id `277620` |
| Skill: format_kahoot | `skl-AaXspPNo-wTNR3h-AB` |
| MCP server | `mcps-AaXt8Hzr-J8H-AB` |
| MCP URL | `https://2601.apim.mcp.trial.workato.com` |

**Note:** Not yet BT-managed — trial workspace only. BT path TBD.

## Key lesson: extended_input_schema on workflow_return_result

The `workflow_return_result` step MUST have populated `extended_input_schema` and `extended_output_schema` — not empty arrays. Without them, Workato's MCP layer returns `{"result":null}` even when the recipe runs successfully. The builder auto-generates these; hand-authored recipe JSON must include them explicitly. See `format_kahoot.recipe.json` for the pattern.

## Design decisions

- **Reasoning client-side** — question generation requires LLM judgment (concept selection, distractor quality, difficulty calibration). Python can't do this.
- **Two tools, not one** — `get_kahoot_constraints` lets Claude generate valid questions on the first attempt, reducing format_kahoot retries.
- **Validator inside format_kahoot** — no separate validate tool; errors returned inline with the format call. Claude fixes and retries in one round-trip.
- **XLSX over CSV** — Kahoot's official import format. More robust than CSV (no column-order fragility, handles special characters).
- **No audience/variant param** — Kahoot format is universal. No role-based variants needed.
