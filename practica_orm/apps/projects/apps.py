from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    #1. Se actualiza la ubicación
    name = 'apps.projects'
