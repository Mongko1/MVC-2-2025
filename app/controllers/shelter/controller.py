from fastapi import APIRouter, Depends, Query
from typing import Annotated, List

from app.controllers.shelter.schema import ShelterResponse

from sqlmodel.ext.asyncio.session import AsyncSession
from app.database import get_session
from app.repository.shelter_repo import ShelterRepo

router = APIRouter(prefix="/shetlers")

@router.get("", response_model=List[ShelterResponse])
async def get_all_shelters(db: Annotated[AsyncSession, Depends(get_session)]):
    shelters = await ShelterRepo.get_all(db)

    return [
        ShelterResponse(
            id=shelter.id,
            capacity=shelter.capacity,
            current_population=count,
            risk_level=shelter.risk_level,
        )
        for shelter, count in shelters
    ]