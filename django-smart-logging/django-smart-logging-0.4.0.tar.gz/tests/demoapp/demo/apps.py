from django.apps import AppConfig


class Config(AppConfig):
    name = "demo"

    def ready(self):
        super().ready()
        from django.contrib.admin import site
        from smart_logging.pubsub import subscriber
        from smart_logging.smart_panel import smart_logging_panel

        site.register_panel(smart_logging_panel)
        subscriber.start()
