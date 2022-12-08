#native
from typing import List, AnyStr
from os import path, environ, makedirs
from bson.objectid import ObjectId
import tempfile

from gridfs import GridFS
from pymongo import MongoClient

#project
from file_saver.utils.helpers import get_attr, removekey

import shutil

DEFAULT_FILES_DB = 'filesdb'
DEFAULT_FILES_TABLE = 'fs.files'
DEFAULT_CHUNKS_TABLE = 'fs.chunks'

class MongoDownloader:

   
    def __init__(self, config):

        self.config = config
        
        self.sources = get_attr(self.config, 'sources',[] )
        
        self.temp_directory = get_attr(self.config, 'temp_directory', '/tmp')
        self.continue_on_error =  get_attr(self.config, 'continue_on_error', True)
        self.skip_file_not_found = get_attr(self.config, 'skip_file_not_found', True)

        
        mongo_uri = get_attr(self.config,'mongo_uri', environ.get('MONGO_URI_READ'))
        mongo_database_name = get_attr(self.config,'mongo_database_name', environ.get('MONGO_DATABASE_NAME_READ'))

        if (mongo_database_name == None):
            mongo_database_name = DEFAULT_FILES_DB
        
        self.mongo_files_table = get_attr(self.config,'mongo_files_table', environ.get('MONGO_FILES_TABLE_READ'))
        if (self.mongo_files_table == None):
            self.mongo_files_table = DEFAULT_FILES_TABLE

        self.mongo_chunks_table = get_attr(self.config,'mongo_chunks_table', environ.get('MONGO_CHUNKS_TABLE_READ'))
        if (self.mongo_chunks_table == None):
            self.mongo_chunks_table = DEFAULT_CHUNKS_TABLE
        
        self.client = MongoClient(mongo_uri)
        self.db = self.client[mongo_database_name]
        self.fs = GridFS(self.db)
        
        self.respect_source_directory_structure = get_attr(self.config, 'respect_source_directory_structure', True)
        self.remove_attributes_from_source_structure = get_attr(self.config, 'remove_attributes_from_source_structure', [])
        
         

    def run(self):

      downloaded_files = []
      object_name = ''

     
      sources = self.sources
      temp_directory = self.temp_directory
      respect_source_directory_structure = self.respect_source_directory_structure
      remove_attributes_from_source_structure = self.remove_attributes_from_source_structure 
      
      results: List[AnyStr] = []

      files_collection = self.db[self.mongo_files_table]

     
    
      filename = ''
      objects = []
     
      for source in sources: 

            try: 

                #repository_id = get_attr(source, 'repository_id', None)
                objects = get_attr(source, 'objects', [])

                #if (repository_id == None):
                #    print('repository id is required')
                #    continue
                
                if 'objects' in source:
                    source = removekey(source, 'objects')  
                

                documents = files_collection.find({ **source })
                
                for document in documents:
                    
                    object_id = str(document['_id'])
                    
                    if (respect_source_directory_structure == True):
                        items = source.items()
                        full_path = temp_directory
                        for item in items:
                            if (item[0] not in remove_attributes_from_source_structure):
                                id = item[1]
                                full_path = path.join(full_path, id)
                                print(full_path)
                        makedirs(full_path, exist_ok=True)    

                         

                    extracted_file = str(document['file'])


                    #filter to specific object(s) if informed in the request
                    if (len(objects) > 0):
                        if (object_id not in objects):
                            continue

                    print(f'Downloading object {extracted_file}')    

                    tf = tempfile.NamedTemporaryFile()

                    out = self.fs.get(ObjectId(object_id))
                    tf.write(out.read())

                    if (respect_source_directory_structure == False):
                        filename = path.join(temp_directory,str(extracted_file.replace('/','_')))
                    else:
                        filename = path.join(full_path, path.basename(extracted_file))


                    print(f'Saving file to temporary path: {filename}')
                    shutil.copyfile(tf.name, filename)
                    
                    
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



    












    
    

         
