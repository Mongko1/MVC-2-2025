from typing import List
from sqlmodel import SQLModel, Field, Relationship

class Shelter(SQLModel, table=True):
    __tablename__ = "shelters"

    id: str | None = Field(default_factory=None, primary_key=True)
    capacity: int
    risk_level: int

    assignments: List["Assignment"] = Relationship(back_populates="shelter")