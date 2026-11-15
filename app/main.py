from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.core.config import settings

app = FastAPI(title=settings.app_name, version="0.1.0", description="Central API for social-media data integrations and analytics.")
app.include_router(health_router, prefix=settings.api_v1_prefix)

@app.get("/")
async def root() -> dict[str, str]:
    return {"name": settings.app_name, "docs": "/docs"}
