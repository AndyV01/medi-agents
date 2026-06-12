from datetime import datetime
from typing import Dict, List, TypedDict


class ConversationTurn(TypedDict):
    role: str
    message: str
    timestamp: str


class PatientSessionStore:
    """
    Maneja memoria conversacional por paciente.
    (versión simple inicial)
    """

    def __init__(self):
        # por ahora en memoria (después lo pasamos a PostgreSQL)
        self.sessions: Dict[int, List[ConversationTurn]] = {}

    def get_session(self, patient_id: int) -> List[ConversationTurn]:
        return self.sessions.get(patient_id, [])

    def add_turn(self, patient_id: int, role: str, message: str):
        turn = ConversationTurn(
            role=role,
            message=message,
            timestamp=datetime.utcnow().isoformat()
        )

        if patient_id not in self.sessions:
            self.sessions[patient_id] = []

        self.sessions[patient_id].append(turn)

    def clear_session(self, patient_id: int):
        self.sessions.pop(patient_id, None)