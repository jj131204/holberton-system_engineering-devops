#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
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

    with open('{}.csv'.format(argv), mode='w') as test:
        _csv = csv.writer(test, quoting=csv.QUOTE_ALL)

        for i in todos:
            _csv.writerow([users.get('id'), users.get('username'),
                          i.get('completed'), i.get('title')])
