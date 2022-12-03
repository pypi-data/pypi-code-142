#!/usr/bin/env python
import os, sys
#import asyncio
#import pwd
#import grp
#import crypt
# import questionary
# import nest_asyncio
#import time
import requests

from prompt_toolkit.shortcuts import clear

from domain.management import enable_service_now as dmt_now

from assistant import HOME
from assistant.listen import enable_service_now as assistant_listen_now
from assistant.as_client import is_listen_service_up

# nest_asyncio.apply()

USER = os.environ.get("USERNAME", 'root').lower()

# def what_is_user_secret():
#     try:
# 	    return questionary.password("What is your secret?").ask()
#     except (Exception, KeyboardInterrupt):
#         return None

# def root_password():
#     try:
# 	    return questionary.password("What is the administrative password?").ask()
#     except (Exception, KeyboardInterrupt):
#         return None

def checkIfServiceIsOK(host="localhost", port="5068"):
	try:
		r = requests.get(f'http://{host}:{port}')
		return r.ok
	except (ConnectionError, Exception) as e:
		return False

def enable_service_now():
    #print("Preparing Assistant")
    #print("Please wait...")

    # Not needed 
    #pw = root_password()
    # Make sure assistant is a user.
    # try:
    #     pwd.getpwnam('assistant')
    # except KeyError:
    #     print('User assistant does not exist.')
    #     print("Creating Assistant.")

    #     secret = None
    #     print("Please enter a secret passphrase only you and Assistant can remember.")
    #     print("Or type 'exit' to quit.")
    #     while not secret:
    #         try:
    #             secret = what_is_user_secret()
    #         except KeyboardInterrupt:
    #             print("Type exit to quit.")
    #     if secret == "exit":
    #         sys.exit(1)
    #     encPass = crypt.crypt(secret,"22")
    #     print("Creating Assistant please enter your password.")
    #     # create user assistant
    #     os.system(f"sudo -S useradd -r -p {encPass} -g assistant assistant")
    # Make sure group exists

    # try:
    #     grp.getgrnam('assistant')
    # except KeyError:
    #     print('Group assistant does not exist.')
    #     print("Creating Assistant group")
    #     # Make group assistant
    #     os.system(f"sudo groupadd -r -p '{encPass}' assistant")
    #     # Make sure it has enough permissions.
    #     os.system(f"if getent group root | grep -q '\b${{username}}\b'; then exit 0 else sudo usermod -G root assistant fi")
    #     os.system(f"sudo usermod -g 0 -o assistant")

    # Ask Assistant to launch its services. # Correction, ask it to ask the user...
    if not any([
        os.path.exists("/usr/lib/systemd/user/assistant.service"),
        checkIfServiceIsOK()
    ]):
        print("There is no Assistant Service.")
        print("To download it, type:")
        print("    wget https://gitlab.com/waser-technologies/technologies/assistant/-/raw/main/assistant.service.example")
        print("    mv assistant.service.example /usr/lib/systemd/user/assistant.service")
        sys.exit(1)
    if not any([
        os.path.exists(f"{HOME}/.config/systemd/user/default.target.wants/assistant.service"),
        os.path.exists("/usr/lib/systemd/user/default.target.wants/assistant.service"),
        checkIfServiceIsOK()
        ]):
        print("Assistant Service is not enabled.")
        print("To enable it type")
        print("    systemctl enable --now assistant.service")
        sys.exit(1)
    if is_listen_service_up():
        assistant_listen_now()
    #print("Starting Assistant")
    # try:
    #     time.sleep(100)
    # except KeyboardInterrupt:
    #     sys.exit(1)
    #clear()