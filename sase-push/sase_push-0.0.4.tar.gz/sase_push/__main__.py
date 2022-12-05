"""Main"""
import os
import json
import click
import requests
from requests.auth import HTTPBasicAuth
from sase_push.utils import HiddenPassword, return_yaml
from prismasase.config_mgmt import configuration
from prismasase.configs import Auth

@click.command()
@click.option('--org_id', '-org', help="Enter the Orgnanization ID", required=True)
@click.option('--environment', '--env', '-e', help="Environment: ALTDEV|DEV|QA|PROD", required=True)
@click.option('--description', "-d", help="Descripton", required=True)
@click.option('--user', '--cient_id',
              prompt=True,
              default=lambda: os.environ.get('USER', ''))
@click.option('--password','--client_secret', 
            prompt=True,
            default=lambda: HiddenPassword(os.environ.get('PASSWORD', '')),
            hide_input=True)
def main(org_id: str, environment: str, user: str, password: str, description: str):
    click.secho(f"Using environment: {environment}")
    click.secho(f"Organization: {org_id}")
    config = return_yaml()
    if config[environment.upper()]["TYPE"] == 'sase':
        click.secho(f"You are using SASE Connecting to TSG: {config[environment.upper()]['TSG']}")
        click.secho("Please ensure you enter the currect client ID for username and client secret for password")
    if isinstance(password, HiddenPassword):
        passwd = password.password
    url = f"{config[environment.upper()]['URL']}"
    click.secho(f"Using URL: {url}")
    if config[environment.upper()]["TYPE"] == 'custom':
        params = {
            "org_id": org_id,
            "description": description
        }
        click.secho('pushing configuration please hold can take up to an hour')
        auth = HTTPBasicAuth(user, passwd)
        response = requests.post(url=url,params=params, auth=auth, verify=True)
    else:  
        auth = Auth(tsg_id=config[environment.upper()]['TSG'],client_id=password,client_secret=password,verify=config[environment.upper()['CERT']])
        click.secho(f"pushing configuration directly to {config[environment.upper()['TSG']]}")
        response = configuration.config_commit(folders=['Remote Networks', 'Service Connections'], auth=auth)
    click.secho(f'Returned Response:\n{json.dumps(response, indent=4)}')    
    return response

if __name__ == "__main__":
    main()
