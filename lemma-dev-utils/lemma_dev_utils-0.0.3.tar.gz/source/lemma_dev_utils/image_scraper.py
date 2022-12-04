from IPython.display import clear_output
from IPython import display
from PIL import Image
import imageio

import matplotlib.pyplot as plt
import io
import os

from tqdm import tqdm
import urllib.request
import time
import re

class ImageStructure(list):

    def append(self, *args):
        self.extend(args)

    def plot(self, item):
        plt.axis('off')
        image = plt.imshow(self[item])
        plt.show()
    
    def save_all(self, name_pattern = 'img', path = f'{os.getcwd()}/store_images'):
      
        if not os.path.exists(path):
            os.mkdir(path)
        
        if isinstance(name_pattern, str):
            for n, img in enumerate(self):
                img.save(f'{path}/{n}_{name_pattern}.{img.format.lower()}')
        else:
            assert len(name_pattern) == len(self), 'The file names should be the same as the files to save!'

            for name, img in zip(name_pattern, self):
                img.save(f'{path}/{name}.{img.format.lower()}')

    def __str__(self):
        return str(self)

class ImageExtractor(object):

    def __init__(self, url):
        #opening the url and reading the content
        source = urllib.request.urlopen(url).read().decode("utf-8")

        url_list = self._urlify(source)
        self.urls = self._get_image_urls(url_list)
        
    def _urlify(self, source):

        def extract_url(source):
            #extracting the urls from the web page source
            url_pattern = r"(((https?)|(http?)):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)"
            url_in_content = re.findall(url_pattern, source)
            return url_in_content

        list_to_clean = extract_url(source)
        exclude_str = ['http', 'https', '//', '']
        exclusion = lambda x: x not in exclude_str

        link_list = [list(filter(exclusion, tup))[0] for tup in list_to_clean]
        return link_list

    def _get_image_urls(self, list_input):
        pict_formats = ['png', 'jpg', 'gif', 'webp']
        # endswith returns a boolean value so I can sum them to get a number greater than 0 if True
        inclusion = lambda x: sum([x.endswith(ext) for ext in pict_formats])
        return list(filter(inclusion, list_input))

    def display_list(self):
      
        if not hasattr(self, 'image_list'):
            self.image_list = ImageStructure()

            for url in tqdm(self.urls):
                r = urllib.request.urlopen(url)
                image = Image.open(r)
                self.image_list.append(image)

        return self.image_list

    def save_content(self, path = f'{os.getcwd()}/store_images'):
        image_list = self.image_list if hasattr(self, 'image_list') else self.display_list()
        file_names = [url.rsplit('/', 1)[1] for url in self.urls]
        image_list.save_all(name_pattern = file_names, path = path)

    def show_content(self, fps = 2):
        image_list = self.image_list if hasattr(self, 'image_list') else self.display_list()
        length = len(image_list)

        for n in range(length):
            clear_output(wait=True)
            image_list.plot(n)
            time.sleep(fps)

    def __repr__(self):
        return str(self.urls)