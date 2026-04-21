from langgraph.graph import StateGraph, START, END
from nodes.database import fetch_students_node
from state import AgentState
from nodes.processor import proccess_data_node
from nodes.sheets import sheets_managment

workflow = StateGraph(AgentState)

workflow.add_node("fetch_data", fetch_students_node)
workflow.add_node("proccess_classes", proccess_data_node)
workflow.add_node("sync_sheets", sheets_managment)

workflow.add_edge(START, "fetch_data")
workflow.add_edge("fetch_data", "proccess_classes")
workflow.add_edge("proccess_classes", "sync_sheets")

workflow.add_edge("sync_sheets", END)

app = workflow.compile()
