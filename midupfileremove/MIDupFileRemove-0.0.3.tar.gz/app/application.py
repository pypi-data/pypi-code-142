import datetime
from sys import *
import os 
import hashlib
import time
import psutil

def hashfile(path,blocksize= 1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def FindDuplicate(path):

    flag = os.path.isabs(path)
    if flag==False:
        path= os.path.abspath(path)

    exists = os.path.isdir(path)
    dups = {} 

    if exists:
        for folder, subfolders, files in os.walk(path):
            for file in files:
                path = os.path.join(folder, file)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash]=[path]
        return dups
    else:
        print("Invalide Path")

def CreateLogFile(dict1):
    results = list(filter(lambda x: len(x)>1 ,dict1.values()))

    directory=os.path.join(os.path.expanduser('~'), 'Downloads')

    if len(results) > 0:
      
        separator = '-' * 80
        name = "Logfile "+datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")+".txt"
        log_path = os.path.join(directory,name)
        f = open(log_path, 'w')
        f.write(separator+"\n")
        f.write("List  of removed duplicate files  "+time.ctime()+"\n")
        f.write(separator+"\n")

        count = 0 
        for result in results:
            for subresult in result:
                count += 1
                if count >=2:
                    f.write("{}\n".format(subresult))
            count = 0
        
    else:
        print("Duplicate files are not found")


def DeleteDuplicateFiles(dict1):
    results = list(filter(lambda x: len(x)>1 ,dict1.values()))
    if len(results) > 0:
        count = 0 
        for result in results:
            for subresult in result:
                count += 1
                if count >=2:
                    os.remove(subresult)
            count = 0
        

def main(file_path):
    
    if len(argv)<2:
        print("Insufficient arguments")
        exit()


    if argv[1] == "-h" or argv[1] == "-H":
        print("Enter the directory name as argument .")
        exit()

    if argv[1] == "-u" or argv[1] == "-U":
        print("This script is use to remove the duplicate files from given directory and add names of removed files into log.txt file.")
        exit()

    try:
       Arr = {}
       Arr =  FindDuplicate(file_path)
       CreateLogFile(Arr)
       DeleteDuplicateFiles(Arr)
    except ValueError :
        print("Error: Invalid datatype of input ")

    except Exception:
        print("Invalid input")


