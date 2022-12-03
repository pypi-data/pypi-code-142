# -*- coding: utf-8 -*-
###############################################################################
# author       # TecDroiD
# date         # 2022-12-02
# ---------------------------------------------------------------------------
# description  # a Template for files or directories
#              #
#              #
##############################################################################
import json
import base64
import os
import logging


def pattern_replace(text, pattern, pre='{{', post='}}'):
    ''' replace text with pattern if possible
    '''
    haystack = text
    for key,value in pattern.items():
        logging.debug(f'replacing {key} with {value}')
        haystack = haystack.replace(pre+key+post, value)
    return haystack

class Template():
    ''' this is a filesystem template for upm
    '''
    def from_file(filename):
        ''' read a json file and create a template from it
        '''
        name = os.path.basename(filename)
        with open(filename) as fp:
            template = Template('')
            template.values = json.load(fp)
            return template
        return None

    def scan(name, path, description='', _cpath='', _tmpl=None):
        ''' scan a directory to create a template
        '''
        logging.debug(f'scanning path {path}/{_cpath}')
        template = _tmpl if _tmpl is not None else Template(name, description)
        for file in os.listdir(os.path.join(path,_cpath)):
            # get all files in directory
            relpath = os.path.join(_cpath, file)
            filepath = os.path.join(path, relpath)
            if os.path.isdir(filepath):
                # scan subdirs
                Template.scan(name, path, description, relpath, template)
            else:
                #read file and append data
                with open(filepath, 'rb') as fp:
                    content = fp.read()
                    logging.debug(f'creating file {path}/{_cpath}/{file}')
                    template.add_item(_cpath, file, content)
        return template

    def __init__(self, name, description=''):
        ''' initialize a template
        '''
        self.values = {}
        self.values['name'] = name
        self.values['description'] = description
        self.values['files'] = {}

    def add_item(self, path, name, content=''):
        ''' create a directory path in files structure
        '''
        files = self.files
        if path != '':
            directory = path.split('/')
            # create directory struture if neccessary
            for subdir in directory:
                if not subdir in files:
                    files[subdir] = {}
                files = files[subdir]
        #create the file
        files[name] = base64.b64encode(content).decode('utf8')

    def write_content(self, filename, content, pattern):
        ''' write file content
        '''
        # entry is file
        with open(filename, 'wb') as fp:
            logging.debug(f'filecontent {content}')
            bcontent = base64.b64decode(content.encode('utf8')).decode()
            bcontent = pattern_replace(bcontent, pattern)
            # write file
            fp.write(bcontent.encode('utf8'))

    def create(self, basepath, pattern={}, _cpath='', _files=None ):
        ''' create the template file structure using the patterns
        for pattern replacement
        '''
        files = _files if _files is not None else self.files

        logging.debug(f'---- iteratinging subpath {_cpath}')
        for name,entry in files.items():
            logging.debug(f'** {_cpath} : having {name}')
            # replace
            nname = pattern_replace(name, pattern, '', '')
            relpath = os.path.join(_cpath, nname)
            abspath = os.path.join(basepath, relpath)
            if isinstance(entry, dict):
                # entry is a directory, create subdir
                logging.debug(f'creating directory {abspath}')
                if not os.path.exists(abspath):
                    os.mkdir(abspath)
                logging.debug(f'---- iterating into directory {relpath}')
                self.create(basepath, pattern, relpath, entry)
            else:
                # entry is a file, create and write
                logging.debug(f'creating file  {abspath}')
                self.write_content(abspath, entry, pattern)
         # done - hopefully..

    def dump(self, filename):
        ''' write yourself to a file
        '''
        with open(filename,'w') as fp:
            fp.write(self.json)

    def __repr__(self):
        desc = self.description
        if len(desc) == 0:
            desc ='<NO DESCRIPTION>'
        return f'Template {self.name}\n{desc}'

    @property
    def json(self):
        ''' dump the template to json
        '''
        return json.dumps(self.values, indent=2)

    @property
    def files(self):
        ''' get the files object of the template
        '''
        return self.values['files']

    @property
    def name(self):
        return self.values['name']

    @property
    def description(self):
        return self.values['description']


