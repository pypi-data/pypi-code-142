#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import sys
import uuid

from poppy.core.db.dry_runner import DryRunner
from poppy.core.db.handlers import get_or_create_with_info
from poppy.core.generic.signals import Signal
from poppy.core.logger import logger
from poppy.pop.models.job import JobLog


class BaseTask:
    """
    Base class for tasks to run through the poppy pipeline.
    """
    # default value for the time of jobs when not started
    default_time = datetime.datetime(1900, 1, 1)

    # status for the task
    PENDING = "Pending"
    STOPPED = "Terminated"
    STARTED = "Running"
    STATE = {PENDING, STOPPED, STARTED}

    OK = "OK"
    WARNING = "WARNING"
    ERROR = "ERROR"
    STATUS = {OK, WARNING, ERROR}

    def __init__(
            self, *,
            plugin=None,
            descriptor=None,
            instance_name=None
    ):
        """
        Initialization of some parameters.
        """
        # store the instance name if any
        self.instance_name = instance_name

        # store the pipeline instance
        self.pipeline = None

        # init the list of parents and children tasks
        self.parents = []
        self.children = []

        # a signal to indicate that the job has changed
        self.changed = Signal()

        # an other one to indicate that it has been created
        self.created = Signal()

        # a signal to indicate that the task as started and ended
        self.started = Signal()
        self.ended = Signal()

        # signal when the task is reset
        self.reseted = Signal()

        # a signal to indicate that an error occurred
        self.errored = Signal()

        # set some reusable properties to their default values
        self.reset()

        # store the the plugin of the job
        self.plugin = plugin

        # store the category of the task
        self.category = descriptor['category']

        # store the textual description
        self.description = descriptor['description']

        # init the targets that can be created from task to None
        self.targets = None

    @property
    def instance_name(self):
        """
        Return the instance name if defined otherwise return the task name

        :return: the instance name or the task name
        """
        if self._instance_name:
            return self._instance_name
        else:
            return self.name

    @instance_name.setter
    def instance_name(self, value):
        self._instance_name = value

    def reset(self):
        """
        To reset some attributes of the task, in order to have one new task
        from an existing one.
        """
        logger.debug("Reset task {0}".format(self))
        # create an uuid for this job
        self.uuid = uuid.uuid4()

        # for the state of the task
        self.completed = False
        self.failed = False

        # set the default start and end times
        self.starttime = self.default_time
        self.endtime = self.default_time

        # default values for job state/status
        self._state = self.PENDING
        self._status = self.OK

        # send a signal that the task has been reset
        self.reseted(self)

    def run(self):
        """
        The method that the other tasks must override to perform their
        computations.
        """
        pass

    def input(self):
        """
        Return a list of the input targets necessary to this task. The list
        contains the names of the attributes used for storing targets into the
        properties object of the pipeline. The task should have a reference on
        it.
        """
        return []

    def output(self):
        """
        Should return a structure containing the targets outputs of these task.
        If a task use them as input, it should know the structure to access to
        good properties.
        """
        return []

    def start(self):
        """
        Indicate at which time the job started.
        """
        # indicate that the task started
        logger.debug("Starting task {0}".format(self))

        # store the time
        self.starttime = datetime.datetime.now()

        # indicate that it is in progress
        self.progress()

        # indicate the change
        self.job_changed()

        # indicate the job as started
        self.started(self)

    def stop(self):
        """
        Indicate at which time the job ended.
        """
        # indicate that the task is stopping
        logger.debug("Stopping task {0}".format(self))

        # store the time
        self.endtime = datetime.datetime.now()

        # indicate terminated
        self.terminated()

        # indicate the change
        self.job_changed()

        # send signal ended
        self.ended(self)

    def job(self):
        """
        Create the job representation of the task into the POPPy database.
        """

        # create the representation in the database
        logger.debug("Get/create representation for job {0}".format(self))
        job, created = get_or_create_with_info(
            self.pipeline.db.session,
            JobLog,
            job_name=repr(self),
            job_uuid=str(self.uuid),
            job_category=self.category,
            job_descr=self.description,
            job_task=self.instance_name,
            job_plugin=self.plugin.name,
            create_method_kwargs=dict(
                job_starttime=self.starttime,
                job_endtime=self.endtime,
                job_state=self._state,
                job_status=self._status,
                job_status_descr="",
            ),
        )

        # indicate that the representation has been created
        if created:
            logger.debug("Created representation for job {0}".format(self))
            self.created(job)

        # store the job
        return job

    def __or__(self, child):
        """
        To set the task in the other side of the pipe as a child task.
        """
        # add the task itself as a parent of the child class
        child.parents.append(self)

        # add the child
        self.children.append(child)

        # return the child, since it will be used to create branching
        return child

    def exception(self, message,
                  exception_type='ERROR',
                  exception_level='Critical'):
        """
        Create an exception in the pipeline, i.e. in the POPPy database with the
        given message as description.
        """
        self.pipeline.create_exception(self, message,
                                       exception_type=exception_type,
                                       exception_level=exception_level)

    @DryRunner.dry_run
    def job_changed(self):
        """
        What to do when the status of the job has changed.
        """
        # get the job in the database
        job = self.job()

        # store the new information on the representation
        job.job_starttime = self.starttime
        job.job_endtime = self.endtime
        job.job_state = self._state
        job.job_status = self._status
        job.parent = self.parents[0].job() if len(self.parents) else None

        # commit changed
        self.pipeline.db.update_database()

        # indicate that the task job has changed
        self.changed()

    def state(self, value):
        """
        To change the state of the task job with the given provided argument.
        """
        # check that the value is accepted
        if value not in self.STATE:
            raise ValueError(
                "The state of the task job must be set to {0}".format(self.STATE)
            )

        # store the state
        logger.debug("Task job {0} is now at state {1}".format(self, value))
        self._state = value

        # call internal method to change the state of a target
        self.job_changed()

    def status(self, value):
        """
        To change the status of the target.
        """
        # check that the value is accepted
        if value not in self.STATUS:
            raise ValueError(
                "The status of the task job must be set to " +
                "{0}".format(self.STATUS)
            )

        # store the status
        logger.debug(
            "Task job {0} is now at status {1}".format(self, value)
        )
        self._status = value

        # indicate the status changed
        self.job_changed()

    def ok(self):
        """
        Set to ok the status
        """
        self.status(self.OK)

    def warning(self):
        """
        Set the status to warning.
        """
        self.status(self.WARNING)

    def error(self):
        """
        Set the status to error.
        """
        # store the time
        self.endtime = datetime.datetime.now()

        # flag to indicate an error happened
        self.failed = True

        # indicate terminated
        self.terminated()

        # change the status
        self.status(self.ERROR)

        # send signal error happened
        self.errored(self)

    def pending(self):
        """
        Set the state to pending.
        """
        self.state(self.PENDING)

    def terminated(self):
        """
        Set the state to terminated.
        """
        self.state(self.STOPPED)

    def progress(self):
        """
        Set the state to in progress.
        """
        self.state(self.STARTED)

    def descendants(self):
        """
        Give the children-descendants of a task. Those tasks are dependant of
        this task to be run. By default, it returns the list of children as an
        iterable, but it can be transformed into a generator, to be able to
        create loops in the pipeline, returning at a given pint of the pipeline
        according to some specific conditions.
        """
        # returns the child tasks by default
        for child in self.children:
            yield child

    def ancestors(self):
        """
        Equivalent to the descendants methods, but for the parents of the task.
        Maybe an utility will be find some day with it...
        """
        # returns the child tasks by default
        for parent in self.parents:
            yield parent

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if description is not None:
            self._description = description
        elif description is None and not hasattr(self, "_description"):
            logger.error(
                "There must be a description for task {0}".format(self)
            )
            sys.exit(-1)

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if category is not None or not hasattr(self, "_category"):
            self._category = category
        elif category is None and not hasattr(self, "_category"):
            logger.error(
                "There must be a category for task {0}".format(self)
            )
            sys.exit(-1)

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, children):
        self._children = children

    @property
    def parents(self):
        return self._parents

    @parents.setter
    def parents(self, parents):
        self._parents = parents

    def __repr__(self):
        """
        Represent the task with a name. Use both the task and instance name, except if the instance name is
        not defined.
        """
        # use the name if provided
        if self._instance_name:
            return f'{self.name}: {self._instance_name}'
        else:
            return self.name
