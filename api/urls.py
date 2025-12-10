# api/urls.py
from rest_framework.routers import DefaultRouter
from .views import TodoItemViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'todos', TodoItemViewSet) # Creates routes for /todos/ and /todos/{id}/

# The API URLs are now determined automatically by the router.
urlpatterns = router.urls