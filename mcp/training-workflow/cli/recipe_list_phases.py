import json

PHASES = {
    "addie-plan": [
        {"phase":"01-customer-voice","conversation":1,"label":"Customer Voice Research","type":"step"},
        {"phase":"02-content-audit","conversation":1,"label":"Content Audit","type":"step"},
        {"phase":"03-usage-data","conversation":1,"label":"Usage Data-Informed Design","type":"step"},
        {"phase":"04-needs-analysis","conversation":2,"label":"Needs Analysis","type":"step"},
        {"phase":"05-audience-profile","conversation":2,"label":"Audience Profile","type":"step"},
        {"phase":"06-learning-objectives","conversation":3,"label":"Learning Objectives","type":"step"},
        {"phase":"07-detailed-outline","conversation":3,"label":"Detailed Outline","type":"step"},
        {"phase":"08-script-drafting","conversation":4,"label":"Script Drafting","type":"step"},
        {"phase":"09-knowledge-checks","conversation":4,"label":"Knowledge Checks","type":"step"},
        {"phase":"10-storyboarding","conversation":4,"label":"Storyboarding","type":"step"},
        {"phase":"11-sme-feedback","conversation":5,"label":"SME Feedback (cross-cutting)","type":"step"},
    ],
    "wow-plan": [
        {"phase":"phase-0","conversation":1,"label":"Roadmap Research","type":"step"},
        {"phase":"phase-1","conversation":2,"label":"Brief","type":"step"},
        {"phase":"phase-2","conversation":2,"label":"Working Backwards Press Release","type":"step"},
        {"phase":"phase-3","conversation":3,"label":"Learning Objectives + Scaffolding","type":"step"},
        {"phase":"phase-4","conversation":3,"label":"Module Breakdown","type":"step"},
        {"phase":"phase-5","conversation":3,"label":"Narrative Arc + Memorability","type":"step"},
        {"phase":"phase-6","conversation":4,"label":"Abstract","type":"step"},
        {"phase":"phase-7","conversation":4,"label":"Verification Gates","type":"step"},
    ],
    "brief-me": [
        {
                "phase": "step-1",
                "conversation": None,
                "label": "Confirm account + locate the ETT ticket",
                "type": "step"
        },
        {
                "phase": "step-2",
                "conversation": None,
                "label": "Read the training proposal (Google Drive)",
                "type": "step"
        },
        {
                "phase": "step-3",
                "conversation": None,
                "label": "Footprint (Enterprise Data by Workato MCP)",
                "type": "step"
        },
        {
                "phase": "step-4",
                "conversation": None,
                "label": "Company background (web; Salesforce optional)",
                "type": "step"
        },
        {
                "phase": "step-5",
                "conversation": None,
                "label": "Gong",
                "type": "step"
        },
        {
                "phase": "step-6",
                "conversation": None,
                "label": "Gmail",
                "type": "step"
        },
        {
                "phase": "step-7",
                "conversation": None,
                "label": "Slack",
                "type": "step"
        },
        {
                "phase": "step-8",
                "conversation": None,
                "label": "Build the Trainer Summary (Markdown)",
                "type": "step"
        },
        {
                "phase": "step-9",
                "conversation": None,
                "label": "HTML on request only",
                "type": "step"
        },
        {
                "phase": "step-10",
                "conversation": None,
                "label": "Save and present",
                "type": "step"
        },
        {
                "phase": "ref-connector-catalog",
                "conversation": None,
                "label": "Connector Catalog",
                "type": "reference"
        },
        {
                "phase": "ref-data-queries",
                "conversation": None,
                "label": "Data Queries",
                "type": "reference"
        },
        {
                "phase": "ref-ett-ticket-structure",
                "conversation": None,
                "label": "Ett Ticket Structure",
                "type": "reference"
        },
        {
                "phase": "ref-output-spec",
                "conversation": None,
                "label": "Output Spec",
                "type": "reference"
        }
],
}

def main(input):
    skill = (input.get("skill") or "").strip().lower()
    if skill not in PHASES:
        return {"phases_json": json.dumps({"error": "Unknown skill. Use: addie-plan, wow-plan, brief-me"})}
    return {"phases_json": json.dumps(PHASES[skill])}
