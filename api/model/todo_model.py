# api/model/todo_model.py

from django.db import models
from typing import List, Optional

# 1. IMPORT DTO from the new location
from api.dataclass.todo_dto import TodoItemDTO


## --- Custom Exception (FIX: Added TodoDoesNotExist) ---
class TodoDoesNotExist(Exception):
    """Custom exception raised when a TodoItem is not found."""
    pass


## --- Django Model Definition ---
class TodoItem(models.Model):
    """
    The Django Model representing a single Todo item in the database.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    # 2. Add the created_at field (if it was missing)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        app_label = 'api'
        db_table = 'api_todoitem'

    def __str__(self):
        return self.title


## --- Repository Layer ---
class TodoItemRepository:
    """
    Handles data access logic for the TodoItem model.
    """

    # Method to convert Django Model instance to DTO
    def _to_dto(self, model_instance: TodoItem) -> TodoItemDTO:
        """Converts a TodoItem model instance to a TodoItemDTO."""
        return TodoItemDTO(
            id=model_instance.id,
            title=model_instance.title,
            description=model_instance.description,
            completed=model_instance.completed,

            # 3. FIX: Ensure created_at is passed to the DTO constructor
            created_at=model_instance.created_at,
        )

    # Method to convert DTO to Django Model instance (for creation/updates)
    def _to_model(self, dto: TodoItemDTO, model_instance: Optional[TodoItem] = None) -> TodoItem:
        """Converts a TodoItemDTO to a TodoItem model instance."""
        if model_instance is None:
            model_instance = TodoItem()

        model_instance.title = dto.title
        model_instance.description = dto.description
        model_instance.completed = dto.completed
        return model_instance

    def get_all(self) -> List[TodoItemDTO]:
        """Retrieves all Todo items from the database."""
        model_instances = TodoItem.objects.all()
        return [self._to_dto(m) for m in model_instances]

    def create(self, todo_dto: TodoItemDTO) -> TodoItemDTO:
        """Creates a new Todo item in the database."""
        model_instance = self._to_model(todo_dto)
        model_instance.save()
        return self._to_dto(model_instance)

    # Example method added to show how TodoDoesNotExist is raised
    def get_by_id(self, pk: int) -> TodoItemDTO:
        """Retrieves a single Todo item by ID."""
        try:
            # Note: Using .get() raises TodoItem.DoesNotExist if not found
            model_instance = TodoItem.objects.get(pk=pk)
        except TodoItem.DoesNotExist:
            # Raise the custom exception that the Service layer expects
            raise TodoDoesNotExist(f"Todo with id {pk} does not exist.")

        return self._to_dto(model_instance)

    # (Add update, delete methods here if needed)