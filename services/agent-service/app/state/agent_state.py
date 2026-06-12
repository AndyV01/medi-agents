from typing import TypedDict

class AgentState(TypedDict):
 patient_id: str
 message: str
 intent: str
 response: str