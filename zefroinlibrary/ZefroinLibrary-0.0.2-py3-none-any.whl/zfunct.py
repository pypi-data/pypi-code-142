import random

def rand(rnd1,rnd2):
  random.randint(rnd1, rnd2)
  

def slist(inp,revers):
  if type(inp) is list:
    if revers:
      return inp.sort(reverse=revers)
    else:
      return inp.sort()

  else:
    print("REQUIRED LIST, GOT: ", type(inp))

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
  if type(liste) is not list:
    print("REQUIRED LIST, GOT: ", type(liste))
    pass
  else:
    liste = str(liste)
    liste = liste.replace('[','')
    liste = liste.replace(']','')
    liste = liste.replace(',','')
    liste = liste.replace("'", '')
def fwrite(file,text): 
  tempf = open(file,'a')
  tempf.close()
  with open(file,'w') as f:
    f.write(text)
def fread(file):
  with open(file,'r') as f:
    return f.read()
