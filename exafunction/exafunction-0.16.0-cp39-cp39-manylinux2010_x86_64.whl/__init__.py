# Copyright Exafunction, Inc.

# pylint: disable=missing-module-docstring
# pylint: disable=useless-import-alias

from exa import repo
from exa.common_pb.common_pb2 import DataType as DataType
from exa.common_pb.common_pb2 import MethodInfo as MethodInfo
from exa.common_pb.common_pb2 import ModuleContextInfo as ModuleContextInfo
from exa.common_pb.common_pb2 import ModuleInfo as ModuleInfo
from exa.common_pb.common_pb2 import ValueMetadata as ValueMetadata
from exa.py_client.default_session import from_bytes as from_bytes
from exa.py_client.default_session import from_numpy as from_numpy
from exa.py_client.default_session import new_module as new_module
from exa.py_client.default_session import new_module_from_cls as new_module_from_cls
from exa.py_client.default_session import require_modules as require_modules
from exa.py_client.default_session import shutdown_session as shutdown_session
from exa.py_client.module import Module as Module
from exa.py_client.session import ModuleContextSpec as ModuleContextSpec
from exa.py_client.session import PlacementGroupSpec as PlacementGroupSpec
from exa.py_client.session import Session as Session
from exa.py_module.base_module import AutoModule as AutoModule
from exa.py_module.base_module import BaseModule as BaseModule
from exa.py_module.base_module import export as export
from exa.py_module.base_module_context import BaseModuleContext as BaseModuleContext
from exa.py_module.base_module_context import wrap_call as wrap_call
from exa.py_module.method_context import MethodContext as MethodContext
from exa.py_module_repository.module_repository import (
    _allow_module_repository_clear as _allow_module_repository_clear,
)
from exa.py_module_repository.module_repository import (
    get_bazel_runfiles_root as get_bazel_runfiles_root,
)
from exa.py_module_repository.module_repository import glob as glob
from exa.py_module_repository.module_repository import (
    ModuleRepository as ModuleRepository,
)
from exa.py_value.value import Value as Value
from exa.py_value.value import ValueCompressionType as ValueCompressionType
from exa.types import get as get
from exa.types import Picklable as Picklable
from exa.types import TypedDict as TypedDict
from exa.types import ValueDict as ValueDict
from exa.types import ValueLike as ValueLike
from exa.types import ValueTuple as ValueTuple

# Enable extra module distribution without dependencies
try:
    from exa.ffmpeg_pb.ffmpeg_pb2 import DecoderParameters as DecoderParameters
    from exa.ffmpeg_pb.ffmpeg_pb2 import DecoderType as DecoderType
    from exa.ffmpeg_pb.ffmpeg_pb2 import EncoderParameters as EncoderParameters
    from exa.ffmpeg_pb.ffmpeg_pb2 import EncoderType as EncoderType
    from exa.py_ffmpeg.ffmpeg import VideoDecoder as VideoDecoder
    from exa.py_ffmpeg.ffmpeg import VideoEncoder as VideoEncoder
except ImportError as e:
    import os

    if os.environ.get("EXA_DEBUG_IMPORT_EXTRAS", False):
        print("Failed to import Exafunction extras modules")
        raise e


def shutdown():
    """Shutdown for both the default session and module repository."""
    shutdown_session()
    repo.shutdown()
