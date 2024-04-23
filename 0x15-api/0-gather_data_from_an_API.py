#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""

import requests
from sys import argv

def get_employee_todo_list(user_id):
    try:
        # Fetch user data
        user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
        user_data = user_response.json()

        # Fetch user's todo list
        todo_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")
        todo_list = todo_response.json()

        # Filter completed tasks
        completed_tasks = [task['title'] for task in todo_list if task['completed']]

        # Print summary
        print(f"Employee {user_data['name']} is done with tasks ({len(completed_tasks)}/{len(todo_list)}):")
        for task in completed_tasks:
            print(f"\t{task}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python main.py <user_id>")
    else:
        user_id = argv[1]
        get_employee_todo_list(user_id)
