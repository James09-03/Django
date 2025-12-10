# api/serializers.py
from rest_framework import serializers
from .models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id', 'title', 'description', 'is_completed', 'created_at')
        # 'read_only_fields' can be used to prevent updating fields like 'created_at'
        read_only_fields = ('created_at',)