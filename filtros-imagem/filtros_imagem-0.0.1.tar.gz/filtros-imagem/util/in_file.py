from PIL import Image, ImageFilter
import os
import numpy as np

#caminho relativo dos arquivos para entrada e saída
INPUT_DIR = os.path.join('imagens', 'input')
OUTPUT_DIR = os.path.join('imagens', 'output')

def in_file(nome_do_arquivo):
    #retorna o caminho de um arquivo de entrada
    return os.path.join(INPUT_DIR, nome_do_arquivo)