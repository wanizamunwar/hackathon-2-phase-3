"""
__main__.py - Entry point for the Todo Console App.
Handles the main application loop and command parsing.
"""

from src.todo_app.manager import TaskManager
from src.todo_app.cli import display_tasks, get_user_input, get_task_id_input

def print_menu():
    """Prints the main menu options to the console."""
    print("\n--- Todo App Menu ---")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task Complete")
    print("4. Update Task Description")
    print("5. Delete Task")
    print("q. Quit")
    print("---------------------")

def main():
    """Main function to run the Todo application."""
    manager = TaskManager()
    
    while True:
        print_menu()
        choice = get_user_input("Enter your choice: ").lower()

        if choice == '1':
            description = get_user_input("Enter task description: ")
            try:
                task = manager.add_task(description)
                print(f"Task '{task.description}' (ID: {task.id}) added.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '2':
            tasks = manager.get_all_tasks()
            display_tasks(tasks)
        elif choice == '3':
            try:
                task_id = get_task_id_input("Enter the ID of the task to mark complete: ")
                task = manager.mark_task_complete(task_id)
                print(f"Task '{task.description}' (ID: {task.id}) marked complete.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '4':
            try:
                task_id = get_task_id_input("Enter the ID of the task to update: ")
                new_description = get_user_input("Enter new description: ")
                task = manager.update_task_description(task_id, new_description)
                print(f"Task (ID: {task.id}) updated to '{task.description}'.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '5':
            try:
                task_id = get_task_id_input("Enter the ID of the task to delete: ")
                manager.delete_task(task_id)
                print(f"Task (ID: {task_id}) deleted.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 'q':
            print("Exiting Todo App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()