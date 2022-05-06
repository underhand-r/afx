# ------------------------------------------------------------------------------
# Import Sub-Packages
# ------------------------------------------------------------------------------
from django.urls import path
from django.urls import include
from django.contrib import admin

# ------------------------------------------------------------------------------
# URL Patterns
# ------------------------------------------------------------------------------
urlpatterns = [
    path('', include('web.urls')),
    path('admin/', admin.site.urls),
]