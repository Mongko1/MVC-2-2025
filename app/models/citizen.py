from enum import Enum
from typing import List
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

class HealthStatus(str, Enum):
    NORMAL = "Normal"
    RISK = "Risk"

class CitizenType(str, Enum):
    GENERAL = "General"
    VULNERABLE = "Vulnerable"
    VIP = "VIP"

class Citizen(SQLModel, table=True):
    __tablename__ = "citizens"

    id: str | None = Field(default_factory=None, primary_key=True)
    age: int
    health_status: HealthStatus
    registration_date: datetime
    citizen_type: CitizenType