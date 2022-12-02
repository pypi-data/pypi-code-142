#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import os

from collections import deque
from pathlib import Path
# from logger import logger
from pycap2low.logger import logger
from pytrees import AVLTree
# from configuration import ConfigExcept
from pycap2low.configuration import ConfigExcept


def main() -> None:
    # arg_path = '/home/alex/Pro/'
    # arg_recursive = True
    # arg_str_camel_case = '-'
    # arg_excepts = '/home/alex/Desarrollo/Proyectos/py_scripts/pycap2low/pycap2low/except.txt'

    args = _parse_args()
    arg_path = str(Path(args.path).resolve())
    arg_str_camel_case = args.str_camel_case
    arg_recursive = args.recursive
    arg_excepts = args.excepts

    if not os.path.exists(arg_path):
        msg = 'Invalid directory path'
        logger.error(msg)
        raise ValueError(msg)

    if arg_path == os.getcwd():
        msg = 'The directory must be different from the current one'
        logger.error(msg)
        raise ValueError(msg)

    if arg_excepts and not os.path.exists(arg_excepts):
        msg = 'Invalid directory path except'
        logger.error(msg)
        raise ValueError(msg)
    
    if arg_recursive:
        if arg_excepts:
            cfg_excepts = ConfigExcept.load(arg_excepts)
            excepts = __avl_list__(cfg_excepts)
            __ren_listdir_rec_excepts__(arg_path, str_camel_case=arg_str_camel_case, excepts=excepts)
        else:
            __ren_listdir_rec__(arg_path, str_camel_case=arg_str_camel_case)        
    else:
        if arg_excepts:
            cfg_excepts = ConfigExcept.load(arg_excepts)
            excepts = __avl_list__(cfg_excepts)
            __ren_listdir_excepts__(arg_path, str_camel_case=arg_str_camel_case, excepts=excepts)
        else:
            __ren_listdir__(arg_path, str_camel_case=arg_str_camel_case)
        
def _parse_args():
    parser = argparse.ArgumentParser(prog='pycap2low',
                                     description='Convert all file and directory names to lower case')

    parser.add_argument('-v',
                        '--version',
                        action='version',
                        version='%(prog)s 2.0.0')
    parser.add_argument('-a',
                        '--author',
                        action='version',
                        version='%(prog)s was created by software developer Alexis Torres Valdes <alexisdevsol@gmail.com>',
                        help="Show program's author and exit")

    parser.add_argument('path', help='Path of the directory to rename')
    parser.add_argument('-r',
                        '--recursive',
                        action='store_true',
                        help='Apply changes recursively to subdirectories')
    parser.add_argument('--str-camel-case',
                        required=False,
                        help='Camel case separator chain')
    parser.add_argument('--excepts',
                        required=False,
                        help='File path with exceptions')
                        
    return parser.parse_args()

def __avl_list__(it: iter) -> AVLTree:
    avl = AVLTree()

    for e in it:
        avl.insert(e)

    return avl

def _lower(txt: str) -> str:
    return txt.lower()

def _rep_camel_case(txt: str, strr='-') -> str:
    txtr = ''

    for i in range(len(txt) - 1):
        char = str(txt[i])
        camel_case = char.islower() and str(txt[i + 1]).isupper()
        if camel_case:
            txtr += char.lower() + strr
            continue
        txtr += char.lower()
    if txtr != '':
        txtr += str(txt[len(txt) - 1]).lower()

    return txtr

def __ren_listdir_rec__(path: str, str_camel_case=None) -> None:
    func_ren = _lower if not str_camel_case else _rep_camel_case
    q = deque([path])
    while len(q):
        _path = q.popleft()
        for item in os.listdir(_path):
            p = os.path.join(_path, item)
            new_path = __rename__(p, func_ren)            
            if os.path.isdir(new_path):
                q.append(new_path)
    __rename__(path , func_ren)

def __ren_listdir_rec_excepts__(path: str, excepts: AVLTree, str_camel_case=None) -> None:
    func_ren = _lower if not str_camel_case else _rep_camel_case
    
    q = deque([path])
    while len(q):
        _path = q.popleft()
        for item in os.listdir(_path):
            p = os.path.join(_path, item)
            node = excepts.search(ConfigExcept(p))
            if node:
                if not node.val.recursive and os.path.isdir(node.val.path):
                    q.append(new_path)
            else:
                new_path = __rename__(p, func_ren)            
                if os.path.isdir(new_path):
                    q.append(new_path)

    if not excepts.search(ConfigExcept(path)):
        __rename__(path , func_ren)

def __ren_listdir__(path: str, str_camel_case=None) -> None:
    func_ren = _lower if not str_camel_case else _rep_camel_case
    
    for item in os.listdir(path):
        _path = os.path.join(path, item)
        __rename__(_path, func_ren)
    __rename__(path, func_ren)

def __ren_listdir_excepts__(path: str, excepts: AVLTree, str_camel_case=None) -> None:
    func_ren = _lower if not str_camel_case else _rep_camel_case
    
    for item in os.listdir(path):
        _path = os.path.join(path, item)
        if not excepts.search(ConfigExcept(_path)):
            __rename__(_path, func_ren)
    
    if not excepts.search(ConfigExcept(path)):
        __rename__(path, func_ren)

def __rename__(path: str, func_ren) -> str:
    i = path.rfind('/')
    name = path[i + 1:]
    new_path = os.path.join(path[:i], func_ren(name))
    if not os.path.exists(new_path):
        os.rename(path, new_path)
        logger.info("Renamed '%s' => '%s'" % (path, new_path))
        return new_path
    logger.info("Not renamed '%s'" % path)
    return new_path

if __name__ == '__main__':
    main()
