from abc import ABC, abstractmethod

# 1. ABSTRACTION
# Abstract base class defining the contract without exposing internal logic
class BaseTask(ABC):
    def __init__(self, task_id: int, title: str):
        self.id = task_id
        self.title = title
        self._completed = False  # Protected attribute (Encapsulation)

    @abstractmethod
    def mark_complete(self):
        """Abstract method to be implemented by child classes."""
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """Abstract method to export task details."""
        pass


# 2. INHERITANCE & 3. ENCAPSULATION
# StandardTask inherits from BaseTask and encapsulates its completion state logic
class StandardTask(BaseTask):
    def mark_complete(self):
        self._completed = True

    def to_dict(self):
        return {"id": self.id, "title": self.title, "completed": self._completed}

    # 4. POLYMORPHISM
    # Overriding __str__ to provide custom string representation
    def __str__(self):
        status = "✓" if self._completed else " "
        return f"[{status}] {self.id}: {self.title}"


# 2. INHERITANCE & 4. POLYMORPHISM
# TimedTask inherits from BaseTask and overrides mark_complete with unique behavior
class TimedTask(BaseTask):
    def __init__(self, task_id: int, title: str, estimated_minutes: int):
        super().__init__(task_id, title)
        self.estimated_minutes = estimated_minutes
        self.time_spent = 0

    def mark_complete(self):
        self._completed = True
        self.time_spent = self.estimated_minutes  # Auto-fill duration on completion

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self._completed,
            "estimated_minutes": self.estimated_minutes,
            "time_spent": self.time_spent,
        }

    # Polymorphic behavior: Different string format for timed tasks
    def __str__(self):
        status = "✓" if self._completed else " "
        return f"[{status}] {self.id}: {self.title} ({self.estimated_minutes} mins)"


# Execution / Demonstration
tasks: list[BaseTask] = [
    StandardTask(1, "Master Python OOP"),
    TimedTask(2, "Build OOP Architecture Demo", 45),
]

# Polymorphic processing: calling mark_complete() and str() uniformly across types
for task in tasks:
    print("Before:", task)
    task.mark_complete()
    print("After: ", task)
    print("Dict Export:", task.to_dict())
    print("-" * 40)