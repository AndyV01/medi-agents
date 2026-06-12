from app.agents.handoff_agent import HandoffAgent
from app.state.agent_state import AgentState

handoff_agent = HandoffAgent()


def handoff_node(state: AgentState) -> AgentState:

    response = handoff_agent.execute(
        state["message"]
    )

    state["response"] = response

    return state