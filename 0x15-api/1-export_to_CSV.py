#!/usr/bin/python3
"""
Extends your Python script to export data in the CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    usr_id = sys.argv[1]

    user = requests.get(f"{url}users/{usr_id}").json()
    name = user.get("username")

    todo_list = requests.get(f"{url}todos?userId={usr_id}").json()

    with open(f"{usr_id}.csv", "w", newline="") as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for todo in todo_list:
            completed = todo.get("completed")
            title = todo.get("title")
            csv_writer.writerow([int(usr_id), name, completed, title])
