#!/usr/bin/python3
"""
Extends the script(1-export_to_CSV.py) to export data in the JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    usr_id = sys.argv[1]

    todo_list = requests.get(f"{url}todos?userId={usr_id}").json()

    user = requests.get(f"{url}users/{usr_id}").json()
    name = user.get("username")

    new_todo_list = []
    for todo in todo_list:
        todo["task"] = todo["title"]
        todo.pop("title")
        todo["username"] = name
        todo.pop("userId")
        todo.pop("id")
        new_todo_list.append(todo)

    todo_dict = {}
    todo_dict[usr_id] = new_todo_list

    with open(f"{usr_id}.json", "w") as f:
        json.dump(todo_dict, f)
