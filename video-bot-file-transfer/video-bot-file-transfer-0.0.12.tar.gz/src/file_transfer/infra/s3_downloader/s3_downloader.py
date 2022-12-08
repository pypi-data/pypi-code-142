#native
from typing import List, AnyStr
from os import path, makedirs


#externals
import boto3

#project
from file_transfer.utils.helpers import get_attr, remove_last_slash


class S3Downloader:

   
    def __init__(self, config):

        self.config = config
        
        self.source_bucket = get_attr(self.config, 'source_bucket','')
        self.sources = get_attr(self.config, 'sources',[])

        self.aws_credentials = self.config['aws_credentials'] 
      

        self.session = boto3.Session(
            aws_access_key_id=self.aws_credentials['client_id'],
            aws_secret_access_key=self.aws_credentials['client_secret']
        )

        self.temp_directory = get_attr(self.config, 'temp_directory', '/tmp')
        
        
        self.continue_on_error =  get_attr(self.config, 'continue_on_error', True)
        self.skip_file_not_found = get_attr(self.config, 'skip_file_not_found', True)

        self.respect_source_directory_structure = get_attr(self.config, 'respect_source_directory_structure', True)
        self.source_base_path =  remove_last_slash(get_attr(self.config, 'source_base_path', ''))


        
        if (len(str(self.source_base_path)) == 0) and (self.respect_source_directory_structure == True):
            raise Exception('Source base Path is required when Respect Source Directory Structure is true')


    def get_files(self, client, source_bucket, prefix):

                objects = []

                try:
                    #gets all objects from the specific subfolder
                        
                        result = client.list_objects(Bucket=source_bucket, Prefix=prefix, Delimiter='/')
                        if (result['ResponseMetadata']['HTTPStatusCode'] == 200):
                            
                            if 'Contents' in result:
                                for content in result['Contents']:
                                    key = content['Key']
                                    if (key != prefix):
                                        objects.append(key) 

                            if 'CommonPrefixes' in result:
                                for o in result.get('CommonPrefixes'):
                                    new_prefix = o.get('Prefix')
                                    new_objects = self.get_files(client, source_bucket, new_prefix)
                                    objects.extend(new_objects)
                            
                           
                    
                except Exception as err:
                    if (not self.continue_on_error):
                        raise Exception(err) 

                return objects               

    def run(self):

      downloaded_files = []
      object_name = ''

      source_bucket = self.source_bucket
      sources = self.sources
      session = self.session
      respect_source_directory_structure = self.respect_source_directory_structure
      temp_directory = self.temp_directory
      source_base_path = self.source_base_path

      results: List[AnyStr] = []

     
      s3 = session.resource('s3')
      client = boto3.client('s3')
      bucket = s3.Bucket(source_bucket)
      filename = ''
      objects = []
     
     
      for source in sources: 

            try: 

                directory = source['directory']
                objects = []

                if ('objects' in source):
                    objects = list(map(lambda item: path.join(directory, item),source['objects'])) or []

                new_objects = self.get_files(client, source_bucket, directory)
                objects.extend(new_objects) 
                
                for object in objects:
                    
                    base_object = path.basename(object)
                    object_name = object

                    if (not respect_source_directory_structure):
                        filename = path.join(temp_directory,str(object_name.replace('/','_')))
                    else:
                        directory = remove_last_slash(directory)
                        directory = remove_last_slash(str(directory).replace(source_base_path, ''))
                        new_temp_directory = path.join(temp_directory,  directory )
                        makedirs(new_temp_directory, exist_ok=True)
                        filename = path.join(new_temp_directory, path.basename(object_name))

                    
                    print(f'Downloading object {object_name}')
                    print(f'Saving file to temporary path: {filename}')
                    bucket.download_file(object_name, filename  )
                    status = 'OK'
                    message = 'File Downloaded Successfully'
                    results.append({'file': filename, 'status': status, 'message': message})

                    downloaded_files.append(filename)

            except Exception as err:


                message = str(err)
                print(f'{object_name} - Could Not Download File: {str(err)}')
                status = 'ERR'
                message = message
                results.append({'file': filename, 'status': status, 'message': message})

                
                if ((not self.skip_file_not_found) and err.response['Error']['Code']):
                    raise Exception(message)

                if (not self.continue_on_error):
                    raise Exception(message)

                continue

      return results, downloaded_files



    












    
    

         
