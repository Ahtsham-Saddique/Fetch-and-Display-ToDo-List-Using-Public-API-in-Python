# fetch_to_do_list.py
import requests
import json

def get_details():
    url = "https://api.freeapi.app/api/v1/todos/"
    response = requests.get(url)
    data = response.json()

    if data.get("success") and "data" in data:
        inner_data = data["data"]
        if not inner_data:
            print(" No todos found.")
            return
        for todo_data in inner_data:
            title = todo_data["title"]
            description = todo_data.get("description", " ")
            is_complete = todo_data["isComplete"]
            createdAt = todo_data["createdAt"]

            print(f"Title       : {title}")
            print(f"Description : {description}")
            print(f"Completed   : {is_complete}")
            print(f"Created At  : {createdAt}")
            print("-" * 40)
    else:
        print("Connection failed")

def main():
    try:
        get_details()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
