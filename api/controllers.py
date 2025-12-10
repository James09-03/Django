# api/controllers.py

from django.shortcuts import get_object_or_404
from typing import List
from .model.todo_model import TodoItem  # Updated Import Location
from .dataclass.todo_dto import TodoItemDTO


class TodoController:
    """
    Handles all core business logic and model interactions.
    All public methods receive DTOs as input and return DTOs as output
    to maintain a strict, clean architecture.
    """

    @staticmethod
    def list_todos() -> List[TodoItemDTO]:
        """Returns all TodoItem instances converted to a list of DTOs."""
        queryset = TodoItem.objects.all().order_by('created_at')
        # Map the queryset to DTOs using the Model's to_dto() method
        return [item.to_dto() for item in queryset]

    @staticmethod
    def create_todo(dto: TodoItemDTO) -> TodoItemDTO:
        """Creates a new TodoItem from the DTO and returns the resulting DTO."""
        new_item = TodoItem.objects.create(
            # Pass clean DTO attributes directly to the model creation
            title=dto.title,
            description=dto.description,
            is_completed=dto.is_completed
        )
        # Convert the new Model instance back to DTO before returning
        return new_item.to_dto()

    @staticmethod
    def get_todo_by_id(todo_id: int) -> TodoItemDTO:
        """Retrieves a single TodoItem or raises 404, returning the DTO."""
        # Controller handles the database interaction and the 404 check
        todo_item = get_object_or_404(TodoItem, pk=todo_id)
        # Convert the Model instance to DTO before returning
        return todo_item.to_dto()

    @staticmethod
    def update_todo(todo_id: int, dto: TodoItemDTO) -> TodoItemDTO:
        """Updates an existing TodoItem based on the DTO data and returns the resulting DTO."""

        # 1. Retrieve the object (Controller handles 404)
        todo_item = get_object_or_404(TodoItem, pk=todo_id)

        # 2. Update model attributes using clean DTO data
        # Note: In a production system, you might add logic here to only update
        # fields present in the DTO if you were handling PATCH explicitly.
        todo_item.title = dto.title
        todo_item.description = dto.description
        todo_item.is_completed = dto.is_completed

        # 3. Save changes
        todo_item.save()

        # 4. Convert the updated Model instance to DTO before returning
        return todo_item.to_dto()

    @staticmethod
    def delete_todo(todo_id: int):
        """Deletes a TodoItem by ID (Controller handles the 404 check)."""
        # Retrieve object first to ensure it exists before attempting delete
        todo_item = get_object_or_404(TodoItem, pk=todo_id)
        todo_item.delete()
        # Returns None implicitly after successful deletion