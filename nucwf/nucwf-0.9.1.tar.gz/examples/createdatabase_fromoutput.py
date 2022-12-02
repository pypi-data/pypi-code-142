# this script creates from the files in a directory a databased of wave function files
# files are compressed when added, all files of the input directory need to be proper
# wave functions, files are added to the online database 

from nucwf import access
import os
import glob
import re
import fileextract as fe
import re

tolerance=1e-6
uploaddir=os.environ["SCRATCH"]+"/dbupload"
workdir=os.environ["SCRATCH"]+"/wfdbtest/"
inputdir=os.environ["HOME"]+"/papers/uncert-quant-frontiers/data/he4-srg-chsms-jube/000000/"


def get_wffile(OUT):
   """Method extracts wave function file name from output"""
   pattern=re.compile(r"WAVEOUT\:\s*(.*)\s*")
   
   for line in open(OUT):
     if "WAVEOUT:" in line:  
       regexpr=pattern.search(line)  
       waveout=regexpr.group(1)
       exit
   return waveout
    


# create database, download one if existent
wfdb=access.database(workdir=workdir)

filelist=glob.glob(inputdir+'0*submit/work/h*out')

for file_in in filelist:
  # get the run number    
  results=fe.getwf4nprop(file_in)
  # get file name of wave function and read it in
  waveout=get_wffile(file_in)
  print("Read file: ",waveout)
  wavein=access.wavefa4(waveout,printlevel=1)
  # get info from file 
  labels=wavein.get_labels()
  # augment by info from output file 
  labels={**labels,**results}
  # add to database 
  hashnamewf=wfdb.add_file(filename=waveout,**labels)  
  # compress file using the hashname 
  wavein.compress(workdir+hashnamewf,tolerance,printlevel=1)
  # read in again to check basic properties 
  wavein=access.wavefa4(workdir+hashnamewf,printlevel=1)
  
  
#print complete list of files
print(wfdb.pddf)

# now create upload ready version 
wfdb.prep_upload(uploaddir)






