from typing import List
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import selectinload

from app.controllers.citizen.schema import CitizenReportResponse
from app.models.assignment import Assignment
from app.models.citizen import Citizen, CitizenType
from app.models.shelter import Shelter

class CitizenRepo():
    async def get_all(db: AsyncSession, citizen_type: CitizenType) -> List[Citizen]:
        statement = select(Citizen)

        if citizen_type:
            statement = statement.where(Citizen.citizen_type == citizen_type)
        
        result = await db.exec(
            statement
        )
        return result.all()
    
    async def get_all_report(db: AsyncSession):
        result = await db.exec(
            select(Citizen, Shelter, Assignment)
            .join(Assignment, Assignment.citizen_id == Citizen.id, isouter=True)
            .join(Shelter, Shelter.id == Assignment.shelter_id, isouter=True)
        )
        return result.all()