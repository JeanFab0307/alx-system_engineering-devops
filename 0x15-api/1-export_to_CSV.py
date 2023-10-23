#!/usr/bin/python3
"""
Uses a specific RESTAPI to return values in a CSV format file
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

    user = '"{}","{}",'.format(employee['id'], employee['username'])
    tasksRecord = []
    for task in tasks:
        val = user + '"{}","{}"\n'.format(task['completed'], task['title'])
        tasksRecord.append(val)

    pathname = '{}.csv'.format(argv[1])
    with open(pathname, mode="w") as f:
        for task in tasksRecord:
            f.write(task)
