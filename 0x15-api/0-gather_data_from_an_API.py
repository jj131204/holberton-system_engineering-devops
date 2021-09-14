#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

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
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    done_tasks = 0
    total_tasks = len(todos)
    t_title = ""
    for n_task in todos:
        if n_task.get('completed') is True:
            done_tasks += 1

            t_title += "\t" + "{}\n".format(n_task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        users.get('name'), done_tasks, total_tasks))

    print(t_title)
    """for title in n_tasks:
        print("\t", title)"""
