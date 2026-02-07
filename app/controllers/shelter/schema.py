from pydantic import BaseModel

class ShelterResponse(BaseModel):
    id: str
    capacity: int
    current_population: int
    risk_level: int

    model_config = dict(from_attributes=True)