import os
from os.path import abspath, dirname, join
import sys
import django
import shutil
from pathlib import Path
from subprocess import run
from django.conf import settings
from django.core import management

sys.path.insert(0, '.')

def setup_django(debug=False, settings=None):
    if settings:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
    elif debug:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banjo.settings_debug')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banjo.settings')
    django.setup()

    # Loading views causes banjo's route_get and route_post decorators to be invoked,
    # which populates banjo.urls:urlpatterns. 
    from app import views

    management.execute_from_command_line(['', 'makemigrations', 'app', 'banjo'])
    management.execute_from_command_line(['', 'migrate'])

def main():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-s", "--shell", action="store_true")
    parser.add_argument("-p", "--port", type=int, default=5000)
    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument("-m", "--settings")
    args = parser.parse_args()

    if args.shell:
        setup_django(args.debug, settings=args.settings)
        management.execute_from_command_line(['', 'shell_plus'])
    else:
        setup_django(args.debug, settings=args.settings)
        management.execute_from_command_line(['', 'runserver', str(args.port)])
