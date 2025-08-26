from .models import Task


class Database:
    def __init__(self):
        self.tasks: dict[str, Task] = {}

    def get_all(self):
        return list(self.tasks.values())

    def get(self, task_id: str):
        return self.tasks.get(task_id)

    def create(self, task):
        self.tasks[str(task.id)] = task
        return task

    def update(self, task_id: str, task_data: dict):
        if task := self.tasks.get(task_id):
            task_data = {k: v for k, v in task_data.items() if v is not None}
            self.tasks[task_id] = task.copy(update=task_data)
            return self.tasks[task_id]

    def delete(self, task_id: str):
        return self.tasks.pop(task_id, None) is not None


db = Database()
