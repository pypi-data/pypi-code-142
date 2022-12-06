#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path as osp


class Paths(object):
    """
    Class to manage paths from a given root directory. It expects to have a
    root directory, with a config directory containing configuration files, a
    data directory containing some data resources and a scripts directory
    containing scripts to be executed. This is the standard structure of the
    ROC pipeline.
    """
    def __init__(self, root):
        self.root = root

    def from_root(self, *args):
        """
        Given a list of paths, do a concatenation of them with the root
        directory.
        """
        return osp.join(self._root, *args)

    def from_json_schemas(self, *args):
        """
        Given a list of paths, do a concatenation of them with the json schemas
        directory.
        """
        return osp.join(self.json_schemas, *args)

    def from_config(self, *args):
        """
        Given a list of paths, do a concatenation of them with the configuration
        directory.
        """
        return osp.join(self.config, *args)

    def from_scripts(self, *args):
        """
        Given a list of paths, do a concatenation of them with the scripts
        directory.
        """
        return osp.join(self.scripts, *args)

    def from_data(self, *args):
        """
        Given a list of paths, do a concatenation of them with the data
        directory.
        """
        return osp.join(self.data, *args)

    def from_templates(self, *args):
        """
        Given a list of paths, do a concatenation of them with the templates
        directory.
        """
        return osp.join(self.templates, *args)

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, root):
        """
        Check that the root is a valid directory.
        """
        if not osp.isdir(root):
            raise ValueError(
                "Root directory {0} is not a valid directory".format(root)
            )

        # store the root
        self._root = root

        # set also the scripts, config and data directories
        self.data = osp.abspath(osp.join(self._root, "data"))
        self.json_schemas = osp.abspath(osp.join(self._root, "json_schemas"))
        self.config = osp.abspath(osp.join(self._root, "config"))
        self.scripts = osp.abspath(osp.join(self._root, "scripts"))
        self.templates = osp.abspath(osp.join(self._root, "templates"))
