import requests
import csv
from sys import argv

def export_employee_todo_to_csv(user_id):
    try:
        # Fetch user data
        user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
        user_data = user_response.json()

        # Fetch user's todo list
        todo_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")
        todo_list = todo_response.json()

        # Filter completed tasks
        completed_tasks = [(task['completed'], task['title']) for task in todo_list]

        # Write to CSV file
        filename = f"{user_id}.csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for completed, title in completed_tasks:
                csv_writer.writerow([user_id, user_data['username'], completed, title])

        print(f"Data exported to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python main.py <user_id>")
    else:
        user_id = argv[1]
        export_employee_todo_to_csv(user_id)

