# /api/dataclass/todo_dto.py (CORRECTED)

from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class TodoItemDTO:
    """
    Data Transfer Object (DTO) for TodoItem.
    """

    # --- NON-DEFAULT ARGUMENTS (must come first) ---
    title: str  # No default value

    # --- DEFAULT ARGUMENTS (must come last) ---
    id: Optional[int] = field(default=None)  # Default value
    description: Optional[str] = field(default="")  # Default value
    completed: Optional[bool] = field(default=False)  # Default value
    created_at: Optional[datetime] = field(default=None)  # Default value
    updated_at: Optional[datetime] = field(default=None)