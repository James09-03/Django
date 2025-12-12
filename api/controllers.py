# api/controllers.py

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .views import TodoService
# Import the custom exception from the model file
from .model.todo_model import TodoDoesNotExist
from api.dataclass.todo_dto import TodoItemDTO

# Import Serializers
from .serializer.request.todo_create_request import TodoItemCreateRequestSerializer
from .serializer.response.todo_response import TodoItemResponseSerializer


class TodoViewController:
    # -----------------------------------------------
    # A. LIST and CREATE (GET / POST)
    # -----------------------------------------------
    @api_view(['GET', 'POST'])
    def list_or_create(request: Request) -> Response:
        service = TodoService()

        # --- LIST (GET) ---
        if request.method == 'GET':
            # Service returns a list of DTOs
            todo_dtos = service.get_all_todos()

            # Controller converts list of DTOs to JSON Response
            response_serializer = TodoItemResponseSerializer(todo_dtos, many=True)
            return Response(response_serializer.data, status=status.HTTP_200_OK)

        # --- CREATE (POST) ---
        elif request.method == 'POST':
            request_serializer = TodoItemCreateRequestSerializer(data=request.data)

            if request_serializer.is_valid():
                # Get the DTO from the validated data
                todo_dto = request_serializer.to_todo_dto()

                # Service returns a single DTO
                new_item_dto = service.create_todo(validated_dto=todo_dto)

                # Controller converts single DTO to JSON Response
                response_serializer = TodoItemResponseSerializer(new_item_dto)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)

            return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # -----------------------------------------------
    # B. RETRIEVE, UPDATE, DELETE (Detail Operations)
    # -----------------------------------------------
    @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
    def detail_operations(request: Request, pk: int) -> Response:
        service = TodoService()

        try:
            # --- RETRIEVE (GET) ---
            if request.method == 'GET':
                item_dto = service.get_todo_detail(pk=pk)
                response_serializer = TodoItemResponseSerializer(item_dto)
                return Response(response_serializer.data, status=status.HTTP_200_OK)

            # --- DELETE (DELETE) ---
            elif request.method == 'DELETE':
                service.delete_todo(pk=pk)
                return Response(status=status.HTTP_204_NO_CONTENT)

            # --- UPDATE (PUT/PATCH) ---
            elif request.method in ['PUT', 'PATCH']:
                partial = request.method == 'PATCH'
                request_serializer = TodoItemCreateRequestSerializer(data=request.data, partial=partial)

                if request_serializer.is_valid():
                    # Create a DTO from the request data
                    update_dto = request_serializer.to_todo_dto()
                    # Perform update via Service
                    updated_dto = service.update_todo(pk=pk, validated_dto=update_dto)

                    response_serializer = TodoItemResponseSerializer(updated_dto)
                    return Response(response_serializer.data, status=status.HTTP_200_OK)

                return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


        except service.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)