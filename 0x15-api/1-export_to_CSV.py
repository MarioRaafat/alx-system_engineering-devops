#!/usr/bin/python3
""" Python script to export data in the CSV format."""

import sys
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user_data = requests.get(url + "users/{}/".format(user_id)).json()
    user_username = user_data.get("username")
    tasks = requests.get(url + "todos/", params={"userId": user_id}).json()
    for task in tasks:
        print("\"{}\", \"{}\", \"{}\", \"{}\"".format(user_id, user_username, task.get("completed"), task.get("title")))
