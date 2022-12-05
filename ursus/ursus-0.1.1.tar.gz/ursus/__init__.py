import quart.flask_patch  # noqa: F401

from . app import create_app


__all__ = ['create_app']
