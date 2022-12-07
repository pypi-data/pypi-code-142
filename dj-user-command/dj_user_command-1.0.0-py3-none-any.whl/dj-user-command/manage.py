from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand, CommandError
from cryptography.fernet import Fernet
import os

class Command(BaseCommand):
    help = 'Creates a new user and adds them to a list of groups'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='The username of the new user')
        parser.add_argument('encrypted_password', type=str, help='The encrypted password of the new user')
        parser.add_argument('group_names', type=str, nargs='+', help='The names of the groups to add the user to')
        parser.add_argument('--print-public-key', action='store_true', help='Print the public key used to encrypt the password')

    def handle(self, *args, **options):
        username = options['username']
        encrypted_password = options['encrypted_password']
        group_names = options['group_names']
        print_public_key = options['print_public_key']

        # Get the public and private keys from the environment variables
        public_key_path = os.environ['PUBLIC_KEY_PATH']
        private_key_path = os.environ['PRIVATE_KEY_PATH']
        with open(public_key_path, 'rb') as f:
            public_key = f.read()
        with open(private_key_path, 'rb') as f:
            private_key = f.read()

        # Print the public key if the option was specified
        if print_public_key:
            print(public_key)

        # Decrypt the password using the private key
        fernet = Fernet(private_key)
        password = fernet.decrypt(encrypted_password)

        # Create the user
        user = User.objects.create_user(username=username, password=password)

        # Add the user to the specified groups
        for group_name in group_names:
            group = Group.objects.get(name=group_name)
            group.user_set.add(user)
