from django.apps import AppConfig

class LibraryConfig(AppConfig):
    # Default auto field for primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    # Name of the application
    name = 'library'
