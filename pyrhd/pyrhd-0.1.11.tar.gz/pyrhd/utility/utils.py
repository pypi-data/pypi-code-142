import json
import os
import pathlib
import threading
from multiprocessing import Process
from typing import Callable, List, Optional, Sequence, Tuple, Union

import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet
from pyrhd.utility.cprint import aprint


class Utils:
    class requests:
        @staticmethod
        def sourceCode(
            url: Union[str, requests.models.Response],
            selector: str,
            header: Optional[dict] = None,
            cookies: Optional[dict] = None,
        ) -> ResultSet:
            """Returns the selected elements from html source code

            Args:
                url (Union[str, requests.models.Response]): There can be two inputs
                    1. str: when the URL is given, make a request implicitly and then parse the response
                    2. Response: when request is already sent by the calling function, and just need to parse the respose

                selector (str): CSS Selector to select the elements

            Returns:
                ResultSet: Selected elements from the DOM (html source code)
            """
            # If the given url the URL in 'string' format
            if type(url) is str:
                url = requests.get(url, cookies=cookies, headers=header)
            plain_text = url.text
            if url.status_code != 200:
                return []
            # return the selected elements through Beautifulsoup and CSS selector
            return BeautifulSoup(plain_text, "html.parser").select(selector)

        def parseHeader(header_str: str) -> dict:
            """Convert a header in string datatype to dictionary format

            Args:
                header_str (str): header in str

            Returns:
                dict: header in dictionary

            Example:
                Header in str:
                    "
                    GET /wallpapers HTTP/2
                    Host: rog.asus.com
                    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0
                    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
                    Accept-Language: en-US,en;q=0.5
                    Accept-Encoding: gzip, deflate, b
                    "
                to python dict:
                    {
                        'Host': 'rog.asus.com',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Accept-Encoding': 'gzip, deflate, br'
                    }
            """
            d = {}
            lines = header_str.splitlines()
            try:
                a, b = lines[0].strip(": ")
            except:
                lines = lines[1:]

            for line in lines:
                a, b = line.split(": ")
                d[a.strip()] = b.strip()
            return d

        def parseCSSPath(css_path: str) -> str:
            """Parse tag names from the css path

            Args:
                css_path (str): CSS path with tag + (id or class or none)

            Returns:
                str: CSS path with only tag

            Example:
                input:  'html body#rogProduct.vsc-initialized div.layout_default div.main-container.container-s.wp-container section.rog-container.rog-container-m'
                output: 'html body div div section'
            """
            return " ".join(i.split(".")[0].split("#")[0] for i in css_path.split())

    class os:
        @staticmethod
        def makedir(path: str, verbose: bool = False) -> None:
            """Checks whether the given path/directory is present or not,
            if not present, creates one

            Args:
                path (str): Path of the directory to be created
                verbose (bool, optional): Verbose. Defaults to False.
            """
            if not os.path.exists(path):
                os.mkdir(path)
                if verbose:
                    aprint(f"✅  Directory created : '{path}'", "green")
            elif verbose:
                aprint(f"⚠️   Directory existed : '{path}'", "cyan")

        @staticmethod
        def makedirs(path: str, verbose: bool = False) -> None:
            """Calls os.makedirs(path[, exist_ok=True])
                Super-mkdir; create a leaf directory and all intermediate ones.  Works like
                mkdir, except that any intermediate path segment (not just the rightmost)
                will be created if it does not exist. If the target directory already
                exists, don't raise an OSError. This is recursive.

            Args:
                path (str): Path of the directory to be created
                verbose (bool, optional): Verbose. Defaults to False.
            """
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)
                if verbose:
                    aprint(f"✅  Directory created recursively: '{path}'", "green")
            elif verbose:
                aprint(f"⚠️   Directory existed : '{path}'", "cyan")

        @staticmethod
        def cleanPathName(text: str) -> str:
            """Clean the path name according ot the Windows 10 file system rule

            Args:
                text (str): path

            Returns:
                str: cleaned path with no illegal character
            """
            excluded = ["\\", "/", "<", ">", "|", '"', "?", "*", ":"]
            return "".join(i for i in text.strip() if i not in excluded)

        @staticmethod
        def getCFD(f) -> str:
            """Get the absolute "Current File Directory" path

            Args:
                f (str): file absolute path

            Returns:
                str: Absolute path of the parent directory
            """
            return os.path.dirname(f)

        @staticmethod
        def getAllFiles(root_path: str) -> Sequence[str]:
            """Generates all the files present in a root folder (and its sub-folders recursively)

            Args:
                root_path (str): root path where files needs to be searched

            Returns:
                Sequence[str]: path of a single file at a time

            Yields:
                Iterator[Sequence[str]]: paths of all files
            """
            for path, subdirs, files in os.walk(root_path):
                for name in files:
                    yield pathlib.Path(pathlib.PurePath(path, name)).resolve().__str__()

    class threading:
        @staticmethod
        def joinThreads(thr: List[threading.Thread]) -> None:
            """Join all the threads present in the parameter list

            Args:
                thr (List[threading.Thread]): List of all the threads which are to be joined
            """
            [i.join() for i in thr]

        @staticmethod
        def createThread(
            target: Callable, args: Union[List, Tuple], thr_list: List[threading.Thread]
        ) -> threading.Thread:
            """Create a thread, append the thread to a given list
            for further use and finally start the thread.

            Args:
                target (function): target method /function to thread
                args (Union[List, Tuple]): list of arguments to be passed (must be in order)
                thr_list (list): List of threads

            Returns:
                threading.Thread: Newly created thread is returned after starting it
            """
            # Thread arguments must be a encapsulated in a tuple
            if type(args) != tuple:
                args = tuple(args)
            # Create a thread using threading module
            thread = threading.Thread(target=target, args=args)
            thr_list.append(thread)  # Appending to thread's list
            thread.start()  # Starting the thread
            return thread  # Return created thread

    class json:
        @staticmethod
        def saveDict(d: dict, file_path: str, indent: int = 4) -> bool:
            """Save a dictionary in a json file with indentation

            Args:
                d (dict): dictionary to be saved
                file_path (str): path of the json file. All the parent folders must be present inorder to create a json file, else it will return False
                indent (int): Indentation to be used in the saved json file. Defaults to 4.

            Returns:
                bool: True if the operation is successful, else False
            """
            try:
                with open(file_path, "w") as f:
                    json.dump(d, f, indent=indent)
                return True
            except Exception as e:
                aprint(e, "red")
                return False

        @staticmethod
        def prettify(path: str, indent: int = 4) -> bool:
            """Prettify json file and save it back to the same file

            Args:
                path (str): path to the json file
                indent (int, optional): level of indentation. Defaults to 4.

            Returns:
                bool: True if the operation is successful, else False
            """
            try:
                with open(path, "r") as f:
                    tmp = json.load(f)
                with open(path, "w") as f:
                    json.dump(tmp, f, indent=indent)
                return True
            except Exception as e:
                aprint(e, "red")
                return False

    class bs4:
        @staticmethod
        def parseCSSSelector(CSS_Selector: str) -> str:
            elements = CSS_Selector.split()
            return " > ".join(i.split(".")[0].split("#")[0] for i in elements)

        @staticmethod
        def parseHeader(json: dict) -> dict:
            """Parse header from Firefox copied header

            Args:
                json (dict): copied header

            Returns:
                dict: actual header for requests module
            """
            x = list(json.values())[0]["headers"]
            return {i["name"]: i["value"] for i in x}

    class parser:
        @staticmethod
        def firefoxHeader(dikt: Optional[dict]) -> Optional[dict]:
            """Returns the parsed firefox header in dictionary

            Args:
                dikt (Optional[dict]): Dictionary to be parsed

            Returns:
                Optional[dict]: Newly parsed header dictionary
            """
            res = {}
            for j in dikt:
                for i in dikt[j]["headers"]:
                    res[i["name"]] = i["value"]
            return res

    class multiprocessing:
        @staticmethod
        def joinProcesses(proc_list: List[Process]) -> None:
            """Join all the processes present in the parameter list

            Args:
                proc_list (List[multiprocessing.Process]): List of all the processes which are to be joined
            """
            [i.join() for i in proc_list]

        @staticmethod
        def createProcess(
            target: Callable, args: Union[List, Tuple], proc_list: list
        ) -> Process:
            """Create a process, append the process to a given list
            for further use and finally start the process.

            Args:
                target (function): target method /function to process
                args (Union[List, Tuple]): list of arguments to be passed (must be in order)
                proc_list (list): List of processes

            Returns:
                multiprocessing.Process: Newly created process is returned after starting it
            """
            # Process arguments must be a encapsulated in a tuple
            if type(args) != tuple:
                args = tuple(args)
            # Create a process using multiprocessing module
            process = Process(target=target, args=args)
            proc_list.append(process)  # Appending to process's list
            process.start()  # Starting the process
            return process  # Return created process

    @staticmethod
    def site_map_colored(map: list[str]):
        print("Site structure:", "-" * 9)
        aprint("site", "magenta")
        indent = [0]
        i_len = [0]
        for ind, i in enumerate(map):
            initial = "****" if ind == 0 else "*   |"
            underline = "" if ind == 0 else "`" * (i_len[-1] + 1)
            line = f"{initial}{' '*(indent[-1]-i_len[-1]-2)}{underline}|- "
            aprint(line, "magenta", end="")
            aprint(f"{i} 1", "green")
            indent.append(indent[-1] + len(i) + 5)
            i_len.append(len(i) + 3)

        for ind, i in enumerate(map[::-1]):
            initial = "*   " if ind == len(map) - 1 else "*   |"
            indentation = indent.pop()
            last_len = i_len.pop()
            aprint(f"{initial}{' '*(indentation-last_len-3)}", "magenta", end="")
            aprint(("`." * (len(i) // 2 + 6))[: len(i) + 6], "cyan")
            aprint(f"{initial}{' '*(indentation-last_len-3)}|- ", "magenta", end="")
            aprint(f"{i} n", "green")

        aprint("*****", "magenta")
        print("-" * 25)

    @staticmethod
    def site_map(map: list[str]):
        content = []
        content.append("site")
        indent = [0]
        i_len = [0]
        for ind, i in enumerate(map):
            initial = "****" if ind == 0 else "*   |"
            underline = "" if ind == 0 else "`" * (i_len[-1] + 1)
            line = f"{initial}{' '*(indent[-1]-i_len[-1]-2)}{underline}|- {i} 1"
            indent.append(indent[-1] + len(i) + 5)
            i_len.append(len(i) + 3)
            content.append(line)

        for ind, i in enumerate(map[::-1]):
            initial = "*   " if ind == len(map) - 1 else "*   |"
            indentation = indent.pop()
            last_len = i_len.pop()
            many = ("`." * (len(i) // 2 + 6))[: len(i) + 6]
            many = f"|{many[:-1]}" if ind == len(map) - 1 else many
            line1 = f"{initial}{' '*(indentation-last_len-3)}{many}"
            content.append(line1)
            line2 = f"{initial}{' '*(indentation-last_len-3)}|- {i} n"
            content.append(line2)

        content.append("*****")
        print("\n".join(content))
