#!/usr/bin/python3
"""
Uses a specific RESTAPI to return values in a JSON format file
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com{}'
    path = '/users/{}'.format(str(argv[1]))
    response = requests.get(url.format(path))
    employee = response.json()

    path = '/todos/?userId={}'.format(str(argv[1]))
    response = requests.get(url.format(path))
    tasks = response.json()

    tasksRecord = []
    for task in tasks:
        val = {}
        val['task'] = task['title']
        val['completed'] = task['completed']
        val['username'] = employee['username']
        tasksRecord.append(val)

    userId = str(argv[1])
    obj = {userId: tasksRecord}

    pathname = '{}.json'.format(argv[1])
    with open(pathname, mode="w") as f:
        f.write(json.dumps(obj))
