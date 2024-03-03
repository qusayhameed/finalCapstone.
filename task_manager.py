
                      # Task 17 Creating Task Manager

# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# Please open the whole folder provided in the Dropbox for - 
# the task_manager.py to work properly
# 2. Ensure you open the whole folder for this task in VS Code otherwise the-
# program will look in your root directory for the text files.

#====Function Definitions====#
from tabulate import tabulate  # Import tabulate module
import os
from datetime import datetime
from datetime import date
from typing import List, Dict, Any

# Define the datetime format string
DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Function to register a new user
def reg_user(username_password):
    new_username = input("Please enter a new username to the system: ").lower()
    if new_username in username_password:
        print("Username already exists. Please choose a different username.")
        return

    new_password = input("New Password: ").strip()
    confirm_password = input("Confirm Password: ").strip()

    if new_password == confirm_password:
        username_password[new_username] = new_password

        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))
        print("New user added successfully.")
    else:
        print("Passwords do not match.")

# Function for adding a new task
def add_task(task_list, username_password):
    task_username = input("Username of the person assigned to task: ")

    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username.")
        return

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    while True:
        try:
            task_due_date_str = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date_str, DATETIME_STRING_FORMAT).date()
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified (YYYY-MM-DD)")

    curr_date = datetime.today().date()

    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    # Assuming task_list is a list of dictionaries
    task_list: List[Dict[str, Any]] = []

    task_list.append(new_task)

    with open("tasks.txt", "a") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n")  
        task_file.write("\n".join(task_list_to_write))
        task_file.close()
    print("Task successfully added.")


# Function to edit a task
def edit_task(task_list,task_action,curr_user):
    task_number = int(input("Enter the task number to edit (-1 to return to the main menu): "))
    if task_number == -1:
        return

    if task_number < 1 or task_number > len(task_list):
        print("Invalid task number.")
        return

    task_to_edit = task_list[task_number - 1]

    if task_to_edit['completed']:
        print("This task is already completed and cannot be edited.")
        return

    if task_to_edit['username'] != curr_user:
        print("You don't have permission to edit this task.")
        return

    print(f"Editing Task {task_number}:\n")
    print(f"1. Edit assigned user (Current: {task_to_edit['username']})")
    print(f"2. Edit due date (Current: {task_to_edit['due_date'].strftime(DATETIME_STRING_FORMAT)})")
    print("3. Cancel")

    choice = input("Enter your choice: ")

    if choice == '1':
        new_username = input("Enter the new username: ")
        task_to_edit['username'] = new_username
        print("Username updated successfully.")
    elif choice == '2':
        new_due_date_str = input("Enter the new due date (YYYY-MM-DD): ")
        try:
            new_due_date = datetime.strptime(new_due_date_str, DATETIME_STRING_FORMAT).date()
            task_to_edit['due_date'] = new_due_date
            print("Due date updated successfully.")
        except ValueError:
            print("Invalid date format. Task not updated.")
    elif choice == '3':
        print("Task edit canceled.")
    else:
        print("Invalid choice.")

    # Save the updated task back to the task_list
    task_list[task_action - 1] = task_to_edit

    # Save the updated task_list to the tasks.txt file
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))

# Function to update Task overview text file
def update_task_overview(task_list):
    total_tasks = len(task_list)
    completed_tasks = sum(1 for task in task_list if task['completed'])
    incomplete_tasks = total_tasks - completed_tasks

    task_list_date = []
    for task in task_list:
        task_date = task.copy()
        task_date['due_date'] = task_date['due_date'].date()  # Convert due_date to date object
        task_list_date.append(task_date)

    overdue_tasks = sum(1 for task in task_list_date if not task['completed'] and task['due_date'] < date.today())

    try:
        percentage_incomplete = (incomplete_tasks * 100) / total_tasks
        percentage_overdue = (overdue_tasks * 100) / total_tasks
    except ZeroDivisionError:
        print("You can not divide by zero, please try again")
        return

    # Writing to task_overview.txt
    with open("task_overview.txt", "w") as task_overview:
        task_overview.write(f"\033[1m\n\t\tTasks Overview Report\n\033[0m{'-' * 80}")
        task_overview.write(f"\nNumber of tasks: {total_tasks}")
        task_overview.write(f"\nNumber of completed tasks: {completed_tasks}")
        task_overview.write(f"\nNumber of incomplete tasks: {incomplete_tasks}")
        task_overview.write(f"\nNumber of overdue tasks: {overdue_tasks}")
        task_overview.write(f"\nPercentage of incomplete tasks: {percentage_incomplete:.2f}%")
        task_overview.write(f"\nPercentage of overdue tasks: {percentage_overdue:.2f}%")

# Function to mark a task as complete
def mark_complete(task_list):
    task_number = int(input("Enter the task number to mark as complete (-1 to return to the main menu): "))
    if task_number == -1:
        return

    if task_number < 1 or task_number > len(task_list):
        print("Invalid task number.")
        return

    task_to_mark = task_list[task_number - 1]

    if task_to_mark['completed']:
        print("This task is already completed.")
    else:
        task_to_mark['completed'] = True
        print(f"Task {task_number} marked as complete.")
        update_task_overview(task_list)

        # Update tasks.txt with the modified task_list
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        
# Function to view all tasks in a formatted table    
def view_all(task_list):
    if not task_list:
        print("No tasks available.")
        return
    table_data = []
    for index, t in enumerate(task_list, 1):
        table_row = [
            f"Task {index}",
            t['title'],
            t['username'],
            t['due_date'].strftime(DATETIME_STRING_FORMAT),
            t['description']
        ]
        table_data.append(table_row)

    headers = ["Task", "Title", "Assigned to", "Due Date", "Description"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Function to view tasks assigned to the current user
def view_mine(task_list, curr_user):
    print(f"Tasks assigned to {curr_user}:\n")
    for index, t in enumerate(task_list, 1):
        if t['username'] == curr_user:
            disp_str = f"Task {index}:\n"
            disp_str += f"Title: {t['title']}\n"
            disp_str += f"Assigned to: {t['username']}\n"
            disp_str += f"Due Date: {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description:\n{t['description']}\n"
            print(disp_str)

# Function to generate reports
def generate_reports(task_list, username_password):
    today = date.today()
    total_tasks = len(task_list)
    completed_tasks = sum(1 for task in task_list if task['completed'])
    incomplete_tasks = total_tasks - completed_tasks

    task_list_date = []
    for task in task_list:
        task_date = task.copy()
        task_date['due_date'] = task_date['due_date'].date()  # Convert due_date to date object
        task_list_date.append(task_date)

    overdue_tasks = sum(1 for task in task_list_date if not task['completed'] and task['due_date'] < today)

    try:
        percentage_incomplete = (incomplete_tasks * 100) / total_tasks
        percentage_overdue = (overdue_tasks * 100) / total_tasks
        percentage_completed = (completed_tasks * 100) / total_tasks  # Added this line
    except ZeroDivisionError:
        print("You cannot divide by zero, please try again")
        return

    print(f"\033[1m\n\t\tTasks Overview Report\n\033[0m{'-' * 80}")
    print(f"Number of tasks: {total_tasks}")
    print(f"Number of completed tasks: {completed_tasks}")
    print(f"Number of incomplete tasks: {incomplete_tasks}")
    print(f"Number of overdue tasks: {overdue_tasks}")
    print(f"Percentage of incomplete tasks: {percentage_incomplete:.2f}%")
    print(f"Percentage of overdue tasks: {percentage_overdue:.2f}%")
    print(f"Percentage of completed tasks: {percentage_completed:.2f}%")
    # 

    # Generating user_overview.txt
    user_tasks = {}
    for task in task_list:
        user_tasks[task['username']] = user_tasks.get(task['username'], 0) + 1

    total_users = len(set(task['username'] for task in task_list))  # Use unique usernames from task_list
    with open("user_overview.txt", "w") as user_overview:
        user_overview.write(f"Number of users: {total_users}\n")
        user_overview.write(f"Number of tasks: {total_tasks}\n")

        for user, user_task_count in user_tasks.items():
            completed_user_tasks = sum(1 for task in task_list if task['username'] == user and task['completed'])
            incomplete_user_tasks = user_task_count - completed_user_tasks
            overdue_user_tasks = sum(1 for task in task_list_date if task['username'] == user and
                                     not task['completed'] and task['due_date'] < today)

            try:
                percentage_user_tasks = (user_task_count * 100) / total_tasks
                percentage_completed_user_tasks = (completed_user_tasks * 100) / user_task_count
                percentage_incomplete_user_tasks = (incomplete_user_tasks * 100) / user_task_count
                percentage_overdue_user_tasks = (overdue_user_tasks * 100) / user_task_count
            except ZeroDivisionError:
                print("You can not divide by zero, please try again")
                continue  # Changed to 'continue' to avoid returning from the entire function

            user_overview.write(f"\nUser: {user}\n")
            user_overview.write(f"Total tasks assigned: {user_task_count}\n")
            user_overview.write(f"Percentage of total tasks: {percentage_user_tasks:.2f}%\n")
            user_overview.write(f"Percentage of completed tasks: {percentage_completed_user_tasks:.2f}%\n")
            user_overview.write(f"Percentage of incomplete tasks: {percentage_incomplete_user_tasks:.2f}%\n")
            user_overview.write(f"Percentage of overdue tasks: {percentage_overdue_user_tasks:.2f}%\n")

    with open("user_overview.txt", "r") as user_overview_file:
        print(f"\033[1m\n\t\tUser Overview Report\n\033[0m{'-' * 80}\n{user_overview_file.read()}")
    print("User Overview Report generated successfully.")
    input("Please press Enter to return to the main menu: ")
    print()


# Function to display statistics
def display_statistics(task_list, username_password):
    # Check if the text files exist, if not, generate them
    if not os.path.exists("tasks.txt") or not os.path.exists("user.txt"):
        print("Generating necessary text files...")
        generate_reports(task_list, username_password)
    
    # Display statistics from tasks.txt
    with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    total_tasks = len(task_data)
    completed_tasks = sum(1 for task in task_data if task.split(";")[5] == "Yes")
    incomplete_tasks = total_tasks - completed_tasks

    print(f"\033[1m\n\t\tTasks Statistics\n\033[0m{'-' * 80}")
    print(f"Number of tasks: {total_tasks}")
    print(f"Number of completed tasks: {completed_tasks}")
    print(f"Number of incomplete tasks: {incomplete_tasks}")

    # Display statistics from user.txt
    with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")
        user_data = [u for u in user_data if u != ""]

    total_users = len(user_data)

    print(f"\033[1m\n\t\tUser Statistics\n\033[0m{'-' * 80}")
    print(f"Number of users: {total_users}\n")
    input("Please press Enter to return to the main menu: ")
    print()
    

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
   allow a user to login.
'''

# Create default admin account if user.txt doesn't exist
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:
    print("'\033[1m''\033[33m'\n\t\t******************** TASK MANAGER LOGIN \
          ********************"'\033[0m')
    curr_user = input("Username: ").strip().lower()
    curr_pass = input("Password: ").strip()
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True    

                        #====Main Code====#  
# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    curr_t = {}

    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

while True:
    if curr_user == 'admin':    # Admin log in
        menu = input('\033[1m''\033[34m''''Select one of the following options below:
        r - Register a new user
        a - Add a task
        va - View all tasks
        vm - View my tasks
        gr - Generate reports
        ds - Display statistics
        e - Exit
        : ''''\033[0m').lower()

        if menu == 'r':
            reg_user(username_password)
        elif menu == 'a':
            add_task(task_list, username_password)
        elif menu == 'va':
            view_all(task_list)
        elif menu == 'vm':
            user_tasks = [t for t in task_list if t['username'] == curr_user]
            if not task_list:
                print("No tasks available.")
                continue
            if not user_tasks:
                print("\nNo tasks assigned to you!\n")
                continue
            view_mine(task_list,curr_user)
            task_action = input("Enter the task number to edit or mark as \
                                complete (-1 to return to the main menu): ")
            if task_action == '-1':
                continue
            elif task_action.isdigit():
                task_action = int(task_action)
                if 1 <= task_action <= len(task_list):
                    print(f"\nSelected Task {task_action}:\n")
                    print(f"1. Mark as Complete")
                    print(f"2. Edit Task")
                    print(f"3. Cancel")
                    action_choice = input("Enter your choice(1-3 numbers only): ")
                    if action_choice == '1':
                        mark_complete(task_list)
                    elif action_choice == '2':
                        edit_task(task_list,task_action,curr_user )
                else:
                    print("Invalid task number.")
            else:
                print("Invalid input. Please enter a valid task number.")
        elif menu == 'gr':
            generate_reports(task_list, username_password)
        elif menu == 'ds':
            display_statistics(task_list, username_password)
        elif menu == 'e':
            print('Goodbye!!!')
            break
        else:
            print("You have made a wrong choice. Please Try again")
    else:  # Non-admin user menu
        menu = input('\033[1m''\033[34m''''Select one of the following options below:
        r - Register a new user
        a - Add a task
        va - View all tasks
        vm - View my tasks
        e - Exit
        : ''''\033[0m').lower()

        if menu == 'r':
            print("You are not an admin to use this option")
            continue
        if menu == 'a':
            add_task(task_list, username_password)
        elif menu == 'va':
            view_all(task_list)
        elif menu == 'vm':
            user_tasks = [t for t in task_list if t['username'] == curr_user]
            if not task_list:
                print("No tasks available.")
                continue
            if not user_tasks:
                print("\nNo tasks assigned to you!\n")
                continue
            view_mine(task_list,curr_user)
            task_action = input("Enter the task number to edit or mark as complete (-1 to return to the main menu): ")
            if task_action == '-1':
                continue
            elif task_action.isdigit():
                task_action = int(task_action)
                if 1 <= task_action <= len(task_list):
                    print(f"\nSelected Task {task_action}:\n")
                    print(f"1. Mark as Complete")
                    print(f"2. Edit Task")
                    print(f"3. Cancel")
                    action_choice = input("Enter your choice (1-3 Numbers only): ")
                    if action_choice == '1':
                        mark_complete(task_list)
                    elif action_choice == '2':
                        edit_task(task_list,task_action,curr_user )
                else:
                    print("Invalid task number.")
            else:
                print("Invalid input. Please enter a valid task number.")
        elif menu == 'e':
            print('Goodbye!!!')
            break
        else:
            print("You have made a wrong choice. Please Try again")

