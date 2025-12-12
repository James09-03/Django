# api/model/todo_model.py

from django.db import models
from django.shortcuts import get_object_or_404
from ..dataclass.todo_dto import TodoItemDTO  # Relative import to DTO
from typing import List


class TodoItem(models.Model):
    """
    Django Model representing the database schema for a To-Do item.
    Also acts as the Repository, encapsulating all database query logic
    and returning results as DTOs.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # --- DTO CONVERSION METHOD ---
    def to_dto(self) -> TodoItemDTO:
        """Converts the current TodoItem instance into a clean TodoItemDTO."""
        return TodoItemDTO(
            id=self.id,
            title=self.title,
            description=self.description,
            is_completed=self.is_completed
        )

    # --- STATIC QUERY AND COMMAND METHODS (CRUD) ---

    @staticmethod
    def list_todos() -> List[TodoItemDTO]:
        """Queries the database for all TodoItem instances and returns a list of DTOs."""
        queryset = TodoItem.objects.all().order_by('created_at')
        return [item.to_dto() for item in queryset]

    @staticmethod
    def get_todo_by_id(todo_id: int) -> TodoItemDTO:
        """Retrieves a single TodoItem or raises 404, returning the DTO."""
        todo_item = get_object_or_404(TodoItem, pk=todo_id)
        return todo_item.to_dto()

    @staticmethod
    def create_todo(dto: TodoItemDTO) -> TodoItemDTO:
        """Creates a new TodoItem from the DTO and returns the resulting DTO."""
        new_item = TodoItem.objects.create(
            title=dto.title,
            description=dto.description,
            is_completed=dto.is_completed
        )
        return new_item.to_dto()

    @staticmethod
    def update_todo(todo_id: int, dto: TodoItemDTO) -> TodoItemDTO:
        """Updates an existing TodoItem based on the DTO data and returns the resulting DTO."""

        # We retrieve the instance, which ensures 404 handling via the static method
        todo_item = get_object_or_404(TodoItem, pk=todo_id)

        # Update model attributes using clean DTO data
        todo_item.title = dto.title
        todo_item.description = dto.description
        todo_item.is_completed = dto.is_completed

        todo_item.save()

        return todo_item.to_dto()

    @staticmethod
    def delete_todo(todo_id: int):
        """Deletes a TodoItem by ID, returning nothing."""
        # Retrieve object first to ensure it exists before attempting delete
        todo_item = get_object_or_404(TodoItem, pk=todo_id)
        todo_item.delete()
        # Returns None implicitly