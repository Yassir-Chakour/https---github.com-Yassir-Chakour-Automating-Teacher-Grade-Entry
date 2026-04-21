from nodes.database import fetch_students_node
from nodes.processor import proccess_data_node
from utils.google_client import google_client

# initial_state = {
#     "students": [],
#     "class_list": [],
#     "logs": []
# }
#
# result = fetch_students_node(initial_state)
# result = proccess_data_node(result)
result = google_client()

print("Final State:")
print(result)
