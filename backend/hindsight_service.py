import os

from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    base_url=os.getenv("HINDSIGHT_API_URL"),
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

BANK_ID = "assumption-prod"


def analyze_decision(decision: str, current_conditions: str):

    query = f"""
You are the reasoning engine for ASSUMPTION,
an organizational decision-intelligence system.

A user is considering a NEW DECISION.

NEW DECISION:
{decision}

CURRENT CONDITIONS:
{current_conditions}

Your task is to compare the current situation with relevant
historical experiences stored in organizational memory.

Analyze only relevant historical memories.

For each relevant historical experience, identify:

1. Previous decision.
2. Original assumption behind that decision.
3. Conditions that existed when the decision was made.
4. What actually happened.
5. Current conditions supplied by the user.
6. Important similarities between past and current conditions.
7. Important differences between past and current conditions.
8. Whether the historical assumption is still supported,
   at risk, or no longer supported by the available evidence.

CRITICAL RULES:

- The NEW DECISION represents the current decision being evaluated.
- Extract the current assumption directly from the NEW DECISION.
- Never replace the current assumption with a number or assumption from historical memory.
- Historical assumptions must be labeled as HISTORICAL ASSUMPTION.
- Keep current targets and historical targets strictly separate.
- If the current decision expects 600 participants and historical memory contains a 500-participant target, report 600 as the CURRENT ASSUMPTION and 500 as the HISTORICAL ASSUMPTION.
Return EXACTLY this structure:
- Use ASSUMPTION NO LONGER SUPPORTED only when the available historical evidence directly contradicts the current assumption under substantially comparable conditions.
- If historical evidence indicates substantial risk but does not directly contradict the current assumption, use ASSUMPTION AT RISK.
- Do not use ASSUMPTION NO LONGER SUPPORTED merely because historical events had lower outcomes.


STATUS:

[ASSUMPTION STILL SUPPORTED / ASSUMPTION AT RISK /
ASSUMPTION NO LONGER SUPPORTED / INSUFFICIENT HISTORICAL EVIDENCE]

CURRENT ASSUMPTION:

State the assumption contained in the NEW DECISION.
For example, if the NEW DECISION says "expecting 600 student participants",
the CURRENT ASSUMPTION must refer to the 600-student expectation.
Do not use a historical target such as 500 students here.

HISTORICAL ASSUMPTION:

State the original assumption from the relevant historical memory.
Keep historical numbers and current numbers separate.

PREVIOUS CONDITIONS:

...

PREVIOUS OUTCOME:

...

CURRENT CONDITIONS:

...

SIMILARITIES:

...

DIFFERENCES:

...

HISTORICAL EVIDENCE:

...

REASONING:

...

WARNING:

...
"""

    return client.reflect(
    bank_id=BANK_ID,
    query=query,
    response_schema={
        "type": "object",
        "properties": {
            "status": {"type": "string"},
            "current_assumption": {"type": "string"},
            "historical_assumption": {"type": "string"},
            "previous_conditions": {"type": "string"},
            "previous_outcome": {"type": "string"},
            "current_conditions": {"type": "string"},
            "similarities": {"type": "string"},
            "differences": {"type": "string"},
            "historical_evidence": {"type": "string"},
            "reasoning": {"type": "string"},
            "warning": {"type": "string"}
        },
        "required": [
            "status",
            "current_assumption",
            "historical_assumption",
            "previous_conditions",
            "previous_outcome",
            "current_conditions",
            "similarities",
            "differences",
            "historical_evidence",
            "reasoning",
            "warning"
        ]
    }
)


def remember_outcome(outcome: str):

    return client.retain(
        bank_id=BANK_ID,
        content=outcome
    )