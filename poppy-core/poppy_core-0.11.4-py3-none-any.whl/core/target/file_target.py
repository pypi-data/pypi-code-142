#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import os
import os.path as osp
import uuid
from contextlib import contextmanager

from poppy.core.db.dry_runner import DryRunner
from poppy.core.generic.cache import CachedProperty
from poppy.core.logger import logger
from poppy.core.target.base_target import BaseTarget
from poppy.pop.tools import compute_file_sha

__all__ = ["FileTarget"]


class FileTargetException(Exception):
    pass


class FileTarget(BaseTarget):
    """
    FileTarget class
    """

    def __init__(self, *args, filepath=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.filepath = filepath

    def update(self, *args, filepath=None, **kwargs):
        """
        Update the file target instance with the given args/kwargs

        Updated attributes:
          - filepath

        :return:
        """

        super().update(*args, **kwargs)

        if filepath is not None:
            if self.filepath != filepath:  # and self.filepath is not None:
                logger.warning(f"Filepath of FileTarget '{self.id}' was defined multiple times")
            self.filepath = filepath

    def __iter__(self):
        if not self._is_multi_target:
            raise FileTargetException("Simple targets are not iterable, use the 'many=True' flag to generate "
                                      "multi-target objects")

        for idx, filepath in enumerate(self.filepath):
            # TODO: add parametrization of the target id
            yield FileTarget(f"__{self.id}__{idx}__", self._pipeline, filepath=filepath)

    @property
    def filepath(self):
        if self._filepath:
            return self._filepath
        if callable(self._filepath_generator):
            self._filepath = self._filepath_generator(self._pipeline)
            return self._filepath
        return None

    @filepath.setter
    def filepath(self, value):
        # if the filepath was given as a function
        if callable(value):
            self._filepath_generator = value
            self._filepath = None
        else:
            self._filepath_generator = None
            self._filepath = value

    @property
    def file_directory(self):
        if not self._file_directory:
            self._file_directory = osp.dirname(self.filepath)
        return self._file_directory

    @file_directory.setter
    def file_directory(self, value):
        if not osp.isdir(value):
            logger.error("INPUT VALUE IS NOT A VALID DIRECTORY!")
            raise IsADirectoryError
        else:
            self._file_directory = value

        # Update the file path
        self.filepath = osp.join(value, self.filename)

        # indicate that dirname has changed
        self.target_changed()

    @property
    def filename(self):
        if not self._filename:
            self._filename = osp.basename(self.filepath)
        return self._filename

    def get_filename(self):
        return self.name

    def get_filedir(self):
        return self.dir

    @CachedProperty
    def uuid(self):
        # create an uuid
        return uuid.uuid4()

    def get_filesha(self):
        # Return the sha256 of the target file (hexdigest)
        if not self.sha:
            try:
                self.sha = compute_file_sha(self.filepath)
            except:
                logger.debug(
                    "SHA256 cannot be computed because file does not exist, skipping!")
            else:
                self.sha = self.sha.hexdigest()

        return self.sha

    def set_filesha(self):
        """Set the SHA (in case of file update)"""
        try:
            self.sha = compute_file_sha(self.filepath)
        except:
            logger.debug(
                "SHA256 cannot be computed because file does not exist, skipping!")
        else:
            self.sha = self.sha.hexdigest()

        # indicate that filesha has changed
        self.target_changed()

        return self.sha

    def set_dirname(self, value):
        """
        To change the directory of the target file.
        """
        self.file_directory = value

    @DryRunner.dry_run
    def target_changed(self):
        """
        Recreate the representation of the target if it changed.
        """
        return  # FIXME: create/handle new target database model

        # modify the status
        self.representation.file_state = self._state
        self.representation.file_status = self._status

        # modify the file_dir
        self.representation.file_dir = self.dir

        # modify the file_sha
        self.representation.file_sha = self.sha

    def open(self, *args, **kwargs):
        """
        A wrapper around the open function of the file.
        """
        if self._is_multi_target:
            raise FileTargetException("Multi-target instances are not openable, use the 'many=False' flag to generate "
                                      "a simple target object")

        class FileOpen(object):

            def __enter__(instance):
                self.pending()
                self.file = open(self.filepath, *args, **kwargs)
                return self.file

            def __exit__(instance, type, value, traceback):
                if type is not None:
                    self.error()
                self.file.close()
                self.terminated()

        return FileOpen()

    @contextmanager
    def activate(self):
        """
        To use the target as a wrapper around other files type that cannot be
        opened as usual.
        """
        # mark as pending and ok
        self.ok()
        self.pending()

        # try to do the things inside the context
        try:
            # mark as in progress
            self.progress()
            yield
        except self.TargetEmpty as e:
            self.empty()
        except Exception as e:
            self.error()
            self.terminated()
            raise e
        else:
            # mark as terminated
            self.terminated()

    def exists(self):
        """
        Check that the file exists on the system.
        """
        if self.filepath:
            return osp.isfile(self.filepath)
        else:
            # For now, return None not target file
            logger.warning(
                "Target {0} seems to not be a file!".format(self.id))
            return None

    def size(self):
        """
        Return the size in bytes of the file, 0 if the file doesn't exist or
        there is any kind of problem.
        """
        try:
            return os.stat(self.filepath).st_size
        except:
            return 0

    def creation_date(self):
        """
        To get the creation date of a file. ctime does not give the creation
        time but the change time. Use mtime for last modification date instead.
        """
        try:
            return datetime.datetime.fromtimestamp(osp.getmtime(self.filepath))
        except:
            return None
