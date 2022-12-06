#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path as osp
import collections
import importlib
from poppy.core.logger import logger

from poppy.core.generic.metaclasses import ManagerMeta
from poppy.core.configuration import Configuration
from poppy.core.tools.exceptions import print_exception
from poppy.core.generic.cache import CachedProperty
from poppy.core.generic.paths import Paths
from poppy.pop.tools import paths
from poppy.core.task import Task


__all__ = ["Plugin"]


class PluginError(Exception):
    """
    Errors related to plugin loading and definitions.
    """


class Plugin(object, metaclass=ManagerMeta):
    """
    Class to manage plugins module of the pipeline.
    """
    def __init__(self, module_name, module):
        """
        Store the information relative to plugins. Plugins should expose a
        tools module containing a from_config method which returns the absolute
        path to the configuration directory of the plugin with the name of the
        files or directory joined in arguments.
        """
        # store the name of the module
        self.module_name = module_name

        # store the module
        self.module = module


        # load the descriptor and store the name
        self.name = self.descriptor["identification.identifier"]

    def _check_module(self, module):
        """
        Check if a module inside the plugin is importable.
        """
        # name for loading
        name = ".".join([self.module_name, module])

        # first try to import a base for models that will be registered
        if importlib.util.find_spec(name):
            try:
                importlib.import_module(name)
            except ImportError as e:
                print_exception(
                    "Can't load {0} for plugin {1}:".format(
                        module,
                        self.name,
                    )
                )
                raise e

    def get_task_descriptor(self, name):

        tasks = self.tasks

        if name not in tasks:
            raise PluginError(
                "Task {0} not defined in plugin {1} descriptor".format(
                    name,
                    self.name,
                )
            )

        # and to the task information
        return tasks[name]


    def task(self, task_name):
        """
        Create a task from the definition and properties defined in the
        descriptor of the plugin.
        """
        # check that the task is defined in the descriptor
        tasks = self.tasks
        if task_name not in tasks:
            raise PluginError(
                "Task {0} not defined in plugin {1} descriptor".format(
                    task_name,
                    self.name,
                )
            )

        # create the task with the right properties
        return type(
            Task.to_camel_case(task_name),
            (Task,),
            {'plugin_name': self.name, 'name': task_name}
        )

    @CachedProperty
    def tasks(self):
        """
        Create a dictionary of tasks from their description in the plugin
        descriptor.
        """
        # container for tasks
        tasks_data = collections.defaultdict(dict)

        # get the tasks from the descriptor
        descriptor = self.descriptor
        tasks = descriptor["tasks"]

        # loop over tasks in the descriptor
        for task in tasks:
            # add the task
            storage = tasks_data[task["name"]]
            storage["name"] = task["name"]
            storage["category"] = task["category"]
            storage["description"] = task["description"]
            storage["inputs"] = list(task["inputs"].keys())
            storage["outputs"] = list(task["outputs"].keys())
            data = {}
            for name, target in task["inputs"].items():
                data[name] = {
                    "identifier": target["identifier"]
                }
            storage["input_targets"] = data
            data = {}
            for name, target in task["outputs"].items():
                data[name] = {
                    "identifier": target["identifier"]
                }
            storage["output_targets"] = data

        return tasks_data

    @CachedProperty
    def descriptor(self):
        """
        Return the dictionary of the contents of the descriptor of the plugin.
        """
        # check that the path for the descriptor exists
        # get descriptor_path
        descriptor_path = self.paths.from_root(
            "descriptor.json"
        )
        if not osp.isfile(descriptor_path):
            raise PluginError(
                "Cannot access to the descriptor of plugin {0}: {1}".format(
                    self.module_name, descriptor_path,
                )
            )
        else:
            self.descriptor_path = descriptor_path

        # try to read the JSON file
        try:
            data = Configuration(
                descriptor_path,
                paths.from_json_schemas("plugin-descriptor-schema.json"),
            )
            data.read_validate()
        except Exception as e:
            raise PluginError(
                "{0}\nCannot read JSON descriptor of plugin {1}".format(
                    str(e),
                    self.module_name,
                )
            )

        # all is good return data that will be stored in the descriptor
        return data

    @CachedProperty
    def identifier(self):
        return self.descriptor["identification.identifier"]

    @CachedProperty
    def version(self):
        return self.descriptor["release.version"]

    @property
    def module(self):
        return self._module

    @module.setter
    def module(self, module):
        """
        Store the module and check for the good interface of the plugin.
        """
        # keep trace of the module
        self._module = module

        # check that the module is a package
        if not hasattr(self.module, "__path__"):
            raise PluginError(
                "Plugin {0} is not a package".format(self.name)
            )

        # reference the module paths in the plugin (the __path__ contains
        # several paths for importing subpackages, but the first if the package
        # is not doing fancy things should be the root directory of the
        # package, so we only keep the first one as root)
        self.paths = Paths(self.module.__path__[0])

        # load the tasks definitions from the descriptor
        self.tasks

    def load(self):
        """
        Check the integrity of the module after all the rest has been done.
        Imports also module for registration of some commands, tasks, etc.
        """
        # make some verification about the plugin
        # import models
        self._check_module("models")

        # import commands
        self._check_module("commands")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __repr__(self):
        return "Plugin(name={0})".format(self.name)
