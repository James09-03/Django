# api/serializer/response/todo_response.py

from rest_framework import serializers

# Import DTO from its location
from api.model.todo_model import TodoItemDTO

class TodoItemResponseSerializer(serializers.Serializer):
    """
    Serializer for converting TodoItemDTOs into a JSON response.
    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200, read_only=True)
    description = serializers.CharField(read_only=True)
    completed = serializers.BooleanField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    # Required method to work with non-Model instances (like DTOs or dicts)
    def to_representation(self, instance: TodoItemDTO):
        """Maps the DTO instance fields to the serializer fields."""
        return {
            'id': instance.id,
            'title': instance.title,
            'description': instance.description,
            'completed': instance.completed,
            'created_at': instance.created_at,
            'updated_at': instance.updated_at,
        }