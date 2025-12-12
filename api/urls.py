# api/urls.py

from django.urls import path
from . import controllers  # Import the file containing the controller class

urlpatterns = [
    # Map LIST and CREATE methods
    path('todos/', controllers.TodoViewController.create, name='todo-create'),
    path('todos/', controllers.TodoViewController.get_all, name='todo-list'),
    # Note: Will require splitting GET/POST in a cleaner way if using path() twice

    # Map DETAIL, UPDATE, DELETE methods
    path('todos/<int:pk>/', controllers.TodoViewController.detail_operations, name='todo-detail'),
]