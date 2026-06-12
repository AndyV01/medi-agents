from app.agents.triage_agent import TriageAgent
from app.state.agent_state import AgentState

triage_agent = TriageAgent()


def triage_node(state: AgentState) -> AgentState:

    intent = triage_agent.classify(
        state["message"]
    )
    print(f"INTENT FINAL: {intent}") 

    state["intent"] = intent

    return state