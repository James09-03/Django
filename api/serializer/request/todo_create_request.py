# api/serializer/request/todo_create_request.py

from rest_framework import serializers

# Import DTO from its new location
from api.model.todo_model import TodoItemDTO

class TodoItemCreateRequestSerializer(serializers.Serializer):
    """
    Serializer for validating POST request data and converting it to a DTO.
    """
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(required=False, allow_blank=True)
    # Field name 'completed' matches the DTO field name
    completed = serializers.BooleanField(default=False)

    def to_todo_dto(self) -> TodoItemDTO:
        """Converts validated data into the DTO for the Service."""
        return TodoItemDTO(
            title=self.validated_data['title'],
            description=self.validated_data.get('description', ''),
            completed=self.validated_data.get('completed', False)
        )