# api/controllers.py

from django.shortcuts import get_object_or_404
from typing import List
from .models import TodoItem, TodoItemDTO


class TodoController:
    """
    Handles all core business logic and model interactions.
    All methods return DTOs to ensure the View layer only handles clean data.
    """

    @staticmethod
    def list_todos() -> List[TodoItemDTO]:
        """Returns all TodoItem instances converted to a list of DTOs."""
        queryset = TodoItem.objects.all().order_by('created_at')
        # Use the Model's to_dto() method for conversion
        return [item.to_dto() for item in queryset]

    @staticmethod
    def create_todo(dto: TodoItemDTO) -> TodoItemDTO:
        """Creates a new TodoItem from the DTO and returns the resulting DTO."""
        new_item = TodoItem.objects.create(
            title=dto.title,
            description=dto.description,
            is_completed=dto.is_completed
        )
        # Convert the new Model instance back to DTO before returning
        return new_item.to_dto()

    @staticmethod
    def get_todo_by_id(todo_id: int) -> TodoItemDTO:
        """Retrieves a single TodoItem or raises 404, returning the DTO."""
        todo_item = get_object_or_404(TodoItem, pk=todo_id)
        # Convert the Model instance to DTO before returning
        return todo_item.to_dto()

    @staticmethod
    def update_todo(todo_id: int, dto: TodoItemDTO) -> TodoItemDTO:
        """Updates an existing TodoItem based on the DTO data and returns the resulting DTO."""
        todo_item = get_object_or_404(TodoItem, pk=todo_id)

        # Explicit update logic using the clean DTO data
        todo_item.title = dto.title
        todo_item.description = dto.description
        todo_item.is_completed = dto.is_completed

        todo_item.save()
        # Convert the updated Model instance to DTO before returning
        return todo_item.to_dto()

    @staticmethod
    def delete_todo(todo_id: int):
        """Deletes a TodoItem by ID (Controller handles the 404 check)."""
        todo_item = get_object_or_404(TodoItem, pk=todo_id)
        todo_item.delete()
        # Returns None implicitly after deletion