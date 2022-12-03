import subprocess as sub
import os
import sys

def obtener_tiempo(linea,inverso=False):
    t = ""
    if(inverso):
        for c in reversed(linea):
            if(c == ' '):
                break
            t = c + t
    else:
        for c in linea:
            if(c == ' '):
                break
            t = t + c
    return t

def extencion_archivo(cadena):
    e = ""
    for c in reversed(cadena):
        e = c + e
        if(c == '.'):
            break
    return e


archivo_original = sys.argv[1]
archivo_lista = sys.argv[2]
ext = extencion_archivo(archivo_original)
nuevodir = archivo_original[0:28].strip()
nuevodir = nuevodir.replace(ext,"")

archivo = open(archivo_lista,'r')
lineas = archivo.readlines()

canciones = []

for l in lineas:
    linea = l.strip()
    tiempo = obtener_tiempo(linea,True)
    nombre = linea.replace(tiempo,"").strip()
    canciones.append([nombre,tiempo])


sub.call('mkdir "'+ nuevodir +'"', shell=True)

comando = "ffmpeg -i '{ao}' -acodec copy -ss {ini} {fin} {nmb}"


for i in range(len(canciones)):
    nombre = "-to "+canciones[i+1][1] if (i+1 < len(canciones)) else ""
    cancion = canciones[i]
    com = comando.format(ao=archivo_original, ini=cancion[1], fin=nombre, nmb="'"+nuevodir+"/"+cancion[0]+ext+"'")
    print(com)
    #sub.call(com,shell=True)

