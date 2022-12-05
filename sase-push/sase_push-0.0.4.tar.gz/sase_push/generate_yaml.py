"""Generates a YAML Config File"""

from getpass import getpass
from os.path import exists, expanduser
from os import mkdir
import sys

import click
import yaml

@click.command()
@click.option('--custom', is_flag=True, default=False, help='Used to create a custom configuration vs direct to Prisma Access SASE')
def gen_yaml(custom: bool):
    """Generates a prisma access SASE yaml config file

    Raises:
        ValueError: _description_
    """
    click.secho('Running YAML Configs', fg='blue')
    ENVIRONMENTS = ['ALTDEV', 'DEV', 'QA', 'PROD']
    env_dict = {env: {} for env in ENVIRONMENTS}
    CERT = input('Pleae enter certificate for verification or bool True|False: ')
    if isinstance(CERT, str):
        if CERT.lower() == 'true':
            CERT = True
        elif CERT.lower() == 'false':
            CERT = False
        else:
            CERT = CERT
    for env in ENVIRONMENTS:
        if not custom:
            URL = input(f'Please enter {env} URL: ')
            env_dict[env]["TYPE"]= 'custom'
        else:
            URL = "https://api.sase.paloaltonetworks.com/sse/config/v1/config-versions/candidate:push"
            #USERNAME = input(f'Please enter Client ID for {env}: ')
            #PASSWD = getpass(f"Please enter Client Secret for {env}: ")
            TSG = input(f"Please enter the TSG Account Number for {env}: ")
            env_dict[env]["TGS"] = TSG
            env_dict[env]["TYPE"] ='sase'
        env_dict[env]['URL'] = URL
        env_dict[env]['CERT'] = CERT
    home = expanduser('~')
    base_dir = f"{home}/.config"
    if not exists(f"{home}/.config"):
        mkdir(base_dir)
    filename = f"{base_dir}/.sase_push"
    with open(rf'{filename}', 'w', encoding='utf-8') as yam:
        yaml.dump(env_dict, yam)
    click.secho("Created YAML config file for Prisma Access SASE in user directory", fg='green')
    sys.exit()

    
def gen_yaml_dir():
    print('Running YAML Configs')
    CLIENT_ID = input("Please input Client ID: ")
    CLIENT_SECRET = getpass("Please input Client Secret: ")
    TSG = input("Please enter TSG ID: ")
    CERT = input("Please enter custom cert location" +
                 "('true'|'false'|<custom_cert_location>): ")
    if CERT.lower() in ['true', 'false']:
        CERT = CERT.lower()
    elif not exists(CERT):
        raise ValueError(f'{CERT} Does not exist')
    yaml_dict = {
        "TSG": TSG,
        "CLIENT_ID": CLIENT_ID,
        "CLIENT_SECRET": CLIENT_SECRET,
        "CERT": CERT
    }
    home = expanduser('~')
    base_dir = f"{home}/.config"
    if not exists(f"{home}/.config"):
        mkdir(base_dir)
    filename = f"{base_dir}/.prismasase"
    with open(rf'{filename}', 'w', encoding='utf-8') as yam:
        yaml.dump(yaml_dict, yam)
    print("Created YAML config file for Prisma Access SASE in user directory")
    sys.exit()


if __name__ == '__main__':
    gen_yaml()
