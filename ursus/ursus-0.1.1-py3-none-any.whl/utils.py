from typing import Any, AsyncGenerator, Callable, Generator, ParamSpec, Union

from quart.wrappers.response import Response as QuartResponse
from werkzeug.wrappers.response import Response as WerkzeugResponse


ViewFuncArgsT = ParamSpec('ViewFuncArgsT')

# ViewFuncReturnT is recursive, so move the non-recursive definitions to their own union
_ViewFuncReturnPartial = Union[
    str,
    dict[Any, Any],
    QuartResponse,
    WerkzeugResponse,
    AsyncGenerator[bytes, None],
    Generator[bytes, None, None],
    tuple[str, int, dict[str, str]],
]

ViewFuncReturnT = Union[
    _ViewFuncReturnPartial,
    tuple[_ViewFuncReturnPartial, int],
]

# TODO: ignore is here because of a mypy bug. bug is fixed, release hasn't trickled down yet
# <https://github.com/python/mypy/pull/14159>
ViewFuncT = Callable[ViewFuncArgsT, ViewFuncReturnT]  # type: ignore [valid-type, misc]
