#!/usr/bin/python3
"""
script that, using this jsonplaceholder.typicode.com/, for a given employee ID,
returns information about his/her TODO list progress.
"""


import json
import requests
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    username = user.get('username')
    tasks = []
    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks.append(task_dict)
    jsonobj = {}
    jsonobj[userId] = tasks
    with open("{}.json".format(userId), 'w') as jsonfile:
        json.dump(jsonobj, jsonfile)