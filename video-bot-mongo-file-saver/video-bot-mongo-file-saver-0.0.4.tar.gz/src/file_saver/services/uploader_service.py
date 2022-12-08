from file_saver.services.base_service import BaseService
from os import path
from file_saver.utils.helpers import get_attr, check_type
class UploaderService(BaseService):
    
    def __init__(self, config, saver, compresser):

        self.config = config

        #workers
        self.saver = saver
        self.compresser = compresser

        self.compress = get_attr(self.config['saver'],  'compress', False)
        self.temp_directory = get_attr(self.config,  'temp_directory', 'tmp')
        self.save_identifier = get_attr(self.config,  'save_identifier', True)


    def execute(self, data):

        output_files = []
        new_data = []

        for item in data:
            if (check_type(item, str)):
                new_item = item
                new_data.append(new_item)
            else:    
                new_item = get_attr(item, 'location', '')
                if (len(str(new_item)) > 0):
                    new_data.append(new_item)

        
        if (len(new_data) > 0):
            #if required, commpresses files into 1 zip
            if (self.compress == True and self.compresser != None):
                output_file = path.basename('output.zip')
                output_file = path.join(self.temp_directory, output_file)
                results, compressed_file = self.compresser.run(new_data, output_file)
                output_files.append(compressed_file)
            else:
                output_files.extend(new_data)

            #saves files 
            result = self.saver.run(data)     


        return result