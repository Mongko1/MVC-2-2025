from typing import List
from sqlmodel import func, select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.assignment import Assignment
from app.models.shelter import Shelter

class ShelterRepo():
    # Query all shelter with current population
    async def get_all(db: AsyncSession) -> List[Shelter]:        
        result = await db.exec(
            select(
                Shelter,
                func.count(Assignment.id).label("current_population")
            )
            .join(Assignment, isouter=True)
            .group_by(Shelter.id)
        )
        return result.all()
    
    # Query shelter by id
    async def get_by_id(db: AsyncSession, shelter_id: str):
        result = await db.exec(
            select(
                Shelter,
                func.count(Assignment.id).label("current_population")
            )
            .where(Shelter.id == shelter_id)
            .join(Assignment, isouter=True)
            .group_by(Shelter.id)
        )

        return result.one_or_none()