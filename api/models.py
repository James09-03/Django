# api/models.py
from django.db import models


class TodoItem(models.Model):
    """
    Model for a simple to-do item.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # --- DATACLASS (Optional Best Practice) ---
    # For a simple model, a dataclass is often used for typed object passing 
    # in pure Python, but Django's Model instances are the primary data structure.
    # To demonstrate the concept for non-database-backed data:
    from dataclasses import dataclass

    @dataclass
    class TodoData:
        title: str
        is_completed: bool = False