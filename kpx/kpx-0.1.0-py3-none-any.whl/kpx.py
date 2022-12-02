#!/usr/bin/env python3
import json

import configparser
import typer
import os
import boto3

from os.path import expanduser
from typing import Optional
from prettytable import PrettyTable

app = typer.Typer(help="KPC application for aws profiles", no_args_is_help=True)


class IniUtils:
    @staticmethod
    def show_file_content(content):
        output = ''
        for key in content:
            output += f"[{key}]\n"
            for item in content[key]:
                output += f"{item} = {content[key][item]}\n"

            output += "\n"

        return output

    @staticmethod
    def check_directory_exists(file_path):
        os.makedirs(file_path, exist_ok=True)


class AwsConfigOutput:
    def __init__(self, io=None):
        self.io = io

    def success(self, text):
        if self.io is None:
            print(f'<info>{text}</>')
        else:
            self.io.write_line(f'<info>{text}</>')

    def error(self, text):
        if self.io is None:
            print(f'<error>{text}</>')
        else:
            self.io.write_line(f'<error>{text}</>')


class AwsConfigManager:
    def __init__(self, file_credentials, file_config, io=None):
        self.file_credentials = file_credentials
        self.file_config = file_config
        self.aco = AwsConfigOutput(io)

        self.creds = configparser.ConfigParser()
        self.creds.read(file_credentials)

        self.cfg = configparser.ConfigParser()
        self.cfg.read(file_config)

    def update_credentials(self, profile, access_key, secret_key):
        if profile not in self.creds:
            self.creds.update({profile: {
                'aws_access_key_id': '',
                'aws_secret_access_key': '',
            }})

        if self.aco is not None:
            self.aco.success(f'Updating credentials for profile {profile}')

        for key in self.creds[profile]:
            new_value = ''
            if key == 'aws_access_key_id' and access_key is not None:
                new_value = access_key
            if key == 'aws_secret_access_key' and secret_key is not None:
                new_value = secret_key

            self.creds[profile][key] = new_value

        return self

    def update_config(self, profile, region, output):
        if profile != 'default':
            profile = f'profile {profile}'

        if self.aco is not None:
            self.aco.success(f'Updating config for profile {profile}')

        self.cfg.update({
            profile: {
                'region': region,
                'output': output,
            }
        })

    def get_credentials(self, profile_name):
        data = {}
        if profile_name in self.creds:
            for key in self.creds[profile_name]:
                data.update({key: self.creds[profile_name][key]})

        return data

    def get_config(self, profile_name):
        data = {}
        profile_string = f'profile {profile_name}' if profile_name != 'default' else 'default'
        if profile_string in self.cfg:
            for key in self.cfg[profile_string]:
                data.update({key: self.cfg[profile_string][key]})

        return data

    def write_credentials_file(self):
        with open(self.file_credentials, 'w') as file:
            self.creds.write(file)

        return self

    def write_config_file(self):
        with open(self.file_config, 'w') as file:
            self.cfg.write(file)

        return self


# class AwsParameters(IniUtils):
#     def __init__(self, profile):
#         self.profile = profile
#
#         user_home_directory = expanduser('~')
#
#         awc = AwsConfigManager(
#             f'{user_home_directory}/.aws/credentials',
#             f'{user_home_directory}/.aws/config'
#         )
#
#         self.credentials = awc.get_credentials(profile)
#         self.configs = awc.get_config(profile)
#
#     @property
#     def access_key_id(self):
#         if 'aws_access_key_id' not in self.credentials:
#             return None
#         return self.credentials['aws_access_key_id']
#
#     @property
#     def secret_access_key(self):
#         if 'aws_secret_access_key' not in self.credentials:
#             return None
#         return self.credentials['aws_secret_access_key']
#
#     @property
#     def region(self):
#         if 'region' not in self.configs:
#             return None
#         return self.configs['region']
#
#
# class AwsConnectionManager:
#     def __init__(self, profile_name):
#         self._clients = {}
#         self._resources = {}
#
#         self.cfg = AwsParameters(profile_name)
#
#     def get_client(self, name):
#         if name in self._clients:
#             return self._clients[name]
#
#         client = boto3.client(
#             name,
#             region_name=self.cfg.region,
#             aws_access_key_id=self.cfg.access_key_id,
#             aws_secret_access_key=self.cfg.secret_access_key
#         )
#
#         self._clients.update({name: client})
#
#         return client
#
#     def get_resource(self, name):
#         if name in self._resources:
#             return self._resources[name]
#
#         resouce = boto3.resource(
#             name,
#             region_name=self.cfg.region,
#             aws_access_key_id=self.cfg.access_key_id,
#             aws_secret_access_key=self.cfg.secret_access_key
#         )
#
#         self._resources.update({name: resouce})
#
#         return resouce
#
#
# class AwsShow(IniUtils):
#     """
#     AWS Show configurations
#
#     aws
#         {--r|cred : Show credentials file content}
#         {--o|config : Show config file content}
#     """
#
#     def handle(self):
#         user_home_directory = expanduser('~')
#
#         awc = AwsConfigManager(
#             f'{user_home_directory}/.aws/credentials',
#             f'{user_home_directory}/.aws/config',
#             # self.io
#         )
#
#         if self.option('cred'):
#             self.io.write(self._show_file_content(awc.cfg))
#             return None
#
#         if self.option('config'):
#             self.io.write(self._show_file_content(awc.creds))
#             return None


@app.command()
def cfg(
        aws_profile: Optional[str] = typer.Argument('default'),
        region: Optional[str] = typer.Argument("us-east-1"),
        output: Optional[str] = typer.Argument("json")
):
    """
    Configure ~/.aws/config file with profiles settings
    """
    print('AWS config')
    # print(f'AWS_PROFILE: {aws_profile}')
    # print(f'AWS_REGIOn: {region}')
    # print(f'output type: {output}')

    user_home_directory = expanduser('~')

    awc = AwsConfigManager(
        f'{user_home_directory}/.aws/credentials',
        f'{user_home_directory}/.aws/config',
    )

    IniUtils.check_directory_exists(f'{user_home_directory}/.aws/')

    awc.update_config(aws_profile, region, output)
    awc.write_config_file()


@app.command()
def cred(
        aws_profile: Optional[str] = typer.Argument('default'),
        key: Optional[str] = typer.Argument(""),
        secret: Optional[str] = typer.Argument("")
):
    """
    Configure ~/.aws/credentials file with aws credentials
    """
    print('AWS credentials')
    # print(f'AWS_PROFILE: {aws_profile}')
    # print(f'username: {key}')
    # print(f'password: {secret}')

    user_home_directory = expanduser('~')

    awc = AwsConfigManager(
        f'{user_home_directory}/.aws/credentials',
        f'{user_home_directory}/.aws/config',
    )

    IniUtils.check_directory_exists(f'{user_home_directory}/.aws/')

    awc.update_credentials(aws_profile, key, secret)
    awc.write_credentials_file()


@app.command()
def r53(zone_id: Optional[str] = typer.Argument('')):
    """
    List Route53 hosted zones
    """
    client = boto3.client('route53')

    if zone_id != '':
        print(f'List Records for ZoneID: {zone_id}')
        resp = client.list_resource_record_sets(
            HostedZoneId=zone_id
        )

        table = PrettyTable()
        table.field_names = ["Name", "Type", "Targets"]
        table.align['Name'] = 'r'
        table.align['Targets'] = 'l'

        for rec in resp['ResourceRecordSets']:
            if 'AliasTarget' in rec:
                table.add_row([
                    rec['Name'].strip('.'),
                    rec['Type'],
                    '(alias) ' + rec['AliasTarget']['DNSName'].strip('.')[:128]
                ])

            if 'ResourceRecords' in rec:
                table.add_row([
                    rec['Name'].strip('.'),
                    rec['Type'],
                    '\n'.join([d['Value'][:128] for d in rec['ResourceRecords']])
                ])

        print(table.get_string())
        return None

    try:
        resp = client.list_hosted_zones()

        table = PrettyTable()
        table.field_names = ["Domain", "Id", "Records"]
        table.align['Domain'] = 'r'

        for zone in resp['HostedZones']:
            table.add_row([
                zone['Name'].strip('.'),
                zone['Id'].replace('/hostedzone/', ''),
                zone['ResourceRecordSetCount']
            ])

        print(table.get_string())
    except Exception as e:
        print(e)

#
# @app.command()
# def vpc():
#     print('VPC')
#
#
# @app.command()
# def show():
#     pass


if __name__ == '__main__':
    app()
