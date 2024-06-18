#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress."""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user_data = requests.get(url + "users/{}".format(user_id)).json()
    todo_data = requests.get(url + "todos", params={"userId": user_id}).json()
    user_name = user_data.get("name")
    completed_tasks = [
        t.get("title") for t in todo_data if t.get("completed") is True
    ]

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, len(completed_tasks), len(todo_data)))
    [print("\t {}".format(c)) for c in completed_tasks]
