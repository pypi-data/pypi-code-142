from PIL import Image, ImageFont
from util import in_file, out_file

def negativo(img:Image)->Image:

    neg = Image.new(img.mode, img.size, "red")
    w, h = neg.size
    for i in range(w):
        for j in range(h):
            if img.mode == "RGB":
                r, g, b = img.getpixel((i,j))
                neg.putpixel((i,j), (255-r, 255-g, 255-b))
            elif img.mode == "RGBA":
                r, g, b, a = img.getpixel((i,j))
                neg.putpixel((i,j), (255-r, 255-g, 255-b, a))
            else:
                pass
    return neg