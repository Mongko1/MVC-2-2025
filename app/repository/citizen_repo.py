from datetime import datetime
from typing import List
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import selectinload

from app.controllers.citizen.schema import CitizenReportResponse
from app.models.assignment import Assignment
from app.models.citizen import Citizen, CitizenType, HealthStatus
from app.models.shelter import Shelter

class CitizenRepo():
    # Add citizen to database
    async def create(
            db: AsyncSession,
            citizen_id: str,
            age: int,
            health_status: HealthStatus,
            citizen_type: CitizenType
    ) -> Citizen:
        citizen = Citizen(
            id=citizen_id,
            age=age,
            health_status=health_status,
            registration_date=datetime.now(),
            citizen_type=citizen_type
        )

        db.add(citizen)
        await db.flush() 
        await db.refresh(citizen)
        return citizen
    
    # Query all citizen with filter of citizen type
    async def get_all(db: AsyncSession, citizen_type: CitizenType) -> List[Citizen]:
        statement = select(Citizen)

        if citizen_type:
            statement = statement.where(Citizen.citizen_type == citizen_type)
        
        result = await db.exec(
            statement
        )
        return result.all()
    
    # Query all citizen with report of allocation data
    async def get_all_report(db: AsyncSession):
        result = await db.exec(
            select(Citizen, Shelter, Assignment)
            .join(Assignment, Assignment.citizen_id == Citizen.id, isouter=True)
            .join(Shelter, Shelter.id == Assignment.shelter_id, isouter=True)
        )
        return result.all()
    
    # Query citizen by id
    async def get_by_id(db: AsyncSession, citizen_id: str) -> Citizen:
        result = await db.exec(
            select(Citizen)
            .where(Citizen.id == citizen_id)
        )

        return result.one_or_none()