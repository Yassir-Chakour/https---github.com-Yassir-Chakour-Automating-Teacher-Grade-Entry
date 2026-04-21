import gspread
from state import AgentState
from utils.google_client import google_client

def sheets_managment(state: AgentState):
    sh = google_client()
    classes = state['class_list']
    existing_titles = [ws.title for ws in sh.worksheets()]

    for cls in classes:
        if cls not in existing_titles:
            worksheet = sh.add_worksheet(title=cls, rows=100, cols=100)
            worksheet.update_acell("A1", "Student Name")
            worksheet.update_acell("B1", "Grades")
            existing_titles.append(cls)
            print((f"Worksheet {worksheet.title} added..."))
        else:
            print(f"Worksheet '{cls}' already exists. Skipping...")
