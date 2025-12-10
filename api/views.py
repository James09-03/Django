# api/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Note: get_object_or_404 is now handled inside the Controller

from .controllers import TodoController
from .serializer import (
    TodoItemResponseSerializer,
    TodoItemCreateRequestSerializer,
    TodoItemUpdateRequestSerializer
)


# -----------------------------------------------
# A. CREATE and LIST (GET, POST)
# -----------------------------------------------
@api_view(['GET', 'POST'])
def todo_list_create(request):
    """
    Handles LIST (GET) and CREATE (POST) requests.
    Views focus only on HTTP and JSON interaction.
    """

    # 1. LIST OPERATION (GET)
    if request.method == 'GET':
        # Controller returns a list of DTOs
        todo_dtos = TodoController.list_todos()

        # Serialize the list of DTOs directly (many=True for lists)
        serializer = TodoItemResponseSerializer(instance=todo_dtos, many=True)
        return Response(serializer.data)

    # 2. CREATE OPERATION (POST)
    elif request.method == 'POST':
        request_serializer = TodoItemCreateRequestSerializer(data=request.data)

        if request_serializer.is_valid():
            todo_dto = request_serializer.to_todo_dto()

            # Controller returns the new DTO
            new_dto = TodoController.create_todo(todo_dto)

            # Serialize the single DTO for the 201 response
            response_serializer = TodoItemResponseSerializer(instance=new_dto)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------------------------
# B. DETAIL, UPDATE, DELETE (GET, PUT, PATCH, DELETE)
# -----------------------------------------------
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def todo_detail_update_delete(request, pk):
    """
    Handles operations on a single TodoItem (pk is the ID).
    Views use the Controller for all data fetching and modification.
    """

    # 1. RETRIEVE OPERATION (GET)
    if request.method == 'GET':
        # Controller returns a single DTO (and handles 404)
        todo_dto = TodoController.get_todo_by_id(pk)

        response_serializer = TodoItemResponseSerializer(instance=todo_dto)
        return Response(response_serializer.data)

    # 2. DELETE OPERATION (DELETE)
    elif request.method == 'DELETE':
        # Delegate deletion to the Controller
        TodoController.delete_todo(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 3. UPDATE OPERATION (PUT/PATCH)
    elif request.method in ['PUT', 'PATCH']:
        partial = request.method == 'PATCH'
        request_serializer = TodoItemUpdateRequestSerializer(data=request.data, partial=partial)

        if request_serializer.is_valid():
            todo_dto = request_serializer.to_todo_dto()

            # Controller returns the updated DTO
            updated_dto = TodoController.update_todo(pk, todo_dto)

            response_serializer = TodoItemResponseSerializer(instance=updated_dto)
            return Response(response_serializer.data)

        return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)