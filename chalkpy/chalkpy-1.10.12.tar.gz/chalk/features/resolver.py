import dataclasses
import inspect
import typing
from dataclasses import dataclass
from inspect import Parameter
from typing import (
    Any,
    Callable,
    ClassVar,
    Dict,
    Generic,
    List,
    Optional,
    Protocol,
    Sequence,
    Set,
    Type,
    TypeVar,
    Union,
    cast,
    get_args,
    get_origin,
    get_type_hints,
    overload,
)

from pydantic import BaseModel
from typing_extensions import ParamSpec

from chalk.features import DataFrame
from chalk.features.dataframe import DataFrame
from chalk.features.feature_field import Feature
from chalk.features.feature_set import Features, FeaturesImpl
from chalk.features.feature_wrapper import FeatureWrapper, unwrap_feature
from chalk.features.filter import Filter
from chalk.features.tag import Environments, Tags
from chalk.serialization.parsed_annotation import ParsedAnnotation
from chalk.sql.base.protocols import BaseSQLSourceProtocol
from chalk.state import StateWrapper
from chalk.streams import Windowed
from chalk.streams.base import StreamSource
from chalk.streams.types import (
    StreamResolverParam,
    StreamResolverParamKeyedState,
    StreamResolverParamMessage,
    StreamResolverParamMessageWindow,
    StreamResolverSignature,
)
from chalk.utils import MachineType
from chalk.utils.annotation_parsing import ResolverAnnotationParser
from chalk.utils.collection_type import GenericAlias
from chalk.utils.collections import ensure_tuple
from chalk.utils.duration import Duration, ScheduleOptions
from chalk.utils.environment_parsing import env_var_bool

T = TypeVar("T")
P = ParamSpec("P")


@dataclasses.dataclass(frozen=True)
class ResolverArgErrorHandler:
    default_value: Any


@dataclass
class StateDescriptor(Generic[T]):
    kwarg: str
    pos: int
    initial: T
    typ: Type[T]


class FilterFunction(Protocol):
    def __call__(self, *args: Feature) -> bool:
        ...


class SampleFunction(Protocol):
    def __call__(self) -> DataFrame:
        ...


@dataclass
class Cron:
    schedule: Optional[ScheduleOptions] = None
    filter: Optional[FilterFunction] = None
    sample: Optional[SampleFunction] = None
    trigger_downstream: Optional[bool] = True


def _get_expected_features_list(output: Type[Features]) -> Sequence[Feature]:
    if issubclass(output, Features):
        output = output.features

    if len(output) == 1 and issubclass(output[0], DataFrame):
        return output[0].columns
    else:
        return output


class Resolver(Protocol):
    function_definition: str
    fqn: str
    filename: str
    inputs: List[Feature]
    output: Type[Features]
    fn: Callable
    environment: Optional[List[str]]
    tags: Optional[List[str]]
    max_staleness: Optional[Duration]
    machine_type: Optional[MachineType]
    state: Optional[StateDescriptor]
    default_args: List[Optional[ResolverArgErrorHandler]]

    registry: "ClassVar[List[Resolver]]" = []
    hook: "ClassVar[Optional[Callable[[Resolver], None]]]" = None

    def __hash__(self):
        return hash(self.fqn)


def _process_call(result, *, declared_output: Any):
    from chalk.sql import StringChalkQuery
    from chalk.sql.integrations.chalk_query import ChalkQuery

    if isinstance(result, (ChalkQuery, StringChalkQuery)):
        return result.execute_internal(expected_features=_get_expected_features_list(declared_output))

    return result


class SinkResolver:
    registry: "List[SinkResolver]" = []

    def __eq__(self, other):
        return isinstance(other, SinkResolver) and self.fqn == other.fqn

    def __hash__(self):
        return hash(self.fqn)

    def __call__(self, *args, **kwargs):
        return _process_call(self.fn(*args, **kwargs), declared_output=None)

    def __init__(
        self,
        function_definition: str,
        fqn: str,
        filename: str,
        doc: Optional[str],
        inputs: List[Feature],
        output: Type[Features],
        fn: Callable,
        environment: Optional[List[str]],
        tags: Optional[List[str]],
        machine_type: Optional[MachineType],
        buffer_size: Optional[int],
        debounce: Optional[Duration],
        max_delay: Optional[Duration],
        upsert: Optional[bool],
        integration: Optional[BaseSQLSourceProtocol] = None,
    ):
        self.function_definition = function_definition
        self.fqn = fqn
        self.filename = filename
        self.inputs = inputs
        self.output = output
        self.fn = fn
        self.environment = environment
        self.tags = tags
        self.doc = doc
        self.machine_type = machine_type
        self.buffer_size = buffer_size
        self.debounce = debounce
        self.max_delay = max_delay
        self.upsert = upsert
        self.integration = integration

    def __repr__(self):
        return f"SinkResolver(name={self.fqn})"


class OnlineResolver(Resolver):
    cron: Union[ScheduleOptions, Cron]

    def __eq__(self, other):
        return isinstance(other, OnlineResolver) and self.fqn == other.fqn

    def __hash__(self):
        return hash(self.fqn)

    def __call__(self, *args, **kwargs):
        return _process_call(self.fn(*args, **kwargs), declared_output=self.output)

    @property
    def __name__(self):
        return self.fn.__name__

    @property
    def __module__(self):
        return self.fn.__module__

    def __init__(
        self,
        function_definition: str,
        fqn: str,
        filename: str,
        doc: Optional[str],
        inputs: List[Feature],
        output: Type[Features],
        fn: Callable,
        environment: Optional[List[str]],
        tags: Optional[List[str]],
        max_staleness: Optional[Duration],
        cron: Optional[Union[ScheduleOptions, Cron]],
        machine_type: Optional[MachineType],
        when: Optional[Filter],
        state: Optional[StateDescriptor],
        default_args: List[Optional[ResolverArgErrorHandler]],
    ):
        self.function_definition = function_definition
        self.fqn = fqn
        self.filename = filename
        self.inputs = inputs
        self.output = output
        self.fn = fn
        self.environment = environment
        self.tags = tags
        self.max_staleness = max_staleness
        self.cron = cron
        self.doc = doc
        self.machine_type = machine_type
        self.when = when
        self.state = state
        self.default_args = default_args

    def __repr__(self):
        return f"OnlineResolver(name={self.fqn})"


class OfflineResolver(Resolver):
    def __eq__(self, other):
        return isinstance(other, OfflineResolver) and self.fqn == other.fqn

    def __hash__(self):
        return hash(self.fqn)

    def __call__(self, *args, **kwargs):
        return _process_call(self.fn(*args, **kwargs), declared_output=self.output)

    @property
    def __name__(self):
        return self.fn.__name__

    @property
    def __module__(self):
        return self.fn.__module__

    def __init__(
        self,
        function_definition: str,
        fqn: str,
        filename: str,
        doc: Optional[str],
        inputs: List[Feature],
        output: Type[Features],
        fn: Callable,
        environment: Optional[List[str]],
        tags: Optional[List[str]],
        max_staleness: Optional[Duration],
        cron: Union[ScheduleOptions, Cron],
        machine_type: Optional[MachineType],
        state: Optional[StateDescriptor],
        when: Optional[Filter],
        default_args: List[Optional[ResolverArgErrorHandler]],
    ):
        self.when = when
        self.function_definition = function_definition
        self.fqn = fqn
        self.filename = filename
        self.doc = doc
        self.inputs = inputs
        self.output = output
        self.fn = fn
        self.environment = environment
        self.tags = tags
        self.max_staleness = max_staleness
        self.cron = cron
        self.machine_type = machine_type
        self.state = state
        self.default_args = default_args

    def __repr__(self):
        return f"OfflineResolver(name={self.fqn})"


@dataclasses.dataclass(frozen=True)
class ResolverParseResult:
    fqn: str
    inputs: List[Feature]
    state: Optional[StateDescriptor]
    output: Optional[Type[Features]]
    function_definition: str
    function: Callable
    doc: Optional[str]
    default_args: List[Optional[ResolverArgErrorHandler]]


def get_resolver_fqn(function: Callable):
    return f"{function.__module__}.{function.__name__}"


def get_state_default_value(
    state_typ: Type[Any],
    declared_default: Any,
    parameter_name_for_errors: str,
    resolver_fqn_for_errors: str,
) -> Any:
    if not issubclass(state_typ, BaseModel) and not dataclasses.is_dataclass(state_typ):
        raise ValueError(
            f"State value must be a pydantic model or dataclass, "
            f"but argument '{parameter_name_for_errors}' has type '{type(state_typ).__name__}'"
        )

    default = declared_default
    if default is inspect.Signature.empty:
        try:
            default = state_typ()
        except Exception as e:
            cls_name = state_typ.__name__
            raise ValueError(
                (
                    "State parameter must have a default value, or be able to be instantiated "
                    f"with no arguments. For resolver '{resolver_fqn_for_errors}', no default found, and default "
                    f"construction failed with '{str(e)}'. Assign a default in the resolver's "
                    f"signature ({parameter_name_for_errors}: {cls_name} = {cls_name}(...)), or assign a default"
                    f" to each of the fields of '{cls_name}'."
                )
            )

    if not isinstance(default, state_typ):
        raise ValueError(
            f"Expected type '{state_typ.__name__}' for '{parameter_name_for_errors}', but default has type '{type(default).__name__}'"
        )

    return default


def parse_function(
    fn: Callable,
    glbs: Optional[Dict[str, Any]],
    lcls: Optional[Dict[str, Any]],
    ignore_return: bool = False,
) -> ResolverParseResult:
    fqn = get_resolver_fqn(function=fn)
    sig = inspect.signature(fn)
    annotation_parser = ResolverAnnotationParser(fn, glbs, lcls)

    function_definition = inspect.getsource(fn)
    return_annotation = get_type_hints(fn).get("return")
    if return_annotation is None:
        raise TypeError(
            f"Resolver '{fqn}' must have a return annotation. See https://docs.chalk.ai/docs/resolver-outputs for more information."
        )

    ret_val = None

    if isinstance(return_annotation, FeatureWrapper):
        return_annotation = return_annotation._chalk_feature

    if isinstance(return_annotation, Feature):
        assert return_annotation.typ is not None

        if return_annotation.is_has_many:
            assert issubclass(return_annotation.typ.parsed_annotation, DataFrame)
            ret_val = Features[return_annotation.typ.parsed_annotation.columns]
        elif return_annotation.is_has_one:
            assert issubclass(return_annotation.typ.underlying, Features)
            ret_val = Features[return_annotation.typ.underlying.features]
        else:
            # function annotated like def get_account_id(user_id: User.id) -> User.account_id
            ret_val = Features[return_annotation]

    if ret_val is None:
        if not isinstance(return_annotation, type):
            raise TypeError(f"return_annotation {return_annotation} of type {type(return_annotation)} is not a type")
        if issubclass(return_annotation, Features):
            # function annotated like def get_account_id(user_id: User.id) -> Features[User.account_id]
            # or def get_account_id(user_id: User.id) -> User:
            ret_val = return_annotation
        elif issubclass(return_annotation, DataFrame):
            # function annotated like def get_transactions(account_id: Account.id) -> DataFrame[Transaction]
            ret_val = Features[return_annotation]

    if ret_val is None and not ignore_return:
        raise ValueError(f"Resolver {fqn} did not have a valid return type")

    inputs = [annotation_parser.parse_annotation(p) for p in sig.parameters.keys()]

    # Unwrap anything that is wrapped with FeatureWrapper
    inputs = [unwrap_feature(p) if isinstance(p, FeatureWrapper) else p for p in inputs]

    state = None
    default_args: List[Optional[ResolverArgErrorHandler]] = [None for _ in range(len(inputs))]

    for i, (arg_name, parameter) in enumerate(sig.parameters.items()):
        bad_input = lambda: ValueError(
            f"Resolver inputs must be Features or State. Received {str(inputs[i])} for argument '{arg_name}'."
        )
        arg = inputs[i]

        if isinstance(arg, GenericAlias) and get_origin(arg) == Union:
            args = get_args(arg)
            if len(args) != 2:
                raise bad_input()
            if type(None) not in args:
                raise bad_input()
            real_arg = next((a for a in args if a is not type(None)), None)
            if real_arg is None:
                raise bad_input()
            default_args[i] = ResolverArgErrorHandler(None)
            arg = unwrap_feature(real_arg)
            inputs[i] = arg

        if parameter.empty != parameter.default:
            default_args[i] = ResolverArgErrorHandler(parameter.default)

        if not isinstance(arg, (StateWrapper, Feature)):
            raise bad_input()

        if isinstance(arg.typ, ParsedAnnotation) and isinstance(arg.typ.underlying, Windowed):
            f = cast(Windowed, inputs[i].typ.underlying)
            raise ValueError(
                f"Resolver argument '{arg_name}' to '{fqn}' does not select a window. "
                f"Add a selected window, like {inputs[i].name}('{next(iter(f._buckets), '')}'). "
                f"Available windows: {', '.join(f._buckets)}."
            )

        if not isinstance(arg, StateWrapper):
            continue

        if state is not None:
            raise ValueError(
                f"Only one state argument is allowed. Two provided to '{fqn}': '{state.kwarg}' and '{arg_name}'"
            )

        arg_name = parameter.name
        arg = inputs[i]

        state = StateDescriptor(
            kwarg=arg_name,
            pos=i,
            initial=get_state_default_value(
                state_typ=arg.typ,
                resolver_fqn_for_errors=fqn,
                parameter_name_for_errors=arg_name,
                declared_default=parameter.default,
            ),
            typ=arg.typ,
        )

    assert ret_val is None or issubclass(ret_val, Features)

    state_index = state.pos if state is not None else None
    return ResolverParseResult(
        fqn=fqn,
        inputs=[v for i, v in enumerate(inputs) if i != state_index],
        output=ret_val,
        function_definition=function_definition,
        function=fn,
        doc=fn.__doc__,
        state=state,
        default_args=default_args,
    )


@overload
def online(
    *,
    environment: Optional[Environments] = None,
    tags: Optional[Tags] = None,
    cron: Optional[Union[ScheduleOptions, Cron]] = None,
    machine_type: Optional[MachineType] = None,
    when: Optional[Any] = None,
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    ...


@overload
def online(
    fn: Callable[P, T],
    /,
) -> Callable[P, T]:
    ...


def online(
    fn: Optional[Callable[P, T]] = None,
    /,
    *,
    environment: Optional[Environments] = None,
    tags: Optional[Tags] = None,
    cron: Optional[Union[ScheduleOptions, Cron]] = None,
    machine_type: Optional[MachineType] = None,
    when: Optional[Any] = None,
) -> Union[Callable[[Callable[P, T]], Callable[P, T]], Callable[P, T]]:
    caller_frame = inspect.stack()[1]
    caller_filename = caller_frame.filename
    caller_globals = caller_frame.frame.f_globals
    caller_locals = caller_frame.frame.f_locals

    def decorator(fn: Callable[P, T], cf: str = caller_filename):
        parsed = parse_function(fn, caller_globals, caller_locals)
        if not env_var_bool("CHALK_ALLOW_REGISTRY_UPDATES") and parsed.fqn in {s.fqn for s in Resolver.registry}:
            raise ValueError(f"Duplicate resolver {parsed.fqn}")
        if parsed.output is None:
            raise ValueError(f"Online resolvers must return features; '{parsed.fqn}' returns None")

        resolver = OnlineResolver(
            filename=cf,
            function_definition=parsed.function_definition,
            fqn=parsed.fqn,
            doc=parsed.doc,
            inputs=parsed.inputs,
            output=parsed.output,
            fn=parsed.function,
            environment=None if environment is None else list(ensure_tuple(environment)),
            tags=None if tags is None else list(ensure_tuple(tags)),
            max_staleness=None,
            cron=cron,
            machine_type=machine_type,
            when=when,
            state=parsed.state,
            default_args=parsed.default_args,
        )

        Resolver.registry.append(resolver)
        Resolver.hook and resolver.hook(resolver)

        # Return the decorated resolver, which notably implements __call__() so it acts the same as
        # the underlying function if called directly, e.g. from test code
        return resolver

    return decorator(fn) if fn else decorator


@overload
def offline(
    *,
    environment: Optional[Environments] = None,
    tags: Optional[Tags] = None,
    cron: Optional[Union[ScheduleOptions, Cron]] = None,
    machine_type: Optional[MachineType] = None,
    when: Optional[Any] = None,
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    ...


@overload
def offline(
    fn: Callable[P, T],
    /,
) -> Callable[P, T]:
    ...


def offline(
    fn: Optional[Callable[P, T]] = None,
    /,
    *,
    environment: Optional[Environments] = None,
    tags: Optional[Tags] = None,
    cron: Union[ScheduleOptions, Cron] = None,
    machine_type: Optional[MachineType] = None,
    when: Optional[Any] = None,
) -> Union[Callable[[Callable[P, T]], Callable[P, T]], Callable[P, T]]:
    caller_frame = inspect.stack()[1]
    caller_filename = caller_frame.filename
    caller_globals = caller_frame.frame.f_globals
    caller_locals = caller_frame.frame.f_locals

    def decorator(fn: Callable[P, T], cf: str = caller_filename):
        parsed = parse_function(fn, caller_globals, caller_locals)
        if not env_var_bool("CHALK_ALLOW_REGISTRY_UPDATES") and parsed.fqn in {s.fqn for s in Resolver.registry}:
            raise ValueError(f"Duplicate resolver {parsed.fqn}")
        if parsed.output is None:
            raise ValueError(f"Offline resolvers must return features; '{parsed.fqn}' returns None")
        resolver = OfflineResolver(
            filename=cf,
            function_definition=parsed.function_definition,
            fqn=parsed.fqn,
            doc=parsed.doc,
            inputs=parsed.inputs,
            output=parsed.output,
            fn=parsed.function,
            environment=None if environment is None else list(ensure_tuple(environment)),
            tags=None if tags is None else list(ensure_tuple(tags)),
            max_staleness=None,
            cron=cron,
            machine_type=machine_type,
            state=parsed.state,
            when=when,
            default_args=parsed.default_args,
        )
        Resolver.registry.append(resolver)
        Resolver.hook and resolver.hook(resolver)
        return fn

    return decorator(fn) if fn else decorator


@overload
def sink(
    *,
    environment: Optional[Environments] = None,
    tags: Optional[Tags] = None,
    machine_type: Optional[MachineType] = None,
    buffer_size: Optional[int] = None,
    debounce: Optional[Duration] = None,
    max_delay: Optional[Duration] = None,
    upsert: Optional[bool] = None,
    integration: Optional[BaseSQLSourceProtocol] = None,
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    ...


@overload
def sink(
    fn: Callable[P, T],
    /,
) -> Callable[P, T]:
    ...


def sink(
    fn: Optional[Callable[P, T]] = None,
    /,
    *,
    environment: Optional[Environments] = None,
    tags: Optional[Tags] = None,
    machine_type: Optional[MachineType] = None,
    buffer_size: Optional[int] = None,
    debounce: Optional[Duration] = None,
    max_delay: Optional[Duration] = None,
    upsert: Optional[bool] = None,
    integration: Optional[BaseSQLSourceProtocol] = None,
) -> Union[Callable[[Callable[P, T]], Callable[P, T]], Callable[P, T]]:
    caller_frame = inspect.stack()[1]
    caller_filename = caller_frame.filename
    caller_globals = caller_frame.frame.f_globals
    caller_locals = caller_frame.frame.f_locals

    def decorator(fn: Callable[P, T], cf: str = caller_filename):
        parsed = parse_function(fn, caller_globals, caller_locals, ignore_return=True)
        SinkResolver.registry.append(
            SinkResolver(
                filename=cf,
                function_definition=parsed.function_definition,
                fqn=parsed.fqn,
                doc=parsed.doc,
                inputs=parsed.inputs,
                output=parsed.output,
                fn=parsed.function,
                environment=None if environment is None else list(ensure_tuple(environment)),
                tags=None if tags is None else list(ensure_tuple(tags)),
                machine_type=machine_type,
                buffer_size=buffer_size,
                debounce=debounce,
                max_delay=max_delay,
                upsert=upsert,
                integration=integration,
            )
        )
        return fn

    return decorator(fn) if fn else decorator


class StreamResolver:
    registry: "List[StreamResolver]" = []

    def __init__(
        self,
        function_definition: str,
        fqn: str,
        filename: str,
        doc: Optional[str],
        source: StreamSource,
        mode: Optional[str],
        fn: Callable,
        signature: StreamResolverSignature,
        environment: Optional[Union[List[str], str]],
        machine_type: Optional[str],
        output: typing.Union[Type[Features], Type[DataFrame]],
    ):
        super(StreamResolver, self).__init__()
        self.function_definition = function_definition
        self.fqn = fqn
        self.filename = filename
        self.source = source
        self.mode = mode
        self.fn = fn
        self.environment = environment
        self.doc = doc
        self.machine_type = machine_type
        self.signature = signature
        self.output: Type[FeaturesImpl] = output
        fqn_to_windows = {
            o.fqn: o.typ.underlying.buckets_seconds
            for o in self.output.features
            if isinstance(o.typ.underlying, Windowed)
        }
        if len(set(tuple(v) for v in fqn_to_windows.values())) > 1:
            fqn_to_declared_windows = {
                o.fqn: sorted(list(o.typ.underlying._buckets))
                for o in self.output.features
                if isinstance(o.typ.underlying, Windowed)
            }
            periods = [f'{fqn}[{", ".join(window)}]' for fqn, window in fqn_to_declared_windows.items()]
            raise ValueError(f"All features must have the same window periods. Found " f"{', '.join(periods)}")
        self.window_periods_seconds: Optional[Sequence[int]] = next(iter(fqn_to_windows.values()), None)

    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs)

    def __repr__(self):
        return f"StreamResolver(name={self.fqn})"


def _is_stream_resolver_body_type(annotation: Type):
    return (
        annotation in {str, bytes}
        or (inspect.isclass(annotation) and issubclass(annotation, BaseModel))
        or dataclasses.is_dataclass(annotation)
    )


def _parse_stream_resolver_param(
    param: Parameter, annotation_parser: ResolverAnnotationParser, resolver_fqn_for_errors: str
) -> StreamResolverParam:
    if param.kind not in {Parameter.KEYWORD_ONLY, Parameter.POSITIONAL_OR_KEYWORD}:
        raise ValueError(
            f"Stream resolver {resolver_fqn_for_errors} includes unsupported keyword or variadic arg '{param.name}'"
        )

    annotation = annotation_parser.parse_annotation(param.name)
    if isinstance(annotation, StateWrapper):
        default_value = get_state_default_value(
            state_typ=annotation.typ,
            declared_default=param.default,
            resolver_fqn_for_errors=resolver_fqn_for_errors,
            parameter_name_for_errors=param.name,
        )
        return StreamResolverParamKeyedState(
            name=param.name,
            typ=annotation.typ,
            default_value=default_value,
        )

    if _is_stream_resolver_body_type(annotation):
        return StreamResolverParamMessage(name=param.name, typ=annotation)

    if isinstance(annotation, GenericAlias) and get_origin(annotation) in (list, List, Sequence):
        item_typ = get_args(annotation)[0]
        if _is_stream_resolver_body_type(item_typ):
            return StreamResolverParamMessageWindow(name=param.name, item_typ=item_typ)

    raise ValueError(
        f"Stream resolver parameter '{param.name}' of resolver '{resolver_fqn_for_errors}' is not recognized. "
        f"Message payloads must be one of `str`, `bytes`, or pydantic model class. "
        f"Keyed state parameters must be chalk.KeyedState[T]. "
        f"Received: {annotation}"
    )


def parse_stream_resolver_params(
    user_func: Callable, *, resolver_fqn_for_errors: str, annotation_parser: ResolverAnnotationParser
) -> Sequence[StreamResolverParam]:
    sig = inspect.signature(user_func)
    params = [
        _parse_stream_resolver_param(p, annotation_parser, resolver_fqn_for_errors) for p in sig.parameters.values()
    ]

    uses_message_body = any(
        p for p in params if isinstance(p, (StreamResolverParamMessage, StreamResolverParamMessageWindow))
    )

    if not uses_message_body:
        raise ValueError(
            f"Stream resolver '{resolver_fqn_for_errors}' must take as input "
            + f"a pydantic model, `str`, or `bytes` representing the message body"
        )

    keyed_state_params = [p.name for p in params if isinstance(p, StreamResolverParamKeyedState)]
    if len(keyed_state_params) > 1:
        raise ValueError(
            f"Stream resolver '{resolver_fqn_for_errors}' includes more than one KeyedState parameter: {keyed_state_params}"
        )

    return params


def parse_stream_resolver_output_features(
    user_func: Callable,
    *,
    resolver_fqn_for_errors: str,
) -> typing.Union[Type[Features], Type[DataFrame]]:
    """
    :param user_func:
    :param resolver_fqn_for_errors:
    :return: set of fqns of the output features
    """
    return_annotation = get_type_hints(user_func).get("return")
    if return_annotation is None:
        raise TypeError(
            f"Resolver '{user_func.__name__}' must have a return annotation. See "
            f"https://docs.chalk.ai/docs/resolver-outputs for "
            f"more information."
        )

    if not isinstance(return_annotation, type):
        raise TypeError(f"return_annotation {return_annotation} of type {type(return_annotation)} is not a type")

    if issubclass(return_annotation, Features):
        return cast(Type[Features], return_annotation)

    elif issubclass(return_annotation, DataFrame):
        # TODO: validate that these features are in the same namespace and include a pkey
        return cast(Type[DataFrame], return_annotation)

    else:
        raise ValueError(
            f"Stream resolver '{resolver_fqn_for_errors}' did not have a valid return type: "
            + f"must be a features class, chalk.features.Features[], or a chalk.features.DataFrame"
        )


def _parse_and_register_stream_resolver(
    *,
    caller_globals: Optional[Dict[str, Any]],
    caller_locals: Optional[Dict[str, Any]],
    fn: Callable,
    source: StreamSource,
    caller_filename: str,
    mode: Optional[str] = None,
    environment: Optional[Union[List[str], str]] = None,
    machine_type: Optional[MachineType] = None,
) -> StreamResolver:
    fqn = f"{fn.__module__}.{fn.__name__}"
    function_definition = inspect.getsource(fn)
    annotation_parser = ResolverAnnotationParser(fn, caller_globals, caller_locals)
    params = parse_stream_resolver_params(
        fn,
        resolver_fqn_for_errors=fqn,
        annotation_parser=annotation_parser,
    )

    output_features: Type[DataFrame] | Type[Features] = parse_stream_resolver_output_features(
        fn,
        resolver_fqn_for_errors=fqn,
    )

    signature = StreamResolverSignature(
        params=params,
        output_feature_fqns=set(o.fqn for o in output_features.features),
    )

    resolver = StreamResolver(
        filename=caller_filename,
        source=source,
        mode=mode,
        function_definition=function_definition,
        fqn=fqn,
        doc=fn.__doc__,
        fn=fn,
        environment=environment,
        machine_type=machine_type,
        signature=signature,
        output=output_features,
    )

    StreamResolver.registry.append(resolver)
    return resolver
