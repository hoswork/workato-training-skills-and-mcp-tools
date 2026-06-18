import re
import json


def _check(artifact, rules):
    if not rules.get("applicable", True):
        return {"findings": [], "pass": True, "note": rules.get("note", "")}
    findings = []
    for phrase in rules.get("banned_phrases", []):
        if phrase.lower() in artifact.lower():
            findings.append({"type": "banned_phrase", "match": phrase, "message": "Remove or rephrase: '{}'".format(phrase)})
    for pat in rules.get("regex_patterns", []):
        flags = re.IGNORECASE if pat.get("ignore_case", True) else 0
        try:
            for m in re.finditer(pat["pattern"], artifact, flags):
                findings.append({"type": "pattern", "match": m.group(), "message": pat.get("message", "Pattern flagged")})
        except re.error:
            pass
    for check in rules.get("presence_checks", []):
        pattern = check.get("pattern", "")
        if pattern and not re.search(pattern, artifact, re.IGNORECASE | re.DOTALL):
            findings.append({"type": "missing", "match": "", "message": check.get("message", "Required element missing")})
    exclamation_max = rules.get("exclamation_max")
    if exclamation_max is not None:
        count = artifact.count("!")
        if count > exclamation_max:
            findings.append({"type": "count", "match": "{} exclamation marks".format(count), "message": "Max {} allowed, found {}".format(exclamation_max, count)})
    return {"findings": findings, "pass": len(findings) == 0}


_SIP_BANNED = [
    "leverage","utilize","synergy","paradigm","best-in-class","circle back","deep dive",
    "game-changer","game changer","disruptive","revolutionary","10x","crush it","killing it",
    "rockstar","ninja","guru","hack","unlock","supercharge","turbocharge","skyrocket",
    "empower","democratize","seamless","frictionless","robust","scalable","world-class",
    "cutting-edge","next-gen","enterprise-grade","very","really","just","basically",
    "actually","simply","obviously","clearly","best","fastest","easiest","most powerful",
    "incredible","amazing","awesome","insane","unbelievable","mind-blowing","stunning",
    "killer","epic","legendary","ultimate","perfect","unmatched","unparalleled","unprecedented",
    "act now","don't miss","limited time","before it's too late","you can't afford",
    "what are you waiting for","you need this","you won't believe","you'll love","you deserve",
    "imagine if you","honestly","to be honest","frankly","act autonomously","reason over",
    "reason about","understands","learns on its own","thinks for itself","decides for itself",
]
_SIP_REGEX = [
    {"pattern": r"\b(the only|the first|the fastest|the most|no one else|nothing else|unlike anything)\b", "message": "Unsubstantiated absolute", "ignore_case": True},
    {"pattern": r"\b(was|were|is|are|been)\s+\w+ed\b", "message": "Passive voice (soft check)", "ignore_case": True},
]

def _sip_rules(audience):
    banned = [p for p in _SIP_BANNED if not (audience in ("training","education") and p == "magic")]
    return {"applicable": True, "banned_phrases": banned, "regex_patterns": _SIP_REGEX, "exclamation_max": 1}


_FC_SPELLING = [
    {"pattern": r"\bdata pill\b|\bdata-pill\b", "message": "Use 'Datapill' (one word)", "ignore_case": True},
    {"pattern": r"\bdata tree\b|\bdata-tree\b", "message": "Use 'Datatree' (one word)", "ignore_case": True},
    {"pattern": r"\bKnowledge Check(?!s)\b", "message": "Use 'Knowledge Checks' (plural)", "ignore_case": True},
]

def _fc_rules(audience):
    if audience == "workato":
        return {"applicable": False, "note": "fact-check: training/education only", "banned_phrases": [], "regex_patterns": []}
    presence = [{"pattern": r"feature_ga_dependency", "message": "Missing feature_ga_dependency field"}] if audience == "training" else [{"pattern": r"verified.on", "message": "Missing verified-on date on screenshots"}]
    return {"applicable": True, "banned_phrases": [], "regex_patterns": _FC_SPELLING, "presence_checks": presence}


def _sc_rules(audience):
    presence = [{"pattern": r"you.ll know this worked when|you will know this worked when", "message": "Missing verifier sentence"}] if audience in ("training","education") else []
    return {"applicable": True, "banned_phrases": [], "regex_patterns": [], "presence_checks": presence}


def _cc_rules(audience):
    if audience == "workato":
        return {"applicable": False, "note": "calibrate-challenge: training/education only", "banned_phrases": [], "regex_patterns": []}
    presence = [
        {"pattern": r"\d+\s*(minutes?|seconds?)\s*\((validated|provisional)\)", "message": "Missing time estimate"},
        {"pattern": r"you.ll know this worked when|you will know this worked when", "message": "Missing verifier sentence"},
    ] if audience == "training" else [{"pattern": r"\d+\s*(minutes?|seconds?)\s*\((validated|provisional)\)", "message": "Missing time estimate"}]
    return {"applicable": True, "banned_phrases": [], "regex_patterns": [], "presence_checks": presence}


def _dc_rules(audience):
    return {"applicable": True, "banned_phrases": [], "regex_patterns": [], "note": "delight-check: no mechanical checks, LLM reasoning only"}


_TSG_BANNED = ["pedagogy","pedagogical","pedagogically","KC","KCs"]
_TSG_REGEX = [
    {"pattern": r"\bdata pill\b|\bdata-pill\b", "message": "Use 'Datapill'", "ignore_case": True},
    {"pattern": r"\bdata tree\b|\bdata-tree\b", "message": "Use 'Datatree'", "ignore_case": True},
    {"pattern": r"\bKnowledge Check(?!s)\b", "message": "Use 'Knowledge Checks' (plural)", "ignore_case": True},
    {"pattern": r"\bfires?\b(?!\s+up)", "message": "Banned verb 'fire' -- use emit/runs/triggers/send", "ignore_case": True},
    {"pattern": r"\b(content spine|lab spine|course spine)\b", "message": "Banned metaphor 'spine'", "ignore_case": True},
    {"pattern": r"\bWorkato is (hard|difficult|complex|complicated)\b", "message": "Do not frame Workato as hard", "ignore_case": True},
]

def _tsg_rules(audience):
    if audience == "workato":
        return {"applicable": False, "note": "team-style-guide: training/education only", "banned_phrases": [], "regex_patterns": []}
    return {"applicable": True, "banned_phrases": _TSG_BANNED, "regex_patterns": _TSG_REGEX}


_RULES = {
    "say-it-plain": _sip_rules, "fact-check": _fc_rules, "stick-check": _sc_rules,
    "calibrate-challenge": _cc_rules, "delight-check": _dc_rules, "team-style-guide": _tsg_rules,
}


def main(input):
    artifact = input.get("artifact", "")
    audience = (input.get("audience") or "workato").strip().lower()
    raw = input.get("pillars_json") or "[]"
    try: requested = json.loads(raw)
    except: requested = []
    if not requested: requested = list(_RULES.keys())
    results = {}
    for pillar in requested:
        if pillar in _RULES:
            results[pillar] = _check(artifact, _RULES[pillar](audience))
    return {"results_json": json.dumps(results)}
