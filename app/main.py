from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import init_db

from app.controllers.citizen import controller as citizen_controller
from app.controllers.shelter import controller as shelter_controller

app = FastAPI()

app.include_router(citizen_controller.router, tags=["Citizen Management"])
app.include_router(shelter_controller.router, tags=["Shelter Management"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
async def root():
    return {"message": "Welcome to Emergency Shelter Allocation System."}