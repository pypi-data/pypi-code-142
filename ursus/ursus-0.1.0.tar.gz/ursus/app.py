from typing import Callable

import quart

from .powerdns import views as powerdns_views


def create_app(load_config_callback: Callable[[quart.Quart], None]) -> quart.Quart:
    app = quart.Quart(__name__)
    load_config_callback(app)

    app.register_blueprint(powerdns_views.blueprint)
    init_auth(app)

    return app


def init_auth(app: quart.Quart) -> None:
    from .extensions import auth

    auth.init_app(app)
