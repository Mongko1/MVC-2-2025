from enum import Enum
from sqlmodel import SQLModel, Field
from datetime import datetime

class CitizenType(str, Enum):
    GENERAL = "General"
    VULNERABLE = "Vulnerable"
    VIP = "VIP"

class Citizen(SQLModel, table=True):
    __tablename__ = "citizens"

    id: str | None = Field(default_factory=None, primary_key=True)
    age: int
    health_status: str
    registration_date: datetime
    citizen_type: CitizenType