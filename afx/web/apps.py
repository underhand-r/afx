# ------------------------------------------------------------------------------
# Import Sub-Packages
# ------------------------------------------------------------------------------
from django.apps import AppConfig

# ------------------------------------------------------------------------------
# Class
# ------------------------------------------------------------------------------
class WebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web'