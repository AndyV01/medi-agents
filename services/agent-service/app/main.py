from fastapi import FastAPI

from app.api.routes import router
from app.core.logger import setup_logger

logger = setup_logger("agent-service")

app = FastAPI(
    title="MediAgent Agent Service",
    version="1.0.0"
)

app.include_router(router)


@app.on_event("startup")
async def startup_event():
    logger.info("Agent Service iniciado")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Agent Service detenido")