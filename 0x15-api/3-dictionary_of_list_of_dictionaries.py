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
    users = requests.get(
                    "https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    dict_ = {u.get('id'): [{"task": t.get('title'),
                            "completed": t.get('completed'),
                            "username": u.get('username')}
                           for t in todos if u.get('id') == t.get('userId')]
             for u in users}

    with open("todo_all_employees.json", mode='w') as test:
        json.dump(dict_, test)
