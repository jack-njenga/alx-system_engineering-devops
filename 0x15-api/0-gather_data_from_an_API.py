#!/usr/bin/python3
"""
Returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    try:
        int_id = int(emp_id)
    except Exception as e:
        print("agrument is not an integer")
        pass

    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(f"{url}todos/").json()
    count = 0
    obj_list = []

    for obj in response:
        if int(obj["userId"]) == int_id:
            obj_list.append(obj)
        else:
            count += 1

    tt = len(obj_list) + count
    user = requests.get(f"{url}users/{str(emp_id)}")
    name = user.json()["name"]
    print(f"Employee {name} is done with tasks({len(obj_list)}/{tt}):")
    for obj in obj_list:
        print(f"\t {obj['title']}")
