# Task Manager

## Description
This project, Task Manager, is a command-line-based task management application developed in Python. The application allows administrators and limitted options, to register new users, add tasks, view all tasks, and view tasks assigned to a specific user. The project focuses on code refactoring using the principle of abstraction and introduces additional features like task editing, marking tasks as complete, and generating reports.


## Table of Contents 
- [Installation](#installation)
- [Usage](#usage)
- [Reports](#reports)
- [Credits](#credits)

## Installation
To run the Task Manager project locally, follow these steps:

1. Clone the repository to your local machine.
Example:
   Open your command prompt if you have a windows pc  
   git clone [https://github.com/qusayhameed/finalCapstone]
   cd task-manager (Find the full directory in your PC)
2. Ensure you have Python installed on your system.
3. Open the entire project folder in VS Code or any preferred Python IDE.
4. Run the `task_manager.py` file.

Usage:
After running the application, follow the on-screen instructions to navigate through the menu and perform various tasks.
If you are an admin user, you will have additional options such as generating reports 
and displaying statistics. For non-admin users, certain admin-only functionalities will not be available.

Part of the functionalies in the code:
Register a new user (r) or add a new task (a) from the main menu.
View all tasks (va) or view tasks assigned to the current user (vm).
Generate reports (gr) to get insights into task and (ds) to show users and tasks statistics.

![2](https://github.com/qusayhameed/finalCapstone./assets/153082978/1430ca7c-0eca-4135-856f-1b27816b912f)


![3](https://github.com/qusayhameed/finalCapstone./assets/153082978/871a2baf-7236-4309-8120-6bbcbf9979c9)


Registration (r):
To register a new user, select 'r' from the main menu.
Avoid duplicate usernames, and handle errors gracefully.

![4](https://github.com/qusayhameed/finalCapstone./assets/153082978/fd15e722-044f-4a4e-83f1-32ecfb21cf1f)

Adding a Task (a):
To add a new task, select 'a' from the main menu.

Viewing All Tasks (va):
To view all tasks, select 'va' from the main menu.

![5](https://github.com/qusayhameed/finalCapstone./assets/153082978/bf287ad8-51a2-467c-9cec-11a708fdd69e)


Viewing My Tasks (vm):
To view tasks assigned to the current user, select 'vm' from the main menu.
Tasks are displayed with corresponding numbers for identification.
Choose a specific task by entering its number.
Enter '-1' to return to the main menu.
For a selected task:
Mark it as complete.
Edit the assigned user or due date (if the task is incomplete).

![8](https://github.com/qusayhameed/finalCapstone./assets/153082978/a87f6cc2-d5f4-4e40-9994-0e669d7a5a5a)


Reports:
To generate reports, choose 'gr' from the main menu.
Two text files, task_overview.txt and user_overview.txt, will be generated.

![6](https://github.com/qusayhameed/finalCapstone./assets/153082978/37c36efe-6a11-4663-bd2f-b52bd9a7792f)

Statistics:
To generate reports, choose 'Ds' from the main menu.
A sttstics will be shown from Two text files, task_overview.txt and user_overview.txt

![9](https://github.com/qusayhameed/finalCapstone./assets/153082978/0579aaf0-e622-4a2e-96ea-d75bddc04232)

task_overview.txt
Total tasks, completed tasks, incomplete tasks, overdue tasks.
Percentages of incomplete and overdue tasks.

![10](https://github.com/qusayhameed/finalCapstone./assets/153082978/6db0e793-f312-4179-b35f-ecd007376cea)

user_overview.txt
Total users and tasks.
User-specific information:
Total tasks assigned.
Percentages of total, completed, incomplete, and overdue tasks.

![11](https://github.com/qusayhameed/finalCapstone./assets/153082978/44cb9609-daad-412e-81d0-fcf1634e3bea)



Credits:
This project objects were given by HyperionDev, CoGrammar https://github.com/skills-cogrammar.                                                                       
Created by:
Qusay Hameed - Developer
Feel free to contribute to the project or report any issues on the GitHub repository.

