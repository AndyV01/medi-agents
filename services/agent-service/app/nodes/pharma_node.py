from app.agents.pharma_agent import PharmaAgent
from app.state.agent_state import AgentState

pharma_agent = PharmaAgent()


def pharma_node(state: AgentState) -> AgentState:

    response = pharma_agent.execute(
        state["message"]
    )

    state["response"] = response

    return state