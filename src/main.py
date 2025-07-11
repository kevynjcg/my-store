
from src.api.v1.api_router import api_router
from fastapi import APIRouter, FastAPI
from fastapi.responses import RedirectResponse


version = "v1"
app = FastAPI()
app.include_router(api_router, prefix=f"/api/{version}")

@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")
