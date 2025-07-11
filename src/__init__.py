
from src.api.v1.api_router import api_router
from fastapi import APIRouter, FastAPI



version = "v1"
app = FastAPI()
app.include_router(api_router, prefix=f"/api/{version}")


@app.get("/")
def root():
    return {"message": "🚀 FastAPI is live on Railway! Try /api/v1 or /docs"}
