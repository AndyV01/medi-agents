from app.agents.stock_agent import StockAgent
from app.state.agent_state import AgentState

stock_agent = StockAgent()


def stock_node(state: AgentState) -> AgentState:

    response = stock_agent.execute(
        state["message"],
        history=state.get("history", [])
    )

    state["response"] = response

    return state