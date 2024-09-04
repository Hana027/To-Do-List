import os

TODO_FILE = 'todo.txt'

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            tasks = [task.strip() for task in file.readlines()]
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def mark_task_complete(tasks, task_number):
    if 0 < task_number <= len(tasks):
        completed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task '{completed_task}' marked as complete.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_number = int(input("Enter task number to mark as complete: "))
            mark_task_complete(tasks, task_number)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if _name_ == "_main_":
    main()
