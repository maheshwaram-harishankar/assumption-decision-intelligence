import os

from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    base_url=os.getenv("HINDSIGHT_API_URL"),
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

BANK_ID = "assumption-prod"

client.create_bank(
    bank_id=BANK_ID,
    name="ASSUMPTION Organizational Memory"
)

payment_experience = """
Decision ID: ARCH-001

Decision date: 2026-03-15

Decision:

Use synchronous processing for the payment service.

Original assumption:

Traffic would remain below 1,000 requests per minute.

Evidence available at decision time:

Traffic was approximately 700 requests per minute.

Outcome:

Traffic later increased to 5,000 requests per minute.

Observed impact:

The synchronous payment service experienced severe latency and timeout problems.

Resolution:

The team migrated critical payment processing to an asynchronous architecture.

Important:

The dates and numbers above are part of this organization's recorded history.

Do not invent or modify dates, numbers, events, or evidence.
"""


event_experience = """
Decision ID: EVENT-001

Decision:

Conduct a technical event expecting 500 student participants.

Original assumption:

Approximately 500 students would participate.

Conditions at decision time:

The event was announced only two weeks before the event.
Promotion was limited.
There was no external industry speaker.
Initial student interest was moderate.

Outcome:

Only 100 students participated.

Observed result:

The expected participation of 500 students was not achieved.

Important:

The event participation numbers and conditions above are part of this organization's recorded history.

Do not invent or modify dates, numbers, events, conditions, or outcomes.
"""


print("Creating ASSUMPTION organizational memory...")

client.retain(
    bank_id=BANK_ID,
    content=payment_experience
)

client.retain(
    bank_id=BANK_ID,
    content=event_experience
)

print("ASSUMPTION organizational memories stored successfully.")