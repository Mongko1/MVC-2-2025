from fastapi import APIRouter, Depends, Query
from typing import Annotated, List

from fastapi.responses import JSONResponse

from app.controllers.shelter.schema import AllocateShelterParams, ShelterResponse

from sqlmodel.ext.asyncio.session import AsyncSession
from app.database import get_session
from app.models.assignment import Assignment
from app.models.shelter import RiskLevel
from app.repository.assignment_repo import AssignmentRepo
from app.repository.citizen_repo import CitizenRepo
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

@router.post("/allocate")
async def allocate_shelter(
    db: Annotated[AsyncSession, Depends(get_session)],
    request: Annotated[AllocateShelterParams, Query()]
    ):
    row = await ShelterRepo.get_by_id(db, request.shelter_id)
    if not row:
        return JSONResponse(content="Shelter not found.", status_code=200)
    
    shelter, current_population = row
    if current_population >= shelter.capacity:
        return JSONResponse(content="Failed to allocate this citizen to the shelter. The shelter has reached its maximum capacity.", status_code=200)
    
    citizen = await CitizenRepo.get_by_id(db, request.citizen_id)
    if not citizen:
        return JSONResponse(content="Citizen not found.", status_code=200)
    
    assignment = await AssignmentRepo.get_by_citizen_id(db, request.citizen_id)
    if assignment:
        return JSONResponse(content=f"Citizen is already allocated to shelter {assignment.shelter_id}.", status_code=200)
    
    if citizen.health_status == "Risk":
        if shelter.risk_level == RiskLevel.HIGH:
            return JSONResponse(content="This citizen has a high health risk and cannot be allocated to a high-risk shelter. Please choose a lower-risk shelter.", status_code=200)

    await AssignmentRepo.create(db, request.citizen_id, request.shelter_id)

    return JSONResponse(content="Alocate success.", status_code=200)