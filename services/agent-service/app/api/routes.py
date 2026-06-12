from fastapi import APIRouter, Request

from app.agents.triage_agent import TriageAgent
from app.schemas.chat import ChatRequest, ChatResponse
from app.graph.patient_graph import build_graph

router = APIRouter()

triage_agent = TriageAgent()

graph = build_graph()

@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "agent-service"
    }


@router.post("/agents/chat", response_model=ChatResponse)
async def chat(request: Request, payload: ChatRequest):

    session_store = request.app.state.session_store

    # 1. guardar mensaje del usuario
    session_store.add_turn(
        patient_id=payload.patient_id,
        role="user",
        message=payload.message
    )

    # 2. obtener contexto (opcional ahora, clave después)
    history = session_store.get_session(payload.patient_id)

    # 3. ejecutar graph con contexto
    result = graph.invoke({
        "patient_id": payload.patient_id,
        "message": payload.message,
        "history": history, 
        "intent": "",
        "response": ""
    })

    # 4. guardar respuesta del agente
    session_store.add_turn(
        patient_id=payload.patient_id,
        role="assistant",
        message=result["response"]
    )

    return ChatResponse(
        response=result["response"]
    )