# ASSUMPTION

### Decision Intelligence Through Persistent Organizational Memory

ASSUMPTION is an AI-powered decision-intelligence system that evaluates new organizational decisions against relevant historical experiences stored in persistent organizational memory.

Instead of making decisions based only on the current situation, ASSUMPTION checks whether the assumptions behind a new decision are supported by what the organization has previously experienced.

---

## Problem Statement

Organizations make decisions based on assumptions about future conditions.

However, these assumptions may become unreliable when conditions change.

Important information about previous decisions and their outcomes can also be difficult to reuse when making new decisions.

ASSUMPTION addresses this problem by connecting current decision analysis with historical organizational memory.

---

## How ASSUMPTION Works

The system follows this workflow:

1. The user enters a **New Decision**.
2. The user enters the **Current Conditions**.
3. ASSUMPTION searches relevant historical organizational experiences.
4. The AI compares historical and current conditions.
5. The system identifies similarities and differences.
6. The system evaluates the current assumption.
7. The result is classified as:
   - ASSUMPTION STILL SUPPORTED
   - ASSUMPTION AT RISK
   - ASSUMPTION NO LONGER SUPPORTED
   - INSUFFICIENT HISTORICAL EVIDENCE
8. The user can record the actual outcome of the decision.
9. The outcome is stored back into organizational memory for future analysis.

---

## Key Features

### Historical Decision Analysis
Compares a current decision with relevant historical organizational experiences.

### Assumption Identification
Separates the assumption contained in the current decision from assumptions recorded in historical decisions.

### Condition Comparison
Identifies similarities and differences between previous and current conditions.

### Evidence-Based Reasoning
Uses organizational memory as evidence rather than treating historical outcomes as guaranteed predictions.

### Persistent Organizational Memory
Actual outcomes can be stored and reused in future decision analysis.

### Structured AI Output
The system produces structured information including:

- Current assumption
- Historical assumption
- Previous conditions
- Previous outcome
- Current conditions
- Similarities
- Differences
- Historical evidence
- Reasoning
- Warning

---

## Example

### New Decision

> Conduct another technical event expecting 600 student participants.

### Current Conditions

> Registration started one week before the event. Only 130 students have registered. Promotion is limited. No external speaker is available.

ASSUMPTION compares these conditions with relevant historical event experiences and reports whether the current assumption is supported, at risk, or no longer supported by the available evidence.

---

## Technology Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI
- Pydantic

### AI / Organizational Memory
- Hindsight

### Development Environment
- Python virtual environment
- REST API communication between frontend and backend

---

## Project Structure

```text
assumption-decision-intelligence/
│
├── backend/
│   ├── hindsight_service.py
│   ├── main.py
│   ├── prompts.py
│   ├── seed_memory.py
│   ├── test_hindsight.py
│   └── test_reflect.py
│
├── frontend/
│   └── index.html
│
├── .gitignore
└── README.md