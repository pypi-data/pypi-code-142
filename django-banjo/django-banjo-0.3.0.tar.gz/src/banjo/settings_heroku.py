import django_heroku
from .settings import *
import environ

django_heroku.settings(locals())

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
}
