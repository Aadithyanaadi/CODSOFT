import json

TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def view_tasks(tasks):
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "Done" if task['done'] else "Pending"
        print(f"{i}. {task['title']} - {status}")
    print()

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added!")

def mark_done(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]['done'] = True
        save_tasks(tasks)
        print("Task marked as done!")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        save_tasks(tasks)
        print("Task deleted!")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
