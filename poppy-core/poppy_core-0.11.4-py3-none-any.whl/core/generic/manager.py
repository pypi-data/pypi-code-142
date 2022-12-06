#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from poppy.core.logger import logger

from poppy.core.generic.signals import Signal

__all__ = ["Manager", "MultipleClassManager"]


class Manager(object):

    """
    A base class to manage objects needing to be registered, and to inform
    other objects of their creation, deletion, etc.
    """

    # keep the list of manager instances to delete their content at the end of the pipeline run
    manager_list = []

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        Manager.manager_list.append(instance)
        return instance

    def __init__(self):
        """
        Create containers and signals.
        """
        # containers
        self.availables = {}
        self.instances = []
        self.instancesByName = {}

        # signals
        self.added = Signal()
        self.created = Signal()
        self.deleted = Signal()

    def __getitem__(self, name):
        """
        Get an instance from the manager given only its name, as it was a
        dictionary.
        """

        try:
            return self.instancesByName[name]
        except:
            logger.error("POPPY COMPONENT '{0}' IS NOT DEFINED!\n".format(name) +
                         "(Check first in the descriptors and settings.py file)")
            raise ValueError(
                "POPPY COMPONENT '{0}' IS NOT DEFINED!\n".format(name) +
                         "(Check first in the descriptors and settings.py file)"
            )

    def __contains__(self, name):
        """
        Check if the manager contains a given instance by its name.
        """
        return name in self.instancesByName

    def __iter__(self):
        """
        Iter over all the class instances
        """
        return iter(self.instances)

    def add(self, name, cls):
        """
        Add a class to the register.
        """
        # check presence of the class or not
        if name in self.availables:
            logger.error("Class {0} already available".format(name))
            raise ValueError(
                "The class {0} is already defined".format(name)
            )

        # make the class available
        logger.debug("Class {0} now available".format(name))
        self.availables[name] = cls

        # send a signal with the name and the class
        self.added(name, cls)

    def create(self, instance):
        """
        Register created instance.
        """
        # register it
        logger.debug("Registering instance {0}".format(instance))
        self.instances.append(instance)
        if hasattr(instance, "name"):
            self.instancesByName[instance.name] = instance

        # send signal created
        self.created(instance)

    def delete(self, instance):
        """
        Unregister an instance.
        """
        # remove the instance from the manager
        logger.debug(f"Unregistering instance '{instance.__class__.__name__}:{instance.name}'")
        self.instances.remove(instance)
        self.instancesByName.pop(instance.name, None)

        # send a signal that it has been deleted
        self.deleted(instance)

    def delete_all(self):
        """
        Unregister all the instances.
        """
        for instance in list(self.instances):
            self.delete(instance)






class MultipleClassManager(Manager):

    def add(self, name, cls):
        """
        Add a class to the register.
        """
        # make the class available
        logger.debug("Class {0} now available".format(name))
        self.availables[name] = cls

        # send a signal with the name and the class
        self.added(name, cls)
