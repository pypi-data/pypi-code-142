import random
import os
def rand(rnd1,rnd2):
  return random.randint(rnd1, rnd2)

def curdir():
  return os.getcwd()

def get_file_path(file_name):
  return os.path.join(curdir(), file_name)

def get_file_name(file_path):
  return os.path.basename(file_path)

def get_file_extension(file_name):
  return os.path.splitext(file_name)[1]

def get_file_size(file_path):
  return os.path.getsize(file_path)

def get_file_date(file_path):
  return os.path.getmtime

def openf(filename):
  os.system(filename)

def slist(inp,revers):
  
  if revers:
    return inp.sort(reverse=True)
  else:
    return inp.sort()


def splist(inp):
  
  lista = []
  inp = inp.split(' ', ',')
  for i in inp:
    lista.append(i)
  lista = str(lista)
  lista = lista.replace('[','')
  lista = lista.replace(']','')
  lista = lista.replace(',','')
  lista = lista.replace("'", '')

  return lista
  
def rmlist(liste):
  if type(liste) is list:
    liste = str(liste)
    liste = liste.replace('[','')
    liste = liste.replace(']','')
    liste = liste.replace(',','')
    liste = liste.replace("'", '')
    return liste
  else:
    print("REQUIRED LIST, GOT: ", type(liste))
    pass
    
def fwrite(file,text): 
  tempf = open(file,'a')
  tempf.close()
  with open(file,'w') as f:
    f.write(text)
def fread(file):
  with open(file,'r') as f:
    return f.read()
