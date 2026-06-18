"""
Shared snippet 2 — checker logic.
Embedded unchanged into every pillar recipe's second Python step.
Receives: artifact (str), rules (dict from snippet 1)
Returns:  findings (list), pass (bool)
"""
import re, json


def main(input):
    artifact = input.get("artifact", "")
    rules = input.get("rules", {})
    applicable = rules.get("applicable", True)

    if not applicable:
        return {"findings": [], "pass": True, "note": rules.get("note", "")}

    findings = []
    banned = rules.get("banned_phrases", [])

    for phrase in banned:
        if phrase.lower() in artifact.lower():
            findings.append({
                "type": "banned_phrase",
                "match": phrase,
                "message": f"Remove or rephrase: '{phrase}'"
            })

    for pat in rules.get("regex_patterns", []):
        flags = re.IGNORECASE if pat.get("ignore_case", True) else 0
        try:
            for m in re.finditer(pat["pattern"], artifact, flags):
                findings.append({
                    "type": "pattern",
                    "match": m.group(),
                    "message": pat.get("message", f"Pattern flagged: {m.group()}")
                })
        except re.error:
            pass

    for check in rules.get("presence_checks", []):
        pattern = check.get("pattern", "")
        if pattern and not re.search(pattern, artifact, re.IGNORECASE | re.DOTALL):
            findings.append({
                "type": "missing",
                "match": "",
                "message": check.get("message", "Required element missing")
            })

    exclamation_max = rules.get("exclamation_max")
    if exclamation_max is not None:
        count = artifact.count("!")
        if count > exclamation_max:
            findings.append({
                "type": "count",
                "match": f"{count} exclamation marks",
                "message": f"Max {exclamation_max} exclamation mark(s) allowed, found {count}"
            })

    return {"findings": findings, "pass": len(findings) == 0}
