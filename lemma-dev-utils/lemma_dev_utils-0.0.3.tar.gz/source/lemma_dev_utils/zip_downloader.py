from pathlib import Path
import urllib.request
from tqdm import tqdm
import zipfile
import os

# Function I wrote to download a file getting a progressbar
def download(url, file_name):

    class MyProgressBar():

        def __init__(self):
            self.pbar = None

            #requesting file size from url
            request = urllib.request.Request(url, method='HEAD')
            self.total_size = int(urllib.request.urlopen(request).headers['Content-Length'])

        def __call__(self, block_num, block_size, wrong_size):
            #if the pbar doesn't exist yet
            if not self.pbar:
                self.pbar = tqdm(ascii=True, desc=f'Downloading {file_name}',
                                 total = self.total_size, position=0, leave=True)

            #tracing the size of the downloaded blocks
            downloaded = block_num * block_size
            missing = self.total_size - downloaded
            
            #updating according to either the missing size or the entire block size
            if downloaded < self.total_size:
                self.pbar.update(block_size)
            else:
                self.pbar.update(missing)

    # Downloading data
    urllib.request.urlretrieve(url, file_name, MyProgressBar())
    return

# Function I wrote to unzip a file getting a progressbar
def unzip(path, file_name):

    # Unzipping the data
    zip_ref = zipfile.ZipFile(file_name)

    for zipped_file in zip_ref.filelist:
        # Finding a file in the zip and opening it
        zipped_name = zipped_file.filename
        origin = zip_ref.open(zipped_name)

        # Creating the path and opening the file to write
        Path(path).mkdir(exist_ok=True)
        destination = open(f"{path}/{zipped_name}", 'wb')
        
        #defining the block size to unzip at each iteration
        block_size = 8192
        #getting the file to unzip size
        file_size = zipped_file.file_size

        #computing the total size to unzip (according to the blocks unzipped each time)
        max_size = ( 1 + (file_size // block_size) ) * block_size + 1

        #setting a progress bar
        pbar = tqdm(ascii=True, desc=f'Unzipping {zipped_name}',
                    total= max_size, position=0, leave=True)
        
        condition = True
        #if there is still a block to unzip continue
        while condition == True:
            block = origin.read(block_size)
            
            if not block:
                condition = False
                break
                
            destination.write(block)
            pbar.update(block_size)

        pbar.update()
        origin.close()
        destination.close()
    return

#download, unzip and remove zip file
def download_unzip(path, url, remove_zip = True):

    file_name = urllib.request.urlopen(url).info().get_filename()
    download(url, file_name)
    unzip(path, file_name)
    
    if remove_zip:
        os.remove(file_name)