import io, base64, json, openpyxl


def main(input):
    # Parse questions JSON
    try:
        questions = json.loads(input.get("questions_json", "[]"))
    except Exception as e:
        return {
            "valid": "false",
            "file_base64": "",
            "mime_type": "",
            "filename": "",
            "errors": json.dumps([{"question_index": -1, "field": "questions_json", "message": f"Invalid JSON: {e}"}])
        }

    # Validate count
    errors = []
    if len(questions) < 1:
        return {
            "valid": "false", "file_base64": "", "mime_type": "", "filename": "",
            "errors": json.dumps([{"question_index": -1, "field": "questions_json", "message": "At least 1 question required"}])
        }
    if len(questions) > 300:
        return {
            "valid": "false", "file_base64": "", "mime_type": "", "filename": "",
            "errors": json.dumps([{"question_index": -1, "field": "questions_json", "message": "Maximum 300 questions allowed"}])
        }

    # Validate each question
    seen = set()
    for i, q in enumerate(questions):
        q_text = q.get("question", "")
        if not q_text:
            errors.append({"question_index": i, "field": "question", "message": "Question text is required"})
        elif len(q_text) > 120:
            errors.append({"question_index": i, "field": "question", "message": f"Exceeds 120 chars ({len(q_text)})"})
        if q_text in seen:
            errors.append({"question_index": i, "field": "question", "message": "Duplicate question"})
        seen.add(q_text)

        for field in ["correct_answer", "distractor_1", "distractor_2", "distractor_3"]:
            val = q.get(field, "")
            if not val:
                errors.append({"question_index": i, "field": field, "message": f"{field} is required"})
            elif len(str(val)) > 75:
                errors.append({"question_index": i, "field": field, "message": f"Exceeds 75 chars ({len(str(val))})"})

        tl = q.get("time_limit", 20)
        if not isinstance(tl, int) or not (5 <= tl <= 120):
            errors.append({"question_index": i, "field": "time_limit", "message": "Must be integer 5-120"})

        pts = q.get("points", 1000)
        if pts not in [0, 1000, 2000]:
            errors.append({"question_index": i, "field": "points", "message": "Must be 0, 1000, or 2000"})

    if errors:
        return {"valid": "false", "file_base64": "", "mime_type": "", "filename": "", "errors": json.dumps(errors)}

    # Generate XLSX
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Kahoot Quiz"
    ws.append(["Question", "Answer 1", "Answer 2", "Answer 3", "Answer 4",
               "Time limit", "Correct answer", "Question type"])

    for q in questions:
        ws.append([
            q["question"],
            q["correct_answer"],
            q["distractor_1"],
            q["distractor_2"],
            q["distractor_3"],
            q.get("time_limit", 20),
            1,
            "Quiz"
        ])

    buf = io.BytesIO()
    wb.save(buf)

    return {
        "valid": "true",
        "file_base64": base64.b64encode(buf.getvalue()).decode("ascii"),
        "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "filename": "kahoot-quiz.xlsx",
        "errors": ""
    }
