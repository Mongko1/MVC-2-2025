from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

from app.models.citizen import Citizen
from app.models.shelter import Shelter

class Assignment(SQLModel, table=True):
    __tablename__ = "assignments"

    id: str | None = Field(default_factory=None, primary_key=True)
    citizen_id: str = Field(foreign_key="citizens.id")
    shelter_id: str = Field(foreign_key="shelters.id")
    check_in_date: datetime

    citizen: Citizen | None = Relationship(back_populates="assignments")
    shelter: Shelter | None = Relationship(back_populates="assignments")