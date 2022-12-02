from flaskez.Public.Models import Page
import typing
from flask import render_template, Flask, Blueprint, flash
import pathlib

routes = Blueprint('routes', 'flaskez_blueprint', static_folder=str(pathlib.Path(__file__).parent.resolve()) + "/css",
                   template_folder=str(pathlib.Path(__file__).parent.resolve()) + "/html")


class _Page:
    route = "/"

    def __init__(self, route: typing.Optional[str] = "/"):
        self.route = route

    @routes.route(route)
    def base(self=None, page: str = "base"):
        return render_template(page + ".html")


def instant_setup(pages: list[Page]) -> Flask:
    app = Flask('flaskez_application', static_folder=str(pathlib.Path(__file__).parent.resolve()) + "/css",
                template_folder=str(pathlib.Path(__file__).parent.resolve()) + "/html")
    app.register_blueprint(routes)

    app.run()

    for i, page in enumerate(pages):
        new_page = _Page(page.tpe + str(i))
        if i == 0:
            with app.app_context():
                new_page.base(page.tpe)
        else:
            flash("/" + new_page.route)

    return app
