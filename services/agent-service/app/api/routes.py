from fastapi import APIRouter


from app.agents.triage_agent import TriageAgent
from app.schemas.chat import ChatRequest, ChatResponse
from app.graph.patient_graph import build_graph

router = APIRouter()

triage_agent = TriageAgent()

@router.get("/health")
async def health_check():
 return {
"status": "healthy",
"service": "agent-service"
}
graph = build_graph()
@router.post(
    "/agents/chat",
    response_model=ChatResponse
)
async def chat(request: ChatRequest):

    result = graph.invoke(
        {
            "patient_id": request.patient_id,
            "message": request.message,
            "intent": "",
            "response": ""
        }
    )

    return ChatResponse(
        response=result["response"]
    )