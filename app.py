class ToDoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        # Check if the title is an empty string
        if title == "":
            raise ValueError("Task name cannot be empty")
        # Check if the title contains only spaces
        elif not title.strip():  # This handles the case where the title is spaces-only
            raise ValueError("Task name cannot be only spaces")
        
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

