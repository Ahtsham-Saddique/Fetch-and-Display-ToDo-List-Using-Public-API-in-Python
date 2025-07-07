import requests
import json

def fetch_todo_list():
    url = "https://api.freeapi.app/api/v1/todos/"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("success") and "data" in data:
            todos = data["data"]
            if not todos:
                print("📝 No todos found.")
                return

            print(" To-Do List:")
            print("-" * 40)
            for index, todo in enumerate(todos, start=1):
                print(f"{index}. Title       : {todo['title']}")
