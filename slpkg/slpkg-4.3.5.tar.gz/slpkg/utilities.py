#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import shutil
import tarfile


from slpkg.configs import Configs


class Utilities:

    def __init__(self):
        self.configs = Configs

    def is_installed(self, package: str):
        """ Returns True if a package is installed. """
        for pkg in os.listdir(self.configs.log_packages):
            if package in pkg:
                return pkg

    @staticmethod
    def untar_archive(path: str, archive: str, ext_path: str):
        """ Untar the file to the build folder. """
        tar_file = f'{path}/{archive}'
        untar = tarfile.open(tar_file)
        untar.extractall(ext_path)
        untar.close()

    @staticmethod
    def remove_file_if_exists(path: str, file: str):
        """ Clean the old files. """
        archive = f'{path}/{file}'
        if os.path.isfile(archive):
            os.remove(archive)

    @staticmethod
    def remove_folder_if_exists(path: str, folder: str):
        """ Clean the old folders. """
        directory = f'{path}/{folder}'
        if os.path.isdir(directory):
            shutil.rmtree(directory)

    @staticmethod
    def create_folder(path: str, folder: str):
        """ Creates folder. """
        directory = f'{path}/{folder}'
        if not os.path.isdir(directory):
            os.makedirs(directory)
