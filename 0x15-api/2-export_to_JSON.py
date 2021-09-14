#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    """
        argv[1] = integer as a parameter,
        which is the employee ID
    """
    argv = argv[1]
    users = requests.get(
                    "https://jsonplaceholder.typicode.com/users/{}"
                    .format(argv)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(argv)).json()

    dict_ = {users.get('id'): [{"task": task.get('title'),
                            "completed": task.get('completed'),
                           "username": users.get('username')}for task in todos]}

    with open('{}.json'.format(argv), mode='w') as test:
        json.dump(dict_, test)
