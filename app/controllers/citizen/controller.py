from fastapi import APIRouter, Depends, Query
from typing import Annotated, List

from app.controllers.citizen.schema import CitizenReportResponse, CitizenResponse, GetCitizenParams
from app.repository.citizen_repo import CitizenRepo

from sqlmodel.ext.asyncio.session import AsyncSession
from app.database import get_session

router = APIRouter(prefix="/citizens")

@router.get("", response_model=List[CitizenResponse])
async def get_all_citizens(
    db: Annotated[AsyncSession, Depends(get_session)],
    request: Annotated[GetCitizenParams, Query()]
    ):
    return await CitizenRepo.get_all(db, request.type)

@router.get("/report", response_model=List[CitizenReportResponse])
async def get_all_citizen_reports(db: Annotated[AsyncSession, Depends(get_session)]):
    reports = await CitizenRepo.get_all_report(db)

    return [
        CitizenReportResponse(
            citizen_id=citizen.id,
            shelter_id=shelter.id,
            check_in_date=assignment.check_in_date,
        )
        for citizen, shelter, assignment in reports
    ]