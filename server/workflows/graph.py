from langgraph.graph import END, START, StateGraph

from server.nodes import mark_planning_ready, receive_idea
from server.states import ComicDramaState

builder = StateGraph(ComicDramaState)
builder.add_node("receive_idea", receive_idea)
builder.add_node("mark_planning_ready", mark_planning_ready)
builder.add_edge(START, "receive_idea")
builder.add_edge("receive_idea", "mark_planning_ready")
builder.add_edge("mark_planning_ready", END)

graph = builder.compile()
