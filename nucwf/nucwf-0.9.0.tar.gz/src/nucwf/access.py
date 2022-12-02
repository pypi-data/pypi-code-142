import pandas as pd 
import os
import hashlib
import shutil
import requests
import gzip
import datetime
import re 
import numpy as np
import h5py 
import hdf5plugin 


class database:
    """This class defines an object that accesses wave function files stored online and an index in a pandas table."""
    
    def  __init__(self,webbase="https://just-object.fz-juelich.de:8080/v1/AUTH_1715b19bd3304fb4bb04f4beccea0cf2/wfstore/",pddf_hdf="wf_table.h5",workdir=""):
        """Initializes the object that gives read and write access to wave function files
           - webbase url of online storage for files
             in most cases, files will be already uploaded. Uploading is possible using methods defined below. 
           - pddf_hdf filename of pandas data frame containing the local index of the files.
             The table is generated if not available and written wave function files are added. 
           - workdir working directory for wave function table and wave function file downloads    
        """

        # add "/" to filename if required
        if webbase[-1]!="/":
           webbase=webbase+"/"
        if workdir!="":   
          if workdir[-1]!="/":
            workdir=workdir+"/"
                       
        # keep input in object 
        self.pddf_hdf=pddf_hdf
        self.webbase=webbase
        self.workdir=workdir

        if workdir!="" and (not os.path.exists(workdir)):
           os.mkdir(workdir) 

           
        
        # check whether data frame file is available online 
        url = webbase+pddf_hdf
        r=requests.get(url, stream=True)
        try:
          r.raise_for_status()
          table_online=True
        except requests.HTTPError:
          table_online=False

        print("table_online:",table_online)

        # check whether table is locally available

        table_local=os.path.exists(workdir+pddf_hdf)

        print("table_local:",table_local)

        # use local file if available 
        # download table if online available
        # or generate empty one if neither online nor offline available

        if table_online and not table_local:
           self._download_file_(url,workdir)    
           print("Table file is downloaded: ",url)
           table_local=True 
        
        # if file could not be downloaded and is not available
        # create an empty table otherwise load  table

        if table_local:
          self.pddf=pd.read_hdf(workdir+pddf_hdf, "/wffiles") 
          print("Read in file: ",workdir+pddf_hdf)
          # and if it came from online sources, set local flags to false
          if table_online:
            self.pddf["localavail"]=False
            self.pddf["localonly"]=False
        else:
          self.pddf=pd.DataFrame()
          savedf=self.pddf.copy(deep=True)
          savedf["localavail"]=False
          savedf["localonly"]=False
          savedf.to_hdf(self.workdir+self.pddf_hdf, key='wffiles', mode='w')
          print("Generated empty table ...")

        
# adapted from https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
    def _download_file_(self,url,workdir):
        """Auxiliary routine to download a file given by url to the workdir"""
       
        local_filename = workdir+url.split('/')[-1]
        # NOTE the stream=True parameter below
        with requests.get(url, stream=True) as r:
         r.raise_for_status()
         with open(local_filename, 'wb') as f:
           for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
        return local_filename


    def _prep_label_(self,**labels):
            """This method augments the labels by a standard set of labels given as
               shown in source code. Some basic checks of the file labels are performed. 
            """
            standard_labels={'Z':0,'N':0,"E[MeV]":0.0,
              'NP12A':0, 'NP12B':0, 'NP12':0, 'P12A':0, 'P12B':0,'P12C':0,
              'NP34A':0, 'NP34B':0, 'NP34':0, 'P34A':0, 'P34B':0,'P34C':0,
              'NP3A':0, 'NP3B':0, 'NP3':0, 'P3A':0, 'P3B':0, 'P3C':0,
              'NQ4A':0, 'NQ4B':0, 'NQ4':0, 'Q4A':0, 'Q4B':0, 'Q4C':0,
              'NQA':0, 'NQB':0, 'NQ':0, 'QA':0, 'QB':0, 'QC':0,
              'NPTA':0, 'NPTB':0,'NPT':0, 'PTA':0, 'PTB':0, 'PTC':0,
              'NEA':0, 'NEB':0, 'NE':0, 'EA':0, 'EB':0, 'EC':0,
              'NX':0,
              'taumax':0, 'lsummax':0,'lmax':0, 'j12max':0, 'l3max':0,'l4max':0,'lammax':0,'MTtot':0, 'Jtot':0,
              'MODENN':'none', 'orderNN':'none','LambdaNN':0.0, 'potnr':0, 'empotnr':0,
              'lam3NF':0.0, 'c1':0.0, 'c3':0.0, 'c4':0.0, 'cd':0.0, 'ce':0.0,'cE1':0.0, 'cE3':0.0, 'tnforder':'no3nf','j12max3nf':0,'j3max3nf':0,
              'relcalc':0,
              'nnsrg':0, 'tnfsrg':0, 'lambdaSRGNN':0.0,'lambdaSRG3N':0.0, 'potbareNN':0, 'potbareNNTNF':0, 'ostatSRGNN':0, 'ostatSRGTNF':0,
              'cutnumSRGNN':0.0, 'cutnumSRGTNF':0.0,}
        
            out_label={**standard_labels,**labels}

            # remove entries for uniquefilename,localonly,localavail,addtime,moditime
            try:
              del out_label['uniquefilename']
            except:
              pass  
            try:
              del out_label['localonly']
            except:
              pass  
            try:
              del out_label['localavail']
            except:
              pass  
            try:
              del out_label['addtime']
            except:
              pass  
            try:
              del out_label['moditime']
            except:
              pass  

            try:
              out_label["MTtot"]=out_label["mt4"] 
            except:
              pass  
            try:
              out_label["Jtot"]=out_label["j4"]  
            except:
              pass  
          # remove out_label to shorten dataset, keep energy 
            try:
              del out_label["H1[MeV]"]
            except:
              pass  
            try:
              del out_label["H2[MeV]"]
            except:
              pass  
            try:
              del out_label["ECSB[MeV]"]
            except:
              pass  
            try:
              del out_label["T[MeV]"]
            except:
              pass  
            try:
              del out_label["VNN1[MeV]"]
            except:
              pass  
            try:
              del out_label["VNN2[MeV]"]
            except:
              pass  
            try:
              del out_label["V3N[MeV]"]
            except:
              pass  
            try:
              del out_label["CSB[keV]"]
            except:
              pass  
            try:
              del out_label["NORM31"]
            except:
              pass  
            try:
              del out_label["NORM22"]
            except:
              pass  
            try:
              del out_label["P(S)[%]"]
            except:
              pass  
            try:
              del out_label["P(P)[%]"]
            except:
              pass  
            try:
              del out_label["P(D)[%]"]
            except:
              pass  
            try:
              del out_label["P(p)[%]"]
            except:
              pass  
            try:
              del out_label["P(n)[%]"]
            except:
              pass  
            try:
              del out_label["P(pp)[%]"]
            except:
              pass  
            try:
              del out_label["P(np)[%]"]
            except:
              pass  
            try:
              del out_label["P(nn)[%]"]
            except:
              pass  
            try:
              print(out_label["r(p)[fm]"])  
              del out_label["r(p)[fm]"]
              print("done")  
            except:
              pass  
            try:
              del out_label["r(n)[fm]"]
            except:
              pass  
            try:
              del out_label["r(NN)[fm]"]
            except:
              pass  
            try:
              del out_label["ETA"]
            except:
              pass  
            try:
              del out_label["DEV"]
            except:
              pass  
            try:
              del out_label["mt4"]
            except:
              pass  
            try:
              del out_label["j4"]   
            except:
              pass  
          
       
            # check the grid point numbers to find sums, if necessary 
            if out_label['NP12A']+out_label['NP12B']!=0:
               out_label['NP12']=out_label['NP12A']+out_label['NP12B']   
            if out_label['NP3A']+out_label['NP3B']!=0:
               out_label['NP3']=out_label['NP3A']+out_label['NP3B']   
            if out_label['NQ4A']+out_label['NQ4B']!=0:
               out_label['NQ4']=out_label['NQ4A']+out_label['NQ4B']   
            if out_label['NQA']+out_label['NQB']!=0:
               out_label['NQ']=out_label['NQA']+out_label['NQB']   
            if out_label['NP34A']+out_label['NP34B']!=0:
               out_label['NP34']=out_label['NP34A']+out_label['NP34B']   
            if out_label['NPTA']+out_label['NPTB']!=0:
               out_label['NPT']=out_label['NPTA']+out_label['NPTB']         
            if out_label['NEA']+out_label['NEB']!=0:
               out_label['NE']=out_label['NEA']+out_label['NEB']         

            # make all str lower characters 
            for key in out_label.keys():    
              if type(out_label[key])==type('test'):
                 out_label[key]=out_label[key].lower()

            if not (out_label["MODENN"] in ["av18","chsms","cdbonn","ibm189"]):
               raise(ValueError("'MODENN' not defined"))
            if not (out_label["tnforder"] in ["no3nf","n2lo"]):
               raise(ValueError("'tnforder' not defined"))
            if (out_label["N"] != int(out_label["N"])) or (out_label["N"] < 1) :
               raise(ValueError("'N' not defined"))
            if (out_label["Z"] != int(out_label["Z"])) or (out_label["Z"] < 1) :
               raise(ValueError("'Z' not defined"))
            if (out_label["Jtot"] != int(out_label["Jtot"])) or (out_label["Jtot"] < 0) :
               raise(ValueError("'Jtot' not defined"))
            if  out_label["MTtot"] != int(out_label["MTtot"]) :
               raise(ValueError("'MTtot' not defined"))
           
            return out_label        

    def add_file(self,filename=None,**labels):
        """This routine adds a file to the data base locally
           filename - absolute path to local file
           labels should be given according to standard set (see in _prep_label_).
           return the hashname of the file 
        """

        # prepare dictionary specifying the case wanted
        # also does some basic checks of consistency 

        specs=self._prep_label_(**labels)

        # prepare unique file name for internal use

        uniquefilename,hashname=self._unique_filename_(specs)

        # check for file in existing data base
        # combine spects to a df selection

        try:
          select=(self.pddf["Z"]==specs["Z"])
          for key, value in specs.items():
            select &= (self.pddf[key]==value) 
          if len(self.pddf.loc[select]) > 0:
             wfpresent=True
          else:   
             wfpresent=False
        except:
          # assume empty frame   
          wfpresent=False

        if wfpresent:  
          raise ValueError("wave function is already present!")
      
        # now check whether the hash is already used
        # and prepare flag to mark files that are only local
        
        specs["hashname"]=hashname
        specs["uniquefilename"]=uniquefilename
        specs["localonly"]=True
        specs["localavail"]=True
        specs["addtime"]=pd.to_datetime('now')
        specs["moditime"]=pd.to_datetime(datetime.datetime.fromtimestamp(os.path.getmtime(filename)))
        
        try:
          select=(self.pddf["hashname"]==specs["hashname"])
          if len(self.pddf.loc[select]) > 0:
             wfpresent=True
          else:   
             wfpresent=False
        except:
          # assume empty frame   
          wfpresent=False
          
        if wfpresent:
          print('UNIQUEFILENAME: ',uniquefilename)  
          raise ValueError("hashname is already present! This is an issue ... ")

        # now add file to database
        # first copy to working directory
        shutil.copy(filename,self.workdir+hashname)
        # then add row to data base
        self.pddf=self.pddf.append(specs,ignore_index=True)
        # and save table to disc 
        savedf=self.pddf.copy(deep=True)
        savedf.to_hdf(self.workdir+self.pddf_hdf, key='wffiles', mode='w')

        # returns hashed name of the file
        return hashname 


    def _unique_filename_(self,specs):
        """prepares a unique file name and its hash value"""

        uniquefilename="wf-Z={Z}-N={N}-mt={MTtot}-J={Jtot}-{MODENN}-{orderNN}-cut={LambdaNN}".format(**specs)

        if specs["tnforder"] != "no3nf": 
          uniquefilename+="-tnf={tnforder}-tnfcut={lam3NF}-c1={c1}-c3={c3}-c4={c4}-cd={cd}-ce={ce}".format(**specs)
          if specs["cE1"] != 0.0:  
            uniquefilename+="-cE1={cE1}".format(**specs)
          if specs["cE2"] != 0.0:  
            uniquefilename+="-cE2={cE2}".format(**specs)
          if specs["cE3"] != 0.0:  
            uniquefilename+="-cE3={cE3}".format(**specs)
          if specs["cE4"] != 0.0:  
            uniquefilename+="-cE4={cE4}".format(**specs)
          if specs["cE5"] != 0.0:  
            uniquefilename+="-cE5={cE5}".format(**specs)
          if specs["cE6"] != 0.0:  
            uniquefilename+="-cE6={cE6}".format(**specs)
          if specs["cE7"] != 0.0:  
            uniquefilename+="-cE7={cE7}".format(**specs)
          if specs["cE8"] != 0.0:  
            uniquefilename+="-cE8={cE8}".format(**specs)
          if specs["cE9"] != 0.0:  
            uniquefilename+="-cE9={cE9}".format(**specs)
          if specs["cE10"] != 0.0:  
            uniquefilename+="-cE10={cE10}".format(**specs)
        if specs["nnsrg"] != 'none':
          uniquefilename+="-srgNN={lambdaSRGNN}-{potbareNN}-{ostatSRGNN}-{cutnumSRGNN}".format(**specs)
        if specs["tnfsrg"] != 'False':
          uniquefilename+="-srg3N={lambdaSRG3N}-{potbareNNTNF}-{ostatSRGTNF}-{cutnumSRGTNF}".format(**specs)
          
        if specs["NP12A"]+specs["NP12B"]!=0:   
          uniquefilename+="-np12a={NP12A}-np12b={NP12B}".format(**specs)
        elif  specs["NP12"]!=0:
          uniquefilename+="-np12={NP12}".format(**specs)
          
        if specs["NP3A"]+specs["NP3B"]!=0:   
          uniquefilename+="-np3a={NP3A}-np3b={NP3B}".format(**specs)
        elif  specs["NP3"]!=0:
          uniquefilename+="-np3={NP3}".format(**specs)
          
        if specs["NQ4A"]+specs["NQ4B"]!=0:   
          uniquefilename+="-nq4a={NQ4A}-nq4b={NQ4B}".format(**specs)
        elif  specs["NQ4"]!=0:
          uniquefilename+="-nq4={NQ4}".format(**specs)
            
        if specs["NQA"]+specs["NQB"]!=0:   
          uniquefilename+="-nqa={NQA}-nqb={NQB}".format(**specs)
        elif  specs["NQ"]!=0:
          uniquefilename+="-nq={NQ}".format(**specs)
          
        if specs["NPTA"]+specs["NPTB"]!=0:   
          uniquefilename+="-npta={NPTA}-nptb={NPTB}".format(**specs)
        elif  specs["NPT"]!=0:
          uniquefilename+="-npt={NPT}".format(**specs)
            
        if specs["NEA"]+specs["NEB"]!=0:   
          uniquefilename+="-nea={NEA}-neb={NEB}".format(**specs)
        elif  specs["NE"]!=0:
          uniquefilename+="-ne={NE}".format(**specs)
        if  specs["NX"]!=0:
          uniquefilename+="-nx={NX}".format(**specs)
          
            
        uniquefilename+="-jmx={j12max}-lmx={lmax}-lsum={lsummax}-Tmx={taumax}".format(**specs)
          
        hashname=hashlib.sha256(str.encode(uniquefilename)).hexdigest()
    
        return uniquefilename,hashname
                
        
    def get_file(self,**labels):
        """This routine gets the local name of a file included in the database.
           Labels should be given according to standard set (see in _prep_label_).
           On exit the local filename (hashname) and a unique filename are returned.
           If not available locally, the file is downloaded.
           If not available remote, a ValueError is raised. 
        """

        # prepare dictionary specifying the case wanted

        specs=self._prep_label_(**labels)
        # look for case in database         
        try:
          select=(self.pddf["Z"]==specs["Z"])
          for key, value in specs.items():
            select &= (self.pddf[key]==value) 
          if len(self.pddf.loc[select]) > 0:
             wfpresent=True
          else:   
             wfpresent=False
        except:
          # assume empty frame   
          wfpresent=False

        # if not present, raise an error
        if not wfpresent:  
            raise ValueError("Wave function is not present in this database!")

        # then get filenames ...
        hashname=self.pddf.loc[select]["hashname"].item()
        uniquefilename=self.pddf.loc[select]["uniquefilename"].item()
        
        # if the wave function is present check whether it is locally available
        if not bool(self.pddf.loc[select]["localavail"].item()):
            index=int(self.pddf.index[select].tolist()[0])
            # and download the gzipped version if not available locally
            url=self.webbase+hashname+".gz"
            print("url: ",url)
            print("workdir: ",self.workdir)
            self._download_file_(url,self.workdir)
            # and ungzip the downloaded file 
            with gzip.open(self.workdir+hashname+".gz", 'rb') as f_in:
               with open(self.workdir+hashname, 'wb') as f_out:
                  shutil.copyfileobj(f_in, f_out)
            self.pddf.at[index,"localavail"]=True
            os.remove(self.workdir+hashname+".gz")
            
            # now the unzipped version should be available 
            
        return self.workdir+hashname,uniquefilename 

    def cleanup(self):
        """removes all local files from working directory except a possibly available table file"""

        try:
          select=(self.pddf["localavail"]==True)
          if len(self.pddf.loc[select]) > 0:
             wfpresent=True
          else:   
             wfpresent=False
        except:
          # assume empty frame   
          wfpresent=False

        # if some local files are present 
        if wfpresent:  
          for index,row in self.pddf[select].iterrows():
              # remove the file
              os.remove(self.workdir+row["hashname"])
              # and mark accordingly in table 
              self.pddf.at[index,"localavail"]=False
              self.pddf.at[index,"localonly"]=False

    def prep_upload(self,tmpdir):
        """gzips and moves all new files to temporary directory.
           Leaves the local copies unchanged.
           Also saves table and copies this file to temp directory.
           tmpdir -- directory for temporarily storing new files
           This method is meant as a preparation to upload new files to
           remote database. 
        """

        # add "/" to filename if required
        if tmpdir!="":   
          if tmpdir[-1]!="/":
            tmpdir=tmpdir+"/"
                       

            # first select all new files in database
        try:
          select=(self.pddf["localonly"]==True)
          if len(self.pddf.loc[select]) > 0:
             wfpresent=True
          else:   
             wfpresent=False
        except:
          # assume empty frame   
          wfpresent=False

        # if some new local files are present 
        if wfpresent:  
          for index,row in self.pddf[select].iterrows():
              # first generate a gzipped version of the file
              hashname=row["hashname"]
              with open(self.workdir+hashname, 'rb') as f_in:
                with gzip.open(self.workdir+hashname+".gz", 'wb') as f_out:
                  shutil.copyfileobj(f_in, f_out)

              # now upload the new gzipped file
              shutil.copy(self.workdir+hashname+".gz",tmpdir)
              # remove gzipped file 
              os.remove(self.workdir+row["hashname"]+".gz")              
              # and mark accordingly in table 
              self.pddf.at[index,"localonly"]=False

        # the write table to disk
        savedf=self.pddf.copy(deep=True)
        savedf["localonly"]=False
        savedf["localavail"]=False
        savedf.to_hdf(self.workdir+self.pddf_hdf, key='wffiles', mode='w')
        # and copy table file
        shutil.copy(self.workdir+self.pddf_hdf,tmpdir)
        
    def remove_file(self,index):
        """This routine removes a file from the data base locally.
           The file is idenfied by the index within the table.
           
        """

        # check whether file is downloaded and get hashname
        hashname=self.pddf.iloc[2]['hashname']
        # try to remove file 
        # first copy to working directory
        try:
          os.remove(self.workdir+hashname)
        except:
          pass
        # drop row from table
        self.pddf=self.pddf.drop(self.pddf.index[[index]])
        self.pddf.reset_index(drop=True, inplace=True)
        # and save table to disc 
        savedf=self.pddf.copy(deep=True)
        savedf.to_hdf(self.workdir+self.pddf_hdf, key='wffiles', mode='w')
        
    def merge(self,old):
       """Merges two databases for wave function files
       old -- other database including the wf files and table

       Both databases need to be completely disjunct which is checked according to the
       hashnames of the files.
       """

       # first merge the tables to a preliminary

       mergedf=pd.concat([self.pddf,old.pddf])

       duplicates=mergedf.duplicated(subset=['hashname'])

       if duplicates.any():
         raise(ValueError("Tables are not completely disjunct in terms of filenames!"))

       # now files seem to be disjunct, therefore I add all old files to the new dictory, I keep all other info
       # including the timestamps by using finally the merged table from above

       for index,row in old.pddf.iterrows():
           rowdict=dict(row)       
           hashname,uniquefilename=old.get_file(**rowdict)
           shutil.copy(hashname,self.workdir)
           
           
       # if all files are copied, the two tables can be merged again (includes downloaded file tags)
       # before old files from old table are marked as new
       previoustab=old.pddf.copy(deep=True)
       previoustab["localonly"]=True
       self.pddf=pd.concat([self.pddf,previoustab])
       # reset index so that all rows get a unique numbering
       self.pddf=self.pddf.reset_index(drop=True)

       savedf=self.pddf.copy(deep=True)
       savedf.to_hdf(self.workdir+self.pddf_hdf, key='wffiles', mode='w')

       
class wavefa3:
    """This class defines an object that allows to read a 3-He or 3-H wave function file into numpy arrays
       and to compress the file."""
    def  __init__(self,filen_in,printlevel=0):
        """This opens a A=3 wave function file for reading and reads all info and prints simple statistics.
           Optional parameter printlevel controls amout of printout: 0 = none, 1 = limited, 2 = extensive 
        
           After using this method, the kinematics and data are properties of the objects
            --- see more detailed documentation for the definition of properties of the object
        
        """

        # read in wave function and calculate kinetic energy and norm for checking
        # open file 
        # assume that file only contains one density 
        # read this density and auxiliary fields 
        filein=h5py.File(filen_in, 'r')

        # first read bookkeeping
        # assume that grid and bookkeeping are the same for WF and Faddeev component
        # read the one of the wf
        group=filein['3NBOUNDWAVE']
        # for conversions use 
        self.hbarc=group['hbarc'][()]

        # parameters for info
        self.alpha3Ncdepmax=group['alpha3Ncdepmax'][()]
        self.alpha3Nmax=group['alpha3Nmax'][()]
        self.cdep3N=group['cdep3N'][()]
        self.cdepNN=group['cdepNN'][()]
        self.evenNN=group['evenNN'][()]
        self.j12NNmax=group['j12NNmax'][()]
        self.j33Nmax=group['j33Nmax'][()]
        self.j33Nmin=group['j33Nmin'][()]
        self.l12NNmax=group['l12NNmax'][()]
        self.l33Nmax=group['l33Nmax'][()]
        self.I33Nmax=group['I33Nmax'][()]
        self.mtau33Nmax=group['mtau33Nmax'][()]
        self.mtau33Nmin=group['mtau33Nmin'][()]
        self.pari3Nmax=group['pari3Nmax'][()]
        self.pari3Nmin=group['pari3Nmin'][()]
        self.tau33Nmax=group['tau33Nmax'][()]
        self.tau33Nmin=group['tau33Nmin'][()]

        self.qnalpha3N=group['qnalpha3N'][()]

        
        self.alphaNNcdepmax=group['alphaNNcdepmax'][()]
        self.alphaNNmax=group['alphaNNmax'][()]
        self.mt12NNmax=group['mt12NNmax'][()]
        self.mt12NNmin=group['mt12NNmin'][()]

        self.qnalphaNN=group['qnalphaNN'][()]

        if printlevel>0:
          print('Number of 3N channels:   {0:d}  {1:d}\n'.format(self.alpha3Nmax,self.alpha3Ncdepmax))
          print('Number of 2N channels:   {0:d}  {1:d}\n'.format(self.alphaNNmax,self.alphaNNcdepmax))
        if printlevel>1:  
          print('3N channels:\n')
          print("{0:>5s} {1:>3s} {2:>3s} {3:>3s} {4:>3s} {5:>3s} {6:>3s} {7:>3s} {8:>5s} {9:>5s} {10:>7s} {11:>5s}".format(
          "alpha","l12","s12","j12","t12","l3","I3","j3","tau3","mtau3","alphaNN","pari"))
          for alpha in range(self.alpha3Ncdepmax):
            print("{0:5d} {1:3d} {2:3d} {3:3d} {4:3d} {5:3d} {6:3d} {7:3d} {8:5d} {9:5d} {10:7d} {11:5d}".format(alpha,
                   self.qnalpha3N[alpha,0],self.qnalpha3N[alpha,1],self.qnalpha3N[alpha,2],
                   self.qnalpha3N[alpha,3],self.qnalpha3N[alpha,4],self.qnalpha3N[alpha,5],
                   self.qnalpha3N[alpha,6],self.qnalpha3N[alpha,7],self.qnalpha3N[alpha,8],
                   self.qnalpha3N[alpha,9],self.qnalpha3N[alpha,10]))
            
        if printlevel>2:  
          print('NN channels:\n')
          print("{0:>5s} {1:>3s} {2:>3s} {3:>3s} {4:>3s} {5:>4s}".format(
          "alpha","l12","s12","j12","t12","mt12"))
          for alpha in range(self.alphaNNcdepmax):
            print("{0:5d} {1:3d} {2:3d} {3:3d} {4:3d} {5:4d} ".format(alpha,
                   self.qnalphaNN[alpha,0],self.qnalphaNN[alpha,1],self.qnalphaNN[alpha,2],
                   self.qnalphaNN[alpha,3],self.qnalphaNN[alpha,4]))

            
        # read constants 
        self.alpha_fein=group['alpha_fein'][()]
        self.m_eta=group['m_eta'][()]
        self.m_kaon=group['m_kaon'][()]
        self.m_kaon0=group['m_kaon0'][()]
        self.m_kaonp=group['m_kaonp'][()]
        self.m_omega=group['m_omega'][()]
        self.m_pi=group['m_pi'][()]
        self.m_pi0=group['m_pi0'][()]
        self.m_pip=group['m_pip'][()]
        self.m_rho=group['m_rho'][()]
        self.mlam=group['mlam'][()]
        self.mneu=group['mneu'][()]
        self.mnuc=group['mnuc'][()]
        self.mprot=group['mprot'][()]
        self.msig0=group['msig0'][()]
        self.msigm=group['msigm'][()]
        self.msigp=group['msigp'][()]
        self.mxi0=group['mxi0'][()]
        self.mxiave=group['mxiave'][()]
        self.mxim=group['mxim'][()]


        # now read and print mesh parameters 
        self.meshtype=''.join(list(map(lambda x: x.decode('utf-8'), group['meshtype'][()]))).strip()
        self.p12n1=group['p12n1'][()]
        self.p12n2=group['p12n2'][()]
        self.p12ntot=group['p12ntot'][()]

        self.p12a=group['p12p1'][()]
        self.p12b=group['p12p2'][()]
        self.p12c=group['p12p3'][()]

        self.p12p=group['p12p'][()]
        self.p12w=group['p12w'][()]

        self.p3n1=group['p3n1'][()]
        self.p3n2=group['p3n2'][()]
        self.p3ntot=group['p3ntot'][()]

        self.p3a=group['p3p1'][()]
        self.p3b=group['p3p2'][()]
        self.p3c=group['p3p3'][()]

        self.p3p=group['p3p'][()]
        self.p3w=group['p3w'][()]
        

        if printlevel>0:
          print("MESHTYPE: {0:s}".format(self.meshtype))
          print("NP12:     {0:d} {1:d}  {2:d} ".format(self.p12n1,self.p12n2,self.p12ntot))
          print("P12:      {0:15.6e}  {1:15.6e}  {2:15.6e} \n ".format(self.p12a,self.p12b,self.p12c))
        if printlevel>1:
          print("Grid points: \n")
          for ip in range(self.p12ntot):
            print("P12MESH:   {0:15.6e} {1:15.6e}".format(self.p12p[ip],self.p12w[ip]))

        if printlevel>0:
          print("NP3:     {0:d} {1:d}  {2:d} ".format(self.p3n1,self.p3n2,self.p3ntot))
          print("P3:      {0:15.6e}  {1:15.6e}  {2:15.6e} \n ".format(self.p3a,self.p3b,self.p3c))
        if printlevel>1:
          print("Grid points: \n")
          for ip in range(self.p3ntot):
            print("P3MESH:   {0:15.6e} {1:15.6e}".format(self.p3p[ip],self.p3w[ip]))

        self.wfunc=group['3namp'][()]
        

        # now read additional fields from Faddeev component

        group=filein['3NBOUNDFAD']
        self.fadcomp=group['3namp'][()]
        self.bener=group['BENER'][()]

        
        # integrate to get norm and kinetic energy  
        
        norm=np.einsum("ijkl,ijkl,k,k,j,j->",self.fadcomp,self.wfunc,self.p12p**2,self.p12w,self.p3p**2,self.p3w)
        ekin=(np.einsum("ijkl,ijkl,k,k,j,j->",self.fadcomp,self.wfunc,self.p12p**4,self.p12w,self.p3p**2,self.p3w)/self.mnuc
             +np.einsum("ijkl,ijkl,k,k,j,j->",self.fadcomp,self.wfunc,self.p12p**2,self.p12w,self.p3p**4,self.p3w)*0.75/self.mnuc)
        
        if printlevel>0:
          print("NORM/EKIN:  {0:15.6e} {1:15.6e}".format(3.0*norm,3.0*ekin*self.hbarc))

        filein.close()
        if printlevel>0:
          print("File size read:  {0:d}".format(os.path.getsize(filen_in)))
        

    def compress(self,filen_out,tolerance,printlevel=0):
        """This method write the current data in compressed form to the new file file_out using
           ZFP compression with accuracy tolerance. Optional parameter printlevel controls printout."""
    
        fileout=h5py.File(filen_out, 'w')
        
        # write all entries from self object
        # start with Faddeev component
        groupout=fileout.create_group('3NBOUNDFAD')
        # first bookkeeping to FADCOMP
        # parameters for info
        dsetout=groupout.create_dataset("alpha3Ncdepmax",self.alpha3Ncdepmax.shape,dtype="i4") 
        dsetout[()]=self.alpha3Ncdepmax        
        dsetout=groupout.create_dataset("alpha3Nmax",self.alpha3Nmax.shape,dtype="i4") 
        dsetout[()]=self.alpha3Nmax        
        dsetout=groupout.create_dataset("cdep3N",self.cdep3N.shape,dtype="i4") 
        dsetout[()]=self.cdep3N        
        dsetout=groupout.create_dataset("cdepNN",self.cdepNN.shape,dtype="i4") 
        dsetout[()]=self.cdepNN        
        dsetout=groupout.create_dataset("evenNN",self.evenNN.shape,dtype="i4") 
        dsetout[()]=self.evenNN        
        dsetout=groupout.create_dataset("j12NNmax",self.j12NNmax.shape,dtype="i4") 
        dsetout[()]=self.j12NNmax        
        dsetout=groupout.create_dataset("j33Nmax",self.j33Nmax.shape,dtype="i4") 
        dsetout[()]=self.j33Nmax        
        dsetout=groupout.create_dataset("j33Nmin",self.j33Nmin.shape,dtype="i4") 
        dsetout[()]=self.j33Nmin        
        dsetout=groupout.create_dataset("l12NNmax",self.l12NNmax.shape,dtype="i4") 
        dsetout[()]=self.l12NNmax        
        dsetout=groupout.create_dataset("l33Nmax",self.l33Nmax.shape,dtype="i4") 
        dsetout[()]=self.l33Nmax        
        dsetout=groupout.create_dataset("I33Nmax",self.I33Nmax.shape,dtype="i4") 
        dsetout[()]=self.I33Nmax        
        dsetout=groupout.create_dataset("mtau33Nmax",self.mtau33Nmax.shape,dtype="i4") 
        dsetout[()]=self.mtau33Nmax        
        dsetout=groupout.create_dataset("mtau33Nmin",self.mtau33Nmin.shape,dtype="i4") 
        dsetout[()]=self.mtau33Nmin        
        dsetout=groupout.create_dataset("pari3Nmax",self.pari3Nmax.shape,dtype="i4") 
        dsetout[()]=self.pari3Nmax        
        dsetout=groupout.create_dataset("pari3Nmin",self.pari3Nmin.shape,dtype="i4") 
        dsetout[()]=self.pari3Nmin        
        dsetout=groupout.create_dataset("tau33Nmin",self.tau33Nmin.shape,dtype="i4") 
        dsetout[()]=self.tau33Nmin
        dsetout=groupout.create_dataset("tau33Nmax",self.tau33Nmax.shape,dtype="i4") 
        dsetout[()]=self.tau33Nmax
    
        dsetout=groupout.create_dataset("qnalpha3N",self.qnalpha3N.shape,dtype="i4") 
        dsetout[()]=self.qnalpha3N        


        dsetout=groupout.create_dataset("alphaNNcdepmax",self.alphaNNcdepmax.shape,dtype="i4") 
        dsetout[()]=self.alphaNNcdepmax        
        dsetout=groupout.create_dataset("alphaNNmax",self.alphaNNmax.shape,dtype="i4") 
        dsetout[()]=self.alphaNNmax        
        dsetout=groupout.create_dataset("mt12NNmax",self.mt12NNmax.shape,dtype="i4") 
        dsetout[()]=self.mt12NNmax        
        dsetout=groupout.create_dataset("mt12NNmin",self.mt12NNmin.shape,dtype="i4") 
        dsetout[()]=self.mt12NNmin        

        dsetout=groupout.create_dataset("qnalphaNN",self.qnalphaNN.shape,dtype="i4") 
        dsetout[()]=self.qnalphaNN        
        

        # then read constants 
        dsetout=groupout.create_dataset("alpha_fein",self.alpha_fein.shape,dtype="f8") 
        dsetout[()]=self.alpha_fein        
        dsetout=groupout.create_dataset("m_eta",self.m_eta.shape,dtype="f8") 
        dsetout[()]=self.m_eta        
        dsetout=groupout.create_dataset("m_kaon",self.m_kaon.shape,dtype="f8") 
        dsetout[()]=self.m_kaon        
        dsetout=groupout.create_dataset("m_kaon0",self.m_kaon0.shape,dtype="f8") 
        dsetout[()]=self.m_kaon0        
        dsetout=groupout.create_dataset("m_kaonp",self.m_kaonp.shape,dtype="f8") 
        dsetout[()]=self.m_kaonp        
        dsetout=groupout.create_dataset("m_omega",self.m_omega.shape,dtype="f8") 
        dsetout[()]=self.m_omega        
        dsetout=groupout.create_dataset("m_pi",self.m_pi.shape,dtype="f8") 
        dsetout[()]=self.m_pi        
        dsetout=groupout.create_dataset("m_pi0",self.m_pi0.shape,dtype="f8") 
        dsetout[()]=self.m_pi0        
        dsetout=groupout.create_dataset("m_pip",self.m_pip.shape,dtype="f8") 
        dsetout[()]=self.m_pip        
        dsetout=groupout.create_dataset("m_rho",self.m_rho.shape,dtype="f8") 
        dsetout[()]=self.m_rho        
        dsetout=groupout.create_dataset("mlam",self.mlam.shape,dtype="f8") 
        dsetout[()]=self.mlam    
        dsetout=groupout.create_dataset("mneu",self.mneu.shape,dtype="f8") 
        dsetout[()]=self.mneu        
        dsetout=groupout.create_dataset("mnuc",self.mnuc.shape,dtype="f8") 
        dsetout[()]=self.mnuc        
        dsetout=groupout.create_dataset("mprot",self.mprot.shape,dtype="f8") 
        dsetout[()]=self.mprot    
        dsetout=groupout.create_dataset("msig0",self.msig0.shape,dtype="f8") 
        dsetout[()]=self.msig0    
        dsetout=groupout.create_dataset("msigm",self.msigm.shape,dtype="f8") 
        dsetout[()]=self.msigm        
        dsetout=groupout.create_dataset("msigp",self.msigp.shape,dtype="f8") 
        dsetout[()]=self.msigp        
        dsetout=groupout.create_dataset("mxi0",self.mxi0.shape,dtype="f8") 
        dsetout[()]=self.mxi0
        dsetout=groupout.create_dataset("mxiave",self.mxiave.shape,dtype="f8") 
        dsetout[()]=self.mxiave
        dsetout=groupout.create_dataset("mxim",self.mxim.shape,dtype="f8") 
        dsetout[()]=self.mxim
        dsetout=groupout.create_dataset("hbarc",self.hbarc.shape,dtype="f8") 
        dsetout[()]=self.hbarc


        # then grid points to FADCOMP
        meshname=list(self.meshtype)
        dsetout=groupout.create_dataset("meshtype",(len(meshname),),dtype="|S1") 
        dsetout[()]=meshname
        
        dsetout=groupout.create_dataset("p12n1",self.p12n1.shape,dtype="i4") 
        dsetout[()]=self.p12n1
        dsetout=groupout.create_dataset("p12n2",self.p12n2.shape,dtype="i4") 
        dsetout[()]=self.p12n2
        dsetout=groupout.create_dataset("p12ntot",self.p12ntot.shape,dtype="i4") 
        dsetout[()]=self.p12ntot

        dsetout=groupout.create_dataset("p12p1",self.p12a.shape,dtype="f8") 
        dsetout[()]=self.p12a
        dsetout=groupout.create_dataset("p12p2",self.p12b.shape,dtype="f8") 
        dsetout[()]=self.p12b
        dsetout=groupout.create_dataset("p12p3",self.p12c.shape,dtype="f8") 
        dsetout[()]=self.p12c
        

        dsetout=groupout.create_dataset("p12p",self.p12p.shape,dtype="f8") 
        dsetout[()]=self.p12p
        dsetout=groupout.create_dataset("p12w",self.p12w.shape,dtype="f8") 
        dsetout[()]=self.p12w

        dsetout=groupout.create_dataset("p3n1",self.p3n1.shape,dtype="i4") 
        dsetout[()]=self.p3n1
        dsetout=groupout.create_dataset("p3n2",self.p3n2.shape,dtype="i4") 
        dsetout[()]=self.p3n2
        dsetout=groupout.create_dataset("p3ntot",self.p3ntot.shape,dtype="i4") 
        dsetout[()]=self.p3ntot

        dsetout=groupout.create_dataset("p3p1",self.p3a.shape,dtype="f8") 
        dsetout[()]=self.p3a
        dsetout=groupout.create_dataset("p3p2",self.p3b.shape,dtype="f8") 
        dsetout[()]=self.p3b
        dsetout=groupout.create_dataset("p3p3",self.p3c.shape,dtype="f8") 
        dsetout[()]=self.p3c
        

        dsetout=groupout.create_dataset("p3p",self.p3p.shape,dtype="f8") 
        dsetout[()]=self.p3p
        dsetout=groupout.create_dataset("p3w",self.p3w.shape,dtype="f8") 
        dsetout[()]=self.p3w

        # write binding energy to FADCOMP group
        # write amplitude data set in compressed form
        dsetout=groupout.create_dataset("BENER",self.bener.shape,dtype="f8") 
        dsetout[()]=self.bener
        
        dsetout=groupout.create_dataset("3namp",self.fadcomp.shape,dtype="f4", **hdf5plugin.Zfp(accuracy=tolerance)) 
        dsetout[()]=self.fadcomp


        # now do same for wave function
        groupout=fileout.create_group('3NBOUNDWAVE') 

        # first bookkeeping to FADCOMP
        # parameters for info
        dsetout=groupout.create_dataset("alpha3Ncdepmax",self.alpha3Ncdepmax.shape,dtype="i4") 
        dsetout[()]=self.alpha3Ncdepmax        
        dsetout=groupout.create_dataset("alpha3Nmax",self.alpha3Nmax.shape,dtype="i4") 
        dsetout[()]=self.alpha3Nmax        
        dsetout=groupout.create_dataset("cdep3N",self.cdep3N.shape,dtype="i4") 
        dsetout[()]=self.cdep3N        
        dsetout=groupout.create_dataset("cdepNN",self.cdepNN.shape,dtype="i4") 
        dsetout[()]=self.cdepNN        
        dsetout=groupout.create_dataset("evenNN",self.evenNN.shape,dtype="i4") 
        dsetout[()]=self.evenNN        
        dsetout=groupout.create_dataset("j12NNmax",self.j12NNmax.shape,dtype="i4") 
        dsetout[()]=self.j12NNmax        
        dsetout=groupout.create_dataset("j33Nmax",self.j33Nmax.shape,dtype="i4") 
        dsetout[()]=self.j33Nmax        
        dsetout=groupout.create_dataset("j33Nmin",self.j33Nmin.shape,dtype="i4") 
        dsetout[()]=self.j33Nmin        
        dsetout=groupout.create_dataset("l12NNmax",self.l12NNmax.shape,dtype="i4") 
        dsetout[()]=self.l12NNmax        
        dsetout=groupout.create_dataset("l33Nmax",self.l33Nmax.shape,dtype="i4") 
        dsetout[()]=self.l33Nmax        
        dsetout=groupout.create_dataset("I33Nmax",self.I33Nmax.shape,dtype="i4") 
        dsetout[()]=self.I33Nmax        
        dsetout=groupout.create_dataset("mtau33Nmax",self.mtau33Nmax.shape,dtype="i4") 
        dsetout[()]=self.mtau33Nmax        
        dsetout=groupout.create_dataset("mtau33Nmin",self.mtau33Nmin.shape,dtype="i4") 
        dsetout[()]=self.mtau33Nmin        
        dsetout=groupout.create_dataset("pari3Nmax",self.pari3Nmax.shape,dtype="i4") 
        dsetout[()]=self.pari3Nmax        
        dsetout=groupout.create_dataset("pari3Nmin",self.pari3Nmin.shape,dtype="i4") 
        dsetout[()]=self.pari3Nmin        
        dsetout=groupout.create_dataset("tau33Nmin",self.tau33Nmin.shape,dtype="i4") 
        dsetout[()]=self.tau33Nmin
        dsetout=groupout.create_dataset("tau33Nmax",self.tau33Nmax.shape,dtype="i4") 
        dsetout[()]=self.tau33Nmax
    
        dsetout=groupout.create_dataset("qnalpha3N",self.qnalpha3N.shape,dtype="i4") 
        dsetout[()]=self.qnalpha3N        


        dsetout=groupout.create_dataset("alphaNNcdepmax",self.alphaNNcdepmax.shape,dtype="i4") 
        dsetout[()]=self.alphaNNcdepmax        
        dsetout=groupout.create_dataset("alphaNNmax",self.alphaNNmax.shape,dtype="i4") 
        dsetout[()]=self.alphaNNmax        
        dsetout=groupout.create_dataset("mt12NNmax",self.mt12NNmax.shape,dtype="i4") 
        dsetout[()]=self.mt12NNmax        
        dsetout=groupout.create_dataset("mt12NNmin",self.mt12NNmin.shape,dtype="i4") 
        dsetout[()]=self.mt12NNmin        
    
        dsetout=groupout.create_dataset("qnalphaNN",self.qnalphaNN.shape,dtype="i4") 
        dsetout[()]=self.qnalphaNN        
        

        # then read constants 
        dsetout=groupout.create_dataset("alpha_fein",self.alpha_fein.shape,dtype="f8") 
        dsetout[()]=self.alpha_fein        
        dsetout=groupout.create_dataset("m_eta",self.m_eta.shape,dtype="f8") 
        dsetout[()]=self.m_eta        
        dsetout=groupout.create_dataset("m_kaon",self.m_kaon.shape,dtype="f8") 
        dsetout[()]=self.m_kaon        
        dsetout=groupout.create_dataset("m_kaon0",self.m_kaon0.shape,dtype="f8") 
        dsetout[()]=self.m_kaon0        
        dsetout=groupout.create_dataset("m_kaonp",self.m_kaonp.shape,dtype="f8") 
        dsetout[()]=self.m_kaonp        
        dsetout=groupout.create_dataset("m_omega",self.m_omega.shape,dtype="f8") 
        dsetout[()]=self.m_omega        
        dsetout=groupout.create_dataset("m_pi",self.m_pi.shape,dtype="f8") 
        dsetout[()]=self.m_pi        
        dsetout=groupout.create_dataset("m_pi0",self.m_pi0.shape,dtype="f8") 
        dsetout[()]=self.m_pi0        
        dsetout=groupout.create_dataset("m_pip",self.m_pip.shape,dtype="f8") 
        dsetout[()]=self.m_pip        
        dsetout=groupout.create_dataset("m_rho",self.m_rho.shape,dtype="f8") 
        dsetout[()]=self.m_rho        
        dsetout=groupout.create_dataset("mlam",self.mlam.shape,dtype="f8") 
        dsetout[()]=self.mlam    
        dsetout=groupout.create_dataset("mneu",self.mneu.shape,dtype="f8") 
        dsetout[()]=self.mneu        
        dsetout=groupout.create_dataset("mnuc",self.mnuc.shape,dtype="f8") 
        dsetout[()]=self.mnuc        
        dsetout=groupout.create_dataset("mprot",self.mprot.shape,dtype="f8") 
        dsetout[()]=self.mprot    
        dsetout=groupout.create_dataset("msig0",self.msig0.shape,dtype="f8") 
        dsetout[()]=self.msig0    
        dsetout=groupout.create_dataset("msigm",self.msigm.shape,dtype="f8") 
        dsetout[()]=self.msigm        
        dsetout=groupout.create_dataset("msigp",self.msigp.shape,dtype="f8") 
        dsetout[()]=self.msigp        
        dsetout=groupout.create_dataset("mxi0",self.mxi0.shape,dtype="f8") 
        dsetout[()]=self.mxi0
        dsetout=groupout.create_dataset("mxiave",self.mxiave.shape,dtype="f8") 
        dsetout[()]=self.mxiave
        dsetout=groupout.create_dataset("mxim",self.mxim.shape,dtype="f8") 
        dsetout[()]=self.mxim
        dsetout=groupout.create_dataset("hbarc",self.hbarc.shape,dtype="f8") 
        dsetout[()]=self.hbarc


        # then grid points to FADCOMP
        meshname=list(self.meshtype)
        dsetout=groupout.create_dataset("meshtype",(len(meshname),),dtype="|S1") 
        dsetout[()]=meshname
        
        dsetout=groupout.create_dataset("p12n1",self.p12n1.shape,dtype="i4") 
        dsetout[()]=self.p12n1
        dsetout=groupout.create_dataset("p12n2",self.p12n2.shape,dtype="i4") 
        dsetout[()]=self.p12n2
        dsetout=groupout.create_dataset("p12ntot",self.p12ntot.shape,dtype="i4") 
        dsetout[()]=self.p12ntot

        dsetout=groupout.create_dataset("p12p1",self.p12a.shape,dtype="f8") 
        dsetout[()]=self.p12a
        dsetout=groupout.create_dataset("p12p2",self.p12b.shape,dtype="f8") 
        dsetout[()]=self.p12b
        dsetout=groupout.create_dataset("p12p3",self.p12c.shape,dtype="f8") 
        dsetout[()]=self.p12c
        

        dsetout=groupout.create_dataset("p12p",self.p12p.shape,dtype="f8") 
        dsetout[()]=self.p12p
        dsetout=groupout.create_dataset("p12w",self.p12w.shape,dtype="f8") 
        dsetout[()]=self.p12w

        dsetout=groupout.create_dataset("p3n1",self.p3n1.shape,dtype="i4") 
        dsetout[()]=self.p3n1
        dsetout=groupout.create_dataset("p3n2",self.p3n2.shape,dtype="i4") 
        dsetout[()]=self.p3n2
        dsetout=groupout.create_dataset("p3ntot",self.p3ntot.shape,dtype="i4") 
        dsetout[()]=self.p3ntot

        dsetout=groupout.create_dataset("p3p1",self.p3a.shape,dtype="f8") 
        dsetout[()]=self.p3a
        dsetout=groupout.create_dataset("p3p2",self.p3b.shape,dtype="f8") 
        dsetout[()]=self.p3b
        dsetout=groupout.create_dataset("p3p3",self.p3c.shape,dtype="f8") 
        dsetout[()]=self.p3c
        

        dsetout=groupout.create_dataset("p3p",self.p3p.shape,dtype="f8") 
        dsetout[()]=self.p3p
        dsetout=groupout.create_dataset("p3w",self.p3w.shape,dtype="f8") 
        dsetout[()]=self.p3w

        # write amplitude data set in compressed form        
        dsetout=groupout.create_dataset("3namp",self.wfunc.shape,dtype="f4", **hdf5plugin.Zfp(accuracy=tolerance)) 
        dsetout[()]=self.wfunc

        fileout.close()
        if printlevel>0:
          print("File size written:  {0:d}".format(os.path.getsize(filen_out)))

    def get_labels(self):
        """This method returns the available labels of the amplitude as necessary for a database access.
           Labels that are not stored in file are filled with zeros and need to be guessed from
           elsewhere. 
        """

        if(self.mtau33Nmax!=self.mtau33Nmin):
           raise ValueError("Non-unique mtau3.")
            
        if(self.mtau33Nmax==-1):
            Z=1
            N=2
        elif(self.mtau33Nmax==1):
            Z=2
            N=1
        else:
           raise ValueError("mtau3 is not well defined in 3N wave function.")
       
        standard_labels={'Z':Z,'N':N,
              'NP12A':self.p12n1, 'NP12B':self.p12n2, 'NP12':self.p12ntot, 'P12A':self.p12a, 'P12B':self.p12b,'P12C':self.p12c,
              'NP3A':self.p3n1, 'NP3B':self.p3n2, 'NP3':self.p3ntot, 'P3A':self.p3a, 'P3B':self.p3b,'P3C':self.p3c,
              'NP34A':0, 'NP34B':0, 'NP34':0, 'P34A':0, 'P34B':0,'P34C':0,
              'NQ4A':0, 'NQ4B':0, 'NQ4':0, 'Q4A':0, 'Q4B':0, 'Q4C':0,
              'NQA':0, 'NQB':0, 'NQ':0, 'QA':0, 'QB':0, 'QC':0,
              'NPTA':0, 'NPTB':0,'NPT':0, 'PTA':0, 'PTB':0, 'PTC':0,
              'NEA':0, 'NEB':0, 'NE':0, 'EA':0, 'EB':0, 'EC':0,
              'NX':0,
              'taumax':self.tau33Nmax, 'lsummax':0,'lmax':self.l33Nmax, 'j12max':self.j12NNmax,
              'l3max':self.l33Nmax,'l4max':0,'lammax':0,'MTtot':self.mtau33Nmax, 'Jtot':self.j33Nmax,
              'MODENN':'none', 'orderNN':'none','LambdaNN':0.0, 'potnr':0, 'empotnr':0,
              'lam3NF':0.0, 'c1':0.0, 'c3':0.0, 'c4':0.0, 'cd':0.0, 'ce':0.0,'cE1':0.0, 'cE3':0.0, 'tnforder':'no3nf','j12max3nf':0,'j3max3nf':0,
              'relcalc':0,
              'nnsrg':'none', 'tnfsrg':0, 'lambdaSRGNN':0.0,'lambdaSRG3N':0.0, 'potbareNN':0, 'potbareNNTNF':0, 'ostatSRGNN':0, 'ostatSRGTNF':0,
              'LambdaSRGNN':0.0, 'LambdaSRGTNF':0.0,}

        return standard_labels 
          
    
class wavefa4:
    """This class defines an object that allows to read a 4-He wave function file into numpy arrays
       and to compress the file."""
    def  __init__(self,filen_in,printlevel=0):
        """This opens a A=4 wave function file for reading and reads all info and prints simple statistics.
           Optional parameter printlevel controls amout of printout: 0 = none, 1 = limited, 2 = extensive 
        
           After using this method, the kinematics and data are properties of the objects
            --- see more detailed documentation for the definition of properties of the object
        """

        # read in wave function and calculate kinetic energy and norm for checking
        # open file 
        # assume that file only contains one density 
        # read this density and auxiliary fields 
        filein=h5py.File(filen_in, 'r')

        # first read bookkeeping
        # assume that grid and bookkeeping are the same for WF and Yakubovsky components
        # read the one of the wf
        group=filein['WF4N31']
        # for conversions use 
        self.hbarc=group['hbarc'][()]

        # book parameters for info
        self.alpha3Ncdepmax=group['alpha3Ncdepmax'][()]
        self.alpha3Nmax=group['alpha3Nmax'][()]
        self.cdep3N=group['cdep3N'][()]
        self.cdepNN=group['cdepNN'][()]
        self.evenNN=group['evenNN'][()]
        self.j12NNmax=group['j12NNmax'][()]
        self.j33Nmax=group['j33Nmax'][()]
        self.j33Nmin=group['j33Nmin'][()]
        self.l12NNmax=group['l12NNmax'][()]
        self.l33Nmax=group['l33Nmax'][()]
        self.I33Nmax=group['I33Nmax'][()]
        self.mtau33Nmax=group['mtau33Nmax'][()]
        self.mtau33Nmin=group['mtau33Nmin'][()]
        self.pari3Nmax=group['pari3Nmax'][()]
        self.pari3Nmin=group['pari3Nmin'][()]
        self.tau33Nmax=group['tau33Nmax'][()]
        self.tau33Nmin=group['tau33Nmin'][()]

        self.qnalpha3N=group['qnalpha3N'][()]
        
        self.alphaNNcdepmax=group['alphaNNcdepmax'][()]
        self.alphaNNmax=group['alphaNNmax'][()]
        self.mt12NNmax=group['mt12NNmax'][()]
        self.mt12NNmin=group['mt12NNmin'][()]

        self.qnalphaNN=group['qnalphaNN'][()]

        self.alpha4N31cdepmax=group['alpha4N31cdepmax'][()]
        self.alpha4N31max=group['alpha4N31max'][()]
        self.cdep4N=group['cdep4N'][()]
        self.I44N31Nmax=group['I44N31Nmax'][()]
        self.j44N31max=group['j44N31max'][()]
        self.j44N31min=group['j44N31min'][()]
        self.l44N31max=group['l44N31max'][()]
        self.lsummax4N31=group['lsummax4N31'][()]
        self.mtau44N31Nmin=group['mtau44N31Nmin'][()]
        self.mtau44N31max=group['mtau44N31max'][()]
        self.pari4N31max=group['pari4N31max'][()]
        self.pari4N31min=group['pari4N31min'][()]
        self.tau44N31Nmax=group['tau44N31Nmax'][()]
        self.tau44N31Nmin=group['tau44N31Nmin'][()]

        self.qnalpha4N31=group['qnalpha4N31'][()]
        
        if printlevel>0:
          print('Number of 4N31 channels:   {0:d}  {1:d}\n'.format(self.alpha4N31max,self.alpha4N31cdepmax))
          print('Number of 3N channels:   {0:d}  {1:d}\n'.format(self.alpha3Nmax,self.alpha3Ncdepmax))
          print('Number of 2N channels:   {0:d}  {1:d}\n'.format(self.alphaNNmax,self.alphaNNcdepmax))

        if printlevel>1:  
          print('4N31 channels:\n')
          print("{0:>5s} {1:>3s} {2:>3s} {3:>3s} {4:>3s} {5:>3s} {6:>3s} {7:>3s} {8:>5s} {9:>3s} {10:>3s} {11:>3s} {12:>5s} {13:>5s}  {14:>7s} {15:>7s} {16:>7s}".format(
                 "alpha","l12",   "s12",  "j12",  "t12",  "l3",   "I3",    "j3",  "tau3",  "l4",   "I4",   "j4",    "tau4",  "mtau4","alphaNN","alpha3N","pari"))
          for alpha in range(self.alpha4N31cdepmax):
            print("{0:5d} {1:3d} {2:3d} {3:3d} {4:3d} {5:3d} {6:3d} {7:3d} {8:5d} {9:3d} {10:3d} {11:3d} {12:5d} {13:5d}  {14:7d} {15:7d} {16:7d}".format(alpha,
                   self.qnalpha4N31[alpha,0],self.qnalpha4N31[alpha,1],self.qnalpha4N31[alpha,2],
                   self.qnalpha4N31[alpha,3],self.qnalpha4N31[alpha,4],self.qnalpha4N31[alpha,5],
                   self.qnalpha4N31[alpha,6],self.qnalpha4N31[alpha,7],self.qnalpha4N31[alpha,8],
                   self.qnalpha4N31[alpha,9],self.qnalpha4N31[alpha,10],self.qnalpha4N31[alpha,11],
                   self.qnalpha4N31[alpha,12],self.qnalpha4N31[alpha,13],self.qnalpha4N31[alpha,14],
                   self.qnalpha4N31[alpha,15]))
            
        if printlevel>2:  
          print('3N channels:\n')
          print("{0:>5s} {1:>3s} {2:>3s} {3:>3s} {4:>3s} {5:>3s} {6:>3s} {7:>3s} {8:>5s} {9:>5s} {10:>7s} {11:>5s}".format(
          "alpha","l12","s12","j12","t12","l3","I3","j3","tau3","mtau3","alphaNN","pari"))
          for alpha in range(self.alpha3Ncdepmax):
            print("{0:5d} {1:3d} {2:3d} {3:3d} {4:3d} {5:3d} {6:3d} {7:3d} {8:5d} {9:5d} {10:7d} {11:5d}".format(alpha,
                   self.qnalpha3N[alpha,0],self.qnalpha3N[alpha,1],self.qnalpha3N[alpha,2],
                   self.qnalpha3N[alpha,3],self.qnalpha3N[alpha,4],self.qnalpha3N[alpha,5],
                   self.qnalpha3N[alpha,6],self.qnalpha3N[alpha,7],self.qnalpha3N[alpha,8],
                   self.qnalpha3N[alpha,9],self.qnalpha3N[alpha,10]))
            
        if printlevel>2:  
          print('NN channels:\n')
          print("{0:>5s} {1:>3s} {2:>3s} {3:>3s} {4:>3s} {5:>4s}".format(
          "alpha","l12","s12","j12","t12","mt12"))
          for alpha in range(self.alphaNNcdepmax):
            print("{0:5d} {1:3d} {2:3d} {3:3d} {4:3d} {5:4d} ".format(alpha,
                   self.qnalphaNN[alpha,0],self.qnalphaNN[alpha,1],self.qnalphaNN[alpha,2],
                   self.qnalphaNN[alpha,3],self.qnalphaNN[alpha,4]))

            
        # read constants 
        self.alpha_fein=group['alpha_fein'][()]
        self.m_eta=group['m_eta'][()]
        self.m_kaon=group['m_kaon'][()]
        self.m_kaon0=group['m_kaon0'][()]
        self.m_kaonp=group['m_kaonp'][()]
        self.m_omega=group['m_omega'][()]
        self.m_pi=group['m_pi'][()]
        self.m_pi0=group['m_pi0'][()]
        self.m_pip=group['m_pip'][()]
        self.m_rho=group['m_rho'][()]
        self.mlam=group['mlam'][()]
        self.mneu=group['mneu'][()]
        self.mnuc=group['mnuc'][()]
        self.mprot=group['mprot'][()]
        self.msig0=group['msig0'][()]
        self.msigm=group['msigm'][()]
        self.msigp=group['msigp'][()]
        self.mxi0=group['mxi0'][()]
        self.mxiave=group['mxiave'][()]
        self.mxim=group['mxim'][()]


        # now read and print mesh parameters 
        self.meshtype=''.join(list(map(lambda x: x.decode('utf-8'), group['meshtype'][()]))).strip()
        self.p12n1=group['p12n1'][()]
        self.p12n2=group['p12n2'][()]
        self.p12ntot=group['p12ntot'][()]

        self.p12a=group['p12p1'][()]
        self.p12b=group['p12p2'][()]
        self.p12c=group['p12p3'][()]

        self.p12p=group['p12p'][()]
        self.p12w=group['p12w'][()]

        self.p3n1=group['p3n1'][()]
        self.p3n2=group['p3n2'][()]
        self.p3ntot=group['p3ntot'][()]

        self.p3a=group['p3p1'][()]
        self.p3b=group['p3p2'][()]
        self.p3c=group['p3p3'][()]

        self.p3p=group['p3p'][()]
        self.p3w=group['p3w'][()]

        self.q4n1=group['q4n1'][()]
        self.q4n2=group['q4n2'][()]
        self.q4ntot=group['q4ntot'][()]

        self.q4a=group['q4p1'][()]
        self.q4b=group['q4p2'][()]
        self.q4c=group['q4p3'][()]

        self.q4p=group['q4p'][()]
        self.q4w=group['q4w'][()]
        

        if printlevel>0:
          print("MESHTYPE: {0:s}".format(self.meshtype))
          print("NP12:     {0:d} {1:d}  {2:d} ".format(self.p12n1,self.p12n2,self.p12ntot))
          print("P12:      {0:15.6e}  {1:15.6e}  {2:15.6e} \n ".format(self.p12a,self.p12b,self.p12c))
        if printlevel>1:
          print("Grid points: \n")
          for ip in range(self.p12ntot):
            print("P12MESH:   {0:15.6e} {1:15.6e}".format(self.p12p[ip],self.p12w[ip]))

        if printlevel>0:
          print("NP3:     {0:d} {1:d}  {2:d} ".format(self.p3n1,self.p3n2,self.p3ntot))
          print("P3:      {0:15.6e}  {1:15.6e}  {2:15.6e} \n ".format(self.p3a,self.p3b,self.p3c))
        if printlevel>1:
          print("Grid points: \n")
          for ip in range(self.p3ntot):
            print("P3MESH:   {0:15.6e} {1:15.6e}".format(self.p3p[ip],self.p3w[ip]))

        if printlevel>0:
          print("NQ4:     {0:d} {1:d}  {2:d} ".format(self.q4n1,self.q4n2,self.q4ntot))
          print("Q4:      {0:15.6e}  {1:15.6e}  {2:15.6e} \n ".format(self.q4a,self.q4b,self.q4c))
        if printlevel>1:
          print("Grid points: \n")
          for ip in range(self.q4ntot):
            print("Q4MESH:   {0:15.6e} {1:15.6e}".format(self.q4p[ip],self.q4w[ip]))
            
        self.wf4n31=group['4n31amp'][()]
        

        # now read additional fields for YAK4N31 component

        group=filein['YAK4N31']
        self.yak4n31=group['4n31amp'][()]
        self.bener=group['BENER'][()]

        # and then for wave function in 4N22 coordinates 
        # assume that grid and bookkeeping are the same for WF and Yakubovsky components
        # read the one of the wf
        group=filein['WF4N22']

        # book parameters for info
        
        self.beta4N22cdepmax=group['beta4N22cdepmax'][()]
        self.beta4N22max=group['beta4N22max'][()]
        self.cdep4N=group['cdep4N'][()]
        self.I4N22max=group['I4N22max'][()]
        self.j44N22max=group['j44N22max'][()]
        self.j44N22min=group['j44N22min'][()]
        self.lam4N22max=group['lam4N22max'][()]
        self.lsummax4N22=group['lsummax4N22'][()]
        self.mtau44N22max=group['mtau44N22max'][()]
        self.mtau44N22min=group['mtau44N22min'][()]
        self.pari4N22max=group['pari4N22max'][()]
        self.pari4N22min=group['pari4N22min'][()]
        self.tau44N22max=group['tau44N22max'][()]
        self.tau44N22min=group['tau44N22min'][()]

        self.qnbeta4N22=group['qnbeta4N22'][()]
        
        if printlevel>0:
          print('Number of 4N22 channels:   {0:d}  {1:d}\n'.format(self.beta4N22max,self.beta4N22cdepmax))

        if printlevel>1:  
          print('4N22 channels:\n')
          print("{0:>5s} {1:>3s} {2:>3s} {3:>3s} {4:>3s} {5:>3s} {6:>3s} {7:>3s} {8:>5s} {9:>3s} {10:>3s} {11:>3s} {12:>5s} {13:>5s}  {14:>9s} {15:>9s} {16:>7s}".format(
                 "alpha","l12",   "s12",  "j12",  "t12",  "l34",   "s34",    "j34",   "t34",  "lam",   "I",   "j4",    "tau4",  "mtau4","alphaNN12","alphaNN34","pari"))
          for alpha in range(self.beta4N22cdepmax):
            print("{0:5d} {1:3d} {2:3d} {3:3d} {4:3d} {5:3d} {6:3d} {7:3d} {8:5d} {9:3d} {10:3d} {11:3d} {12:5d} {13:5d}  {14:7d} {15:7d} {16:7d}".format(alpha,
                   self.qnbeta4N22[alpha,0],self.qnbeta4N22[alpha,1],self.qnbeta4N22[alpha,2],
                   self.qnbeta4N22[alpha,3],self.qnbeta4N22[alpha,4],self.qnbeta4N22[alpha,5],
                   self.qnbeta4N22[alpha,6],self.qnbeta4N22[alpha,7],self.qnbeta4N22[alpha,8],
                   self.qnbeta4N22[alpha,9],self.qnbeta4N22[alpha,10],self.qnbeta4N22[alpha,11],
                   self.qnbeta4N22[alpha,12],self.qnbeta4N22[alpha,13],self.qnbeta4N22[alpha,14],
                   self.qnbeta4N22[alpha,15]))
            
        # now read and print mesh parameters 
        self.p34n1=group['p34n1'][()]
        self.p34n2=group['p34n2'][()]
        self.p34ntot=group['p34ntot'][()]

        self.p34a=group['p34p1'][()]
        self.p34b=group['p34p2'][()]
        self.p34c=group['p34p3'][()]

        self.p34p=group['p34p'][()]
        self.p34w=group['p34w'][()]

        self.qn1=group['qn1'][()]
        self.qn2=group['qn2'][()]
        self.qntot=group['qntot'][()]

        self.qa=group['qp1'][()]
        self.qb=group['qp2'][()]
        self.qc=group['qp3'][()]

        self.qp=group['qp'][()]
        self.qw=group['qw'][()]
        

        if printlevel>0:
          print("MESHTYPE: {0:s}".format(self.meshtype))
          print("NP34:     {0:d} {1:d}  {2:d} ".format(self.p34n1,self.p34n2,self.p34ntot))
          print("P34:      {0:15.6e}  {1:15.6e}  {2:15.6e} \n ".format(self.p34a,self.p34b,self.p34c))
        if printlevel>1:
          print("Grid points: \n")
          for ip in range(self.p34ntot):
            print("P34MESH:   {0:15.6e} {1:15.6e}".format(self.p34p[ip],self.p34w[ip]))

        if printlevel>0:
          print("NQ:     {0:d} {1:d}  {2:d} ".format(self.qn1,self.qn2,self.qntot))
          print("Q:      {0:15.6e}  {1:15.6e}  {2:15.6e} \n ".format(self.qa,self.qb,self.qc))
        if printlevel>1:
          print("Grid points: \n")
          for ip in range(self.qntot):
            print("QMESH:   {0:15.6e} {1:15.6e}".format(self.qp[ip],self.qw[ip]))
            
        self.wf4n22=group['4n22amp'][()]

        # now read additional fields for Yakubovsky component in 4n22
        group=filein['YAK4N22']
        self.yak4n22=group['4n22amp'][()]

        
        # integrate to get norm and kinetic energy  
        
        norm=(12*np.einsum("ijklm,ijklm,l,k,j->",self.yak4n31,self.wf4n31,self.p12p**2*self.p12w, self.p3p**2*self.p3w,   self.q4p**2*self.q4w)
             +6*np.einsum("ijklm,ijklm,l,k,j->",self.yak4n22,self.wf4n22, self.p12p**2*self.p12w, self.p34p**2*self.p34w, self.qp**2*self.qw))

        ekin=(12*np.einsum("ijklm,ijklm,l,k,j->",self.yak4n31,self.wf4n31,self.p12p**4*self.p12w, self.p3p**2*self.p3w,   self.q4p**2*self.q4w)/self.mnuc
             +6*np.einsum("ijklm,ijklm,l,k,j->",self.yak4n22,self.wf4n22, self.p12p**4*self.p12w, self.p34p**2*self.p34w, self.qp**2*self.qw)/self.mnuc
             +12*np.einsum("ijklm,ijklm,l,k,j->",self.yak4n31,self.wf4n31,self.p12p**2*self.p12w, self.p3p**4*self.p3w,   self.q4p**2*self.q4w)*0.75/self.mnuc
             +6*np.einsum("ijklm,ijklm,l,k,j->",self.yak4n22,self.wf4n22, self.p12p**2*self.p12w, self.p34p**4*self.p34w, self.qp**2*self.qw)/self.mnuc
             +12*np.einsum("ijklm,ijklm,l,k,j->",self.yak4n31,self.wf4n31,self.p12p**2*self.p12w, self.p3p**2*self.p3w,   self.q4p**4*self.q4w)*2.0/(3.0*self.mnuc)
             +6*np.einsum("ijklm,ijklm,l,k,j->",self.yak4n22,self.wf4n22, self.p12p**2*self.p12w, self.p34p**2*self.p34w, self.qp**4*self.qw)*0.5/self.mnuc)
        
        if printlevel>0:
          print("NORM/EKIN:  {0:15.6e} {1:15.6e}".format(norm,ekin*self.hbarc))

        filein.close()
        if printlevel>0:
          print("File size read:  {0:d}".format(os.path.getsize(filen_in)))
        

    def compress(self,filen_out,tolerance,printlevel=0):
        """This method write the current data in compressed form to the new file file_out using
           ZFP compression with accuracy tolerance. Optional parameter printlevel controls printout."""
    
        fileout=h5py.File(filen_out, 'w')
        
        # write all entries from self object
        # start with wave function in 4N31 coordinates
        groupout=fileout.create_group('WF4N31')
        # first bookkeeping to 4N31 wf 
        # parameters for info
        dsetout=groupout.create_dataset("alpha3Ncdepmax",self.alpha3Ncdepmax.shape,dtype="i4") 
        dsetout[()]=self.alpha3Ncdepmax        
        dsetout=groupout.create_dataset("alpha3Nmax",self.alpha3Nmax.shape,dtype="i4") 
        dsetout[()]=self.alpha3Nmax        
        dsetout=groupout.create_dataset("cdep3N",self.cdep3N.shape,dtype="i4") 
        dsetout[()]=self.cdep3N        
        dsetout=groupout.create_dataset("cdepNN",self.cdepNN.shape,dtype="i4") 
        dsetout[()]=self.cdepNN        
        dsetout=groupout.create_dataset("evenNN",self.evenNN.shape,dtype="i4") 
        dsetout[()]=self.evenNN        
        dsetout=groupout.create_dataset("j12NNmax",self.j12NNmax.shape,dtype="i4") 
        dsetout[()]=self.j12NNmax        
        dsetout=groupout.create_dataset("j33Nmax",self.j33Nmax.shape,dtype="i4") 
        dsetout[()]=self.j33Nmax        
        dsetout=groupout.create_dataset("j33Nmin",self.j33Nmin.shape,dtype="i4") 
        dsetout[()]=self.j33Nmin        
        dsetout=groupout.create_dataset("l12NNmax",self.l12NNmax.shape,dtype="i4") 
        dsetout[()]=self.l12NNmax        
        dsetout=groupout.create_dataset("l33Nmax",self.l33Nmax.shape,dtype="i4") 
        dsetout[()]=self.l33Nmax        
        dsetout=groupout.create_dataset("I33Nmax",self.I33Nmax.shape,dtype="i4") 
        dsetout[()]=self.I33Nmax        
        dsetout=groupout.create_dataset("mtau33Nmax",self.mtau33Nmax.shape,dtype="i4") 
        dsetout[()]=self.mtau33Nmax        
        dsetout=groupout.create_dataset("mtau33Nmin",self.mtau33Nmin.shape,dtype="i4") 
        dsetout[()]=self.mtau33Nmin        
        dsetout=groupout.create_dataset("pari3Nmax",self.pari3Nmax.shape,dtype="i4") 
        dsetout[()]=self.pari3Nmax        
        dsetout=groupout.create_dataset("pari3Nmin",self.pari3Nmin.shape,dtype="i4") 
        dsetout[()]=self.pari3Nmin        
        dsetout=groupout.create_dataset("tau33Nmin",self.tau33Nmin.shape,dtype="i4") 
        dsetout[()]=self.tau33Nmin
        dsetout=groupout.create_dataset("tau33Nmax",self.tau33Nmax.shape,dtype="i4") 
        dsetout[()]=self.tau33Nmax
    
        dsetout=groupout.create_dataset("qnalpha3N",self.qnalpha3N.shape,dtype="i4") 
        dsetout[()]=self.qnalpha3N        


        dsetout=groupout.create_dataset("alphaNNcdepmax",self.alphaNNcdepmax.shape,dtype="i4") 
        dsetout[()]=self.alphaNNcdepmax        
        dsetout=groupout.create_dataset("alphaNNmax",self.alphaNNmax.shape,dtype="i4") 
        dsetout[()]=self.alphaNNmax        
        dsetout=groupout.create_dataset("mt12NNmax",self.mt12NNmax.shape,dtype="i4") 
        dsetout[()]=self.mt12NNmax        
        dsetout=groupout.create_dataset("mt12NNmin",self.mt12NNmin.shape,dtype="i4") 
        dsetout[()]=self.mt12NNmin        

        dsetout=groupout.create_dataset("qnalphaNN",self.qnalphaNN.shape,dtype="i4") 
        dsetout[()]=self.qnalphaNN        

        dsetout=groupout.create_dataset("I44N31Nmax",self.I44N31Nmax.shape,dtype="i4") 
        dsetout[()]=self.I44N31Nmax        
        dsetout=groupout.create_dataset("alpha4N31cdepmax",self.alpha4N31cdepmax.shape,dtype="i4") 
        dsetout[()]=self.alpha4N31cdepmax        
        dsetout=groupout.create_dataset("alpha4N31max",self.alpha4N31max.shape,dtype="i4") 
        dsetout[()]=self.alpha4N31max        
        dsetout=groupout.create_dataset("cdep4N",self.cdep4N.shape,dtype="i4") 
        dsetout[()]=self.cdep4N        
        dsetout=groupout.create_dataset("j44N31max",self.j44N31max.shape,dtype="i4") 
        dsetout[()]=self.j44N31max        
        dsetout=groupout.create_dataset("j44N31min",self.j44N31min.shape,dtype="i4") 
        dsetout[()]=self.j44N31min        
        dsetout=groupout.create_dataset("l44N31max",self.l44N31max.shape,dtype="i4") 
        dsetout[()]=self.l44N31max        
        dsetout=groupout.create_dataset("lsummax4N31",self.lsummax4N31.shape,dtype="i4") 
        dsetout[()]=self.lsummax4N31        
        dsetout=groupout.create_dataset("mtau44N31Nmin",self.mtau44N31Nmin.shape,dtype="i4") 
        dsetout[()]=self.mtau44N31Nmin        
        dsetout=groupout.create_dataset("mtau44N31max",self.mtau44N31max.shape,dtype="i4") 
        dsetout[()]=self.mtau44N31max        
        dsetout=groupout.create_dataset("pari4N31max",self.pari4N31max.shape,dtype="i4") 
        dsetout[()]=self.pari4N31max        
        dsetout=groupout.create_dataset("pari4N31min",self.pari4N31min.shape,dtype="i4") 
        dsetout[()]=self.pari4N31min        
        dsetout=groupout.create_dataset("tau44N31Nmax",self.tau44N31Nmax.shape,dtype="i4") 
        dsetout[()]=self.tau44N31Nmax        
        dsetout=groupout.create_dataset("tau44N31Nmin",self.tau44N31Nmin.shape,dtype="i4") 
        dsetout[()]=self.tau44N31Nmin

        dsetout=groupout.create_dataset("qnalpha4N31",self.qnalpha4N31.shape,dtype="i4") 
        dsetout[()]=self.qnalpha4N31        
        


        # then read constants 
        dsetout=groupout.create_dataset("alpha_fein",self.alpha_fein.shape,dtype="f8") 
        dsetout[()]=self.alpha_fein        
        dsetout=groupout.create_dataset("m_eta",self.m_eta.shape,dtype="f8") 
        dsetout[()]=self.m_eta        
        dsetout=groupout.create_dataset("m_kaon",self.m_kaon.shape,dtype="f8") 
        dsetout[()]=self.m_kaon        
        dsetout=groupout.create_dataset("m_kaon0",self.m_kaon0.shape,dtype="f8") 
        dsetout[()]=self.m_kaon0        
        dsetout=groupout.create_dataset("m_kaonp",self.m_kaonp.shape,dtype="f8") 
        dsetout[()]=self.m_kaonp        
        dsetout=groupout.create_dataset("m_omega",self.m_omega.shape,dtype="f8") 
        dsetout[()]=self.m_omega        
        dsetout=groupout.create_dataset("m_pi",self.m_pi.shape,dtype="f8") 
        dsetout[()]=self.m_pi        
        dsetout=groupout.create_dataset("m_pi0",self.m_pi0.shape,dtype="f8") 
        dsetout[()]=self.m_pi0        
        dsetout=groupout.create_dataset("m_pip",self.m_pip.shape,dtype="f8") 
        dsetout[()]=self.m_pip        
        dsetout=groupout.create_dataset("m_rho",self.m_rho.shape,dtype="f8") 
        dsetout[()]=self.m_rho        
        dsetout=groupout.create_dataset("mlam",self.mlam.shape,dtype="f8") 
        dsetout[()]=self.mlam    
        dsetout=groupout.create_dataset("mneu",self.mneu.shape,dtype="f8") 
        dsetout[()]=self.mneu        
        dsetout=groupout.create_dataset("mnuc",self.mnuc.shape,dtype="f8") 
        dsetout[()]=self.mnuc        
        dsetout=groupout.create_dataset("mprot",self.mprot.shape,dtype="f8") 
        dsetout[()]=self.mprot    
        dsetout=groupout.create_dataset("msig0",self.msig0.shape,dtype="f8") 
        dsetout[()]=self.msig0    
        dsetout=groupout.create_dataset("msigm",self.msigm.shape,dtype="f8") 
        dsetout[()]=self.msigm        
        dsetout=groupout.create_dataset("msigp",self.msigp.shape,dtype="f8") 
        dsetout[()]=self.msigp        
        dsetout=groupout.create_dataset("mxi0",self.mxi0.shape,dtype="f8") 
        dsetout[()]=self.mxi0
        dsetout=groupout.create_dataset("mxiave",self.mxiave.shape,dtype="f8") 
        dsetout[()]=self.mxiave
        dsetout=groupout.create_dataset("mxim",self.mxim.shape,dtype="f8") 
        dsetout[()]=self.mxim
        dsetout=groupout.create_dataset("hbarc",self.hbarc.shape,dtype="f8") 
        dsetout[()]=self.hbarc


        # then grid points to FADCOMP
        meshname=list(self.meshtype)
        dsetout=groupout.create_dataset("meshtype",(len(meshname),),dtype="|S1") 
        dsetout[()]=meshname
        
        dsetout=groupout.create_dataset("p12n1",self.p12n1.shape,dtype="i4") 
        dsetout[()]=self.p12n1
        dsetout=groupout.create_dataset("p12n2",self.p12n2.shape,dtype="i4") 
        dsetout[()]=self.p12n2
        dsetout=groupout.create_dataset("p12ntot",self.p12ntot.shape,dtype="i4") 
        dsetout[()]=self.p12ntot

        dsetout=groupout.create_dataset("p12p1",self.p12a.shape,dtype="f8") 
        dsetout[()]=self.p12a
        dsetout=groupout.create_dataset("p12p2",self.p12b.shape,dtype="f8") 
        dsetout[()]=self.p12b
        dsetout=groupout.create_dataset("p12p3",self.p12c.shape,dtype="f8") 
        dsetout[()]=self.p12c
        

        dsetout=groupout.create_dataset("p12p",self.p12p.shape,dtype="f8") 
        dsetout[()]=self.p12p
        dsetout=groupout.create_dataset("p12w",self.p12w.shape,dtype="f8") 
        dsetout[()]=self.p12w

        dsetout=groupout.create_dataset("p3n1",self.p3n1.shape,dtype="i4") 
        dsetout[()]=self.p3n1
        dsetout=groupout.create_dataset("p3n2",self.p3n2.shape,dtype="i4") 
        dsetout[()]=self.p3n2
        dsetout=groupout.create_dataset("p3ntot",self.p3ntot.shape,dtype="i4") 
        dsetout[()]=self.p3ntot

        dsetout=groupout.create_dataset("p3p1",self.p3a.shape,dtype="f8") 
        dsetout[()]=self.p3a
        dsetout=groupout.create_dataset("p3p2",self.p3b.shape,dtype="f8") 
        dsetout[()]=self.p3b
        dsetout=groupout.create_dataset("p3p3",self.p3c.shape,dtype="f8") 
        dsetout[()]=self.p3c
        

        dsetout=groupout.create_dataset("p3p",self.p3p.shape,dtype="f8") 
        dsetout[()]=self.p3p
        dsetout=groupout.create_dataset("p3w",self.p3w.shape,dtype="f8") 
        dsetout[()]=self.p3w

        dsetout=groupout.create_dataset("q4n1",self.q4n1.shape,dtype="i4") 
        dsetout[()]=self.q4n1
        dsetout=groupout.create_dataset("q4n2",self.q4n2.shape,dtype="i4") 
        dsetout[()]=self.q4n2
        dsetout=groupout.create_dataset("q4ntot",self.q4ntot.shape,dtype="i4") 
        dsetout[()]=self.q4ntot

        dsetout=groupout.create_dataset("q4p1",self.q4a.shape,dtype="f8") 
        dsetout[()]=self.q4a
        dsetout=groupout.create_dataset("q4p2",self.q4b.shape,dtype="f8") 
        dsetout[()]=self.q4b
        dsetout=groupout.create_dataset("q4p3",self.q4c.shape,dtype="f8") 
        dsetout[()]=self.q4c
        

        dsetout=groupout.create_dataset("q4p",self.q4p.shape,dtype="f8") 
        dsetout[()]=self.q4p
        dsetout=groupout.create_dataset("q4w",self.q4w.shape,dtype="f8") 
        dsetout[()]=self.q4w
        
        # write amplitude data set in compressed form
        
        dsetout=groupout.create_dataset("4n31amp",self.wf4n31.shape,dtype="f4", **hdf5plugin.Zfp(accuracy=tolerance)) 
        dsetout[()]=self.wf4n31
        
        # now do same for the 4N31 Yakubovsky component
        groupout=fileout.create_group('YAK4N31') 

        # first bookkeeping 
        # parameters for info
        dsetout=groupout.create_dataset("alpha3Ncdepmax",self.alpha3Ncdepmax.shape,dtype="i4") 
        dsetout[()]=self.alpha3Ncdepmax        
        dsetout=groupout.create_dataset("alpha3Nmax",self.alpha3Nmax.shape,dtype="i4") 
        dsetout[()]=self.alpha3Nmax        
        dsetout=groupout.create_dataset("cdep3N",self.cdep3N.shape,dtype="i4") 
        dsetout[()]=self.cdep3N        
        dsetout=groupout.create_dataset("cdepNN",self.cdepNN.shape,dtype="i4") 
        dsetout[()]=self.cdepNN        
        dsetout=groupout.create_dataset("evenNN",self.evenNN.shape,dtype="i4") 
        dsetout[()]=self.evenNN        
        dsetout=groupout.create_dataset("j12NNmax",self.j12NNmax.shape,dtype="i4") 
        dsetout[()]=self.j12NNmax        
        dsetout=groupout.create_dataset("j33Nmax",self.j33Nmax.shape,dtype="i4") 
        dsetout[()]=self.j33Nmax        
        dsetout=groupout.create_dataset("j33Nmin",self.j33Nmin.shape,dtype="i4") 
        dsetout[()]=self.j33Nmin        
        dsetout=groupout.create_dataset("l12NNmax",self.l12NNmax.shape,dtype="i4") 
        dsetout[()]=self.l12NNmax        
        dsetout=groupout.create_dataset("l33Nmax",self.l33Nmax.shape,dtype="i4") 
        dsetout[()]=self.l33Nmax        
        dsetout=groupout.create_dataset("I33Nmax",self.I33Nmax.shape,dtype="i4") 
        dsetout[()]=self.I33Nmax        
        dsetout=groupout.create_dataset("mtau33Nmax",self.mtau33Nmax.shape,dtype="i4") 
        dsetout[()]=self.mtau33Nmax        
        dsetout=groupout.create_dataset("mtau33Nmin",self.mtau33Nmin.shape,dtype="i4") 
        dsetout[()]=self.mtau33Nmin        
        dsetout=groupout.create_dataset("pari3Nmax",self.pari3Nmax.shape,dtype="i4") 
        dsetout[()]=self.pari3Nmax        
        dsetout=groupout.create_dataset("pari3Nmin",self.pari3Nmin.shape,dtype="i4") 
        dsetout[()]=self.pari3Nmin        
        dsetout=groupout.create_dataset("tau33Nmin",self.tau33Nmin.shape,dtype="i4") 
        dsetout[()]=self.tau33Nmin
        dsetout=groupout.create_dataset("tau33Nmax",self.tau33Nmax.shape,dtype="i4") 
        dsetout[()]=self.tau33Nmax
    
        dsetout=groupout.create_dataset("qnalpha3N",self.qnalpha3N.shape,dtype="i4") 
        dsetout[()]=self.qnalpha3N        


        dsetout=groupout.create_dataset("alphaNNcdepmax",self.alphaNNcdepmax.shape,dtype="i4") 
        dsetout[()]=self.alphaNNcdepmax        
        dsetout=groupout.create_dataset("alphaNNmax",self.alphaNNmax.shape,dtype="i4") 
        dsetout[()]=self.alphaNNmax        
        dsetout=groupout.create_dataset("mt12NNmax",self.mt12NNmax.shape,dtype="i4") 
        dsetout[()]=self.mt12NNmax        
        dsetout=groupout.create_dataset("mt12NNmin",self.mt12NNmin.shape,dtype="i4") 
        dsetout[()]=self.mt12NNmin        
    
        dsetout=groupout.create_dataset("qnalphaNN",self.qnalphaNN.shape,dtype="i4") 
        dsetout[()]=self.qnalphaNN        
        
        dsetout=groupout.create_dataset("I44N31Nmax",self.I44N31Nmax.shape,dtype="i4") 
        dsetout[()]=self.I44N31Nmax        
        dsetout=groupout.create_dataset("alpha4N31cdepmax",self.alpha4N31cdepmax.shape,dtype="i4") 
        dsetout[()]=self.alpha4N31cdepmax        
        dsetout=groupout.create_dataset("alpha4N31max",self.alpha4N31max.shape,dtype="i4") 
        dsetout[()]=self.alpha4N31max        
        dsetout=groupout.create_dataset("cdep4N",self.cdep4N.shape,dtype="i4") 
        dsetout[()]=self.cdep4N        
        dsetout=groupout.create_dataset("j44N31max",self.j44N31max.shape,dtype="i4") 
        dsetout[()]=self.j44N31max        
        dsetout=groupout.create_dataset("j44N31min",self.j44N31min.shape,dtype="i4") 
        dsetout[()]=self.j44N31min        
        dsetout=groupout.create_dataset("l44N31max",self.l44N31max.shape,dtype="i4") 
        dsetout[()]=self.l44N31max        
        dsetout=groupout.create_dataset("lsummax4N31",self.lsummax4N31.shape,dtype="i4") 
        dsetout[()]=self.lsummax4N31        
        dsetout=groupout.create_dataset("mtau44N31Nmin",self.mtau44N31Nmin.shape,dtype="i4") 
        dsetout[()]=self.mtau44N31Nmin        
        dsetout=groupout.create_dataset("mtau44N31max",self.mtau44N31max.shape,dtype="i4") 
        dsetout[()]=self.mtau44N31max        
        dsetout=groupout.create_dataset("pari4N31max",self.pari4N31max.shape,dtype="i4") 
        dsetout[()]=self.pari4N31max        
        dsetout=groupout.create_dataset("pari4N31min",self.pari4N31min.shape,dtype="i4") 
        dsetout[()]=self.pari4N31min        
        dsetout=groupout.create_dataset("tau44N31Nmax",self.tau44N31Nmax.shape,dtype="i4") 
        dsetout[()]=self.tau44N31Nmax        
        dsetout=groupout.create_dataset("tau44N31Nmin",self.tau44N31Nmin.shape,dtype="i4") 
        dsetout[()]=self.tau44N31Nmin

        dsetout=groupout.create_dataset("qnalpha4N31",self.qnalpha4N31.shape,dtype="i4") 
        dsetout[()]=self.qnalpha4N31        
        

        # then read constants 
        dsetout=groupout.create_dataset("alpha_fein",self.alpha_fein.shape,dtype="f8") 
        dsetout[()]=self.alpha_fein        
        dsetout=groupout.create_dataset("m_eta",self.m_eta.shape,dtype="f8") 
        dsetout[()]=self.m_eta        
        dsetout=groupout.create_dataset("m_kaon",self.m_kaon.shape,dtype="f8") 
        dsetout[()]=self.m_kaon        
        dsetout=groupout.create_dataset("m_kaon0",self.m_kaon0.shape,dtype="f8") 
        dsetout[()]=self.m_kaon0        
        dsetout=groupout.create_dataset("m_kaonp",self.m_kaonp.shape,dtype="f8") 
        dsetout[()]=self.m_kaonp        
        dsetout=groupout.create_dataset("m_omega",self.m_omega.shape,dtype="f8") 
        dsetout[()]=self.m_omega        
        dsetout=groupout.create_dataset("m_pi",self.m_pi.shape,dtype="f8") 
        dsetout[()]=self.m_pi        
        dsetout=groupout.create_dataset("m_pi0",self.m_pi0.shape,dtype="f8") 
        dsetout[()]=self.m_pi0        
        dsetout=groupout.create_dataset("m_pip",self.m_pip.shape,dtype="f8") 
        dsetout[()]=self.m_pip        
        dsetout=groupout.create_dataset("m_rho",self.m_rho.shape,dtype="f8") 
        dsetout[()]=self.m_rho        
        dsetout=groupout.create_dataset("mlam",self.mlam.shape,dtype="f8") 
        dsetout[()]=self.mlam    
        dsetout=groupout.create_dataset("mneu",self.mneu.shape,dtype="f8") 
        dsetout[()]=self.mneu        
        dsetout=groupout.create_dataset("mnuc",self.mnuc.shape,dtype="f8") 
        dsetout[()]=self.mnuc        
        dsetout=groupout.create_dataset("mprot",self.mprot.shape,dtype="f8") 
        dsetout[()]=self.mprot    
        dsetout=groupout.create_dataset("msig0",self.msig0.shape,dtype="f8") 
        dsetout[()]=self.msig0    
        dsetout=groupout.create_dataset("msigm",self.msigm.shape,dtype="f8") 
        dsetout[()]=self.msigm        
        dsetout=groupout.create_dataset("msigp",self.msigp.shape,dtype="f8") 
        dsetout[()]=self.msigp        
        dsetout=groupout.create_dataset("mxi0",self.mxi0.shape,dtype="f8") 
        dsetout[()]=self.mxi0
        dsetout=groupout.create_dataset("mxiave",self.mxiave.shape,dtype="f8") 
        dsetout[()]=self.mxiave
        dsetout=groupout.create_dataset("mxim",self.mxim.shape,dtype="f8") 
        dsetout[()]=self.mxim
        dsetout=groupout.create_dataset("hbarc",self.hbarc.shape,dtype="f8") 
        dsetout[()]=self.hbarc


        # then grid points to FADCOMP
        meshname=list(self.meshtype)
        dsetout=groupout.create_dataset("meshtype",(len(meshname),),dtype="|S1") 
        dsetout[()]=meshname
        
        dsetout=groupout.create_dataset("p12n1",self.p12n1.shape,dtype="i4") 
        dsetout[()]=self.p12n1
        dsetout=groupout.create_dataset("p12n2",self.p12n2.shape,dtype="i4") 
        dsetout[()]=self.p12n2
        dsetout=groupout.create_dataset("p12ntot",self.p12ntot.shape,dtype="i4") 
        dsetout[()]=self.p12ntot

        dsetout=groupout.create_dataset("p12p1",self.p12a.shape,dtype="f8") 
        dsetout[()]=self.p12a
        dsetout=groupout.create_dataset("p12p2",self.p12b.shape,dtype="f8") 
        dsetout[()]=self.p12b
        dsetout=groupout.create_dataset("p12p3",self.p12c.shape,dtype="f8") 
        dsetout[()]=self.p12c
        

        dsetout=groupout.create_dataset("p12p",self.p12p.shape,dtype="f8") 
        dsetout[()]=self.p12p
        dsetout=groupout.create_dataset("p12w",self.p12w.shape,dtype="f8") 
        dsetout[()]=self.p12w

        dsetout=groupout.create_dataset("p3n1",self.p3n1.shape,dtype="i4") 
        dsetout[()]=self.p3n1
        dsetout=groupout.create_dataset("p3n2",self.p3n2.shape,dtype="i4") 
        dsetout[()]=self.p3n2
        dsetout=groupout.create_dataset("p3ntot",self.p3ntot.shape,dtype="i4") 
        dsetout[()]=self.p3ntot

        dsetout=groupout.create_dataset("p3p1",self.p3a.shape,dtype="f8") 
        dsetout[()]=self.p3a
        dsetout=groupout.create_dataset("p3p2",self.p3b.shape,dtype="f8") 
        dsetout[()]=self.p3b
        dsetout=groupout.create_dataset("p3p3",self.p3c.shape,dtype="f8") 
        dsetout[()]=self.p3c
        

        dsetout=groupout.create_dataset("p3p",self.p3p.shape,dtype="f8") 
        dsetout[()]=self.p3p
        dsetout=groupout.create_dataset("p3w",self.p3w.shape,dtype="f8") 
        dsetout[()]=self.p3w

        dsetout=groupout.create_dataset("q4n1",self.q4n1.shape,dtype="i4") 
        dsetout[()]=self.q4n1
        dsetout=groupout.create_dataset("q4n2",self.q4n2.shape,dtype="i4") 
        dsetout[()]=self.q4n2
        dsetout=groupout.create_dataset("q4ntot",self.q4ntot.shape,dtype="i4") 
        dsetout[()]=self.q4ntot

        dsetout=groupout.create_dataset("q4p1",self.q4a.shape,dtype="f8") 
        dsetout[()]=self.q4a
        dsetout=groupout.create_dataset("q4p2",self.q4b.shape,dtype="f8") 
        dsetout[()]=self.q4b
        dsetout=groupout.create_dataset("q4p3",self.q4c.shape,dtype="f8") 
        dsetout[()]=self.q4c
        

        dsetout=groupout.create_dataset("q4p",self.q4p.shape,dtype="f8") 
        dsetout[()]=self.q4p
        dsetout=groupout.create_dataset("q4w",self.q4w.shape,dtype="f8") 
        dsetout[()]=self.q4w
        
        # write amplitude data set in compressed form        
        dsetout=groupout.create_dataset("4n31amp",self.yak4n31.shape,dtype="f4", **hdf5plugin.Zfp(accuracy=tolerance)) 
        dsetout[()]=self.yak4n31

        # write binding energy to FADCOMP group
        dsetout=groupout.create_dataset("BENER",self.bener.shape,dtype="f8") 
        dsetout[()]=self.bener


        # then wave function in 4N22 coordinates
        groupout=fileout.create_group('WF4N22')
        # first bookkeeping to 4N22 wf 
        # parameters for info
        dsetout=groupout.create_dataset("cdepNN",self.cdepNN.shape,dtype="i4") 
        dsetout[()]=self.cdepNN        
        dsetout=groupout.create_dataset("evenNN",self.evenNN.shape,dtype="i4") 
        dsetout[()]=self.evenNN        
        dsetout=groupout.create_dataset("j12NNmax",self.j12NNmax.shape,dtype="i4") 
        dsetout[()]=self.j12NNmax        
        dsetout=groupout.create_dataset("l12NNmax",self.l12NNmax.shape,dtype="i4") 
        dsetout[()]=self.l12NNmax        
    
        dsetout=groupout.create_dataset("alphaNNcdepmax",self.alphaNNcdepmax.shape,dtype="i4") 
        dsetout[()]=self.alphaNNcdepmax        
        dsetout=groupout.create_dataset("alphaNNmax",self.alphaNNmax.shape,dtype="i4") 
        dsetout[()]=self.alphaNNmax        
        dsetout=groupout.create_dataset("mt12NNmax",self.mt12NNmax.shape,dtype="i4") 
        dsetout[()]=self.mt12NNmax        
        dsetout=groupout.create_dataset("mt12NNmin",self.mt12NNmin.shape,dtype="i4") 
        dsetout[()]=self.mt12NNmin        

        dsetout=groupout.create_dataset("qnalphaNN",self.qnalphaNN.shape,dtype="i4") 
        dsetout[()]=self.qnalphaNN        

        dsetout=groupout.create_dataset("I4N22max",self.I4N22max.shape,dtype="i4") 
        dsetout[()]=self.I4N22max        
        dsetout=groupout.create_dataset("beta4N22cdepmax",self.beta4N22cdepmax.shape,dtype="i4") 
        dsetout[()]=self.beta4N22cdepmax        
        dsetout=groupout.create_dataset("beta4N22max",self.beta4N22max.shape,dtype="i4") 
        dsetout[()]=self.beta4N22max        
        dsetout=groupout.create_dataset("cdep4N",self.cdep4N.shape,dtype="i4") 
        dsetout[()]=self.cdep4N        
        dsetout=groupout.create_dataset("j44N22max",self.j44N22max.shape,dtype="i4") 
        dsetout[()]=self.j44N22max        
        dsetout=groupout.create_dataset("j44N22min",self.j44N22min.shape,dtype="i4") 
        dsetout[()]=self.j44N22min        
        dsetout=groupout.create_dataset("lam4N22max",self.lam4N22max.shape,dtype="i4") 
        dsetout[()]=self.lam4N22max        
        dsetout=groupout.create_dataset("lsummax4N22",self.lsummax4N22.shape,dtype="i4") 
        dsetout[()]=self.lsummax4N22        
        dsetout=groupout.create_dataset("mtau44N22max",self.mtau44N22max.shape,dtype="i4") 
        dsetout[()]=self.mtau44N22max        
        dsetout=groupout.create_dataset("mtau44N22min",self.mtau44N22min.shape,dtype="i4") 
        dsetout[()]=self.mtau44N22min        
        dsetout=groupout.create_dataset("pari4N22max",self.pari4N22max.shape,dtype="i4") 
        dsetout[()]=self.pari4N22max        
        dsetout=groupout.create_dataset("pari4N22min",self.pari4N22min.shape,dtype="i4") 
        dsetout[()]=self.pari4N22min        
        dsetout=groupout.create_dataset("tau44N22max",self.tau44N22max.shape,dtype="i4") 
        dsetout[()]=self.tau44N22max        
        dsetout=groupout.create_dataset("tau44N22min",self.tau44N22min.shape,dtype="i4") 
        dsetout[()]=self.tau44N22min

        dsetout=groupout.create_dataset("qnbeta4N22",self.qnbeta4N22.shape,dtype="i4") 
        dsetout[()]=self.qnbeta4N22        
        
        # then write constants 
        dsetout=groupout.create_dataset("alpha_fein",self.alpha_fein.shape,dtype="f8") 
        dsetout[()]=self.alpha_fein        
        dsetout=groupout.create_dataset("m_eta",self.m_eta.shape,dtype="f8") 
        dsetout[()]=self.m_eta        
        dsetout=groupout.create_dataset("m_kaon",self.m_kaon.shape,dtype="f8") 
        dsetout[()]=self.m_kaon        
        dsetout=groupout.create_dataset("m_kaon0",self.m_kaon0.shape,dtype="f8") 
        dsetout[()]=self.m_kaon0        
        dsetout=groupout.create_dataset("m_kaonp",self.m_kaonp.shape,dtype="f8") 
        dsetout[()]=self.m_kaonp        
        dsetout=groupout.create_dataset("m_omega",self.m_omega.shape,dtype="f8") 
        dsetout[()]=self.m_omega        
        dsetout=groupout.create_dataset("m_pi",self.m_pi.shape,dtype="f8") 
        dsetout[()]=self.m_pi        
        dsetout=groupout.create_dataset("m_pi0",self.m_pi0.shape,dtype="f8") 
        dsetout[()]=self.m_pi0        
        dsetout=groupout.create_dataset("m_pip",self.m_pip.shape,dtype="f8") 
        dsetout[()]=self.m_pip        
        dsetout=groupout.create_dataset("m_rho",self.m_rho.shape,dtype="f8") 
        dsetout[()]=self.m_rho        
        dsetout=groupout.create_dataset("mlam",self.mlam.shape,dtype="f8") 
        dsetout[()]=self.mlam    
        dsetout=groupout.create_dataset("mneu",self.mneu.shape,dtype="f8") 
        dsetout[()]=self.mneu        
        dsetout=groupout.create_dataset("mnuc",self.mnuc.shape,dtype="f8") 
        dsetout[()]=self.mnuc        
        dsetout=groupout.create_dataset("mprot",self.mprot.shape,dtype="f8") 
        dsetout[()]=self.mprot    
        dsetout=groupout.create_dataset("msig0",self.msig0.shape,dtype="f8") 
        dsetout[()]=self.msig0    
        dsetout=groupout.create_dataset("msigm",self.msigm.shape,dtype="f8") 
        dsetout[()]=self.msigm        
        dsetout=groupout.create_dataset("msigp",self.msigp.shape,dtype="f8") 
        dsetout[()]=self.msigp        
        dsetout=groupout.create_dataset("mxi0",self.mxi0.shape,dtype="f8") 
        dsetout[()]=self.mxi0
        dsetout=groupout.create_dataset("mxiave",self.mxiave.shape,dtype="f8") 
        dsetout[()]=self.mxiave
        dsetout=groupout.create_dataset("mxim",self.mxim.shape,dtype="f8") 
        dsetout[()]=self.mxim
        dsetout=groupout.create_dataset("hbarc",self.hbarc.shape,dtype="f8") 
        dsetout[()]=self.hbarc


        # then grid points to FADCOMP
        meshname=list(self.meshtype)
        dsetout=groupout.create_dataset("meshtype",(len(meshname),),dtype="|S1") 
        dsetout[()]=meshname
        
        dsetout=groupout.create_dataset("p12n1",self.p12n1.shape,dtype="i4") 
        dsetout[()]=self.p12n1
        dsetout=groupout.create_dataset("p12n2",self.p12n2.shape,dtype="i4") 
        dsetout[()]=self.p12n2
        dsetout=groupout.create_dataset("p12ntot",self.p12ntot.shape,dtype="i4") 
        dsetout[()]=self.p12ntot

        dsetout=groupout.create_dataset("p12p1",self.p12a.shape,dtype="f8") 
        dsetout[()]=self.p12a
        dsetout=groupout.create_dataset("p12p2",self.p12b.shape,dtype="f8") 
        dsetout[()]=self.p12b
        dsetout=groupout.create_dataset("p12p3",self.p12c.shape,dtype="f8") 
        dsetout[()]=self.p12c
        

        dsetout=groupout.create_dataset("p12p",self.p12p.shape,dtype="f8") 
        dsetout[()]=self.p12p
        dsetout=groupout.create_dataset("p12w",self.p12w.shape,dtype="f8") 
        dsetout[()]=self.p12w

        dsetout=groupout.create_dataset("p34n1",self.p34n1.shape,dtype="i4") 
        dsetout[()]=self.p34n1
        dsetout=groupout.create_dataset("p34n2",self.p34n2.shape,dtype="i4") 
        dsetout[()]=self.p34n2
        dsetout=groupout.create_dataset("p34ntot",self.p34ntot.shape,dtype="i4") 
        dsetout[()]=self.p34ntot

        dsetout=groupout.create_dataset("p34p1",self.p34a.shape,dtype="f8") 
        dsetout[()]=self.p34a
        dsetout=groupout.create_dataset("p34p2",self.p34b.shape,dtype="f8") 
        dsetout[()]=self.p34b
        dsetout=groupout.create_dataset("p34p3",self.p34c.shape,dtype="f8") 
        dsetout[()]=self.p34c
        

        dsetout=groupout.create_dataset("p34p",self.p34p.shape,dtype="f8") 
        dsetout[()]=self.p34p
        dsetout=groupout.create_dataset("p34w",self.p34w.shape,dtype="f8") 
        dsetout[()]=self.p34w

        dsetout=groupout.create_dataset("qn1",self.qn1.shape,dtype="i4") 
        dsetout[()]=self.qn1
        dsetout=groupout.create_dataset("qn2",self.qn2.shape,dtype="i4") 
        dsetout[()]=self.qn2
        dsetout=groupout.create_dataset("qntot",self.qntot.shape,dtype="i4") 
        dsetout[()]=self.qntot

        dsetout=groupout.create_dataset("qp1",self.qa.shape,dtype="f8") 
        dsetout[()]=self.qa
        dsetout=groupout.create_dataset("qp2",self.qb.shape,dtype="f8") 
        dsetout[()]=self.qb
        dsetout=groupout.create_dataset("qp3",self.qc.shape,dtype="f8") 
        dsetout[()]=self.qc
        

        dsetout=groupout.create_dataset("qp",self.qp.shape,dtype="f8") 
        dsetout[()]=self.qp
        dsetout=groupout.create_dataset("qw",self.qw.shape,dtype="f8") 
        dsetout[()]=self.qw
        
        # write amplitude data set in compressed form
        
        dsetout=groupout.create_dataset("4n22amp",self.wf4n22.shape,dtype="f4", **hdf5plugin.Zfp(accuracy=tolerance)) 
        dsetout[()]=self.wf4n22


        # then wave function in 4N22 coordinates
        groupout=fileout.create_group('YAK4N22')
        # first bookkeeping to 4N22 wf 
        # parameters for info
        dsetout=groupout.create_dataset("cdepNN",self.cdepNN.shape,dtype="i4") 
        dsetout[()]=self.cdepNN        
        dsetout=groupout.create_dataset("evenNN",self.evenNN.shape,dtype="i4") 
        dsetout[()]=self.evenNN        
        dsetout=groupout.create_dataset("j12NNmax",self.j12NNmax.shape,dtype="i4") 
        dsetout[()]=self.j12NNmax        
        dsetout=groupout.create_dataset("l12NNmax",self.l12NNmax.shape,dtype="i4") 
        dsetout[()]=self.l12NNmax        
    
        dsetout=groupout.create_dataset("alphaNNcdepmax",self.alphaNNcdepmax.shape,dtype="i4") 
        dsetout[()]=self.alphaNNcdepmax        
        dsetout=groupout.create_dataset("alphaNNmax",self.alphaNNmax.shape,dtype="i4") 
        dsetout[()]=self.alphaNNmax        
        dsetout=groupout.create_dataset("mt12NNmax",self.mt12NNmax.shape,dtype="i4") 
        dsetout[()]=self.mt12NNmax        
        dsetout=groupout.create_dataset("mt12NNmin",self.mt12NNmin.shape,dtype="i4") 
        dsetout[()]=self.mt12NNmin        

        dsetout=groupout.create_dataset("qnalphaNN",self.qnalphaNN.shape,dtype="i4") 
        dsetout[()]=self.qnalphaNN        

        dsetout=groupout.create_dataset("I4N22max",self.I4N22max.shape,dtype="i4") 
        dsetout[()]=self.I4N22max        
        dsetout=groupout.create_dataset("beta4N22cdepmax",self.beta4N22cdepmax.shape,dtype="i4") 
        dsetout[()]=self.beta4N22cdepmax        
        dsetout=groupout.create_dataset("beta4N22max",self.beta4N22max.shape,dtype="i4") 
        dsetout[()]=self.beta4N22max        
        dsetout=groupout.create_dataset("cdep4N",self.cdep4N.shape,dtype="i4") 
        dsetout[()]=self.cdep4N        
        dsetout=groupout.create_dataset("j44N22max",self.j44N22max.shape,dtype="i4") 
        dsetout[()]=self.j44N22max        
        dsetout=groupout.create_dataset("j44N22min",self.j44N22min.shape,dtype="i4") 
        dsetout[()]=self.j44N22min        
        dsetout=groupout.create_dataset("lam4N22max",self.lam4N22max.shape,dtype="i4") 
        dsetout[()]=self.lam4N22max        
        dsetout=groupout.create_dataset("lsummax4N22",self.lsummax4N22.shape,dtype="i4") 
        dsetout[()]=self.lsummax4N22        
        dsetout=groupout.create_dataset("mtau44N22max",self.mtau44N22max.shape,dtype="i4") 
        dsetout[()]=self.mtau44N22max        
        dsetout=groupout.create_dataset("mtau44N22min",self.mtau44N22min.shape,dtype="i4") 
        dsetout[()]=self.mtau44N22min        
        dsetout=groupout.create_dataset("pari4N22max",self.pari4N22max.shape,dtype="i4") 
        dsetout[()]=self.pari4N22max        
        dsetout=groupout.create_dataset("pari4N22min",self.pari4N22min.shape,dtype="i4") 
        dsetout[()]=self.pari4N22min        
        dsetout=groupout.create_dataset("tau44N22max",self.tau44N22max.shape,dtype="i4") 
        dsetout[()]=self.tau44N22max        
        dsetout=groupout.create_dataset("tau44N22min",self.tau44N22min.shape,dtype="i4") 
        dsetout[()]=self.tau44N22min

        dsetout=groupout.create_dataset("qnbeta4N22",self.qnbeta4N22.shape,dtype="i4") 
        dsetout[()]=self.qnbeta4N22        
        
        # then write constants 
        dsetout=groupout.create_dataset("alpha_fein",self.alpha_fein.shape,dtype="f8") 
        dsetout[()]=self.alpha_fein        
        dsetout=groupout.create_dataset("m_eta",self.m_eta.shape,dtype="f8") 
        dsetout[()]=self.m_eta        
        dsetout=groupout.create_dataset("m_kaon",self.m_kaon.shape,dtype="f8") 
        dsetout[()]=self.m_kaon        
        dsetout=groupout.create_dataset("m_kaon0",self.m_kaon0.shape,dtype="f8") 
        dsetout[()]=self.m_kaon0        
        dsetout=groupout.create_dataset("m_kaonp",self.m_kaonp.shape,dtype="f8") 
        dsetout[()]=self.m_kaonp        
        dsetout=groupout.create_dataset("m_omega",self.m_omega.shape,dtype="f8") 
        dsetout[()]=self.m_omega        
        dsetout=groupout.create_dataset("m_pi",self.m_pi.shape,dtype="f8") 
        dsetout[()]=self.m_pi        
        dsetout=groupout.create_dataset("m_pi0",self.m_pi0.shape,dtype="f8") 
        dsetout[()]=self.m_pi0        
        dsetout=groupout.create_dataset("m_pip",self.m_pip.shape,dtype="f8") 
        dsetout[()]=self.m_pip        
        dsetout=groupout.create_dataset("m_rho",self.m_rho.shape,dtype="f8") 
        dsetout[()]=self.m_rho        
        dsetout=groupout.create_dataset("mlam",self.mlam.shape,dtype="f8") 
        dsetout[()]=self.mlam    
        dsetout=groupout.create_dataset("mneu",self.mneu.shape,dtype="f8") 
        dsetout[()]=self.mneu        
        dsetout=groupout.create_dataset("mnuc",self.mnuc.shape,dtype="f8") 
        dsetout[()]=self.mnuc        
        dsetout=groupout.create_dataset("mprot",self.mprot.shape,dtype="f8") 
        dsetout[()]=self.mprot    
        dsetout=groupout.create_dataset("msig0",self.msig0.shape,dtype="f8") 
        dsetout[()]=self.msig0    
        dsetout=groupout.create_dataset("msigm",self.msigm.shape,dtype="f8") 
        dsetout[()]=self.msigm        
        dsetout=groupout.create_dataset("msigp",self.msigp.shape,dtype="f8") 
        dsetout[()]=self.msigp        
        dsetout=groupout.create_dataset("mxi0",self.mxi0.shape,dtype="f8") 
        dsetout[()]=self.mxi0
        dsetout=groupout.create_dataset("mxiave",self.mxiave.shape,dtype="f8") 
        dsetout[()]=self.mxiave
        dsetout=groupout.create_dataset("mxim",self.mxim.shape,dtype="f8") 
        dsetout[()]=self.mxim
        dsetout=groupout.create_dataset("hbarc",self.hbarc.shape,dtype="f8") 
        dsetout[()]=self.hbarc


        # then grid points to FADCOMP
        meshname=list(self.meshtype)
        dsetout=groupout.create_dataset("meshtype",(len(meshname),),dtype="|S1") 
        dsetout[()]=meshname
        
        dsetout=groupout.create_dataset("p12n1",self.p12n1.shape,dtype="i4") 
        dsetout[()]=self.p12n1
        dsetout=groupout.create_dataset("p12n2",self.p12n2.shape,dtype="i4") 
        dsetout[()]=self.p12n2
        dsetout=groupout.create_dataset("p12ntot",self.p12ntot.shape,dtype="i4") 
        dsetout[()]=self.p12ntot

        dsetout=groupout.create_dataset("p12p1",self.p12a.shape,dtype="f8") 
        dsetout[()]=self.p12a
        dsetout=groupout.create_dataset("p12p2",self.p12b.shape,dtype="f8") 
        dsetout[()]=self.p12b
        dsetout=groupout.create_dataset("p12p3",self.p12c.shape,dtype="f8") 
        dsetout[()]=self.p12c
        

        dsetout=groupout.create_dataset("p12p",self.p12p.shape,dtype="f8") 
        dsetout[()]=self.p12p
        dsetout=groupout.create_dataset("p12w",self.p12w.shape,dtype="f8") 
        dsetout[()]=self.p12w

        dsetout=groupout.create_dataset("p34n1",self.p34n1.shape,dtype="i4") 
        dsetout[()]=self.p34n1
        dsetout=groupout.create_dataset("p34n2",self.p34n2.shape,dtype="i4") 
        dsetout[()]=self.p34n2
        dsetout=groupout.create_dataset("p34ntot",self.p34ntot.shape,dtype="i4") 
        dsetout[()]=self.p34ntot

        dsetout=groupout.create_dataset("p34p1",self.p34a.shape,dtype="f8") 
        dsetout[()]=self.p34a
        dsetout=groupout.create_dataset("p34p2",self.p34b.shape,dtype="f8") 
        dsetout[()]=self.p34b
        dsetout=groupout.create_dataset("p34p3",self.p34c.shape,dtype="f8") 
        dsetout[()]=self.p34c
        

        dsetout=groupout.create_dataset("p34p",self.p34p.shape,dtype="f8") 
        dsetout[()]=self.p34p
        dsetout=groupout.create_dataset("p34w",self.p34w.shape,dtype="f8") 
        dsetout[()]=self.p34w

        dsetout=groupout.create_dataset("qn1",self.qn1.shape,dtype="i4") 
        dsetout[()]=self.qn1
        dsetout=groupout.create_dataset("qn2",self.qn2.shape,dtype="i4") 
        dsetout[()]=self.qn2
        dsetout=groupout.create_dataset("qntot",self.qntot.shape,dtype="i4") 
        dsetout[()]=self.qntot

        dsetout=groupout.create_dataset("qp1",self.qa.shape,dtype="f8") 
        dsetout[()]=self.qa
        dsetout=groupout.create_dataset("qp2",self.qb.shape,dtype="f8") 
        dsetout[()]=self.qb
        dsetout=groupout.create_dataset("qp3",self.qc.shape,dtype="f8") 
        dsetout[()]=self.qc
        

        dsetout=groupout.create_dataset("qp",self.qp.shape,dtype="f8") 
        dsetout[()]=self.qp
        dsetout=groupout.create_dataset("qw",self.qw.shape,dtype="f8") 
        dsetout[()]=self.qw
        
        # write amplitude data set in compressed form
        
        dsetout=groupout.create_dataset("4n22amp",self.yak4n22.shape,dtype="f4", **hdf5plugin.Zfp(accuracy=tolerance)) 
        dsetout[()]=self.yak4n22
                
        fileout.close()
        if printlevel>0:
          print("File size written:  {0:d}".format(os.path.getsize(filen_out)))



    def get_labels(self):
        """This method returns the available labels of the amplitude as necessary for a database access.
           Labels that are not stored in file are filled with zeros and need to be guessed from
           elsewhere. 
        """

        if(self.mtau44N31max!=self.mtau44N31Nmin):
           raise ValueError("Non-unique mtau4.")
        if(self.mtau44N31max!=self.mtau44N22min):
           raise ValueError("Non-unique mtau4.")
        if(self.mtau44N31max!=self.mtau44N22max):
           raise ValueError("Non-unique mtau4.")
            
        if(self.mtau44N31max==0):
            Z=2
            N=2
        else:
           raise ValueError("mtau4 is not well defined in 4N wave function.")

        lmax=max([self.l33Nmax,self.l44N31max,self.lam4N22max])
       
        standard_labels={'Z':Z,'N':N,
              'NP12A':self.p12n1, 'NP12B':self.p12n2, 'NP12':self.p12ntot, 'P12A':self.p12a, 'P12B':self.p12b,'P12C':self.p12c,
              'NP3A':self.p3n1, 'NP3B':self.p3n2, 'NP3':self.p3ntot, 'P3A':self.p3a, 'P3B':self.p3b,'P3C':self.p3c,
              'NQ4A':self.q4n1, 'NQ4B':self.q4n2, 'NQ4':self.q4ntot, 'Q4A':self.q4a, 'Q4B':self.q4b,'Q4C':self.q4c,
              'NP34A':self.p34n1, 'NP34B':self.p34n2, 'NP34':self.p34ntot, 'P34A':self.p34a, 'P34B':self.p34b,'P34C':self.p34c,
              'NQA':self.qn1, 'NQB':self.qn2, 'NQ':self.qntot, 'QA':self.qa, 'QB':self.qb,'QC':self.qc,
              'NPTA':0, 'NPTB':0,'NPT':0, 'PTA':0, 'PTB':0, 'PTC':0,
              'NEA':0, 'NEB':0, 'NE':0, 'EA':0, 'EB':0, 'EC':0,
              'NX':0,
              'taumax':self.tau44N31Nmax, 'lsummax':self.lsummax4N31,'lmax':lmax, 'j12max':self.j12NNmax,
              'l3max':self.l33Nmax,'l4max':self.l44N31max,'lammax':self.lam4N22max,'MTtot':self.mtau44N31max, 'Jtot':self.j44N31max,
              'MODENN':'none', 'orderNN':'none','LambdaNN':0.0, 'potnr':0, 'empotnr':0,
              'lam3NF':0.0, 'c1':0.0, 'c3':0.0, 'c4':0.0, 'cd':0.0, 'ce':0.0,'cE1':0.0, 'cE3':0.0, 'tnforder':'no3nf','j12max3nf':0,'j3max3nf':0,
              'relcalc':0,
              'nnsrg':'none', 'tnfsrg':0, 'lambdaSRGNN':0.0,'lambdaSRG3N':0.0, 'potbareNN':0, 'potbareNNTNF':0, 'ostatSRGNN':0, 'ostatSRGTNF':0,
              'LambdaSRGNN':0.0, 'LambdaSRGTNF':0.0,}

        return standard_labels 
          
          
