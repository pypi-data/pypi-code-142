# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
import glob
import os
import shutil
import zipfile

import yaml

"""
    File (such as file, io, html, xml etc) Utility.
"""


def get_app_file_path(app_root_path, *args):
    """get absolute path of file under app_root_path folder.
    :param str app_root_path:
    :param args: name sequence of path such as a,b,c
    :return:
    """
    path = os.path.join(app_root_path, *args)
    os.makedirs(path, exist_ok=True)
    return path


def zip_dir(dir_path, zipfile_path):
    filelist = []
    if os.path.isfile(dir_path):
        filelist.append(dir_path)
    else:
        for root, dirs, files in os.walk(dir_path):
            for name in files:
                filelist.append(os.path.join(root, name))

    zf = zipfile.ZipFile(zipfile_path, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dir_path):]
        zf.write(tar, arcname)
    zf.close()


def unzip_file(zipfile_path, savedir_path):
    if not os.path.exists(savedir_path):
        os.makedirs(savedir_path)
    zfile = zipfile.ZipFile(zipfile_path)
    for name in zfile.namelist():
        if name.endswith("/"):
            dirname = savedir_path + os.sep + name
            if os.path.exists(dirname):
                os.removedirs(dirname)
            os.makedirs(dirname)
        else:
            filename = savedir_path + os.sep + name
            if os.path.exists(filename):
                os.remove(filename)
            fd = open(filename, 'wb')
            fd.write(zfile.read(name))
            fd.close()
    zfile.close()


# copy all the files/directories under srcpath to despath
def copy_tree(srcpath, despath):
    if not os.path.exists(despath):
        os.makedirs(despath)
    srcfilenames = os.listdir(srcpath)
    for srcfilename in srcfilenames:
        srcfilepath = srcpath + os.sep + srcfilename
        if os.path.isdir(srcfilepath):
            shutil.copytree(srcfilepath, despath + os.sep + srcfilename)
        else:
            shutil.copy(srcfilepath, despath)


def delete_files(dir_path, extension):
    dir_list = os.listdir(dir_path)
    for entry in dir_list:
        entry_fp = dir_path + os.sep + entry
        if os.path.isdir(entry_fp):
            delete_files(entry_fp, extension)
        elif entry_fp.endswith(extension):
            os.remove(entry_fp)


def safe_write(filename, content):
    """Writes the content to a temp file and then moves the temp file to 
    given filename to avoid overwriting the existing file in case of errors.
    """
    f = open(filename + '.tmp', 'w')
    f.write(content)
    f.close()
    os.rename(f.name, filename)


def discover_files(directory, filename):
    """
        find all the files that file name is equal to filename.
        :param directory|string the absolutely path of directory to be discovered.
        :param filename|string the file name which is to be discovered.
        :return list of file absolute path. 
    """
    filepaths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if filename == file:
                absfile = os.path.join(root, file)
                filepaths.append(absfile)
    return filepaths


def read_file(filepath):
    f = open(filepath, 'r')
    try:
        content = f.read()
    finally:
        f.close()
    return content


def read_yaml(yaml_path):
    """Read yaml from file."""
    with open(yaml_path, 'rt') as f:
        config = yaml.load(stream=f, Loader=yaml.FullLoader)
        return config


def write_yaml(yaml_path, data):
    """Write data to yaml file."""
    with open(yaml_path, 'w') as f:
        yaml.dump(data, f, allow_unicode=True)
    return True


def write_file(file_path, data_string):
    """Write data to a file."""
    with open(file_path, 'w') as f:
        f.write(data_string)
    return True


def search_file(abs_dir_path, file_name):
    """Search file name in abs_dir_path
    :param str abs_dir_path: absolute path of directory to be searched.
    :param str file_name: such as *dict*.txt
    Return file path list being found.
    """
    paths = os.pathsep.join(glob.glob(os.path.join(abs_dir_path, file_name)))
    return paths
