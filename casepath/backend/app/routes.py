from fastapi import APIRouter
from app.models import Case
from app.engine import classify_case, estimate_cost, recommend_services

router = APIRouter()

DB = {}

@router.post("/case")
def create_case(case: Case):
    classification = classify_case(case.client_profile)
    cost = estimate_cost(classification)
    services = recommend_services(classification)

    case.classification = classification
    case.estimated_cost = cost
    case.recommended_services = services

    DB[case.case_id] = case
    return case


@router.get("/case/{case_id}")
def get_case(case_id: str):
    return DB.get(case_id, {"error": "not found"})


@router.get("/cases")
def list_cases():
    return list(DB.values())
