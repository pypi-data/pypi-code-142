import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--nom',help='Nombre del archivo con las marcas de tiempo', required=True)
parser.add_argument('--url',help='URL del video', required=True)
parser.add_argument('--album','-b',help='El archivo contiene álbumes',action='store_true')
parser.add_argument('--artist','-a',help='El archivo contiene artistas',action='store_true')
args = parser.parse_args()
print(args.nom)
print(args.url)
print(args.album)
print(args.artist)




