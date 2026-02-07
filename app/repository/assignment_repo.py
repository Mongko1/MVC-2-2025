import uuid

from datetime import datetime
from typing import List
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import selectinload

from app.controllers.citizen.schema import CitizenReportResponse
from app.models.assignment import Assignment
from app.models.citizen import Citizen, CitizenType, HealthStatus
from app.models.shelter import Shelter

class AssignmentRepo():
    # Add assignment to database
    async def create(
            db: AsyncSession,
            citizen_id: str,
            shelter_id: str
    ) -> Assignment:
        assignment = Assignment(
            id=str(uuid.uuid4()),
            citizen_id=citizen_id,
            shelter_id=shelter_id,
            check_in_date=datetime.now()
        )

        db.add(assignment)
        await db.flush() 
        await db.refresh(assignment)
        return assignment
    
    # Query assignment by citizen id
    async def get_by_citizen_id(
            db: AsyncSession,
            citizen_id: str,
    ) -> Assignment:
        result = await db.exec(
            select(Assignment)
            .where(Assignment.citizen_id == citizen_id)
        )
        return result.one_or_none()