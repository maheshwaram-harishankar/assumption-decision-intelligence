from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.hindsight_service import analyze_decision, remember_outcome

app = FastAPI(
    title="ASSUMPTION",
    description="Decision intelligence powered by persistent organizational memory"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class DecisionRequest(BaseModel):
    decision: str
    current_conditions: str


class OutcomeRequest(BaseModel):
    outcome: str


@app.get("/")
def home():
    return {
        "name": "ASSUMPTION",
        "status": "running"
    }


@app.post("/analyze")
def analyze(request: DecisionRequest):

    result = analyze_decision(
        request.decision,
        request.current_conditions
    )

    return {
    "analysis": result.text,
    "structured": result.structured_output
}


@app.post("/outcome")
def outcome(request: OutcomeRequest):

    remember_outcome(request.outcome)

    return {
        "status": "Outcome stored in organizational memory"
    }