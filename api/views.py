# api/views.py

# 1. REMOVE duplicate and incorrect DTO import.
#    We only need the DTO from its new, correct location.
from api.dataclass.todo_dto import TodoItemDTO

# 2. CORRECT the import from todo_model:
#    - 'TodoRepository' must be changed to 'TodoItemRepository'.
#    - 'TodoItemDTO' is removed here to prevent the duplicate import warning/conflict.
from .model.todo_model import TodoItemRepository, TodoDoesNotExist


# The Service Layer methods now only deal with DTOs and the Repository
class TodoService:
    """
    The Service Layer (Business Logic). Returns DTOs.
    """

    def __init__(self):
        # FIX: Instantiate the repository using the correct class name
        self._todo_repository = TodoItemRepository()

        # Keep the exception reference
        self.DoesNotExist = TodoDoesNotExist

    def get_all_todos(self) -> list[TodoItemDTO]:
        return self._todo_repository.get_all()

    def create_todo(self, validated_dto: TodoItemDTO) -> TodoItemDTO:
        return self._todo_repository.create(validated_dto)

    def get_todo_detail(self, pk: int) -> TodoItemDTO:
        # Assuming you implemented get_by_id in your repository
        return self._todo_repository.get_by_id(pk)

    def update_todo(self, pk: int, validated_dto: TodoItemDTO) -> TodoItemDTO:
        # Assuming you implemented update in your repository
        return self._todo_repository.update(pk, validated_dto)

    def delete_todo(self, pk: int):
        # Assuming you implemented delete in your repository
        self._todo_repository.delete(pk)