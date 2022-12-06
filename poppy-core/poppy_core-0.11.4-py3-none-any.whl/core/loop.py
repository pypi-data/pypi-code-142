#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections

from poppy.core.logger import logger

__all__ = ["Loop", "LegacyLoop"]


class LoopMetaclass(type):
    """
    Simply keep a reference of created loops, since weirdly their reference is
    not kept inside a calling function with no assignment.
    """

    def __init__(cls, *args, **kwargs):
        """
        Containers for registering instances.
        """
        # create has usual
        super(LoopMetaclass, cls).__init__(*args, **kwargs)

        # add container if not present
        if not hasattr(cls, "instances"):
            cls.instances = []

    def __call__(cls, *args, **kwargs):
        """
        Register the instances.
        """
        # create the instance as usual
        instance = super(LoopMetaclass, cls).__call__(*args, **kwargs)

        # register the instance
        cls.instances.append(instance)

        # return
        return instance


class LegacyLoop(object, metaclass=LoopMetaclass):
    """
    A class to create a loop between two tasks in the pipeline easily.
    """

    def __init__(self, pipeline, start, end, iterable):
        """
        Construct the class with information on the looping tasks in the
        pipeline, and on what to iterate.
        """
        # container to track the monkey patched methods
        self._tracker = collections.defaultdict(collections.deque)

        # indicate if an error occurred in the previous iteration
        self._current_task = None

        # indicate if the loop is running
        self._running = False

        # store start and end loop tasks
        self.pipeline = pipeline
        self.start = start
        self.end = end
        self.iterable = iterable

        # now init the loop
        self.init()

    def init(self):
        """
        Init some states for the loop for all tasks belonging to it.
        """
        # search all paths between the two nodes
        self.paths = self.pipeline.graph.find_all_paths(self.start, self.end)

        # for all tasks, connect to the signal of an error
        for tasks in self.paths:
            for task in tasks:
                # on error, change the topology
                task.errored.connect(self._to_next)

    def reset(self):
        """
        Make a reset of the tasks inside the loop.
        """
        # loop over tasks to reset them
        for tasks in self.paths:
            # this a list of paths, so second loop
            for task in tasks:
                # reset the task
                task.reset()

    def _to_next(self, task):
        """
        To handle what to do when we need to go to a next iteration. The next
        iteration is the whole process of going from the starting task and the
        ending task.
        """
        # change the topology of the loop to reset
        with self.update_context(task):
            # pass to the next iteration
            self.next()

            # change topology of the pipeline
            self._change_next_to_start(task)

            # reset tasks
            self.reset()

            # keep a trace of the current task
            self._current_task = task

    def _change_next_to_start(self, task):
        """
        To change the next task returned by the task.
        """
        # store the old method of the task
        self._tracker[task].append(task.descendants)

        # monkey path the descendants generator
        task.descendants = self._start_generator

    def _start_generator(self):
        """
        Generator to return the start task every time it is called.
        """
        logger.debug("Putting task {0} as start for loop".format(self.start))
        yield self.start

    def update_context(self, task):
        class UpdateContext(object):

            def __enter__(self):
                pass

            def __exit__(instance, type, value, traceback):
                if isinstance(value, StopIteration):
                    # end of the iterator, de-hook the end task
                    logger.debug("End of the loop")

                    # disconnect start if required
                    self.start.started.disconnect(self.starting)

                    # if a task have an error, descendants are those of the end
                    task.descendants = self.end.descendants

        return UpdateContext()

    def starting(self, start):
        """
        To make a first iteration on the iterable before starting the start
        task.
        """
        # call the first iteration to be able to set inputs if needed
        if not self._running:
            self._running = True
            # change the topology of the loop to reset
            with self.update_context(start):
                # pass to the next iteration
                self.next()

        # put the old method to the task
        if self._current_task is not None:
            task = self._current_task
            task.descendants = self._tracker[task].pop()
            task = None

    def next(self):
        """
        To pass to the next iteration of the loop.
        """
        # call the iterator again
        next(self.iterable)

    def delete(self):
        """
        Remove the reference to the loop.
        """
        self.instances.remove(self)

    @property
    def pipeline(self):
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        self._pipeline = pipeline

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        self._start = start

        # connect to the started signal to make a first iteration
        self._start.started.connect(self.starting)

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        self._end = end

        # connect to the end of the task to do make the loop
        self._end.ended.connect(self._to_next)


class Loop(object, metaclass=LoopMetaclass):
    """
    A class to create a loop between two tasks in the pipeline easily.
    """

    def __init__(self, pipeline, start, end, generator):
        """
        Construct the class with information on the looping tasks in the
        pipeline, and on what to iterate.
        """
        # container to track the monkey patched methods
        self._tracker = collections.defaultdict(collections.deque)

        # indicate if an error occurred in the previous iteration
        self._current_task = None

        # indicate if the loop is running
        self._running = False

        # store start and end loop tasks
        self.pipeline = pipeline
        self.start = start
        self.end = end
        self._generator = generator
        self._iterable = None

        # now init the loop
        self.init()

    @property
    def iterable(self):
        if self._iterable is None:
            self._iterable = self._generator(self)
        return self._iterable

    def init(self):
        """
        Init some states for the loop for all tasks belonging to it.
        """
        # search all paths between the two nodes
        self.paths = self.pipeline.graph.find_all_paths(self.start, self.end)

        # for all tasks, connect to the signal of an error
        for tasks in self.paths:
            for task in tasks:
                # on error, change the topology
                task.errored.connect(self._to_next)

    def reset(self):
        """
        Make a reset of the tasks inside the loop.
        """
        # loop over tasks to reset them
        for tasks in self.paths:
            # this a list of paths, so second loop
            for task in tasks:
                # reset the task
                task.reset()

    def _to_next(self, task):
        """
        To handle what to do when we need to go to a next iteration. The next
        iteration is the whole process of going from the starting task and the
        ending task.
        """
        # change the topology of the loop to reset
        with self.update_context(task):
            # pass to the next iteration
            self.next()

            # change topology of the pipeline
            self._change_next_to_start(task)

            # reset tasks
            self.reset()

            # keep a trace of the current task
            self._current_task = task

    def _change_next_to_start(self, task):
        """
        To change the next task returned by the task.
        """
        # store the old method of the task
        self._tracker[task].append(task.descendants)

        # monkey path the descendants generator
        task.descendants = self._start_generator

    def _start_generator(self):
        """
        Generator to return the start task every time it is called.
        """
        logger.debug("Putting task {0} as start for loop".format(self.start))
        yield self.start

    def update_context(self, task):
        class UpdateContext(object):

            def __enter__(self):
                pass

            def __exit__(instance, type, value, traceback):
                if isinstance(value, StopIteration):
                    # end of the iterator
                    # de-hook the end task and fix dependencies in case of
                    # errors
                    logger.debug("End of the loop")

                    # disconnect start if required
                    self.start.started.disconnect(self.starting)

                    # force descendants/ancestors in case of error during loop tasks processing
                    # in practice, we change the workflow from:
                    # > task_start --> [loop_task_1 -> loop_task_2 -> loop_task_3] --> task_end
                    # to:
                    # > task_start --> task_end
                    # side effect: loops are always considered successful
                    # TODO: allow loops to be considered failed

                    # force the descendants of the loop to be the task(s) just after the loop
                    # 'loop_task_n' is replaced by 'task_end'
                    task.descendants = self.end.descendants

                    for dependency in task.descendants():
                        # force the ancestors task(s) after the loop to depends on the task just before the loop
                        # 'loop_task_3' is replaced by 'task_start'
                        dependency.ancestors = self.start.ancestors

        return UpdateContext()

    def starting(self, start):
        """
        To make a first iteration on the iterable before starting the start
        task.
        """
        # call the first iteration to be able to set inputs if needed
        if not self._running:
            self._running = True
            # change the topology of the loop to reset
            with self.update_context(start):
                # pass to the next iteration
                self.next()

        # put the old method to the task
        if self._current_task is not None:
            task = self._current_task
            task.descendants = self._tracker[task].pop()
            task = None

    def next(self):
        """
        To pass to the next iteration of the loop.
        """
        # call the iterator again
        next(self.iterable)

    def delete(self):
        """
        Remove the reference to the loop.
        """
        self.instances.remove(self)

    @property
    def pipeline(self):
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        self._pipeline = pipeline

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        self._start = start

        # connect to the started signal to make a first iteration
        self._start.started.connect(self.starting)

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        self._end = end

        # connect to the end of the task to do make the loop
        self._end.ended.connect(self._to_next)

    @property
    def inputs(self):
        _inputs = {}
        for task in self.start.parents:
            _inputs.update(task.outputs)
        return _inputs

    @property
    def outputs(self):
        _outputs = {}
        for task in self.end.children:
            _outputs.update(task.inputs)
        return _outputs
