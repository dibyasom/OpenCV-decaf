import json


FILE_PATH = "data/users.json"

try:
    with open(FILE_PATH) as msg:
        processed_msg = json.load(msg)
        for key, value in processed_msg.items():
            print(key, value)
except OSError:
    print("File not found")
