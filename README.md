# Smart-Task-Manager
Developed a Python task manager using supporting task creation, search, filtering, and status updates. 
# Smart Task Manager (CLI)

A simple command-line task manager written in Python that stores tasks in a JSON file.  
Great for demonstrating file I/O, basic data structures, and user interaction on a résumé.

## Features

- Add tasks with:
  - Title
  - Optional description
  - Priority (`low`, `medium`, `high`)
  - Optional due date (`YYYY-MM-DD`)
- List:
  - All tasks
  - Only incomplete tasks
  - Only completed tasks
- Mark tasks as complete
- Delete tasks
- Search tasks by keyword in title or description
- Tasks are saved to `tasks.json` so they persist between runs

## Tech Stack

- Python 3
- Standard library only (`json`, `os`, `datetime`)

## How to Run

1. Clone this repository or download the files.
2. Make sure you have Python 3 installed.
3. In the project folder, run:

   ```bash
   python task_manager.py
Use the menu to:

Add tasks

List tasks

Complete tasks

Delete tasks

Search tasks

Example Usage
text
Copy code
==== Smart Task Manager ====
1. List all tasks
2. List incomplete tasks
3. List completed tasks
4. Add a new task
5. Complete a task
6. Delete a task
7. Search tasks
0. Exit
Choose an option:
