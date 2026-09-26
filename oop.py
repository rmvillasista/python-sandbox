class Task:
    def __init__(self, task_id: int, title: str):
        self.id = task_id
        self.title = title
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {"id": self.id, "title": self.title, "completed": self.completed}

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.id}: {self.title}"

# Example Usage
t1 = Task(1, "Master Python OOP")
print("Before:", t1)
t1.mark_complete()
print("After: ", t1)