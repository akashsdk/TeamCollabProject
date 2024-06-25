from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('teamcollab.urls')),  # Include the URLs from teamcollab
]
