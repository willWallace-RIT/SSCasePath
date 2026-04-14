from pydantic import BaseModel
from typing import List, Optional

class ClientProfile(BaseModel):
    age: int
    employment_status: str
    housing_status: str
    mental_health_risk: bool = False

class Case(BaseModel):
    case_id: str
    client_profile: ClientProfile
    answers: dict = {}
    classification: Optional[str] = None
    estimated_cost: float = 0
    recommended_services: List[str] = []
