from typing import TypedDict, List


class ConversationTurn(TypedDict):
    role: str
    message: str
    timestamp: str


class AgentState(TypedDict):
    patient_id: int
    message: str

    history: List[ConversationTurn]

    intent: str
    response: str