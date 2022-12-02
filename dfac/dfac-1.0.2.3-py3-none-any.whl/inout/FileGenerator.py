import os
class FileGenerator:
    
    def print_out(self,var, filename):
        if not os.path.exists("outputfiles"):
            os.mkdir("outputfiles")
        file = open("outputfiles/"+filename,'w')
        file.write(var)
        file.close()