import os
from azure.keyvault.secrets import SecretClient
from azure.identity import EnvironmentCredential
from pathlib import Path
import sqlalchemy
from sqlalchemy.engine import URL
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from google.cloud import storage
import base64
import requests

vault_url = os.environ['AZURE_VAULT_URL']
credential = EnvironmentCredential()
client = SecretClient(vault_url,credential=credential)


class MssqlConnector:
    driver = '{ODBC Driver 17 for SQL Server}'
    server = None
    database = None
    uid = None
    pwd = None

    def __init__(self) -> None:
        pass

    @classmethod
    def connector(cls, database=None):
        if cls.database and database == None:
            database = cls.database
        if cls.uid:
            if database:
                connection_string = f'''
                DRIVER={cls.driver};
                SERVER={cls.server};
                DATABASE={database};
                UID={cls.uid};
                PWD={cls.pwd};
                '''
            else:
                connection_string = f'''
                DRIVER={cls.driver};
                SERVER={cls.server};
                UID={cls.uid};
                PWD={cls.pwd};
                '''
        else:
            if database:
                connection_string = f'''
                DRIVER={cls.driver};
                SERVER={cls.server};
                DATABASE={database};
                Trusted_Connection=yes;
                '''
            else:
                connection_string = f'''
                DRIVER={cls.driver};
                SERVER={cls.server};
                Trusted_Connection=yes;
                '''
        connection_url = URL.create(
                "mssql+pyodbc",
                host= cls.server,  # plain (unescaped) text
                password= cls.pwd,
                username= cls.uid,
                database= database,
                query= dict(driver='ODBC Driver 17 for SQL Server')
            )
            
        return sqlalchemy.create_engine(connection_url, fast_executemany=True)

    @classmethod
    def query(cls, query):
        connector = cls.connector()
        cnxn = connector.connect().execution_options(autocommit=True)
        count = cnxn.execute(query).rowcount

        print(str(count), 'rows affected')

        return None

class DW001Connector(MssqlConnector):
    server = client.get_secret('dw001-server').value
    uid = client.get_secret('dw001-uid').value
    pwd = client.get_secret('dw001-pwd').value

class AzureADSConnector(MssqlConnector):
    server = client.get_secret('azureADS-server').value
    database = 'ADS'
    uid = client.get_secret('azureADS-uid').value
    pwd = client.get_secret('azureADS-pwd').value

class AzureTMPConnector(MssqlConnector):
    server = client.get_secret('azureADS-server').value
    database = 'TMP'
    uid = client.get_secret('azureADS-uid').value
    pwd = client.get_secret('azureADS-pwd').value

    


def upload_blob_from_memory(bucket_name, contents, destination_blob_name, content_type='text/csv'):
    
    """Uploads a file to the bucket
    content_type = 'text/csv'
    bucket_name = 'format_address_file'
    destination_blob_name = 'CL011F.csv'
    contents = text or csv file
    """
    
    storage_client = storage.Client(project= client.get_secret('gcs-id').value)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(contents, content_type=content_type) 