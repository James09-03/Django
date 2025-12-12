# api/urls.py

from django.urls import path
from .controllers import TodoViewController

urlpatterns = [
    # Route for listing all todos (GET) and creating a new one (POST)
    path(
        'todos/',
        TodoViewController.list_or_create,
        name='todo-list-create'
    ),

    # Route for retrieving (GET), updating (PUT/PATCH), and deleting (DELETE)
    path(
        'todos/<int:pk>/',
        TodoViewController.detail_operations,
        name='todo-detail-operations'
    ),
]