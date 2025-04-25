from datetime import datetime
from enum import Enum
import json
import os

class Priority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class Status(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

class Task:
    def __init__(self, title, description=None, due_date=None, priority=None, status=None):
        if not title:
            raise ValueError("Task title is required")
            
        self.id = self._generate_id()
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority if priority else Priority.MEDIUM.value
        self.status = status if status else Status.PENDING.value
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.category = None
        self.tags = []
    
    def _generate_id(self):
        return int(datetime.now().timestamp() * 1000)
    
    def update(self, title=None, description=None, due_date=None, priority=None, status=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if due_date:
            self.due_date = due_date
        if priority:
            self.priority = priority
        if status:
            self.status = status
        self.updated_at = datetime.now()
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "category": self.category,
            "tags": self.tags
        }

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()
    
    def create_task(self, title, description=None, due_date=None, priority=None, status=None):
        task = Task(title, description, due_date, priority, status)
        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def get_all_tasks(self):
        return self.tasks
    
    def get_task_by_title(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None
    
    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id, **kwargs):
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        
        task.update(**kwargs)
        self.save_tasks()
        return task
    
    def update_task_by_title(self, title, **kwargs):
        task = self.get_task_by_title(title)
        if not task:
            raise ValueError("Task not found")
        
        task.update(**kwargs)
        self.save_tasks()
        return task
    
    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        
        self.tasks.remove(task)
        self.save_tasks()
        return True
    
    def delete_task_by_title(self, title):
        task = self.get_task_by_title(title)
        if not task:
            raise ValueError("Task not found")
        
        self.tasks.remove(task)
        self.save_tasks()
        return True
    
    def delete_all_tasks(self):
        self.tasks = []
        self.save_tasks()
        return True
    
    def filter_tasks_by_priority(self, priority):
        """Filter tasks by priority, ensuring case-sensitive comparison."""
        valid_priorities = [p.value for p in Priority]
        if priority not in valid_priorities:
            priority_map = {p.value.lower(): p.value for p in Priority}
            priority = priority_map.get(priority.lower(), priority)
            
        return [task for task in self.tasks if task.priority == priority]
    
    def filter_tasks_by_status(self, status):
        return [task for task in self.tasks if task.status == status]
    
    def filter_tasks_by_category(self, category):
        return [task for task in self.tasks if task.category == category]
    
    def filter_tasks_by_tag(self, tag):
        return [task for task in self.tasks if tag in task.tags]
    
    def sort_tasks_by_due_date(self):
        """Sort tasks by due date, handling None values and different date formats."""
        def get_date_key(task):
            if not task.due_date:
                return datetime.max
            try:
                return datetime.fromisoformat(task.due_date)
            except ValueError:
                # Try to parse the date string in a more flexible way
                try:
                    return datetime.strptime(task.due_date, "%Y-%m-%d")
                except ValueError:
                    return datetime.max
                
        return sorted(self.tasks, key=get_date_key)

    def add_category_to_task(self, task_id, category):
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        
        task.category = category
        self.save_tasks()
        return task
    
    def add_tag_to_task(self, task_id, tag):
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        
        if tag not in task.tags:
            task.tags.append(tag)
            self.save_tasks()
        return task
    
    def remove_tag_from_task(self, task_id, tag):
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        
        if tag in task.tags:
            task.tags.remove(tag)
            self.save_tasks()
        return task
    
    def save_tasks(self):
        tasks_data = [task.to_dict() for task in self.tasks]
        with open("tasks.json", "w") as file:
            json.dump(tasks_data, file, indent=2)
    
    def load_tasks(self):
        if not os.path.exists("tasks.json"):
            return
        
        with open("tasks.json", "r") as file:
            try:
                tasks_data = json.load(file)
                for task_data in tasks_data:
                    task = Task(
                        task_data["title"],
                        task_data["description"],
                        task_data["due_date"],
                        task_data["priority"],
                        task_data["status"]
                    )
                    task.id = task_data["id"]
                    task.created_at = datetime.fromisoformat(task_data["created_at"])
                    task.updated_at = datetime.fromisoformat(task_data["updated_at"])
                    task.category = task_data["category"]
                    task.tags = task_data["tags"]
                    self.tasks.append(task)
            except json.JSONDecodeError:
                pass
    

    def delete_all_tasks(self):
        """Delete all tasks from the task list."""
        self.tasks = []
        self.save_tasks()
        return True

if __name__ == "__main__":
    task_manager = TaskManager()
    
    while True:
        print("\n===== Task Manager =====")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Filter Tasks")
        print("6. Categorize Tasks")
        print("7. Tag Management")
        print("0. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            due_date = input("Enter due date (YYYY-MM-DD) (optional): ")
            priority = input("Enter priority (Low/Medium/High) (default: Medium): ")
            
            if not priority:
                priority = Priority.MEDIUM.value
            
            try:
                task_manager.create_task(title, description, due_date, priority)
                print(f"Task '{title}' created successfully!")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            tasks = task_manager.get_all_tasks()
            
            if not tasks:
                print("No tasks found.")
            else:
                print("\n===== Task List =====")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.title} - {task.status}")
                    if task.description:
                        print(f"   Description: {task.description}")
                    if task.due_date:
                        print(f"   Due Date: {task.due_date}")
                    print(f"   Priority: {task.priority}")
                    if task.category:
                        print(f"   Category: {task.category}")
                    if task.tags:
                        print(f"   Tags: {', '.join(task.tags)}")
                    print()
        
        elif choice == "3":
            tasks = task_manager.get_all_tasks()
            
            if not tasks:
                print("No tasks found.")
                continue
            
            print("\n===== Task List =====")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.title}")
            
            try:
                index = int(input("\nEnter task number to update: ")) - 1
                if index < 0 or index >= len(tasks):
                    print("Invalid task number.")
                    continue
                
                task = tasks[index]
                
                print(f"\nUpdating Task: {task.title}")
                title = input(f"Enter new title (current: {task.title}) (leave empty to keep current): ")
                description = input(f"Enter new description (current: {task.description}) (leave empty to keep current): ")
                due_date = input(f"Enter new due date (current: {task.due_date}) (leave empty to keep current): ")
                priority = input(f"Enter new priority (current: {task.priority}) (leave empty to keep current): ")
                status = input(f"Enter new status (Pending/In Progress/Completed) (current: {task.status}) (leave empty to keep current): ")
                
                update_data = {}
                if title:
                    update_data["title"] = title
                if description:
                    update_data["description"] = description
                if due_date:
                    update_data["due_date"] = due_date
                if priority:
                    update_data["priority"] = priority
                if status:
                    update_data["status"] = status
                
                task_manager.update_task(task.id, **update_data)
                print("Task updated successfully!")
            
            except (ValueError, IndexError):
                print("Invalid input.")
        
        elif choice == "4":
            print("\n===== Delete Task =====")
            print("1. Delete a specific task")
            print("2. Delete all tasks")
            
            delete_choice = input("\nEnter your choice: ")
            
            if delete_choice == "1":
                tasks = task_manager.get_all_tasks()
                
                if not tasks:
                    print("No tasks found.")
                    continue
                
                print("\n===== Task List =====")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.title}")
                
                try:
                    index = int(input("\nEnter task number to delete: ")) - 1
                    if index < 0 or index >= len(tasks):
                        print("Invalid task number.")
                        continue
                    
                    task = tasks[index]
                    confirm = input(f"Are you sure you want to delete '{task.title}'? (yes/no): ")
                    
                    if confirm.lower() == "yes":
                        task_manager.delete_task(task.id)
                        print("Task deleted successfully!")
                
                except (ValueError, IndexError):
                    print("Invalid input.")
            
            elif delete_choice == "2":
                confirm = input("Are you sure you want to delete ALL tasks? (yes/no): ")
                
                if confirm.lower() == "yes":
                    task_manager.delete_all_tasks()
                    print("All tasks deleted successfully!")
            
            else:
                print("Invalid choice.")
        
        elif choice == "5":
            print("\n===== Filter Tasks =====")
            print("1. Filter by priority")
            print("2. Filter by status")
            print("3. Filter by category")
            print("4. Filter by tag")
            print("5. Sort by due date")
            
            filter_choice = input("\nEnter your choice: ")
            
            if filter_choice == "1":
                priority = input("Enter priority to filter by (Low/Medium/High): ")
                tasks = task_manager.filter_tasks_by_priority(priority)
            
            elif filter_choice == "2":
                status = input("Enter status to filter by (Pending/In Progress/Completed): ")
                tasks = task_manager.filter_tasks_by_status(status)
            
            elif filter_choice == "3":
                category = input("Enter category to filter by: ")
                tasks = task_manager.filter_tasks_by_category(category)
            
            elif filter_choice == "4":
                tag = input("Enter tag to filter by: ")
                tasks = task_manager.filter_tasks_by_tag(tag)
            
            elif filter_choice == "5":
                tasks = task_manager.sort_tasks_by_due_date()
            
            else:
                print("Invalid choice.")
                continue
            
            if not tasks:
                print("No tasks found with the specified filter.")
            else:
                print(f"\n===== Filtered Tasks ({len(tasks)}) =====")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")