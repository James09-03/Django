# api/serializer/request/todo_create_request.py

from rest_framework import serializers
from api.dataclass.todo_dto import TodoItemDTO # Import the DTO

class TodoItemCreateRequestSerializer(serializers.Serializer):
    """
    Serializer for validating POST request data (creating a new item).
    It converts validated data into a TodoItemDTO.
    """
    # Define required fields for creation
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(required=False, allow_blank=True)
    is_completed = serializers.BooleanField(default=False)

    def to_todo_dto(self) -> TodoItemDTO:
        """Converts validated data into the DTO for the Controller."""
        return TodoItemDTO(
            title=self.validated_data['title'],
            description=self.validated_data.get('description', ''),
            is_completed=self.validated_data.get('is_completed', False)
        )