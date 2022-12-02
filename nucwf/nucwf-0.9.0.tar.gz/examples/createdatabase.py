# this script creates from the files in a directory a databased of wave function files
# files are compressed when added, all files of the input directory need to be proper
# wave functions, files are added to the online database 

from nucwf import access
import os
import glob
import re

tolerance=1e-6
wfinputdir="/Users/andreasnogga/work/3n-wf"
uploaddir="/Users/andreasnogga/work/wfuploadprep"

def file_info(filen):
    """Method to extract lables from the filename."""

    filelabel={}

    try:
      resexpr=re.search(r"Lam=([0-9.]*)-.*c1=([\-0-9.]*)-c3=([\-0-9.]*)-c4=([\-0-9.]*)-cd=([\-0-9.]*)-ce=([\-0-9.]*[0-9])",filen)           
      filelabel['lam3NF']=float(resexpr.group(1))
      filelabel['c1']=float(resexpr.group(2))
      filelabel['c3']=float(resexpr.group(3))
      filelabel['c4']=float(resexpr.group(4))
      filelabel['cd']=float(resexpr.group(5))
      filelabel['ce']=float(resexpr.group(6))
    except:
      pass

    try:
      resexpr=re.search(r"chsms\-(.*)\-cut\=([0-9]*)\-pCoul",filen)           
      filelabel['MODENN']='chsms'
      filelabel['empotnr']=1
      filelabel['orderNN']=resexpr.group(1).lower()
      cutnum=int(resexpr.group(2))
      filelabel['LambdaNN']=[400.0,450.0,500.0,550.0][cutnum-1]
    except:
      pass

    if 'm189' in filen.lower(): 
     try:
       resexpr=re.search(r"chsms\-ib\-m189\-(.*)\-cut\=([0-9]*)\-pCoul",filen)
       filelabel['MODENN']='IBM189'.lower()
       filelabel['empotnr']=1
       filelabel['orderNN']=resexpr.group(1).lower()
       cutnum=int(resexpr.group(2))
       filelabel['LambdaNN']=[400.0,450.0,500.0,550.0][cutnum-1]
     except:
       pass

    try:
      resexpr=re.search(r"npt\=([0-9]*)\+([0-9]*)",filen)           
      filelabel['NPTA']=int(resexpr.group(1))
      filelabel['NPTB']=int(resexpr.group(2))
      filelabel['NPT']=filelabel['NPTA']+filelabel['NPTB']      
    except:
      pass

    try:
      resexpr=re.search(r"ne\=([0-9]*)\+([0-9]*)",filen)           
      filelabel['NEA']=int(resexpr.group(1))
      filelabel['NEB']=int(resexpr.group(2))
      filelabel['NE']=filelabel['NEA']+filelabel['NEB']      
    except:
      pass

    try:
      resexpr=re.search(r"nx\=([0-9]*)",filen)           
      filelabel['NX']=int(resexpr.group(1))
    except:
      pass
      
    return filelabel 


# create database, download one if existent
wfdb=access.database(workdir="/Users/andreasnogga/work/wfdbtest")

filelist=glob.glob(wfinputdir+'/*h5')

for file_in in filelist:

  # get wave function   
  print("Read file: ",file_in) 
  wavein=access.wavefa3(file_in,printlevel=1)
  labels=wavein.get_labels()

  # now I need to overwrite or add the known parameters
  # e.g., this needs editing depending on the directory
  filelabel=file_info(file_in)
  labels={**labels,**filelabel}
  
  # add file to database
  hashnamewf=wfdb.add_file(filename=file_in,**labels)  
  # compress to same name
  hashnamewf=wfdb.workdir+"/"+hashnamewf
  print("Compress file ....") 
  wavein.compress(hashnamewf,tolerance=tolerance,printlevel=1)
  # read compressed file to check consistency
  print("Now read compressed file ....") 
  wavein=access.wavefa3(hashnamewf,printlevel=1)
  
#print complete list of files

print(wfdb.pddf)

# now create upload ready version 
wfdb.prep_upload(uploaddir)






