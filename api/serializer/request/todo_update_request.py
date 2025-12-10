# api/serializer/request/todo_update_request.py

from .todo_create_request import TodoItemCreateRequestSerializer


class TodoItemUpdateRequestSerializer(TodoItemCreateRequestSerializer):
    # Note: No custom methods or fields are needed here since the base class
    # already provides the necessary fields and the conversion to DTO.
    pass