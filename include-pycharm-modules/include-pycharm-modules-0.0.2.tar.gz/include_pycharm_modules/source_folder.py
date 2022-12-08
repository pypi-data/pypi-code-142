import logging
import os
import re
import sys
import warnings

from bs4 import BeautifulSoup

log = logging.getLogger(__name__)


# generically add all pycharm source folders to the search path
def import_source_folders(path: str):
    idea_path = os.path.join(path, ".idea/")
    for file in os.listdir(idea_path):
        if file.endswith(".iml"):
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")

                file = os.path.join(idea_path, file)
                try:
                    page = open(file)
                    soup = BeautifulSoup(page.read(), 'lxml')
                    source_folders = soup.find_all('sourcefolder')
                    print("found", len(source_folders), "modlules to import in", file)

                    for source_folder in source_folders :
                        source = re.sub('^/', '', source_folder['url'].split("$MODULE_DIR$")[-1])
                        if source == "modules":
                            continue

                        module_path = os.path.join(path, source)
                        if os.path.exists(module_path):
                            print(f"adding module {module_path}")
                            sys.path.append(module_path)
                finally:
                    page.close()
