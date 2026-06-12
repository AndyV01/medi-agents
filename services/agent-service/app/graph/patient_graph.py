from langgraph.graph import StateGraph
from langgraph.graph import START, END

from app.state.agent_state import AgentState

from app.nodes.triage_node import triage_node
from app.nodes.stock_node import stock_node
from app.nodes.pharma_node import pharma_node
from app.nodes.appointment_node import appointment_node
from app.nodes.handoff_node import handoff_node


def route_intent(state: AgentState) -> str:
    """
    Decide a qué agente enviar la conversación.
    """

    return state["intent"]


def build_graph():

    graph = StateGraph(AgentState)

     # Nodos

    graph.add_node(
        "triage",
        triage_node
    )

    graph.add_node(
        "stock",
        stock_node
    )

    graph.add_node(
        "pharma",
        pharma_node
    )

    graph.add_node(
        "appointment",
        appointment_node
    )

    graph.add_node(
        "handoff",
        handoff_node
    )

    # Inicio

    graph.add_edge(
        START,
        "triage"
    )

    # Router

    graph.add_conditional_edges(
        "triage",
        route_intent,
        {
            "stock": "stock",
            "pharma": "pharma",
            "appointment": "appointment",
            "handoff": "handoff"
        }
    )

    # Finalización

    graph.add_edge(
        "stock",
        END
    )

    graph.add_edge(
        "pharma",
        END
    )

    graph.add_edge(
        "appointment",
        END
    )

    graph.add_edge(
        "handoff",
        END
    )

    return graph.compile()