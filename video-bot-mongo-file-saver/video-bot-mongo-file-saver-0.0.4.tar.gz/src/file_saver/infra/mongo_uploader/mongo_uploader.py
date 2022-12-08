#native
from typing import List, AnyStr
from os import path, environ


from gridfs import GridFS

#project
from file_saver.utils.helpers import get_attr

from pymongo import MongoClient

class MongoUploader:

   
    def __init__(self, config):

        self.config = config
        

        mongo_uri = get_attr(self.config,'mongo_uri', environ.get('MONGO_URI'))
        mongo_database_name = get_attr(self.config,'mongo_database_name', environ.get('MONGO_DATABASE_NAME'))

        self.repository_id = get_attr(self.config,'repository_id', None)

        if (self.repository_id  == None):
            raise Exception('Repository id is required')

        self.mongo_files_table = get_attr(self.config,'mongo_files_table', environ.get('MONGO_FILES_TABLE'))
        self.mongo_chunks_table = get_attr(self.config,'mongo_chunks_table', environ.get('MONGO_CHUNKS_TABLE'))

        self.client = MongoClient(mongo_uri)
        self.db = self.client[mongo_database_name]
        self.fs = GridFS(self.db)
         

    def run(self, files):

      
      results: List[AnyStr] = []

     

      for file in files: 

            try: 
                
                
                if ('location' in file):
                    filename = file['location']
                else:
                    filename = file 


                print(f'Saving file {filename}')

                
                #logs_collection = self.db['files']  
                #log = {'message': 'File Uploaded Successfully','status': 'ok', "date": datetime.datetime.utcnow() }
                #file_id = logs_collection.insert_one(log).inserted_id
                
                with open(filename, "rb") as f:
                    if ('location' in file):
                        file_id = self.fs.put(f.read(), **file, repository_id = self.repository_id, source = filename, file = path.basename(filename))
                    else:    
                        file_id = self.fs.put(f.read(), repository_id = self.repository_id, source = filename, file = path.basename(filename))

                status = 'OK'
                message = 'File Uploaded Successfully'

                results.append({'repository_id': self.repository_id, 'file': file, 'status': status, 'message': message, 'mongo_file_id': file_id})

            except Exception as err:
                message = str(err)
                print(f'{filename} - Could Not Upload File: {str(err)}')
                status = 'ERR'
                message = message
                results.append({'file': file, 'status': status, 'message': message})
                continue

      return results



    












    
    

         
