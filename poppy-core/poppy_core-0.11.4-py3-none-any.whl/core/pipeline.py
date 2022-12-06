#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import collections
import os.path as osp
from contextlib import contextmanager

from poppy.core.conf import settings
from poppy.core.db.connector import Connector
from poppy.core.db.dry_runner import DryRunner
from poppy.core.db.handlers import link_databases
from poppy.core.generic.cache import CachedProperty
from poppy.core.generic.graph import Graph
from poppy.core.tools.lock import LockFile
from poppy.core.logger import logger
from poppy.core.properties import Properties
from poppy.core.tools.exceptions import print_exception
from poppy.core.loop import Loop
from poppy.pop.models.job import JobException, exception_level_list, exception_type_list

__all__ = ["Pipeline"]


class PipelineError(Exception):
    """
    Errors for the pipeline.
    """


class EmptyLoopError(Exception):
    """
    Errors for the pipeline loop.
    """


class Pipeline(object):
    """
    Pipeline is the class to manage the task workflow. The module pop is
    responsible for a few more jobs to done, such as scripts to load the
    pipeline and the various commands allowed to test and launch the pipeline.

    All created tasks inside commands will be managed by the Pipeline class.
    """

    def __init__(self, args):
        """
        Initialization of some parameters used by the pipeline.
        """
        # create a property object to be able to share information across
        # tasks
        self.properties = Properties()
        self.properties += vars(args)

        # store the pipeline args
        self.args = args

        # store the pipeline targets
        self.targets = {}

        # store the pipeline configuration
        self.configuration = None

        # link databases
        self._link_databases()

        # set the connector for the POPPy database
        self.db = Connector.manager[settings.MAIN_DATABASE]

        # create the dry runner, which allow to not execute decorated functions
        self.dry_runner = DryRunner()
        self.dry_run = args.dry_run

        # a dict of tasks linked to the pipeline
        # the dict is indexed using the task instance names
        self.tasks = {}

        # a graph containing the topology of the pipeline
        self.graph = Graph()

        # default value of the task used as entry point for the pipeline
        self._entry_point = None
        self._start = None
        self._end = None

        # Initialize ignored_target list
        self.properties.ignored_target = []

        # no new topology to generate by default
        self._is_new_topology = False

        # container for loops between tasks
        self._loops = []

        # Initialize Lock instance
        self.lock = LockFile()

        # Exit attribute (if set to True, then force the exit of the pipeline
        # properly)
        self._exit = False

        # Flag about to set to True if pipeline has no entry point
        self.no_entry_point = False

    @property
    def lock_path(self):
        return self.lock

    @lock_path.setter
    def lock_path(self, dirpath_and_filename):
        if (dirpath_and_filename and
                len(list(dirpath_and_filename)) == 2):
            self.lock.dirpath = dirpath_and_filename[0]
            self.lock.filename = dirpath_and_filename[1]

    @CachedProperty
    def output(self):
        """
        Returns the output path, from the command line, and if not present,
        from the configuration file.
        """
        # check if output defined in command line
        if self.properties.output is not None:
            # validate the directory
            output = osp.expanduser(self.properties.output)
            # self._validate_dir(output)
            return output

        # else check in the configuration file
        path = str(self.properties.configuration["pipeline.output_path"])

        if path.startswith('$ROOT_DIRECTORY'):
            path = path.replace('$ROOT_DIRECTORY', settings.ROOT_DIRECTORY)

        output = osp.expanduser(path)

        # validate directory
        # self._validate_dir(output)
        return output

    @CachedProperty
    def provider(self):
        """
        Returns the provider of this pipeline. First read command line
        arguments, and if not present, uses the value given in the
        configuration file.
        """
        # check if provider defined in command line
        if self.properties.provider is not None:
            provider = self.properties.provider
        else:
            # else check in the configuration file
            provider = self.properties.configuration["pipeline.provider"]

        # return the provider, stored as an attribute
        return provider

    def exit(self):
        """If called, then set self._exit attribute to True."""
        self._exit = True

    def _validate_dir(self, dirname):
        """
        Check if the directory is existing.
        """
        # check directory is existing
        if osp.isdir(dirname):
            return

        # raise error
        raise PipelineError(
            "{0} is not a valid output directory".format(dirname))

    def _link_databases(self):
        """
        Link databases defined in the configuration file to the connectors to
        made them accessible from the registry.
        """
        # check that a configuration file is available
        if "configuration" not in self.properties:
            return

        # get the defined databases
        databases = self.properties.configuration["pipeline.databases"]
        
        # link databases with their connectors
        link_databases(databases)

        # for each defined database of the pipeline, give it the properties
        # (parameters) of the pipeline
        for database in databases:
            Connector.manager[database["identifier"]
                              ].configuration = self.properties

    def run(self):
        """
        Run the tasks registered into the pipeline.
        """

        # Check self.exit value, and exit if true
        if self._exit:
            logger.info('Exiting current pipeline session...')
            return

        # get the entry point of the topology of the pipeline
        entry_point = self.start

        # check that the pipeline can be run
        if entry_point is None:
            if not self.no_entry_point:
                logger.error(
                    "The pipeline is not linked to an entry point task, " +
                    "and cannot be run."
                )
            else:
                logger.debug('Pipeline has not entry point, exiting')
            return

        # generate the new topology if necessary
        self.generate_topology(entry_point)

        # bind the main-db and other connectors
        self.db.bind()

        # run the entry point task, allowing to loop through the graph
        self._run_tasks(entry_point)

    def generate_topology(self, task):
        """
        Generate the dependency graph of the pipeline from the entry point of
        the task.
        """
        # if topology needs to be generated
        if not self._is_new_topology:
            return

        # clear the old graph
        self.graph = Graph()

        # set the pipeline and dependency graph for the entry point task
        self._set_pipeline(task)

        # change the flag to indicate no new generation
        self._is_new_topology = False

    def _set_pipeline(self, task):
        # if the task is already in the graph, we do not need to continue
        if task in self.graph:
            return

        # add the pipeline to the task
        task.pipeline = self

        # instantiate the targets
        # note: we need the pipeline ref to instantiate the targets
        task.instantiate_targets()

        # # FIXME remove legacy target support
        # # add a reference to each output target in the pipeline
        # for target in task.outputs.values():
        #     self.properties[target.id] = target

        # add a reference to the task in the pipeline
        self.tasks[task.instance_name] = task

        # loop over children
        for child in task.descendants():
            # add the child to the graph
            self.graph.add_node(task, child)
            self._set_pipeline(child)

        # do the same for parents
        for parent in task.ancestors():
            self._set_pipeline(parent)

    def _setup_queue(self, entry_point):
        """
        Set up the task queue

        :param entry_point: the first task of the workflow
        """
        # create a queue to store the tasks to call
        self.queue = collections.deque()

        # set the first task in the queue
        self.queue.append(entry_point)

    def _run_tasks(self, entry_point):
        """
        Run each task of the workflow starting by the entry point task

        :param entry_point: the first task of the workflow
        :return:
        """

        # Start locking
        self.lock.start()

        # set up the task queue
        self._setup_queue(entry_point)

        # loop on elements on the queue while it is not empty
        while (len(self.queue) != 0):
            # take a task from the queue
            task = self.queue.pop()

            # if a task is already completed, pass it, since its children
            # should have been already run, same if an error happened already
            # with him
            if task.completed or task.failed:
                continue

            # loop over dependencies of the task
            run_dependency = False
            for dependency in task.ancestors():
                # check the dependency is already completed or not
                if not dependency.completed:
                    # run the task if not completed (append it to the stack)
                    run_dependency = True
                    self.queue.append(dependency)

            # take dependencies from the stack if they need to be run
            if run_dependency:
                continue

            # check that dependencies are completed after all of them have been
            # executed, else a problem occurred in a dependency and the task
            # cannot be run
            for dependency in task.ancestors():
                if not dependency.completed:
                    logger.error(
                        (
                            "Task {0} has a dependency problem " +
                            "with task {1}"
                        ).format(task, dependency)
                    )
                    return

            # if dependencies satisfied, run the task
            try:
                with self._starter(task):
                    self.check_and_run_task(task)
            except RuntimeError:
                # If RunTimeError is "generator didn't yield", then
                # assuming that the exception has been raised due to empty loop
                # generator
                if str(sys.exc_info()[1]) == "generator didn't yield":
                    logger.info("Empty loop")
                elif str(sys.exc_info()[1]) == "generator raised StopIteration":
                    logger.debug("End of the loop")
                else:
                    logger.exception(f'Error running task {task}, skip it!')
            except:
                logger.exception(f'Error running task {task}, skip it!')

            # If exit has been requested in the task then break
            if self._exit:
                logger.info('Exiting the current pipeline session...')
                break

            # then run its child, if completed
            for child in task.descendants():
                # add children to the stack to be used
                self.queue.append(child)

        # Stop locking
        self.lock.stop()

    def check_and_run_task(self, task):
        """
        Responsible to launch the task and check that inputs and outputs are
        correctly created.
        """

        # FIXME: update checks and database links
        # check existence of inputs
        # self._check_existing(task.input())

        # put targets inside the database
        # self._input_target_job_map(task)

        # run the task
        task.run()

        # check existence of outputs
        # self._check_existing(task.output())

        # put outputs inside the database
        # self._output_target_job_map(task)

    def _check_existing(self, targets):
        """
        Check that all the outputs of the given task exist to say that the
        task is completed.
        """
        # loop through target and check existing
        for target in targets:

            # If target is in the ignored_target list,
            # then skip checking
            if target in self.properties.ignored_target:
                logger.debug("Ignore checking of target {0}".format(target))
                continue

            # check target in properties
            if target not in self.properties:
                message = (
                    "The target {0} is not available in the " +
                    "pipeline"
                ).format(target)
                raise PipelineError(message)

            # get the target instance
            tt = self.properties[target]

            # get the target instance
            instance = self.properties[target]

            # not existing, task not completed
            if not instance.is_empty and not instance.exists():
                message = "The target {0} doesn't exist".format(target)
                raise PipelineError(message)

    @contextmanager
    def _starter(self, task):
        """
        Return a context manager for automatic stuff when launching a task such
        setting parameters inside the database, indicating the task status into
        POPPy database, putting I/O files, etc.
        """
        # indicate that the job started
        task.start()

        # launch the task and catch errors occurring while executing
        try:
            yield
        except Exception as exception:
            # record the exception into the database
            self._handle_exception(task, exception)

            # clean if an exception occurred
            task.error()
            return

        # check that all output targets exists before saying that the task is
        # completed
        task.completed = True

        # clean up
        task.stop()

    def _handle_exception(self, task, exception, message=None):
        """
        To create an exception object for the database and store it.
        """
        # print the message of error
        if isinstance(exception, EmptyLoopError):
            # create a specific message for empty loop
            if message is None:
                message = '%s - %s' % (exception.__class__.__name__,
                                       str(exception))
            mess = print_exception(message=message,
                                   log_level='info',
                                   use_traceback=False)
        else:
            mess = print_exception(message)

        # set the exception in the database
        self.create_exception(task, mess)

    @DryRunner.dry_run
    def create_exception(self, task, message,
                         exception_type='ERROR',
                         exception_level='Critical'):
        """
        To create the representation of an exception in the database and store
        it.
        """

        if exception_type not in exception_type_list:
            logger.error(f'Job exception cannot be stored in the database: \n'
                         f'exception type is not valid {exception_type}')
            return None

        if exception_level not in exception_level_list:
            logger.error(f'Job exception cannot be stored in the database: \n'
                         f'exception level is not valid {exception_level}')
            return None

        # create the representation of the exception
        representation = JobException(
            job=task.job(),
            exception_msg=message,
            exception_type=exception_type,
            exception_level=exception_level
        )
        # FIXME type and level may have default value here, but every exception
        # should define its own type and level

        # add into the database
        self.db.add(representation)
        self.db.update_database()

    def __or__(self, task):
        """
        Used to link the first task to the pipeline and be able to loop
        through the task graph to run appropriately the tasks with their
        dependencies.
        """
        # keep a reference to the first task linked to the pipeline, used as an
        # entry point to loop through the graph of dependency
        self.entry_point = task

        # flag to indicate that a new topology of the pipeline has been set and
        # that is necessary to regenerate the dependency graph if running the
        # pipeline
        self._is_new_topology = True

        # return the task
        return task

    def loop(self, start, end, generator):
        """
        Create a loop between two task in the pipeline topology, according to
        the values given by the provided generator.

        Starts by checking if the topology of the pipeline is existing. Then
        regenerate the topology by security. An instance of the loop is created
        that will override the descendants and ancestors of the start and end
        tasks provided in argument, at the appropriate times.
        """
        # the generation of a loop requires a topology for the pipeline, i.e.
        # that the dependency graph has been created, so checks the basics for
        # its generation
        entry_point = self.start

        # check that the pipeline can be run
        if entry_point is None:
            logger.error(
                "The pipeline doesn't have a topology created and cannot " +
                "generate a loop between tasks {0} and {1}".format(
                    start,
                    end,
                )
            )
            return

        # generate the new topology if necessary
        self.generate_topology(entry_point)

        # create the loop
        loop = Loop(self, start, end, generator)

        # add the loop into the container
        self._loops.append(loop)

    @property
    def dry_run(self):
        """
        To change the state of the dry run mode for the pipeline.

        If True, the dry run mode is activated, else it is deactivated.

        :getter: the state of the dry run mode in the pipeline (True/False).
        :setter: the state of the dry run mode in the pipeline (True/False).
        :type: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        self._dry_run = dry_run
        if dry_run:
            self.dry_runner.activate()
        else:
            self.dry_runner.deactivate()

    @property
    def entry_point(self):
        return self._entry_point

    @entry_point.setter
    def entry_point(self, task):
        self._entry_point = task

    @property
    def start(self):
        """
        The starting task, if different from the start of the task chain.

        If the starting task is changing and a task has already been set as the
        starting one, the old task ancestors are restored to the old state.

        The ancestors of the given starting task are kept to be restored
        later if necessary. Then the generator of the task ancestors is
        replaced by a null generator and the new starting task is set to the
        given one.

        :getter: the selected task for the start.
        :setter: the task in the chain that will mark the start of the pipeline.
        :type: :class:`poppy.pop.task.Task`
        """
        return self._start

    @start.setter
    def start(self, task):
        # store the old method for ancestors
        if task is not self._start:
            # if not the first setting
            if self._start is not None:
                # give old method to the task
                self._start.ancestors = self._old_start_ancestors

            # keep a trace of the method of ancestors of the new starting task
            self._old_start_ancestors = task.ancestors

            def null_generator(*args, **kwargs):
                """
                Not doing yield from () because of stupidity of pylint marking
                it as invalid syntax because of python2 for youcompleteme in
                vim.
                """
                return
                yield

            # set the new ancestors for the starting task
            task.ancestors = null_generator

            # set the new starting task
            self._start = task

    @property
    def end(self):
        """
        The ending task, if different from the end of the task chain.

        If the ending task is changing and a task has already been set as the
        ending one, the old task descendants are restored to the old state.

        The descendants of the given ending task are kept to be restored
        later if necessary. Then the generator of the task descendants is
        replaced by a null generator and the new ending task is set to the
        given one.

        :getter: the selected task for the end.
        :setter: the task in the chain that will mark the end of the pipeline.
        :type: :class:`poppy.pop.task.Task`
        """
        return self._end

    @end.setter
    def end(self, task):
        # store the old method for descendants
        if task is not self._end:
            # if not the first setting
            if self._end is not None:
                # give old method to the task
                self._end.descendants = self._old_end_descendants

            # keep a trace of the method of descendants of the new ending task
            self._old_end_descendants = task.descendants

            def null_generator(*args, **kwargs):
                """
                Not doing yield from () because of stupidity of pylint marking
                it as invalid syntax because of python2 for youcompleteme in
                vim.
                """
                return
                yield

            # set the new descendants for the task
            task.descendants = null_generator

            # set the new ending task
            self._end = task

    def get(self, keyword,
            default=None,
            args=False,
            create=False):
        """
        Return a pipeline property.

        :param keyword: property keyword
        :param default: default value if property keyword not found
        :param args: If True, property is an argument
        :param create: If True, create property in pipeline if not found
        :return: property value
        """

        if args:
            property_dict = self.args.__dict__
        else:
            property_dict = self.properties

        # Get value from property, if not found or NoneType use default value
        value = property_dict.get(keyword)

        if value is None and default is not None:
            value = default

            # If not found and create is True, then create property with
            # default value in the pipeline
            if create:
                property_dict[keyword] = default

        return value
