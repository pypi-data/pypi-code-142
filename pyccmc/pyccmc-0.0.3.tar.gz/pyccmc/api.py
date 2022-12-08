import sys
import os
import re
import hashlib
import http.client
import json
import logging
import time
import zipfile

from pathlib import Path
from colorama import init, Fore, Back
from tqdm import tqdm

import browser_cookie3
import requests
import webbrowser

from fake_useragent import UserAgent

from pyccmc.apidocs import apidocs

# import networkx as nx
# import matplotlib.pyplot as plt

http.client._MAXLINE = 955360  # hack to allow for too big api headers
work_dir = sys.argv[0]


# numpy scipy pandas matplotlib pygraphviz pydot pyyaml gdal

def get_connected_upload_ids(artist='tigabeatz', limit=3, maxnodes=3, config={}):
    def reqccm(query_construct):
        rquery = False
        for key in query_construct:
            if not rquery:
                rquery = str(key) + '=' + str(query_construct[key])
            else:
                rquery = rquery + '&' + str(key) + '=' + str(query_construct[key])
        rquery = config['api']['base_url'] + rquery
        # print(rquery)
        # http.client._MAXLINE = 65536001  # hack to allow for too big api headers
        req = requests.Session().get(rquery, timeout=60, proxies=config['local']['proxy'])
        return req.json()

    def queryid(uid):
        r, s = [], []
        # print('asking for upload_id:', uid)
        queryremix = {
            'remixes': uid,
            'dataview': 'list_narrow',  # 'files', list_narrow
            'format': 'json'
        }
        for remix in reqccm(queryremix):
            r.append(remix['upload_id'])
            # print(remix['upload_id'], remix['upload_name'], remix['user_name'])

        querysource = {
            'sources': uid,
            'dataview': 'list_narrow',  # 'files', list_narrow
            'format': 'json'
        }
        for source in reqccm(querysource):
            s.append(source['upload_id'])
            # print(source['upload_id'], source['upload_name'], source['user_name'])

        # print(s, upload['upload_id'], upload['upload_name'], upload['user_name'], r)
        ug = {
            'upload_id': uid,
            'sources': s,
            'remixes': r
        }
        return ug, [*r, *s]

    # get the users uploads with their sources and remixes
    queryuser = {
        'user': artist,
        'dataview': 'list_narrow',  # 'files', list_narrow
        'format': 'json',
        'limit': limit
    }
    uploads_from_user = reqccm(queryuser)

    uploads = []
    print(' \n get user files and direct dependencies \n')
    for upload in tqdm(uploads_from_user, ascii=True, unit_scale=True, ncols=80, unit='b', ):
        conected_ids, nd = queryid(upload['upload_id'])
        uploads.extend(nd)
        uploads.append(upload['upload_id'])

    print('\n scan dependency tree \n')
    for upload in tqdm(uploads, ascii=True, unit_scale=True, ncols=80, unit='b', ):
        idx = uploads.index(upload)
        if idx < maxnodes:
            # print('working at id:', uploads.index(upload), upload, 'from' , len(uploads))
            conected_ids, nd = queryid(upload)
            for i in nd:
                if i not in uploads:
                    # print('adding uploads dependencies to uploads list', i)
                    uploads.append(i)

    pregraphdat = []
    print('\n prepare for graph generation and get metadata \n')
    for uid in tqdm(uploads, ascii=True, unit_scale=True, ncols=80, unit='b', ):
        f, g = queryid(uid)
        queryremix = {
            'ids': uid,
            'dataview': 'list_narrow',  # 'files', list_narrow
            'format': 'json'
        }
        f['metadata'] = reqccm(queryremix)
        pregraphdat.append(f)
        # print(f)

    graphdat = {
        'nodes': [],
        'links': []
    }

    for x in pregraphdat:
        # print(x)
        graphdat['nodes'].append(
            {
                'id': x['upload_id'],
                'name': x['metadata'][0]['upload_name'],
                'metadata': x['metadata'][0],
                'labels': [x['metadata'][0]['upload_name'], x['metadata'][0]['user_name']]
            }
        )
        for y in x['sources']:
            graphdat['links'].append(
                {
                    'source': y,
                    'target': x['upload_id'],
                    'labels': ['source']
                }
            )
        for z in x['remixes']:
            graphdat['links'].append(
                {
                    'source': x['upload_id'],
                    'target': z,
                    'labels': ['remix']
                }
            )

    # # create graph for viz
    # G = nx.Graph()
    # for node in graphdat['nodes']:
    #     # print('ading node', node['id'], node['name'])
    #     G.add_node(node['id'], name=node['name'])
    #
    # for edge in graphdat['links']:
    #     # print('adding edge', edge)
    #     G.add_edge(edge['source'], edge['target'], lables=edge['labels'])
    # # G.add_nodes_from(graphdat['nodes'])

    # print(G.number_of_nodes(), G.number_of_edges())

    # nx.draw(G)
    # nx.draw_random(G)
    # plt.savefig("path.png")

    return json.dumps(graphdat, indent=4)


def metaclient(workdir=os.path.join(os.path.dirname(os.path.abspath(work_dir)), 'dist')):
    # todo: add file search and merge with index
    # todo: report csv extract of artist, upload_name, upload_date, file_name, index_id, index_status, file_status, file_location
    # metdadata
    metadata = []

    # get folders to scan
    subfolders = [f.name for f in os.scandir(workdir) if f.is_dir()]
    scandirs = []
    for i in subfolders:
        if len(i) == 40:
            scandirs.append(i)

    # get files to read
    readfiles = []
    for i in scandirs:
        try:
            readfiles.append(os.path.join(workdir, i, 'metadata.json'))
        except FileNotFoundError as err:
            logging.debug(str(err))

    # read files
    for i in readfiles:
        try:
            with open(i) as json_file:
                metadict = json.load(json_file)
                metadata.append(metadict)
        except FileNotFoundError as err:
            logging.debug(str(err))

    # read the index
    try:
        with open(Path(os.path.join(workdir, 'index.json'))) as json_file:
            index = json.load(json_file)
    except FileNotFoundError as err:
        logging.debug(str(err))

    # show what we have got and merge with index
    cat = []
    for query in metadata:
        for metadict in query:
            metadict['index_data'] = []
            for f in metadict['files']:
                element = {}
                en = hashlib.sha1(f['download_url'].encode('utf-8')).hexdigest()
                element[en] = {
                    "download_url": f['download_url'],
                    "download_name": f['file_name'],
                    "download_folder": os.path.join(metadict['user_name'], metadict['upload_name']),
                }
                index_ident = hashlib.sha1(str(element[en]).encode('utf-8')).hexdigest()
                element[en]['index_id'] = index_ident
                if index_ident in index:
                    element[en]['indexed'] = True
                else:
                    element[en]['indexed'] = False
                metadict['index_data'].append(element[en])
            cat.append(metadict)
    return cat


def test_query(query_construct, base_url='http://ccmixter.org/api/query?', details=False):
    # construct an api request from given dict
    rquery = False
    foundfields = []
    ok = True

    for key in query_construct:
        if not rquery:
            rquery = str(key) + '=' + str(query_construct[key])
        else:
            rquery = rquery + '&' + str(key) + '=' + str(query_construct[key])
    rquery = base_url + rquery

    try:
        # http.client._MAXLINE = 655360  # hack to allow for too big api headers
        req = requests.Session().get(rquery, timeout=300)
        for f in req.json():
            # trying to read the nessecary fields to download files
            try:
                foundfields.append(f['user_name'])
                foundfields.append(f['upload_name'])
                foundfields.append(f['upload_id'])
            except KeyError:
                ok = False

            for fi in f['files']:
                try:
                    foundfields.append(fi['download_url'])
                    foundfields.append(fi['file_name'])
                    foundfields.append(fi['file_format_info']['mime_type'])
                except:
                    ok = False
    except:
        ok = False

    if not details:
        return ok
    else:
        return ok, rquery, foundfields


def request_ccm(artist, limit, q=False, config={}):
    # construct an api request and download folder
    rquery = False

    if not q:
        # artist
        query_construct = {
            'user': artist,
            'dataview': 'list_narrow',  # 'files', list_narrow
            'format': 'json',
            'limit': limit
        }
    else:
        query_construct = q

    for key in query_construct:
        if not rquery:
            rquery = str(key) + '=' + str(query_construct[key])
        else:
            rquery = rquery + '&' + str(key) + '=' + str(query_construct[key])

    rquery = config['api']['base_url'] + rquery
    tgf = config['local']['base_path'] / str(hashlib.sha1(rquery.encode('utf-8')).hexdigest())
    logging.info('query executed: \n' + Fore.GREEN + str(rquery) + '\n generated download folder: \n' +
                 Fore.GREEN + str(tgf))

    # execute the api request
    logging.info('requesting ccmixter with ' + rquery)
    http.client._MAXLINE = 65536001  # hack to allow for too big api headers
    req = requests.Session().get(rquery, timeout=60, proxies=config['local']['proxy'])

    return tgf, rquery, req, req.json()


def get_valid_filename(s):
    # from https://github.com/django/django/blob/master/django/utils/text.py
    s = str(s).strip().replace(' ', '_')
    t = re.sub(r'(?u)[^-\w.]', '_', s)
    return str(t).strip().replace('__', '_').strip('_')


def generate_download_list(rdata, runlevel):
    # prepare download list with all filenames and if zipped get the files structure to unpack to
    dwn = []
    for f in rdata.json():
        for fi in f['files']:
            element = {}
            en = hashlib.sha1(fi['download_url'].encode('utf-8')).hexdigest()
            myfolder = os.path.join(f['user_name'], f['upload_name'])
            element[en] = {
                "download_url": fi['download_url'],
                "download_name": fi['file_name'],
                "download_folder": get_valid_filename(myfolder),
            }
            if fi['file_format_info']['mime_type'] == "application/zip":
                element[en]['download_extract'] = []
                for u in fi['file_format_info']['zipdir']['files']:
                    a = re.search(r'/(.+)\s.+\(', u)
                    element[en]['download_extract'].append(a.group(1))
            dwn.append(element)
    if runlevel:
        print(Back.RED + json.dumps(rdata.json(), sort_keys=True, indent=4))
        print(Back.BLUE + json.dumps(dwn, sort_keys=True, indent=4))
    return dwn


def download_file(ccmfile, tf, td, config, headers=None, cookies=None):
    # download and extract files
    # todo: extract tar, rar, ...
    try:

        # add referer to the request header
        headers["Referer"] = ccmfile['download_url']

        with tf.open('wb') as o:
            m = requests.Session().get(
                ccmfile['download_url'],
                allow_redirects=True,
                stream=True,
                proxies=config['local']['proxy'],
                headers=headers,
                cookies=cookies)
            logging.info(Fore.RED + 'downloading ' + ccmfile['download_url'])
            logging.debug(m.cookies.get_dict())
            for data in tqdm(m.iter_content(),
                             ascii=True, unit_scale=True, ncols=80, unit='b', ):
                o.write(data)

        if ccmfile['download_name'].endswith('.zip'):
            logging.info('extracting ' + str(ccmfile['download_extract']))
            try:
                with zipfile.ZipFile(tf, "r") as z:
                    z.extractall(td)
            except zipfile.BadZipFile as err:
                logging.error(err)
        return True
    except Exception as e:
        logging.error(str(e))
        return False


def download_files(tf, config, downloads, target_folder, metadata):
    def cli_escape():
        """
        # opens a new browser tab and the ccmixter website, which is needed to
        # get and set cookies and stuff, to be allowed to download files

        https://github.com/fake-useragent/fake-useragent

        https://github.com/borisbabic/browser_cookie3

        https://docs.python.org/3/library/webbrowser.html

        """

        response = None
        while response not in {"chrome", "firefox", "safari"}:
            response = input("Please enter chrome or firefox or safari: ")
            try:
                # browser selection
                ua = UserAgent()
                if response == 'chrome':
                    webbrowser.get(using='chrome').open('http://ccmixter.org', new=2)
                    cookies = browser_cookie3.chrome(domain_name='ccmixter.org')
                    headers = {
                        "User-Agent": ua.chrome,
                        # to be set later: "Referer": ccmfile['download_url'],
                        "Host": "ccmixter.org"
                    }
                elif response == 'safari':
                    webbrowser.get(using='safari').open('http://ccmixter.org', new=2)
                    cookies = browser_cookie3.safari(domain_name='ccmixter.org')
                    headers = {
                        "User-Agent": ua.safari,
                        # to be set later: "Referer": ccmfile['download_url'],
                        "Host": "ccmixter.org"
                    }
                else:
                    webbrowser.get(using='firefox').open('http://ccmixter.org', new=2)
                    cookies = browser_cookie3.firefox(domain_name='ccmixter.org')
                    headers = {
                        "User-Agent": ua.firefox,
                        # to be set later: "Referer": ccmfile['download_url'],
                        "Host": "ccmixter.org"
                    }

                timer = 15
                while timer > 0:
                    time.sleep(1)
                    timer -= 1
                    logging.info('Waiting for {} seconds'.format(timer))

            except Exception as err:
                logging.error(f'{err}')
                cookies, headers = None, None

            return cookies, headers

    cookies, headers = cli_escape()

    try:
        with open(config['local']['index']) as json_file:
            index = json.load(json_file)
    except FileNotFoundError:
        index = []

    for d in downloads:

        for k in d.keys():
            logging.debug(d[k]['download_name'])
            if not config['local']['dryrun']:
                logging.info('downloading ' + d[k]['download_name'])
                ftd = tf / d[k]['download_folder']
                ftf = ftd / d[k]['download_name']
                os.makedirs(ftd, exist_ok=True)
                logging.debug('downloader working at ' + str(k) + ' which is ' + str(d[k]))
                if not str(hashlib.sha1(str(d[k]).encode('utf-8')).hexdigest()) in index:
                    try:
                        logging.debug(str(d[k]))
                        if download_file(d[k], ftf, ftd, config, headers, cookies):
                            # only update index if everything went ok
                            index.append(str(hashlib.sha1(str(d[k]).encode('utf-8')).hexdigest()))

                            # writing index and metadata
                            # todo: better update instead of writing full index each time
                            logging.debug('writing index:' + str(config['local']['index']))
                            with open(config['local']['index'], 'w') as j_file:
                                json.dump(index, j_file)

                            logging.debug('appending to: ' + str(tf / 'metadata.json'))
                            pf = target_folder / 'metadata.json'
                            with open(pf, 'w+') as js_file:
                                json.dump(metadata, js_file)

                    except FileNotFoundError as err:
                        logging.error(str(err))

                    except Exception as e:
                        print(e)
                else:
                    logging.info(d[k]['download_name'] + ' already downloaded')
            else:
                logging.info('dry running ' + d[k]['download_name'])


def run_itq(config):
    my_query_construct = {}
    done = False
    while not done:
        user_help = """
##########################################
- type ask to manually set a selection 
  of api parameters
- type quit to exit
##########################################\n
your selection :>
        """
        uin = input(user_help)
        print(uin)

        if uin == 'quit':
            done = True
        elif uin == 'ask':
            for param in apidocs['parameters']:
                user_help = '# please set ' + param + '\n' + ' ' + str(apidocs['parameters'][param]['desc']) + '\n' \
                            + str(apidocs['parameters'][param]['val']) + ' #\n:>'
                my_query_construct[param] = input(user_help)

            # overwrite with data view defaults
            my_query_construct['dataview'] = 'list_narrow'  # 'files', list_narrow
            my_query_construct['format'] = 'json'

            # overwrite limit for test
            try:
                olimit = my_query_construct['limit']
            except IndexError:
                olimit = 10
            my_query_construct['limit'] = '1'

            # execute query
            status, queryreturn, fnffld = test_query(my_query_construct, details=True)
            if not status:
                logging.warning(Fore.RED + 'this query does not deliver downloadable files, it returns:')
                logging.warning(Fore.BLUE + str(queryreturn) + str(queryreturn.text))
                done = False
            else:
                print(Fore.GREEN + str(status), my_query_construct)
                # send query request, restore limit
                my_query_construct['limit'] = olimit
                target_folder, query, r, metadata = request_ccm('', my_query_construct['limit'], my_query_construct,
                                                                config=config)
                # generate a list of downloadable files
                downloads = generate_download_list(r, config['local']['dryrun'])
                for i in downloads:
                    for y in i:
                        logging.info(i[y]['download_name'])
                # go = False
                while True:
                    print('download these files?')
                    uip = input('type yes to download or no to leave \n :>')
                    if uip == 'yes':
                        return target_folder, query, r, metadata
                    if uip == 'no':
                        print('cu')
                        sys.exit(0)
        else:
            done = False
