from django.shortcuts import render
# api/views.py
from rest_framework import viewsets
from .models import TodoItem
from .serializers import TodoItemSerializer

class TodoItemViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Todo items.
    This single class handles all CRUD operations:
    - POST (Create)
    - GET (Retrieve list/single)
    - PUT/PATCH (Update)
    - DELETE (Delete)
    """
    queryset = TodoItem.objects.all().order_by('created_at')
    serializer_class = TodoItemSerializer

    # Optional: Customize the save method if needed, but not required for basic CRUD
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)