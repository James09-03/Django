# api/controllers.py (Now acting as TodoViewController)

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

# Import the new Service Layer (the refactored views.py)
from .views import TodoService

# Import Serializers from their respective packages
from .serializer.request import (
    TodoItemCreateRequestSerializer,
    TodoItemUpdateRequestSerializer
)


# NOTE: The SerializerValidations class is custom to your reference project.
# Since we don't have it, we will manually perform the validation and DTO conversion
# in the view functions, but keep the structure clean.

class TodoViewController:
    """
    API Controller layer: Handles the HTTP request/response cycle,
    performs validation, and delegates processing to the TodoService.
    """

    # -----------------------------------------------
    # A. CREATE
    # -----------------------------------------------
    @api_view(['POST'])
    def create(request: Request) -> Response:
        # 1. Validate incoming JSON data
        request_serializer = TodoItemCreateRequestSerializer(data=request.data)

        if request_serializer.is_valid():
            # 2. Convert validated data into DTO
            todo_dto = request_serializer.to_todo_dto()

            # 3. Delegate to Service Layer
            return TodoService().create_todo(validated_dto=todo_dto)

        # Return validation errors
        return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # -----------------------------------------------
    # B. LIST
    # -----------------------------------------------
    @api_view(['GET'])
    def get_all(request: Request) -> Response:
        # 1. No request body to validate, just delegate
        # 2. Delegate to Service Layer
        return TodoService().get_all_todos()

    # -----------------------------------------------
    # C. RETRIEVE, UPDATE, DELETE (Detail Operations)
    # -----------------------------------------------
    @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
    def detail_operations(request: Request, pk: int) -> Response:

        # --- RETRIEVE (GET) ---
        if request.method == 'GET':
            return TodoService().get_todo_detail(pk=pk)

        # --- DELETE (DELETE) ---
        elif request.method == 'DELETE':
            return TodoService().delete_todo(pk=pk)

        # --- UPDATE (PUT/PATCH) ---
        elif request.method in ['PUT', 'PATCH']:
            # 1. Determine partial update
            partial = request.method == 'PATCH'
            request_serializer = TodoItemUpdateRequestSerializer(data=request.data, partial=partial)

            if request_serializer.is_valid():
                # 2. Convert validated data into DTO
                todo_dto = request_serializer.to_todo_dto()

                # 3. Delegate to Service Layer
                return TodoService().update_todo(pk=pk, validated_dto=todo_dto)

            # Return validation errors
            return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Default case (should be unreachable)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)