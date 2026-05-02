"""
Mini-project #1: To Do App
"""

tasks = []

def show_tasks():
    if not tasks:
        print("There are no tasks.")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

while True:
    print("""
    --- To Do App ---
    1. View tasks
    2. Add new task
    3. Delete task
    4. Quit program
          """)
    option = input("Select an option (1-4): ")
    match option:
        case "1":
            show_tasks()
            continue
        case "2":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
            print(f"New task added: {new_task}")
            continue
        case "3":
            show_tasks()
            if len(tasks) == 0:
                print("There are no tasks, so you can't delete any.")
                continue
            else:
                try:
                    del_idx = int(input("Enter task index to delete: "))
                    del_idx -= 1
                    if del_idx < 0 or del_idx >= len(tasks):
                        print("Invalid index. Try again.")
                        continue
                    else:
                        deleted_task = tasks.pop(del_idx)
                        print(f"Task deleted: {deleted_task}")
                        continue
                except ValueError:
                    print("Invalid option. Try to enter a number from 1 to 4.")
                    continue
        case "4":
            quit_confirmation = input("Are you sure you want to quit? (y/n): ")
            if quit_confirmation == "y":
                print("Quitting...")
                break
            else:
                continue
        case _:
            print("Invalid input. Please enter the number of the task you want to delete.")
            continue
