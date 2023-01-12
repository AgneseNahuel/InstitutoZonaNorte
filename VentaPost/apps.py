from django.apps import AppConfig


class VentapostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'VentaPost'

    def ready(self):
        import VentaPost.signals
