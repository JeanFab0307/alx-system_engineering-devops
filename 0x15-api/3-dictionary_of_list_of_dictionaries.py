#!/usr/bin/python3
"""
Uses a specific RESTAPI to return values in a JSON format file
"""
import json
import requests

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com{}'
    path = '/users'
    response = requests.get(url.format(path))
    employee = response.json()
    pathname = 'todo_all_employees.json'
    userRecord = {}

    for empl in employee:
        userId = empl['id']
        path = '/todos/?userId={}'.format(userId)
        response = requests.get(url.format(path))
        tasks = response.json()

        tasksRecord = []
        for task in tasks:
            val = {}
            val['username'] = empl['username']
            val['task'] = task['title']
            val['completed'] = task['completed']
            tasksRecord.append(val)

        userRecord[str(userId)] = tasksRecord

    with open(pathname, mode="w") as f:
        f.write(json.dumps(userRecord))
