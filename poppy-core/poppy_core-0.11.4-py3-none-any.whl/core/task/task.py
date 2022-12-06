#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from poppy.core.logger import logger

from .base_task import BaseTask


class Task(BaseTask):
    _targets_definition = None

    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # reset the targets definition attribute to avoid sharing targets definition with subclasses
        cls._targets_definition = {'inputs': [], 'outputs': []}

    @classmethod
    def legacy_as_task(cls, run_func=None, *, plugin_name=None, name=None, legacy=True):
        """
        Method used to ensure backward compatibility with the previous decorator API

        :param run_func: the decorated function
        :param plugin_name: the plugin name
        :param name: the task name
        :param legacy: flag indicating which API is used (the legacy or the new one)
        :return: a task class that run the decorated function
        """
        _plugin_name = cls.plugin_name if plugin_name is None else plugin_name
        _name = cls.name if name is None else name

        if legacy:
            logger.warning(f"Deprecation Warning: Task ('{_plugin_name}/{_name}') "
                           "should be declare with the new decorator API")

        return type(
            cls.to_camel_case(_name),
            (cls,),
            {'plugin_name': _plugin_name, 'name': _name, 'run': run_func}
        )

    @staticmethod
    def to_camel_case(snake_str):
        components = snake_str.split('_')
        # We capitalize the first letter of each component and join them together
        return ''.join(x.title() for x in components)

    @classmethod
    def as_task(cls, run_func=None, *, plugin_name=None, name=None):
        """
        Use the decorated function as a task

        :param run_func: the decorated function
        :param plugin_name: the plugin name
        :param name: the task name
        :return: a task class that run the decorated function
        """

        if run_func is None:
            def inner_function(_run_func):
                return cls.legacy_as_task(_run_func, plugin_name=plugin_name, name=name, legacy=False)

            return_value = inner_function
        else:
            return_value = cls.legacy_as_task(run_func)

        return return_value

    def instantiate_target(self, target_list, target_definition):
        """
        Instantiate a new target using the given definition and store the target id in a list

        :param target_list: the list used to store the target ids
        :param target_definition: the target definition
        :return:
        """
        target_class, identifier, args, kwargs = target_definition

        target_class(identifier, self.pipeline, *args, **kwargs)

        target_list.append(identifier)


    def instantiate_targets(self):

        # get the targets defined in the task class
        self.add_targets()

        # instantiate each target
        for target_definition in self._targets_definition['inputs']:
            self.instantiate_target(self._inputs, target_definition)

        for target_definition in self._targets_definition['outputs']:
            self.instantiate_target(self._outputs, target_definition)

    def add_targets(self):
        """
        Method to override to add targets

        :return:
        """
        pass

    def __init__(self, instance_name=None):
        plugin_instance = self.get_plugin()
        task_descriptor = self.get_descriptor()

        super().__init__(plugin=plugin_instance, descriptor=task_descriptor, instance_name=instance_name)

        # store the id of the inputs/outputs targets
        self._inputs = []
        self._outputs = []

    @property
    def inputs(self):
        """
        Generate a subset of the pipeline targets containing only the task inputs

        :return: the input targets
        """
        return {target_id: self.pipeline.targets[target_id] for target_id in self._inputs}

    @property
    def outputs(self):
        """
        Generate a subset of the pipeline targets containing only the task outputs

        :return: the output targets
        """
        return {target_id: self.pipeline.targets[target_id] for target_id in self._outputs}

    @classmethod
    def get_descriptor(cls):
        plugin_instance = cls.get_plugin()
        return plugin_instance.get_task_descriptor(cls.name)

    @classmethod
    def get_plugin(cls):
        from poppy.core.plugin import Plugin
        return Plugin.manager[cls.plugin_name]


    @classmethod
    def add_input(cls, target_class, identifier, *args, **kwargs):
        # create the targets def dict if not defined
        cls._targets_definition['inputs'].append((target_class, identifier, args, kwargs))

    @classmethod
    def add_output(cls, target_class, identifier, *args, **kwargs):
        cls._targets_definition['outputs'].append((target_class, identifier, args, kwargs))

    def input(self):
        task_descriptor = self.get_descriptor()
        return task_descriptor["inputs"]

    def output(self):
        task_descriptor = self.get_descriptor()
        return task_descriptor["outputs"]
