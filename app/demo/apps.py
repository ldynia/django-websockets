from django.apps import AppConfig


class DemoConfig(AppConfig):

    name = 'demo'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        from . import signals
