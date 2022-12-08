#native
from typing import List, AnyStr
from os import path, makedirs
import ntpath
import shutil


#project
from file_transfer.utils.helpers import get_attr


class LocalFileSaver:

   
    def __init__(self, config):

        self.config = config
        
        self.target_directory = self.config['target_directory']

        self.respect_source_directory_structure = get_attr(self.config, 'respect_source_directory_structure', True)
        self.use_attributes_to_generate_directory_structure = get_attr(self.config, 'use_attributes_to_generate_directory_structure', True)
        self.source_base_path =  get_attr(self.config, 'source_base_path', '')
        
        if (len(str(self.source_base_path)) == 0) and (self.respect_source_directory_structure == True):
            raise Exception('Source base Path is required when Respect Source Directory Structure is true')
         

    def run(self, files: List[AnyStr]):

      target_directory = self.target_directory
      respect_source_directory_structure = self.respect_source_directory_structure
      use_attributes_to_generate_directory_structure = self.use_attributes_to_generate_directory_structure
      source_base_path = self.source_base_path

      results: List[AnyStr] = []
     

      for file in files: 

            try: 
                
                if ('location' in file):
                    filename = file['location']
                else:
                    filename = file 

                print(f'Saving file {filename}')

                if (respect_source_directory_structure == True):
                    key_filename = ntpath.basename(filename)
                    key = filename.replace(source_base_path, target_directory)
                    full_file_path = key.replace(key_filename,'')
                    makedirs(full_file_path, exist_ok=True)
                else:
                    if (use_attributes_to_generate_directory_structure == False or not(('location' in file)) ):
                        key_filename = ntpath.basename(filename)
                        key = path.join(target_directory, key_filename)
                    else:
                        items = file.items()
                        full_path = target_directory
                        key_filename = ntpath.basename(filename)
                        for item in items:
                            if (item[0] != 'location'):
                                id = item[1]
                                full_path = path.join(full_path, id)
                        makedirs(full_path, exist_ok=True)   
                        key = path.join(full_path, key_filename)
                                



                shutil.copyfile(filename, key)

                status = 'OK'
                message = 'File Uploaded Successfully'
                results.append({'file': file, 'status': status, 'message': message, 'target': key})

            except Exception as err:
                message = str(err)
                print(f'{filename} - Could Not Upload File: {str(err)}')
                status = 'ERR'
                message = message
                results.append({'file': file, 'status': status, 'message': message})
                continue

      return results
      