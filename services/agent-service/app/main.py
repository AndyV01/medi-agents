from fastapi import FastAPI
from app.api.routes import router
from app.core.logger import setup_logger
from app.services.session_store import PatientSessionStore

logger = setup_logger("agent-service")

app = FastAPI(
    title="MediAgent Agent Service",
    version="1.0.0"
)

app.include_router(router)


@app.on_event("startup")
async def startup_event():
    logger.info("Agent Service iniciado")

    # 👇 ACÁ LO CREÁS UNA SOLA VEZ
    app.state.session_store = PatientSessionStore()


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Agent Service detenido")