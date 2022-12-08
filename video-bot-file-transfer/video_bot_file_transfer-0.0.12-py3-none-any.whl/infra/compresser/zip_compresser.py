from typing import List, AnyStr
from file_transfer.utils.helpers import get_attr
import ntpath

import zipfile

class ZipCompresser:

   
    def __init__(self, config):
        self.config = config
        
         

    def run(self, files: List[AnyStr], output_file: AnyStr = 'output.zip'):
     
      results: List[AnyStr] = []
        
      try: 

       

        with zipfile.ZipFile(output_file, "w") as zf:
            
            for file in files: 
                    
                filename = file
                print(f'Adding file for compressing: {filename}')
                arcname  =ntpath.basename(filename)
                zf.write(filename, arcname)
                status = 'OK'
                message = 'File added successfully'
                results.append({'filename': filename, 'status': status, 'message': message})
            
           


      except Exception as err:
        message = str(err)
        print(f'{output_file} - Could not compress file: {str(err)}')
        status = 'ERR'
        results.append({'output_file': output_file, 'status': status, 'message': message})
                          

      return results, output_file



    












    
    

         
