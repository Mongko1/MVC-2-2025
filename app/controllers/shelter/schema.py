from pydantic import BaseModel

from app.models.shelter import RiskLevel

class AllocateShelterParams(BaseModel):
    citizen_id: str
    shelter_id: str

class ShelterResponse(BaseModel):
    id: str
    capacity: int
    current_population: int
    risk_level: RiskLevel

    model_config = dict(from_attributes=True)