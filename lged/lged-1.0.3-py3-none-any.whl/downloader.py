from tqdm import tqdm
import requests
import os
import click
from urllib.parse import unquote

def download_file(link, path):
    maximum_retries = 3
    
    filename = os.path.basename(link)
    filename = unquote(filename)

    click.echo(click.style(f"{filename}", fg="green"))
    with open(f"{path}/{filename}", 'wb') as f:
        download_size = 0
        while maximum_retries > 0:
            requests.adapters.HTTPAdapter(max_retries=maximum_retries)
            response = requests.get(link, stream=True, headers={'Accept-Encoding': None, 'Content-Encoding': 'gzip'})
            download_size = response.headers.get('content-length')
            if download_size is None and maximum_retries > 0:
                maximum_retries -= 1
            else:
                break
        pbar = tqdm(
            total=int(download_size),
            initial=0,
            unit='B',
            unit_scale=True,
            position=0,
            leave=True)
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                pbar.set_description("Downloading... ")
                pbar.update(len(chunk))
        pbar.close()
        print("\n")
