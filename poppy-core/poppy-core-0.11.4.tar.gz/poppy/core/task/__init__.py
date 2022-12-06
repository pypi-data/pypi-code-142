from .task import Task

__all__ = ['Task', 'TaskError']

class TaskError(Exception):
    """
    Error associated to tasks.
    """