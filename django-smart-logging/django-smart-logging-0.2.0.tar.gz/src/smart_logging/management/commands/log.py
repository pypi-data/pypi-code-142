import logging

from django.core.management.base import BaseCommand


def parse_bool(v):
    if v is None:
        return v
    return v.lower() in ["true", "t", "on", "y"]


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("logger", nargs="+", type=str)
        parser.add_argument("--level", type=str)
        parser.add_argument("--handler", action="append", dest="handlers")
        parser.add_argument("--propagate", type=str)

    def handle(self, *args, **options):
        from smart_logging.pubsub import subscriber

        cfg = {}
        if options["level"]:
            cfg["level"] = logging._checkLevel(options["level"].upper())
        if p := parse_bool(options["propagate"]):
            cfg["propagate"] = p
        if options["handlers"] is not None:
            cfg["handlers"] = options["handlers"]

        for logger_name in options["logger"]:
            cfg["logger"] = logger_name
            subscriber.notify(cfg)

        self.stdout.write(
            self.style.SUCCESS(
                'Successfully configured loggers "%s"' % options["logger"]
            )
        )
