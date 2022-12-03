try: from PIL import Image, ImageFont, ImageDraw
except: print("pillow not found, use pip to install\n  pip install pillow")
from textwrap import wrap as wr
from requests import get
from io import BytesIO
import json, os
path = os.path.dirname(__file__)

class gquote:
    def __init__(self, base = None, headers = None, proxy = None, output = True, format = "png", fonts = None, shape = "box", background = None, color = None):
        self.base    = "https://zenquotes.io/api/random" if not base else base
        self.headers = headers
        self.proxy  = proxy
        self.format = format
        self.output = False
        self.backg  = background
        self.shape  = shape
        self.shapes = {"box": [(1080, 1350), 20], "portrait": [(1080, 1920), 18]}
        try: self.shape = self.shapes[self.shape]
        except Exception as e: raise ValueError("box and portrait shapes are only available")
        self.color, self.tcolor = inverse(color) if color else ("#000000", "#FFFFFF")
        if output:
            if type(output) is str:
                if "." in output: self.output = output
                else: raise ValueError("output path should include output format e.g: /home/xd/quote.png")
            else: self.output = "./quote.png"
        self.fonts = [f"{path}/fonts/Barkentina.ttf", f"{path}/fonts/Ubuntu-Italic.ttf"]
        if fonts and type(fonts) is list and len(fonts) >= 2: self.fonts = fonts
        if not background: return
        try:
           self.backg = Image.open(background)
        except Exception as e:
           raise ValueError(f"Custom Background you passed is invalid \n\n {e}")
        if self.backg: self.shape = [self.backg.size, 20 if (self.backg.size[1] <= 1350) else 18]


    def run(self):
        tquote = get(self.base, headers=self.headers, proxies=self.proxy)
        if tquote.status_code != 200:
            print("bad api!", tquote.status_code)
            exit(1)
        # Edit the following according to your api
        # you should give quote and author vars
        # it will do the rest!
        tquote = json.loads(tquote.text)
        quote  = tquote[0]['q']
        self.author = "~ " + tquote[0]['a'] + " ~"
        # leave these
        self.quote  = "“" + quote + "”"
        # bwidth is text width on every line
        # wquote is list of text divided on lines
        # len(wquote) gives you no. lines
        bwidth = self.shape[1]
        wquote = wr(self.quote, width=bwidth)
        if len(wquote) > 7:
           while len(wquote) > 7:
                 bwidth += 1
                 wquote = wr(self.quote, width=bwidth)
        # new 16:9 image
        im   = Image.new("RGB", self.shape[0]) if not self.backg else self.backg
        draw = ImageDraw.Draw(im)
        # load fonts
        fontsize = 100 if bwidth == 18 else 100 - bwidth
        # Font used Doesn't look good in bright Backgrounds 000=Black
        font  = ImageFont.truetype(self.fonts[1] if "000" in self.tcolor else self.fonts[0], fontsize)
        sfont = ImageFont.truetype(self.fonts[1], 40)
        # try to center text horz/vertical
        # padding is dist. between each line
        padding = 50;
        # determine all lines height
        w, h = draw.textsize('TEST', font=font)
        totalH = (h*len(wquote))+(padding*len(wquote))+120
        ch = (self.shape[0][1] - totalH) / 2
        for i in wquote:
            w, h = draw.textsize(i, font=font)
            draw.text( ( (1080-w)/2, ch), i, fill=self.tcolor, font=font, stroke_width=5 if self.backg else None, stroke_fill=self.color if self.backg else None)
            ch += h + padding
        # finally draw author with diffrent font
        w, h = draw.textsize(self.author, font=sfont)
        draw.text( ( (1080-w)/2, ch+80), self.author, fill=self.tcolor, font=sfont, stroke_width=5 if self.backg else None, stroke_fill=self.color if self.backg else None)
        # export
        if self.output: im.save(self.output)
        else: # export to memory
            out = BytesIO()
            im.save(out, format=self.format, quality=100)
            return out

        print('saved to ', self.output)
        return self.output

def inverse(color):
    #* i commented inverse code as i don't need it
    #* might be useful later tho
    if len(color) == 3: # for RGB format
        #*c = [255-i for i in color]
        #*c = '#' + "".join(["{:02x}".format(i) for i in c])
        w = "#FFFFFF"
        if ((color[0]*0.299) + (color[1]*0.587) + (color[2]*0.114)) >= 128: w = "#000000"
    else: # for HEX format
        # first detect '#' and remove it
        c = color.replace("#", "")
        # group to twos
        c = (c[0:2], c[2:4], c[4:6])
        # convert to rgb
        c = [int(i, base=16) for i in c]
        ### White/Black Acorrding to each color intense ### 
        w = "#FFFFFF"
        if ((c[0]*0.299) + (c[1]*0.587) + (c[2]*0.114)) >= 128: w = "#000000"
        ### https://stackoverflow.com/a/3943023     LOL ###

        # invert rgb colors
        #*c = [255-i for i in c]
        # convert rgb back to hex
        #*c = ["{:02x}".format(i) for i in c]
        # join results
        #*c = '#' + "".join(c)
    

    # don't use white as border color
    #*if c == "#ffffff": c = "#757575"
    #*if c == "#000000": c = "#3d3d3d"

    return color, w