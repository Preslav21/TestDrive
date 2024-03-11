class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_as_completed(self, task):
        if task in self.tasks:
            # Assuming we want to remove the task when marked as completed
            self.tasks.remove(task)

    def is_task_completed(self, task):
        return task not in self.tasks

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
