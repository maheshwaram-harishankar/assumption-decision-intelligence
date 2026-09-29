import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    base_url=os.getenv("HINDSIGHT_API_URL"),
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

BANK_ID = "assumption-demo"

print("Creating ASSUMPTION memory bank...")

client.create_bank(
    bank_id=BANK_ID,
    name="ASSUMPTION Decision Memory"
)

print("Memory bank ready!")

# Store our first real experience
experience = """
Decision:
The company chose synchronous processing for its payment service.

Assumption:
Traffic would remain below 1,000 requests per minute.

Evidence at the time:
Average traffic was approximately 700 requests per minute.

Outcome:
Six months later, traffic increased to 5,000 requests per minute.
The synchronous architecture caused severe latency and timeout problems.

Resolution:
The team migrated critical processing to asynchronous architecture.

Lesson:
The original decision made sense when traffic was low,
but its core assumption stopped being true as traffic increased.
"""

print("Storing past experience...")

client.retain(
    bank_id=BANK_ID,
    content=experience
)

print("Experience stored!")

# Ask Hindsight to find the relevant past experience
query = """
We are considering synchronous processing for a new payment service.
Current traffic is around 5,000 requests per minute.

Find previous decisions or experiences related to:
- synchronous processing
- traffic assumptions
- high traffic failures
- architectural decisions
"""

print("\nSearching Hindsight memory...")

result = client.recall(
    bank_id=BANK_ID,
    query=query
)

print("\n===== HINDSIGHT RECALL =====")

for memory in result.results:
    print("\n--- Memory ---")
    print(memory.text)

print("\n===== TEST COMPLETE =====")