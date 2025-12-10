# api/models.py

from django.db import models
from .dataclass.todo_dto import TodoItemDTO # Import the DTO from its new location

# --- MODEL DEFINITION ---
class TodoItem(models.Model):
    """
    Django Model representing the database schema for a To-Do item.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # --- DTO CONVERSION METHOD ---
    def to_dto(self) -> TodoItemDTO:
        """
        Converts the current TodoItem instance into a clean TodoItemDTO.
        This method keeps the conversion logic contained within the Model layer.
        """
        return TodoItemDTO(
            id=self.id,
            title=self.title,
            description=self.description,
            is_completed=self.is_completed
        )