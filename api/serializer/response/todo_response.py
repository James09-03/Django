# api/serializer/response/todo_response.py

from rest_framework import serializers


# Note: We do NOT need to import the Model here, only the DTO structure is required.

class TodoItemResponseSerializer(serializers.Serializer):
    """
    Serializer for outgoing data (response body).
    It defines the definitive API output structure based on the DTO.
    """
    # Fields are read-only as they are only used for output
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    is_completed = serializers.BooleanField(read_only=True)

