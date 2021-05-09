from django.apps import AppConfig


class EventConfig(AppConfig):
    name = 'backend.digest'
    verbose_name = "Справочники"

    def ready(self):
        pass