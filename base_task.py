
from abc import ABC, abstractmethod

# Abstraction and Encapsulation
class BaseTask(ABC):
    """Abstract base class defining the task contract."""

    def __init__(self, task_id: int, title: str):
        self.id = task_id
        self.title = title
        self._completed = False  # Encapsulated state

    @abstractmethod
    def mark_complete(self) -> None:
        """Abstract method to be implemented by child classes."""
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """Abstract method to export task details."""
        pass