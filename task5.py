import os

class Task:
    def __init__(self, task_id, name, description):
        self.task_id = task_id
        self.name = name
        self.description = description

    def __str__(self):
        return f"ID: {self.task_id}, Name: {self.name}, Description: {self.description}"

    def to_file_string(self):
        return f"{self.task_id},{self.name},{self.description}\n"

    @classmethod
    def from_file_string(cls, file_string):
        task_id, name, description = file_string.strip().split(',')
        return cls(int(task_id), name, description)

class TaskManager:
    def __init__(self, filename='tasks.txt'):
        self.tasks = []
        self.next_id = 1
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    for line in file:
                        task = Task.from_file_string(line)
                        self.tasks.append(task)
                        if task.task_id >= self.next_id:
                            self.next_id = task.task_id + 1
        except Exception as e:
            print(f"Error loading tasks: {e}")

    def save_tasks(self):
        try:
            with open(self.filename, 'w') as file:
                for task in self.tasks:
                    file.write(task.to_file_string())
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def create_task(self, name, description):
        task = Task(self.next_id, name, description)
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
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
                self.save_tasks()
                print(f"Task ID {task_id} updated successfully!")
                return
        print(f"Task ID {task_id} not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
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
