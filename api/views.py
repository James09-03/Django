# api/views.py (TodoService - Updated to call Model directly)

# Removed the import: from .controllers import TodoController
from rest_framework.response import Response
from rest_framework import status
from typing import Dict, Any, List

# New import for the Model/Repository
from .model.todo_model import TodoItem


class TodoService:
    # ... (_create_success_response and _list_success_response helpers remain) ...

    # ----------------------------------------------------
    # CRUD Methods (Delegating to the Model/Repository)
    # ----------------------------------------------------

    def create_todo(self, validated_dto: Any) -> Response:
        """Creates a todo item by delegating to the Model/Repository."""
        new_dto = TodoItem.create_todo(validated_dto)  # <-- Direct call to Model
        return self._create_success_response(new_dto, status.HTTP_201_CREATED)

    def get_all_todos(self) -> Response:
        """Retrieves all todo items by delegating to the Model/Repository."""
        dto_list = TodoItem.list_todos()  # <-- Direct call to Model
        return self._list_success_response(dto_list)

    def get_todo_detail(self, pk: int) -> Response:
        """Retrieves a single todo item by delegating to the Model/Repository."""
        # Model handles 404
        dto = TodoItem.get_todo_by_id(pk)  # <-- Direct call to Model
        return self._create_success_response(dto, status.HTTP_200_OK)

    def update_todo(self, pk: int, validated_dto: Any) -> Response:
        """Updates a todo item by delegating to the Model/Repository."""
        updated_dto = TodoItem.update_todo(pk, validated_dto)  # <-- Direct call to Model
        return self._create_success_response(updated_dto, status.HTTP_200_OK)

    def delete_todo(self, pk: int) -> Response:
        """Deletes a todo item by delegating to the Model/Repository."""
        # Model handles 404 and deletion
        TodoItem.delete_todo(pk)  # <-- Direct call to Model
        return Response(status=status.HTTP_204_NO_CONTENT)