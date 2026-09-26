from base_task import BaseTask

# Inheritance and Polymorphism
class StandardTask(BaseTask):
    """Standard task implementation."""

    def mark_complete(self) -> None:
        self._completed = True

    def to_dict(self) -> dict:
        return {"id": self.id, "title": self.title, "completed": self._completed}

    def __str__(self) -> str:
        status = "✓" if self._completed else " "
        return f"[{status}] {self.id}: {self.title}"


class TimedTask(BaseTask):
    """Task with duration tracking."""

    def __init__(self, task_id: int, title: str, estimated_minutes: int):
        super().__init__(task_id, title)
        self.estimated_minutes = estimated_minutes
        self.time_spent = 0

    def mark_complete(self) -> None:
        self._completed = True
        self.time_spent = self.estimated_minutes

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "completed": self._completed,
            "estimated_minutes": self.estimated_minutes,
            "time_spent": self.time_spent,
        }

    def __str__(self) -> str:
        status = "✓" if self._completed else " "
        return f"[{status}] {self.id}: {self.title} ({self.estimated_minutes} mins)"