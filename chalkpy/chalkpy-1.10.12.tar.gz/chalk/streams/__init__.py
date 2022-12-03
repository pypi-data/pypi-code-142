import inspect
from typing import Callable, List, Optional, Union

from chalk.state import KeyedState
from chalk.streams._file_source import FileSource
from chalk.streams._kafka_source import KafkaSource
from chalk.streams._windows import Windowed, windowed
from chalk.streams.base import StreamSource
from chalk.utils import MachineType


def stream(
    *,
    source: StreamSource,
    mode: Optional[str] = None,
    environment: Optional[Union[List[str], str]] = None,
    machine_type: Optional[MachineType] = None,
):
    caller_frame = inspect.stack()[1]
    caller_filename = caller_frame.filename
    caller_globals = caller_frame.frame.f_globals
    caller_locals = caller_frame.frame.f_locals
    from chalk.features.resolver import _parse_and_register_stream_resolver

    def decorator(fn: Callable):
        return _parse_and_register_stream_resolver(
            caller_globals=caller_globals,
            caller_locals=caller_locals,
            fn=fn,
            source=source,
            mode=mode,
            caller_filename=caller_filename,
            environment=environment,
            machine_type=machine_type,
        )

    return decorator


__all__ = [
    "FileSource",
    "KafkaSource",
    "KeyedState",
    "StreamSource",
    "Windowed",
    "stream",
    "windowed",
]
