# api/dataclass/todo_dto.py

from dataclasses import dataclass


@dataclass
class TodoItemDTO:
    """
    Data Transfer Object (DTO) for the TodoItem resource.
    This defines the clean, typed data structure passed between
    the Serializer and the Controller/Model layers.
    """
    title: str
    description: str
    is_completed: bool

    # ID is optional as it won't be present during creation (POST)
    id: int | None = None