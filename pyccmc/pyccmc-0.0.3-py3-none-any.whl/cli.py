#!/usr/bin/env python
import argparse
import logging

from pyccmc.api import *

print(
    "Download and Extract Ccmixter Artists uploads and work with the metadata. "
    "Api documentation: http://ccmixter.org/query-api")

# script info
__author__ = 'tigabeatz'
__contact__ = 'https://dev.azure.com/kreaterra/_git/ccmclient'
__license__ = 'gpl-3.0'
__version__ = '0.0.3'

PROGRAM_HELP = """
###########################################################
- just type a username (secret mixter mode)

OR

- type itq to start interactive query mode
- type mdm to generate metadata list for downloaded files
- type graph to vizualize the network of uploads and remixes 
  centering on the users uploads

###########################################################\n
your selection:"""


def add_args():
    # command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", help="Check if this tool is working",
                        default=False)
    parser.add_argument("--artist", help="An Ccmixter artist name")
    parser.add_argument("--limit", help="Maximum allowed results",
                        default=10)
    parser.add_argument("--dryrun", help="Do not download data files",
                        default=False)
    parser.add_argument("--itq", help="Interactive query api parameters",
                        default=False)
    parser.add_argument("--mdm", help="manage metadata",
                        default=False)
    parser.add_argument("--graph", help="prepare for graph display",
                        default=False)
    parser.add_argument("--proxy", help="http(s):\\url:port")
    parser.add_argument("--query", help="json with cc mixter api parameters {user:tigabeatz;limit:1}")
    parser.add_argument("--folder", help=" where to store your requests data, defaults to ccmclient folder",
                        default=os.path.dirname(os.path.abspath(work_dir)))
    parser.add_argument("--logfile", help="C:/ccmrepo/ccmclient.log",
                        default=os.path.dirname(os.path.abspath(work_dir)) + '/ccmclient.log')
    parser.add_argument("--index", help="e.g. C:/ccmrepo/index.json; used to keep track of already "
                                        "downloaded files accross different queries",
                        default=os.path.dirname(os.path.abspath(work_dir)) + '/index.json')

    return parser.parse_args()


def main():
    # color shell initialization
    init(autoreset=True)

    args = add_args()

    # logging
    logging.basicConfig(filename=os.path.join(os.path.abspath(work_dir), Path(args.logfile)), filemode='w',
                        level=logging.INFO,
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

    logging.debug(str('setup: ') + ' sys: ' + sys.version + ' ' + sys.platform + ' ccmclient version: '
                  + __version__)

    # settings
    config = {}
    config['local'] = {
        "base_path": Path(args.folder),
        "index": Path(args.index),
        "dryrun": False,
        "proxy": {
            "http": args.proxy,
            "https": args.proxy,
            "ftp": args.proxy
        }
    }
    config['local']['dryrun'] = args.dryrun
    config['api'] = {
        "base_url": "http://ccmixter.org/api/query?"
    }

    # #### handle cli options and request cc mixter api ####
    cleave = False
    try:
        if args.graph:
            a = str(input('username'))
            b = int(input('limit'))
            c = int(input('maxdepth'))
            gd = get_connected_upload_ids(a, b, c)
            cleave = True
            with open(os.path.join(os.path.dirname(os.path.abspath(work_dir)), 'user_graph.json'), 'w') as o:
                o.write(gd)
            print('written to user_graph.json')
        # metadata manager
        elif args.mdm:
            cleave = True
            with open(os.path.join(os.path.dirname(os.path.abspath(work_dir)), 'metacat.json'), 'w') as o:
                o.write(json.dumps(metaclient(os.path.dirname(os.path.abspath(work_dir))),
                                   indent=4))
            print('written to metacat.json')

        # test this application
        elif args.test:
            print('hello mixter!')
            sys.exit()


        # advanced query per ui
        elif args.itq:
            # importing the dictionary of ccmixter api fields
            # from apidocs import apidocs
            target_folder, query, r, metadata = run_itq(config)
            cleave = True

        # advanced query per args
        elif args.query:
            my_query_construct = json.loads(str(args.query))

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
                print(Fore.RED + 'this query does not deliver downloadable files, it returns:')
                print(Fore.BLUE + str(queryreturn.text))
                logging.error('query does not deliver any downloadable results')
                raise ValueError('query does not deliver any downloadable results')
            else:
                print(Fore.GREEN + str(status), my_query_construct)
                # send query request, restore limit
                my_query_construct['limit'] = olimit
                target_folder, query, r, metadata = request_ccm('', my_query_construct['limit'], my_query_construct,
                                                                config=config)

        # get user input if not set by parameters
        elif (not args.artist) and (not args.query) and (not args.itq) and (not args.mdm):

            uin = input(PROGRAM_HELP)
            print(uin)

            if uin == 'itq':
                target_folder, query, r, metadata = run_itq(config)
                cleave = True
            elif uin == 'graph':
                a = str(input('username'))
                b = int(input('limit'))
                c = int(input('maxdepth'))
                gd = get_connected_upload_ids(a, b, c, config)
                cleave = True
                with open(os.path.join(os.path.dirname(os.path.abspath(work_dir)), 'user_graph.json'), 'w') as o:
                    o.write(gd)
                print('written to user_graph.json')
            elif uin == 'mdm':
                cleave = True
                with open(os.path.join(os.path.dirname(os.path.abspath(work_dir)), 'metacat.json'), 'w') as o:
                    o.write(json.dumps(metaclient(os.path.dirname(os.path.abspath(work_dir))),
                                       indent=4))
                print('written to metacat.json')
            else:
                # config['user'] = input('ccmixter artists user name:')
                config['user'] = uin
                config['limit'] = input('limit of api results, defaults to 10:')
                while len(config['user']) == 0:
                    config['user'] = input('ccmixter artists user name:')
                if len(config['limit']) == 0:
                    config['limit'] = 10
                # send artists api request
                target_folder, query, r, metadata = request_ccm(config['user'], config['limit'], config=config)

        # just use the args, quick download of a mixters uploads
        elif args.artist and args.limit:
            config['user'] = args.artist
            config['limit'] = args.limit
            # send artists api request
            target_folder, query, r, metadata = request_ccm(config['user'], config['limit'], config=config)
        else:
            print(Fore.RED + str(args) + 'INVALID ARGUMENTS')
            raise NotImplementedError('function combination not implemented')
    except NotImplementedError as err:
        print(Fore.WHITE + str(err))
        sys.exit()
    except InterruptedError:
        if not cleave:
            print(Fore.RED + 'error during setup')
        # ask user to quit
        if not args.artist:
            while True:
                if input('to close ccmclient type y:') == 'y':
                    sys.exit()
        else:
            sys.exit()

    if not cleave:
        # downloading and processing, updating index and metadata, will exit because of error (r == empty)
        # if selection failed
        try:
            logging.debug('creating downloads')

            # generate a list of downloadable files
            downloads = generate_download_list(r, config['local']['dryrun'])

            logging.debug('the downloads are: ' + str(downloads))
            # logging.debug(str(downloads))
            with open(os.path.join(os.path.dirname(os.path.abspath(work_dir)), 'downloads.json'), 'w+') as o:
                o.write(json.dumps(downloads)),

            if len(downloads) == 0:
                raise ValueError('unknown artist name')

            for dl in downloads:
                for ld in dl:
                    logging.info('found: ' + str(dl[ld]['download_name']))

            # download and extract files, init index
            logging.info('downloading to ' + str(target_folder))
            download_files(target_folder, config, downloads, target_folder, metadata)

        except ValueError as err:
            logging.error(str(err))
        except NotImplementedError as err:
            logging.error(err)
        except InterruptedError:
            if not cleave:
                print(Fore.RED + 'error during setup')
            logging.error('something happend. check the log, index and metadata files for details')
        except Exception as e:
            print(str(e))
        finally:
            # ask user to quit
            if not args.artist:
                logging.debug('done')
                print(Fore.RED + 'bye, happy mixting!')
                sys.exit()

            else:
                sys.exit()
    sys.exit()


if __name__ == '__main__':
    main()
