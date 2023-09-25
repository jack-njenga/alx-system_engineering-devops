#!/usr/bin/python3
"""
Extends the script(0-gather_data_from_an_API.py) to export
data in the JSON format.
"""

import requests
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    filename = "todo_all_employees.json"
    users = requests.get(f"{url}users").json()
    usr_ids = []

    for usr in users:
        usr_ids.append(usr.get("id"))

    todo_dict = {}
    for _id in usr_ids:
        user = requests.get(f"{url}users/{_id}").json()
        name = user.get("username")

        todos = requests.get(f"{url}todos?userId={_id}").json()
        todo_list = []
        for todo in todos:
            try:
                todo["task"] = todo["title"]
                todo.pop("title")
                todo["username"] = name
                todo.pop("id")
                todo.pop("userId")
                todo_list.append(todo)
            except Exceptions as e:
                pass
        todo_dict[_id] = list(todo_list)

    with open(f"{filename}", "w") as f:
        json.dump(todo_dict, f)
