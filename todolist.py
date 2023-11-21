import datetime

class Task:
    def __init__(self, description, due_date=None, priority=None):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[{(self.priority or 5)}/{5}] {self.description} ({status})"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None, priority=None):
        new_task = Task(description, due_date, priority)
        self.tasks.append(new_task)

    def display_tasks(self):
        for task in self.tasks:
            print(task)

    def mark_task_completed(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                task.completed = True
                break

    def update_task(self, task_description, new_description=None, due_date=None, priority=None):
        for task in self.tasks:
            if task.description == task_description:
                if new_description:
                    task.description = new_description
                if due_date:
                    task.due_date = due_date
                if priority:
                    task.priority = priority
                break

    def remove_task(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                self.tasks.remove(task)
                break


# Create a To-Do List instance
todo_list = ToDoList()

# Add some sample tasks
todo_list.add_task("Finish Python project", due_date=datetime.date(2023, 11, 25), priority=3)
todo_list.add_task("Buy groceries", priority=2)
todo_list.add_task("Attend meeting", due_date=datetime.date(2023, 11, 21), priority=1)

# Display the current to-do list
todo_list.display_tasks()

# Mark a task as completed
todo_list.mark_task_completed("Finish Python project")

# Update a task
todo_list.update_task("Buy groceries", new_description="Buy milk, eggs, and bread")

# Remove a task
todo_list.remove_task("Attend meeting")

# Display the updated to-do list
todo_list.display_tasks()