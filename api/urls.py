# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Maps to todo_list_create (GET/POST)
    path('todos/', views.todo_list_create, name='todo-list-create'),

    # Maps to todo_detail_update_delete (GET/PUT/PATCH/DELETE)
    path('todos/<int:pk>/', views.todo_detail_update_delete, name='todo-detail-update-delete'),
]