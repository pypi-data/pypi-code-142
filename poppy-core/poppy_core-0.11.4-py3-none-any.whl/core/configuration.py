#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path as osp
from poppy.core.logger import logger
import shutil
import jsonschema
import json
import sys

from poppy.core.generic.dot_dict import DotDict
from poppy.core.generic.metaclasses import ManagerMeta

__all__ = ["Configuration", "ConfigurationNotFound"]




class ConfigurationNotFound(Exception):
    """
    Exception for the case a configuration file is not found.
    """


class Configuration(DotDict, metaclass=ManagerMeta):
    """
    Class to manage parameters from the configuration file easily, retrieve
    them and setting them again.
    """
    def __init__(self, filename=None, schema=None, name=None, *args, **kwargs):
        """
        To set the filename of the configuration file to read.
        """
        # Configure as usual
        super(Configuration, self).__init__(*args, **kwargs)

        # store the file name
        self.filename = filename

        # store the schema
        self.schema = schema

        # set the name used to register the configuration
        self.name = name

    def read(self):
        """
        Read the configuration file in the json format and set the parameters
        inside the instance itself.
        """
        # check the filename is set
        if not self.filename:
            logger.error(
                "The filename must be set into the configuration class"
            )
            return

        # standard verification for the file
        if osp.isfile(self.filename):
            # open the file and read its structure in json
            with open(self.filename, 'rt') as f:
                # put parameters into dictionary
                logger.debug(
                    "Reading parameters from the configuration file " +
                    "{0}".format(self.filename)
                )
                self.update(json.load(f, object_pairs_hook=DotDict))

        else:
            raise ConfigurationNotFound(
                "The configuration file {0} doesn't exist".format(
                    self.filename
                )
            )

        # if the file extends another one, make a merge
        self.extends()

    def read_validate(self):
        """
        Read the configuration file in JSON format and validate with the schema
        provided.
        """
        # read the file as usual
        self.read()

        # check there is a schema
        if not self.schema:
            logger.error(
                "The path to the schema for {0} is not given".format(
                    self.filename
                )
            )
            sys.exit(-1)

        # read the schema
        schema = self.__class__(self.schema)
        schema.read()

        # check the validity of the descriptor against the schema
        jsonschema.validate(
            self,
            schema,
            format_checker=jsonschema.FormatChecker(),
        )

    def write(self):
        """
        Overwrite the content of the configuration file by the parameters
        actually set, and make a copy of the old file before doing it in order
        to preserve some errors when a problem occurred in the application. A
        clean copy of the configuration file should also always be available in
        SVN repository of the program.
        """
        # returns if filename not set
        if not self.filename:
            return

        # start by doing a copy of the old file (preserving mtime and atime)
        logger.debug("Backup the file into {0}".format(self.filename + "~"))
        shutil.copy2(self.filename, self.filename + "~")

        # now dump the parameters inside the json file
        logger.debug("Writing parameters to {0}".format(self.filename))
        with open(self.filename, "w") as f:
            json.dump(self, f, ensure_ascii=False, indent=4)

    def extends(self):
        """
        Check if the file extends another one, read it and make the merge
        between the source file and this one.
        """
        # check presence of the extends keyword
        if "extends" not in self:
            return

        # get the path of the file to extend
        path = self["extends"]

        # check that path is absolute or not
        if not osp.isabs(path):
            # relative path, make it absolute relatively to the current file
            # get path of the current file
            current = osp.abspath(osp.dirname(self.filename))

            # join the path to the current file
            path = osp.abspath(osp.join(current, path))

        # read the parent file
        parent = self.__class__(path)
        parent.read()

        # merge the two dictionaries
        self.merge(parent, self)
        self.update(parent)

    @classmethod
    def merge(cls, destination, source):
        """
        Recursively merge b dictionary into a dictionary.
        """
        # loop over items in the overriding dict
        for key, value in source.items():
            # check the value is a dictionary
            if isinstance(value, dict):
                # get the field with the key in the destination
                node = destination.get(key, {})

                # merge recursively the value
                cls.merge(node, value)
            else:
                # change the value
                destination[key] = value
