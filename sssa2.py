todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Added: {task}")

def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Removed: {task}")
    else:
        print("Task not found!")

while True:
    action = input("Add (a), Remove (r), Show (s), Quit (q): ")
    if action == 'a':
        task = input("Enter task: ")
        add_task(task)
    elif action == 'r':
        task = input("Enter task to remove: ")
        remove_task(task)
    elif action == 's':
        print("To-Do List:", todo_list or "Empty")
    elif action == 'q':
        break