from datetime import datetime
from typing import Literal
from pydantic import BaseModel

from app.models.citizen import CitizenType, HealthStatus

class GetCitizenParams(BaseModel):
    type: Literal["General", "Vulnerable", "VIP"] | None = None

class RegisterCitizenParams(BaseModel):
    citizen_id: str
    age: int
    health_status: Literal["Normal", "Risk"]
    citizen_type: Literal["General", "Vulnerable", "VIP"]

class CitizenResponse(BaseModel):
    id: str
    age: int
    health_status: HealthStatus
    registration_date: datetime
    citizen_type: CitizenType

    model_config = dict(from_attributes=True)

class CitizenReportResponse(BaseModel):
    citizen_id: str
    shelter_id: str | None = None
    check_in_date: datetime | None = None

    model_config = dict(from_attributes=True)