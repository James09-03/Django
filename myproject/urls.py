# myproject/urls.py (Your project's main URL configuration)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Include the API application's URLs under the 'api/v1/' prefix
    path('api/v1/', include('api.urls')),
]