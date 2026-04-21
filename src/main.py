from unittest import result

from nodes.database import fetch_students_node
from nodes.processor import proccess_data_node
from utils.google_client import google_client
from nodes.sheets import sheets_managment

initial_state = {
    "students": [],
    "class_list": ['shinobi', '9bi7', 'xwiya'],
    "logs": []
}
#
# result = fetch_students_node(initial_state)
# result = proccess_data_node(result)
# result = google_client()
result = sheets_managment(initial_state)

print("Final State:")
print(result)
