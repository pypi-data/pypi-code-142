from file_transfer.services.base_service import BaseService
from os import path
from file_transfer.utils.helpers import get_attr

class UploaderService(BaseService):
    
    def __init__(self, config, saver, compresser):

        self.config = config

        #workers
        self.saver = saver
        self.compresser = compresser

        self.compress =  get_attr(self.config['saver'],  'compress', False)
        self.temp_directory =   get_attr(self.config,  'temp_directory', 'tmp')
        


    def execute(self, files):

       
        output_files = []

        if (len(files) > 0):
            #if required, commpresses files into 1 zip
            if (self.compress == True and self.compresser != None):
                output_file = path.basename('output.zip')
                output_file = path.join(self.temp_directory, output_file)
                results, compressed_file = self.compresser.run(files, output_file)
                output_files.append(compressed_file)
            else:
                output_files.extend(files)

            #saves files 
            result = self.saver.run(output_files)     


        return result