#!/usr/bin/python3
"""
Uses a specific RESTAPI to return values in a determined format
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

    taskNumber = 0
    taskCompleted = 0
    for task in tasks:
        if task['completed'] is True:
            taskCompleted += 1
        taskNumber += 1

    print('Employee {} is done with tasks({}/{}):'.
          format(employee['name'], taskCompleted, taskNumber))
    for task in tasks:
        if task['completed'] is True:
            print('\t ' + task['title'])
