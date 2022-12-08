#native
from typing import List, AnyStr
import base64


class PureFileSaver:

   
    def __init__(self, config):

        self.config = config
        
       
         

    def run(self, files: List[AnyStr]):

    
      results: List[AnyStr] = []

     
      for file in files: 

            try: 
                
                filename = file

                print(f'Saving file {filename}')

                status = 'OK'
                message = 'File Saved Successfully'

            
                data = {
                    'headers': { "Content-Type": "application/octet-stream" },
                    'statusCode': 200,
                    'body': base64.b64encode(open(filename, 'rb').read()).decode('utf-8'),
                    'isBase64Encoded': True
                }

                return data



                return data

            except Exception as err:
                message = str(err)
                print(f'{filename} - Could not read file: {str(err)}')
                status = 'ERR'
                message = message
                results.append({'file': file, 'status': status, 'message': message})
                continue

      return results



    












    
    

         
