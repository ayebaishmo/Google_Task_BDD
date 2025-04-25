class ToDoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        if not title.strip():  
            raise ValueError("Task name cannot be empty")
        self.tasks.append({"title": title, "done": False})

    def list_tasks(self):
        return self.tasks  

    def complete_task(self, title):
        for task in self.tasks:
            if task["title"] == title:
                task["done"] = True
                return
        raise ValueError(f"Task '{title}' not found!")

    def delete_task(self, title):
        for task in self.tasks:
            if task["title"] == title:
                self.tasks.remove(task)
                return
        raise ValueError(f"Task '{title}' not found!")

    def edit_task(self, old_title, new_title):
        if not new_title.strip():
            raise ValueError("Task name cannot be empty")
        for task in self.tasks:
            if task["title"] == old_title:
                task["title"] = new_title
                return
        raise ValueError(f"Task '{old_title}' not found!")

# Create an instance of the app
todo_app = ToDoApp()

# Add tasks
todo_app.add_task("Buy groceries")
todo_app.add_task("Complete Python project")
todo_app.add_task("Read a book")

# List tasks
print("Current tasks:")
for task in todo_app.list_tasks():
    print(task)

# Complete a task
todo_app.complete_task("Buy groceries")

# Edit a task
todo_app.edit_task("Read a book", "Read a Bible")

# Delete a task
todo_app.delete_task("Complete Python project")

# List tasks after modifications
print("\nUpdated tasks:")
for task in todo_app.list_tasks():
    print(task)