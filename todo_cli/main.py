import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"✅ Added: {title}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return
    print("📋 All Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['title']} [{status}]")

def list_completed_tasks():
    tasks = load_tasks()
    completed = [t for t in tasks if t["done"]]
    if not completed:
        print("😐 No completed tasks yet.")
        return
    print("✅ Completed Tasks:")
    for i, task in enumerate(completed, start=1):
        print(f"{i}. {task['title']}")

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"🎉 Task {index + 1} marked as done!")
    else:
        print("❗ Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑️ Deleted: {removed['title']}")
    else:
        print("❗ Invalid task number.")

def show_menu():
    print("""
To-Do CLI App 📝
1. Add Task
2. View All Tasks
3. Mark Task as Done
4. Delete Task
5. Show Completed Tasks
6. Exit
""")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")
        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            index = int(input("Enter task number to mark as done: ")) - 1
            mark_done(index)
        elif choice == "4":
            list_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        elif choice == "5":
            list_completed_tasks()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice.")
