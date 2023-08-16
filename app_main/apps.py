from django.apps import AppConfig


class AppMainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_main'
    verbose_name = 'Menú principal'

    def ready(self):
        import app_main.signals
