import json

PILLARS = [
  {"name":"say-it-plain","description":"Catches jargon, hype, and marketing-speak","checks_for":"Banned phrases, superlatives, urgency pressure, sincerity tells, agentic overreach, exclamation count","audiences":["training","education","workato"],"has_variant":True},
  {"name":"fact-check","description":"Verifies product claims, GA dates, and PM attribution","checks_for":"Feature GA dates, required spellings, FDE cookbook alignment","audiences":["training","education"],"has_variant":True},
  {"name":"stick-check","description":"Evaluates memorability — whether content will be remembered and applied","checks_for":"Verifier presence, Working Backwards press release, SUCCESs framework","audiences":["training","education","workato"],"has_variant":False},
  {"name":"calibrate-challenge","description":"Checks difficulty calibration and prerequisite assumptions","checks_for":"Time estimate presence, verifier sentence, scaffolding","audiences":["training","education"],"has_variant":True},
  {"name":"delight-check","description":"Evaluates engagement, game beats, and delight principles","checks_for":"LLM reasoning only — all 7 delight principles require judgment","audiences":["training","education","workato"],"has_variant":False},
  {"name":"team-style-guide","description":"Enforces Workato training team style conventions","checks_for":"Banned terms, required spellings, banned verbs, banned metaphors, complexity framing","audiences":["training","education"],"has_variant":True}
]

def main(input):
    audience = (input.get("audience") or "workato").strip().lower()
    result = [p for p in PILLARS if audience in p["audiences"]]
    return {"pillars_json": json.dumps(result)}
