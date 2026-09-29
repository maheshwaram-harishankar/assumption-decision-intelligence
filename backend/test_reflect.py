import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    base_url=os.getenv("HINDSIGHT_API_URL"),
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

BANK_ID = "assumption-demo"

query = """
We are evaluating a new architectural decision.

NEW DECISION:
Use synchronous processing for a payment service.

CURRENT CONDITION:
Expected traffic is 5,000 requests per minute.

Analyze the organization's historical experiences.

Identify:

1. What assumption supported the previous decision?
2. What happened when that assumption stopped being true?
3. Is the same assumption still valid for the new decision?
4. What historical evidence supports your conclusion?
5. Give a clear final status:
   - ASSUMPTION STILL VALID
   - ASSUMPTION AT RISK
   - ASSUMPTION NO LONGER VALID

Do not invent information.
Use only evidence available in the organization's memory.
"""

print("Analyzing decision with Hindsight...\n")

result = client.reflect(
    bank_id=BANK_ID,
    query=query
)

print("===== ASSUMPTION ANALYSIS =====\n")
print(result)