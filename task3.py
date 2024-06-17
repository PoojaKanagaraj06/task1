class Task:
    def __init__(self, task_id, name, description):
        self.task_id = task_id
        self.name = name
        self.description = description

    def __str__(self):
        return f"ID: {self.task_id}, Name: {self.name}, Description: {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create_task(self, name, description):
        task = Task(self.next_id, name, description)
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task '{name}' created successfully!")

    def read_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def update_task(self, task_id, name, description):
        for task in self.tasks:
            if task.task_id == task_id:
                task.name = name
                task.description = description
                print(f"Task ID {task_id} updated successfully!")
                return
        print(f"Task ID {task_id} not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print(f"Task ID {task_id} deleted successfully!")
                return
        print(f"Task ID {task_id} not found.")

def display_menu():
    print("\nTask Manager")
    print("1. Create a new task")
    print("2. Read tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")

def main():
    manager = TaskManager()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            manager.create_task(name, description)
        elif choice == "2":
            manager.read_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            name = input("Enter new task name: ")
            description = input("Enter new task description: ")
            manager.update_task(task_id, name, description)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == "5":
            print("Exiting the Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
