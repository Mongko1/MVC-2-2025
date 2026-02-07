from fastapi import APIRouter, Depends, Query
from typing import Annotated, List

from fastapi.responses import JSONResponse

from app.controllers.citizen.schema import CitizenReportResponse, CitizenResponse, GetCitizenParams, RegisterCitizenParams
from app.repository.citizen_repo import CitizenRepo

from sqlmodel.ext.asyncio.session import AsyncSession
from app.database import get_session

router = APIRouter(prefix="/citizens")

# Route for get all citizen
@router.get("", response_model=List[CitizenResponse])
async def get_all_citizens(
    db: Annotated[AsyncSession, Depends(get_session)],
    request: Annotated[GetCitizenParams, Query()]
    ):
    return await CitizenRepo.get_all(db, request.type)

# Route for get all citizen with report that which one have allocate which one not
@router.get("/report", response_model=List[CitizenReportResponse])
async def get_all_citizen_reports(db: Annotated[AsyncSession, Depends(get_session)]):
    reports = await CitizenRepo.get_all_report(db)

    return [
        CitizenReportResponse(
            citizen_id=citizen.id,
            shelter_id=shelter.id if shelter else None,
            check_in_date=assignment.check_in_date if assignment else None,
        )
        for citizen, shelter, assignment in reports
    ]

# Route to add citizen data to the database
@router.post("/register")
async def register_citizen(
    db: Annotated[AsyncSession, Depends(get_session)],
    request: Annotated[RegisterCitizenParams, Query()]
    ):
    # check that user already register or not
    citizen = await CitizenRepo.get_by_id(db, request.citizen_id)
    if citizen:
        return JSONResponse(content="This citizen already registerd to the system", status_code=200)
    
    # call function to create citizen
    await CitizenRepo.create(
        db,
        request.citizen_id,
        request.age,
        request.health_status,
        request.citizen_type
    )

    return JSONResponse(content="Citizen registration success.", status_code=200)