from app.agents.appointment_agent import AppointmentAgent
from app.state.agent_state import AgentState

appointment_agent = AppointmentAgent()


def appointment_node(state: AgentState) -> AgentState:

    response = appointment_agent.execute(
        patient_id=state["patient_id"],
        message=state["message"]
    )

    state["response"] = response

    return state