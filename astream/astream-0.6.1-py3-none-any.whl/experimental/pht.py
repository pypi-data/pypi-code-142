from abc import ABC
from typing import (
    Any,
    AsyncIterable,
    AsyncIterator,
    Awaitable,
    Callable,
    cast,
    ClassVar,
    Coroutine,
    Generic,
    Iterable,
    Literal,
    overload,
    ParamSpec,
    Protocol,
    TYPE_CHECKING,
    TypeAlias,
    TypeVar,
    Union,
)

from phantom import Phantom

from astream import iter_to_aiter

if not TYPE_CHECKING:

    def reveal_type(instance: object) -> None:
        print(type(instance))


# A boolean predicate that checks if a given string is a greeting. This function is
# of type ``Predicate[str]`` as it requires its argument to be a ``str``.
def is_greeting(instance: str) -> bool:
    return instance.startswith(("Hello", "Hi"))


# Since our predicate requires its argument to be a ``str``, we must make the bound
# of the phantom type ``str`` as well. We do that by making it it's first base. Any
# base specified before Phantom is implicitly interpreted as its bound, unless an
# explicit bound is specified as a class argument.
class Greeting(str, Phantom[str], predicate=is_greeting):
    ...


def is_either_iterable(instance: object) -> bool:
    return isinstance(instance, (Iterable, AsyncIterable))


_T = TypeVar("_T")
_R = TypeVar("_R")
_P = ParamSpec("_P")


# class EitherIterable(
#     Phantom[_T],
#     bound=Union[Iterable[_T], AsyncIterable[_T]],
# ):
#     __bound__ = Iterable | AsyncIterable
_cR = TypeVar("_cR", bound=Coroutine[Any, Any, Any])

ResultT = TypeVar("ResultT", bound="Awaitable[Any]")
_cT = TypeVar("_cT")

CoroFn: TypeAlias = Callable[_P, Coroutine[object, object, _T]]
SyncFn: TypeAlias = Callable[_P, _T]
EitherFn: TypeAlias = Union[CoroFn[_P, _T], SyncFn[_P, _T]]
EitherIterable: TypeAlias = Union[Iterable[_T], AsyncIterable[_T]]


def ensure_async_iterator(src: EitherIterable[_T]) -> AsyncIterator[_T]:
    if isinstance(src, AsyncIterable):
        return aiter(src)
    elif isinstance(src, Iterable):
        return iter_to_aiter(src)
    else:
        raise TypeError(f"Invalid source type: {type(src)}")


@overload
def ensure_coro_fn(fn: CoroFn[_P, _T]) -> CoroFn[_P, _T]:
    ...


@overload
def ensure_coro_fn(fn: SyncFn[_P, _T]) -> CoroFn[_P, _T]:
    ...


def ensure_coro_fn(fn: EitherFn[_P, _T]) -> CoroFn[_P, _T]:
    """Given a sync or async function, return an async function.

    Args:
        fn: The function to ensure is async.
        to_thread: Whether to run the function in a thread, if it is sync.

    Returns:
        An async function that runs the original function.
    """

    if asyncio.iscoroutinefunction(fn):
        return fn

    _fn_sync = cast(Callable[_P, _T], fn)

    async def _async_fn(*args: _P.args, **kwargs: _P.kwargs) -> _T:
        return _fn_sync(*args, **kwargs)

    return _async_fn


def a(x: int) -> str:
    return str(x)


async def b(x: int) -> str:
    return str(x)


f_a = ensure_coro_fn(a)
f_b = ensure_coro_fn(b)

reveal_type(f_a)
reveal_type(f_b)


# class EitherCallable(
#     Phantom[Callable[_P, Coroutine[object, object, _R]] | Callable[_P, _R]], Generic[_P, _R]
# ):
#     __abstract__: ClassVar = True


async def ahoo(ra: int) -> AsyncIterable[int]:
    for i in range(ra):
        yield i


f = range(10)
ah = ahoo(10)

assert isinstance(f, EitherIterable)
assert isinstance(ah, EitherIterable)

reveal_type(ah)
reveal_type(f)

ait = ensure_async_iterator(f)
reveal_type(ait)

reveal_type(f)  # Revealed type is "AnyIterable"
reveal_type(ah)  # Revealed type is "AnyIterable"


async def main() -> None:
    async for i in ensure_async_iterator(ah):
        print(i)
        reveal_type(i)

    async for i in ensure_async_iterator(f):
        print(i)
        reveal_type(i)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())


hello = "Hello there"
# We can narrow types using mypy's type guards
assert isinstance(hello, Greeting)
# or explicitly when we need to
hi = Greeting.parse("Hi there")

# The runtime types are unchanged and will still be str for our greetings
assert type(hello) is str
assert type(hi) is str

# But their static types will be Greeting, retaining the information that our
# strings are not just any strs
if TYPE_CHECKING:
    reveal_type(hello)
    reveal_type(hi)

# As this string doesn't fulfill our __instancecheck__, it will not be an
# instance of Greeting.
assert not isinstance("Goodbye", Greeting)
