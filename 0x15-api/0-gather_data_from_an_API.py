#!/usr/bin/python3
"""
Returns information about a users TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(f"{url}todos/").json()

    todo_list = []
    count = 0

    for todo in response:
        if int(todo["userId"]) == int(sys.argv[1]):
            if todo["completed"]:
                todo_list.append(todo)
            else:
                count = count + 1

    tt = len(todo_list) + count
    user = requests.get(f"{url}users/{str(sys.argv[1])}").json()
    name = user.get('name')

    print(f"Employee {name} is done with tasks({len(todo_list)}/{tt}):")
    for todo in todo_list:
        print(f"\t {todo.get('title')}")
