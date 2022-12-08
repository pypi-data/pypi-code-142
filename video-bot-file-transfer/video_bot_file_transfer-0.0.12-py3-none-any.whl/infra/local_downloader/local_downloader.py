#native
from typing import List, AnyStr
from os import makedirs, path
import os 
import shutil

#project
from file_transfer.utils.helpers import get_attr, remove_last_slash
from file_transfer.utils.file import delete_directory, get_all_files


class LocalDownloader:

   
    def __init__(self, config):

        self.config = config
        
        self.sources = get_attr(self.config, 'sources', [])
                                              
        self.temp_directory = get_attr(self.config, 'temp_directory', '/tmp')
        self.continue_on_error =  get_attr(self.config, 'continue_on_error', True)
        self.skip_file_not_found = get_attr(self.config, 'skip_file_not_found', True)
        self.respect_source_directory_structure = get_attr(self.config, 'respect_source_directory_structure', True)
        self.source_base_path = get_attr(self.config, 'source_base_path', '')

        if (len(str(self.source_base_path)) == 0) and (self.respect_source_directory_structure == True):
            raise Exception('Source base Path is required when Respect Source Directory Structure is true')
         
         

    def run(self):
    
      downloaded_files = []
      object_name = ''

     
      sources = self.sources
      temp_directory = self.temp_directory
      source_base_path = self.source_base_path
      respect_source_directory_structure = self.respect_source_directory_structure

      results: List[AnyStr] = []

     
    
      filename = ''
      objects = []
     
      for source in sources: 

            try: 

                directory = source['directory']
                objects = []

                if ('objects' in source):
                    objects = source['objects'] or []

                try:
                    #gets all objects from the specific subfolder
                    if (len(objects) == 0):
                        arr = os.listdir(directory)
                        objects.extend(arr) 
                                
                       
                except Exception as err:
                    if (not self.continue_on_error):
                        raise Exception(message)   
                        

                
                for object in objects:

                   
                    
                    object_name = path.join(directory, object)
                    
                    
                    if (not path.isdir(object_name)):

                        if (not respect_source_directory_structure):
                            filename = path.join(temp_directory,str(object_name.replace('/','_')))
                        else:
                            directory = remove_last_slash(str(directory).replace(source_base_path, ''))
                            new_temp_directory = path.join(temp_directory,  directory )
                            makedirs(new_temp_directory, exist_ok=True)
                            filename = path.join(new_temp_directory, path.basename(object_name))


                        print(f'Downloading object {object_name}')
                        print(f'Saving file to temporary path: {filename}')
                        shutil.copyfile(object_name, filename )
                        status = 'OK'
                        message = 'File Downloaded Successfully'
                        results.append({'file': filename, 'status': status, 'message': message})
                        downloaded_files.append(filename)
                    else:
                        print(f'Downloading directory {object_name}')
                        print(f'Saving directory to temporary path: {temp_directory}')
                        target_dir = path.join(temp_directory,path.basename(directory), object)
                        delete_directory(target_dir)
                        shutil.copytree(object_name, target_dir )
                        status = 'OK'
                        message = 'File Downloaded Successfully'
                        results.append({'file': target_dir, 'status': status, 'message': message})

                        al_files_in_target_dir = get_all_files(target_dir)
                        downloaded_files.extend(al_files_in_target_dir)

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



    












    
    

         
