import requests
from requests.exceptions import HTTPError
import json
import sys
import os
from bs4 import BeautifulSoup
import time

ext = {".jpg", ".jpeg", ".jfif", "jpe", ".gif", ".png", ".bmp",
       ".svg", ".webp", ".ico"}


def get_url(elem) -> str:
    if 'url' in elem:
        url = elem['url']
        if url[url.rfind('.'):] in ext:
            return url
    return None


def handle_response(text: str) -> [str]:
    urls = set()
    soup = BeautifulSoup(text, 'html.parser')
    divs = soup.find_all('div', class_='serp-item_type_search')
    for item in divs:
        bem = item.get('data-bem')
        if bem is None:
            continue
        json_data = json.loads(bem)
        elem = json_data['serp-item']['preview'][0]
        url = get_url(elem)
        if (url is None and 'origin' in elem):
            url = get_url(elem['origin'])
        if (url is not None):
            urls.add(url)
    return urls


def loadfile(params: (str, str, int)) -> str:

    url = params[0]
    out_dir = params[1]
    index = params[2]

    try:
        p = requests.get(url, timeout=5)
    except Exception as e:
        return(f"Cannot download {url}: {e}")

    if p.status_code == 200:
        c = p.content
        fname = str(index) + url[url.rfind("."):]
        with open(f"{out_dir}/{fname}", "wb") as f:
            f.write(c)
        return ""
    return ""


def run_multi(params: (str, str, int), nw: int, pb: bool):
    print(len(params))
    from concurrent.futures import ProcessPoolExecutor
    if (pb):
        import tqdm as tq
        with ProcessPoolExecutor(max_workers=nw) as pool:
            result = list(tq.tqdm(pool.map(loadfile, params),
                                  total=len(params),
                                  leave=True,
                                  position=0
                                  ))
    else:
        with ProcessPoolExecutor(max_workers=nw) as pool:
            result = pool.map(loadfile, params)
    return result


def save_msg(msg: [str], urls: [str], out_dir: str)->None:
    with open(f"{out_dir}/errors.txt", "w") as f:
        for m in msg:
            if m != "":
                f.write(f"{m}\n")
    with open(f"{out_dir}/indexes.txt", "w") as f:
        for (i, url) in enumerate(urls):
            f.write(f"{str(i)}  {url}\n")


def run_loading(nw: int, out_dir: str, fname: str, pb: bool) -> [str]:
    content = None
    with open(fname, 'r', encoding='utf-8') as f:
        try:
            content = f.read()
        except Exception as e:
            print(f"Cannot load file {fname}: {e}")
            return
    urls = list(handle_response(content))
    print(len(urls))
    start = time.time()
    if (nw == 1):
        messages = []
        if (pb):
            from tqdm import tqdm
            p_bar = tqdm(total=len(urls), leave=True, position=0)
        for (i, url) in enumerate(urls):
            messages += [loadfile((url, out_dir, i))]
            if (pb and i % 10 == 0):
                p_bar.update(10)
        if (pb):
            p_bar.close()
    else:
        params = [(urls[i], out_dir, i) for i in range(len(urls))]
        messages = run_multi(params, nw, pb)
    save_msg(messages, urls, out_dir)


def usage() -> None:
    print("Usage: yil --w=<num_workers for parallel loading>, 1 by default\
   --out_dir=<output dir name, ./downloads by default\
   --f=<html file, mandatory>\
   --help \
   --pb \n\
   pb means showing progress bar")


def get_nw(p_pnum: str) -> int:
    result = 1

    try:
        result = int(p_pnum)
    except Exception as e:
        print(f"Cannot create a number from w:{e}")
        print("will use 1 worker")
    return result


def get_out_dir(p_out_dir: str) -> str:
    result = None
    if (p_out_dir is None):
        print("No out_dir param, will use ./downloads")
        result = "./downloads"
    else:
        result = p_out_dir
    print(result)
    try:
        out_dir = result
        os.makedirs(out_dir, exist_ok=True)
    except Exception as e:
        print(f"Cannot create directory {out_dir}: {e}")
        out_dir = None
    return out_dir


def check_fname(fname: str) -> str:
    if fname is not None and os.path.isfile(fname):
        return fname
    else:
        return None


def main() -> None:
    args = sys.argv
    nw, out_dir, fname = 1, None, None

    params = {'out_dir':None, 'w':1, 'f':None}
    for a in args[1:]:
        split = a.split("=")
        params[split[0].lstrip("-")] = split[1] if len(split) > 1 else None

    if ('help' in params):
        usage()
        return
    out_dir = get_out_dir(params['out_dir'] )
    nw = get_nw(params['w'])
    fname = check_fname(params['f'])

    if (fname is None):
        print("No file name provided...use --help...")
        usage()
        return
    if (out_dir != None):
        run_loading(nw, out_dir, fname, 'pb' in params)


# main()
if __name__ == '__main__':
    main()
