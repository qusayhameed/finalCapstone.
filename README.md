# Task Manager

## Description
TaTask Manager is a Python-based command-line application designed for managing tasks and users. 
This capstone project enhances the functionality of the existing `task_manager.py` file, providing features such as user registration, task assignment, task viewing, and report generation.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Reports](#reports)
- [Credits](#credits)

## Installation
1. Clone the repository to your local machine.
   ```bash
   git clone [https://github.com/qusayhameed/finalCapstone]
Navigate to the project directory.

bash
Copy code
cd task-manager (Find the full directory in your PC)
Run the application.
bash

python task_manager.py

Usage:
Register a new user (r) or add a new task (a) from the main menu.
View all tasks (va) or view tasks assigned to the current user (vm).
Generate reports (gr) to get insights into task and user statistics.

Registration (r):
To register a new user, select 'r' from the main menu.
Avoid duplicate usernames, and handle errors gracefully.

Adding a Task (a):
To add a new task, select 'a' from the main menu.

Viewing All Tasks (va):
To view all tasks, select 'va' from the main menu.

Viewing My Tasks (vm):
To view tasks assigned to the current user, select 'vm' from the main menu.
Tasks are displayed with corresponding numbers for identification.
Choose a specific task by entering its number.
Enter '-1' to return to the main menu.
For a selected task:
Mark it as complete.
Edit the assigned user or due date (if the task is incomplete).

Reports:
To generate reports, choose 'gr' from the main menu.
Two text files, task_overview.txt and user_overview.txt, will be generated.

task_overview.txt
Total tasks, completed tasks, incomplete tasks, overdue tasks.
Percentages of incomplete and overdue tasks.

user_overview.txt
Total users and tasks.
User-specific information:
Total tasks assigned.
Percentages of total, completed, incomplete, and overdue tasks.

Credits
Qusay Hameed - Developer


