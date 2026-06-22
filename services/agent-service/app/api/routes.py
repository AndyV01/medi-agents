from fastapi import APIRouter, Request

from app.schemas.chat import ChatRequest, ChatResponse
from app.graph.patient_graph import build_graph
from pydantic import BaseModel

class HealthResponse(BaseModel):
    status: str
    service: str

router = APIRouter()

graph = build_graph()


@router.get("/health",
           response_model=HealthResponse )
async def health_check():
    return {
        "status": "healthy",
        "service": "agent-service"
    }


@router.post("/agents/chat", response_model=ChatResponse)
async def chat(request: Request, payload: ChatRequest):

    session_store = request.app.state.session_store

    # Obtener historial actual
    history = session_store.get_session(payload.patient_id)
    print("HISTORY:", history)
    # Guardar mensaje del usuario
    session_store.add_turn(
        patient_id=payload.patient_id,
        role="user",
        message=payload.message
    )

    # Ejecutar LangGraph
    result = graph.invoke({
        "patient_id": payload.patient_id,
        "message": payload.message,
        "history": history,
        "intent": "",
        "response": ""
    })

    # Guardar respuesta del sistema
    session_store.add_turn(
        patient_id=payload.patient_id,
        role="assistant",
        message=result["response"]
    )
    print(
     "SESSION:",
     session_store.get_session(payload.patient_id)
    )
    return ChatResponse(
        response=result["response"]
    )