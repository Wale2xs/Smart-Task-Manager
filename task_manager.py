import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # If file is corrupted or empty, start fresh
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def generate_task_id(tasks):
    """Generate a new unique ID based on existing tasks."""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def add_task(tasks):
    print("\n--- Add a New Task ---")
    title = input("Task title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    description = input("Description (optional): ").strip()
    priority = input("Priority (low/medium/high, default=medium): ").strip().lower() or "medium"
    if priority not in {"low", "medium", "high"}:
        print("Invalid priority. Using 'medium'.")
        priority = "medium"

    due_date = input("Due date (YYYY-MM-DD, optional): ").strip()
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Skipping due date.")
            due_date = ""

    task = {
        "id": generate_task_id(tasks),
        "title": title,
        "description": description,
        "priority": priority,
        "due_date": due_date,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added with ID {task['id']}.\n")


def list_tasks(tasks, show_completed=None):
    """List tasks with optional filter by completion status."""
    if not tasks:
        print("\nNo tasks found.\n")
        return

    # Filter by completion state if requested
    filtered = tasks
    if show_completed is True:
        filtered = [t for t in tasks if t["completed"]]
    elif show_completed is False:
        filtered = [t for t in tasks if not t["completed"]]

    if not filtered:
        print("\nNo matching tasks.\n")
        return

    print("\nID | Title                    | Priority | Due Date   | Status")
    print("-" * 65)
    for t in filtered:
        status = "Done" if t["completed"] else "Todo"
        due = t["due_date"] or "-"
        print(f"{t['id']:>2} | {t['title'][:24]:<24} | {t['priority']:^8} | {due:<10} | {status}")
    print()


def find_task_by_id(tasks, task_id):
    """Find a task in the list by its ID."""
    for t in tasks:
        if t["id"] == task_id:
            return t
    return None


def complete_task(tasks):
    print("\n--- Complete a Task ---")
    try:
        task_id = int(input("Enter task ID to mark complete: "))
    except ValueError:
        print("Invalid ID.\n")
        return

    task = find_task_by_id(tasks, task_id)
    if not task:
        print("Task not found.\n")
        return

    if task["completed"]:
        print("Task is already completed.\n")
        return

    task["completed"] = True
    save_tasks(tasks)
    print(f"Task {task_id} marked as complete.\n")


def delete_task(tasks):
    print("\n--- Delete a Task ---")
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid ID.\n")
        return

    task = find_task_by_id(tasks, task_id)
    if not task:
        print("Task not found.\n")
        return

    confirm = input(f"Are you sure you want to delete '{task['title']}'? (y/n): ").strip().lower()
    if confirm != "y":
        print("Delete cancelled.\n")
        return

    tasks.remove(task)
    save_tasks(tasks)
    print(f"Task {task_id} deleted.\n")


def search_tasks(tasks):
    print("\n--- Search Tasks ---")
    keyword = input("Search keyword: ").strip().lower()
    if not keyword:
        print("Keyword cannot be empty.\n")
        return

    results = [
        t for t in tasks
        if keyword in t["title"].lower() or keyword in t["description"].lower()
    ]

    if not results:
        print("No tasks matched your search.\n")
        return

    print(f"\nFound {len(results)} matching task(s):")
    list_tasks(results)


def main_menu():
    tasks = load_tasks()
    while True:
        print("==== Smart Task Manager ====")
        print("1. List all tasks")
        print("2. List incomplete tasks")
        print("3. List completed tasks")
        print("4. Add a new task")
        print("5. Complete a task")
        print("6. Delete a task")
        print("7. Search tasks")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            list_tasks(tasks, show_completed=False)
        elif choice == "3":
            list_tasks(tasks, show_completed=True)
        elif choice == "4":
            add_task(tasks)
        elif choice == "5":
            complete_task(tasks)
        elif choice == "6":
            delete_task(tasks)
        elif choice == "7":
            search_tasks(tasks)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main_menu()