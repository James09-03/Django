# api/admin.py

from .model.todo_model import TodoItem

from django.contrib import admin

# Register your models here.
admin.site.register(TodoItem)