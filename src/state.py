from typing import List, TypedDict

class AgentState(TypedDict):
    students: List[dict]
    class_list: List[str]
    logs: List[str]
