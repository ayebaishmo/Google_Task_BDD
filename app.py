class ToDoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        if not title.strip():  
            raise ValueError("Task name cannot be empty or only spaces")
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
