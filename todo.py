"""
This program implements a todo list application.
This program allows us to print the list, add new todo, delete an existing todo,
and set the todo status to be completed.

The program uses two global dictionary variables to track the todo items.
First dict called "tasks", has key of task id, and value of task description.
Second dict called "stats", has key of task id, and value of task status.
Boolean value True stands for completed, boolean False means not completed.

Examples of two dictionaries look like the followings:
tasks = {1: "Do homework", 2: "Clean room"}
stats = {1: False, 2: True}
"""

tasks = {}
stats = {}

def create_task(description):
    """
    Function create_task is used to add a new task into the application.
    Since dictionaries 'tasks' and 'stats' share the same task id, a new
    task id must be generated first.
    If currently no task, we assign 1 to the new task id.
    If currently one or more tasks exist, we get the maximum key of all tasks,
    and then adding 1 to the max key to get the new task id.

    Afterwards, add entry to both dictionaries.

    @param [str] description: name of the task

    @return [int] id of the newly added tasks
    """

    global tasks, stats 

    if len(tasks) == 0:
        task_id = 1
    else:
        task_id = max(tasks.keys()) + 1

    tasks[task_id] = description
    stats[task_id] = False
    return task_id


def show_tasks():
    """
    Display all the todo tasks (incompleted).
    Firstly, print the header line (provided already).
    Then check the length of either dictionary, if empty, print "No tasks yet!",
    and then terminate the function by "return" statement.
    Otherwise, use for loop to print incompleted tasks with the following format
    task_id: task_description - task_status

    During the for loop, if the task is completed, skip the current iteration.

    @return None
    """
    global tasks, stats 

    print("\n=== Your Todo List ===")
    
    if len(tasks) == 0:
        print("No tasks yet!")
        return
    
    for tid, desc in tasks.items():
        if stats[tid]:
            continue
    print(f"{tid}: {desc} - Incomplete")


def complete_task(tid):
    """
    Function complete_task() change the task status from False to True.
    If the task id can be found in dictionary 'stats', change the value of the
    specific key from True to False.

    @param [id] tid: id of the task

    @return [bool] True if changed, False otherwise
    """
    global stats

    if tid in stats and not stats[tid]:
        stats[tid] = True 
        return True
    else:
        return False


def delete_task(tid):
    """
    Function delete_task() removes the entry from both dictionaries.
    If the task id can be found, delete the entry from both dictionaries.

    @param [id] tid: id of the task

    @return [bool] True if changed, False otherwise
    """
    global tasks, stats

    if tid in tasks:
        del tasks[tid]
        del stats[tid]
        return True
    else:
        return False 


def main():
    """
    Main logic of the program.
    The program will keep waiting for user actions, so implement this with
    infinite while loop.
    For every iteration of the loop, we print the menus, and ask for user to
    enter the option.

    If option is 1, call show_tasks().

    If option is 2, ask for the name of the task, then call create_task(),
    remember to pass the argument and accept the return of the function.
    Then print "Added tasks {task_id}: {task_name}".

    If option is 3, ask for the task id (integer), send it to complete_task().
    The function returns boolean value, use variable to accept the return.
    If the return is True, print "Task #{task_id} marked as completed!",
    otherwise, print "Invalid task id".

    If option is 4, ask for the task id (integer), send it to delete_task().
    The function returns boolean value, use variable to accept the return.
    If the return is True, print "Task #{task_id} deleted",
    otherwise, print "Invalid task id".

    If option i 5, print "Goodbye!" and quit the while loop

    Otherwise, print "Invalid choice.".
    """
    while True:
        print("\n=== Todo Menu ===")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks()

        elif choice == "2":
            desc = input("Enter task description: ")
            tid = create_task(desc)
            print(f"Added task {tid}: {desc}")
        
        elif choice == "3":
            try:
                tid = int(input("Enter task ID to complete: "))
                if complete_task(tid):
                    print(f"Task #{tid} marked as completed!")
                else:
                    print("Invalid task id")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            try:
                tid = int(input("Enter task ID to delete: "))
                if delete_task(tid):
                    print(f"Task #{tid} deleted")
                else:
                    print("Invalid task id")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
