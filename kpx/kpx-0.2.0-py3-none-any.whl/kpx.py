#!/usr/bin/env python3

import configparser
import typer
import boto3

from os.path import expanduser
from typing import Optional
from prettytable import PrettyTable

app = typer.Typer(help="KPC application for aws profiles", no_args_is_help=True)


class Output:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def header(text):
        print(f'{Output.HEADER}{text}{Output.ENDC}')

    @staticmethod
    def success(text):
        print(f'{Output.OKGREEN}{text}{Output.ENDC}')

    @staticmethod
    def error(text):
        print(f'{Output.FAIL}{text}{Output.ENDC}')


class AwsConfigManager:
    def __init__(self, file_credentials, file_config):
        self.file_credentials = file_credentials
        self.file_config = file_config

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


class AwsResourceQuery:
    def __init__(self, client):
        self.client = client

    def get_table_header(self):
        return ["ID", "Name", "Type", "PrivateIP", "PublicIP", "State"]

    def get_instance_name_from_tags(self, instance_tags):
        for item in instance_tags:
            if item['Key'] == 'Name':
                return item['Value']

        return '---'

    def list_ec2_instances(self):
        instances = []
        resp = self.client.describe_instances()
        for reservation in resp['Reservations']:
            for instance in reservation['Instances']:
                # print(instance)
                data = {
                    'id': instance['InstanceId'],
                    'name': self.get_instance_name_from_tags(instance['Tags']),
                    'type': instance['InstanceType'],
                    'PrivateIp': instance['PrivateIpAddress'] if 'PrivateIpAddress' in instance else '-',
                    'PublicIp': instance['PublicIpAddress'] if 'PublicIpAddress' in instance else '-',
                    'state': instance['State']['Name'],
                }

                instances.append(data.values())

        return instances


@app.command()  # pragma: no cover
def cfg(
        aws_profile: Optional[str] = typer.Argument('default'),
        region: Optional[str] = typer.Argument("us-east-1"),
        output: Optional[str] = typer.Argument("json")
):
    """
    Configure ~/.aws/config file with profiles settings
    """
    Output.header('Updating ~/.aws/config file')
    user_home_directory = expanduser('~')

    awc = AwsConfigManager(
        f'{user_home_directory}/.aws/credentials',
        f'{user_home_directory}/.aws/config',
    )

    IniUtils.check_directory_exists(f'{user_home_directory}/.aws/')

    awc.update_config(aws_profile, region, output)
    awc.write_config_file()


@app.command()  # pragma: no cover
def cred(
        aws_profile: Optional[str] = typer.Argument('default'),
        key: Optional[str] = typer.Argument(""),
        secret: Optional[str] = typer.Argument("")
):
    """
    Configure ~/.aws/credentials file with aws credentials
    """
    Output.header('Updating ~/.aws/credentials file')
    user_home_directory = expanduser('~')

    awc = AwsConfigManager(
        f'{user_home_directory}/.aws/credentials',
        f'{user_home_directory}/.aws/config',
    )

    IniUtils.check_directory_exists(f'{user_home_directory}/.aws/')

    awc.update_credentials(aws_profile, key, secret)
    awc.write_credentials_file()


@app.command()  # pragma: no cover
def r53(zone_id: Optional[str] = typer.Argument('')):
    """
    List Route53 hosted zones
    """
    client = boto3.client('route53')

    if zone_id != '':
        Output.header(f'List Records for ZoneID: {zone_id}')
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

        if len(resp['HostedZones']) > 0:
            for zone in resp['HostedZones']:
                table.add_row([
                    zone['Name'].strip('.'),
                    zone['Id'].replace('/hostedzone/', ''),
                    zone['ResourceRecordSetCount']
                ])
            print(table.get_string())
        else:
            account_id = boto3.client('sts').get_caller_identity().get('Account')
            Output.error(f'No hosted zones in account: {account_id}')
    except Exception as e:
        Output.error(e)


@app.command()  # pragma: no cover
def ec2():
    """
    List EC2 instances
    """
    client = boto3.client('ec2')
    arq = AwsResourceQuery(client)

    table = PrettyTable()
    table.field_names = arq.get_table_header()
    table.align['PrivateIP'] = 'r'
    table.align['PublicIP'] = 'r'
    table.align['Name'] = 'r'

    table.add_rows(arq.list_ec2_instances())

    print(table.get_string())


if __name__ == '__main__':  # pragma: no cover
    app()
