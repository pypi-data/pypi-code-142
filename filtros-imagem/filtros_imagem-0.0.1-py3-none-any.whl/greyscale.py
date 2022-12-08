from PIL import Image
from util import in_file, out_file

def greyscale(colorida):
    w, h = colorida.size
    imagem = Image.new("RGB", (w, h))

    #iterando sobre os pixels da imagens
    for x in range(w):
        for y in range(h):
            pixel = colorida.getpixel((x, y))
            #média ponderada para aproximar ao valor real da luminância
            lumi = int(0.3*pixel[0] + 0.59*pixel[1] + 0.11*pixel[2])
            imagem.putpixel((x, y), (lumi, lumi, lumi))
    return imagem