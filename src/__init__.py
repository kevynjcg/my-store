
from src.api.v1.api_router import api_router
from fastapi import APIRouter, FastAPI



version = "v1"
app = FastAPI()
app.include_router(api_router, prefix=f"/api/{version}")
