import os

from celery import Celery
from flask import Flask

from server.api.handlers.register_all_handlers import *  # noqa # pylint: disable=unused-import
from server.database import db
from server.database import migrate
from server.rebar import rebar


# create app
def create_app() -> Flask:
    global celery
    app = Flask(__name__)
    app_settings = os.getenv("APP_SETTINGS", "server.config.DevelopmentConfig")
    app.config.from_object(app_settings)
    app.config.update(
        CELERY_CONFIG={
            "broker_url": "redis://localhost:6379",
            "result_backend": "redis://localhost:6379",
        }
    )
    rebar.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    return app


def make_celery(app=None):
    app = app or create_app()
    celery = Celery(
        "app",
        backend=app.config["CELERY_RESULT_BACKEND"],
        broker=app.config["CELERY_BROKER_URL"],
    )
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery
