# kahoot-generator MCP — server prompt and tool descriptions

## Server description
> Kahoot quiz generator. Claude generates questions client-side; this MCP handles constraint validation and XLSX formatting for Kahoot import.

## Tool: get_kahoot_constraints
> Returns Kahoot field limits: question max 120 chars, answer/distractor max 75 chars, exactly 3 distractors required, 1-300 questions, time_limit 5-120 seconds, points must be 0/1000/2000, output format is xlsx. Call this before generating questions to ensure valid input on the first attempt.

## Tool: format_kahoot
> Validates and formats a question set into a Kahoot-importable XLSX file. Pass questions_json as a JSON array string. Each question needs: question (str), correct_answer (str), distractor_1/2/3 (str), time_limit (int 5-120), points (0/1000/2000). Returns valid=true with file_base64 (xlsx) on success, valid=false with errors array describing which questions and fields need fixing.
