from __future__ import annotations

import copy
import inspect
import pydoc
import typing as t
from importlib.util import find_spec

from pyqtgraph.parametertree import (
    InteractiveFunction,
    Interactor as PtreeInteractor,
    RunOptions as PtreeRunOpts,
)
from pyqtgraph.parametertree.interactive import PARAM_UNSET
from pyqtgraph.parametertree.Parameter import PARAM_TYPES

from qtextras import fns

T = t.TypeVar("T")


class FROM_PREV_IO(PARAM_UNSET):
    """
    Helper class to indicate whether a key in this IO is supposed to come from
    a previous process stage. Typical usage:
    ```if not hyperparam: self[k] = self.FROM_PREV_IO```

    Typically, process objects will have two IO dictionaries: One that hold the input
    spec (which makes use of `FROM_PREV_IO`) and one that holds the runtime process
    values. The latter IO will not make use of `FROM_PREV_IO`.
    """


class RunOptions(PtreeRunOpts):
    # Backwards compatibility
    ON_BUTTON = PtreeRunOpts.ON_ACTION


def bindInteractorOptions(overwrite=False, **opts):
    """
    Decorator to bind options to an interactor. This is useful for when the
    call to `interact` is separate from the function definition, but parameter
    options should be located with the function definition. Used as a decorator:
    >>> from qtextras import bindInteractorOptions as bind, QtExtrasInteractor
    >>> @bind(a=dict(step=5))
    ... def myFunc(a=1):
    ...     print(a)
    >>> step = QtExtrasInteractor().interact(myFunc).child("a").opts["step"]
    >>> assert step == 5
    """

    def wrapper(func: T) -> T:
        if hasattr(func, "__interactor_bind_options__") and not overwrite:
            func.__interactor_bind_options__.update(opts)
        else:
            func.__interactor_bind_options__ = opts
        return func

    return wrapper


class QtExtrasInteractor(PtreeInteractor):
    titleFormat = fns.nameFormatter

    _interactiveFunction = None
    _hideUnspecified = True

    def interact(self, function, **kwargs):
        interactive = self._toInteractiveFunction(function)
        self._interactiveFunction = interactive
        out = super().interact(interactive, **kwargs)
        self._interactiveFunction = None
        return out

    def functionToParameterDict(self, function, **overrides):
        if hasattr(function, "__interactor_bind_options__"):
            overrides = self.combineOverridesAndBindOptions(
                function.__interactor_bind_options__, overrides
            )

        ret = super().functionToParameterDict(function, **overrides)
        keepChildren = []
        for child in ret.pop("children", []):
            if child := self.resolveChildDict(self._interactiveFunction, child):
                keepChildren.append(child)
        ret["children"] = keepChildren
        return ret

    def combineOverridesAndBindOptions(self, bindOptions: dict, overrides: dict):
        if not bindOptions:
            return overrides
        if overrides:
            bindOptions = copy.deepcopy(bindOptions)
        for kk, vv in overrides.items():
            if not isinstance(vv, dict):
                overrides[kk] = dict(value=vv)
        overrides = fns.hierarchicalUpdate(bindOptions, overrides)
        return overrides

    def resolveChildDict(
        self, interactive: InteractiveFunction | None, child: dict[str, t.Any]
    ):
        name, value, typ = child["name"], child["value"], child["type"]
        extra = interactive.extra if interactive else None

        if value is PARAM_UNSET:
            # Easier to track by renaming / reclassifying
            value = child["value"] = FROM_PREV_IO
        if typ not in PARAM_TYPES:
            child["type"] = "display"

        if extra is None:
            # If children are discarded, there is no way to retrieve them. So,
            # in this event, don't remove children that are only displayable
            return child

        if (
            value is FROM_PREV_IO
            or child.get("ignore")
            or (typ not in PARAM_TYPES and self._hideUnspecified)
        ):
            # Avoid causing failures from unspecified parameters, since qtextras
            # allows chaining multiple processes together
            # Also, preserve ignored parameter values while preventing their display

            # TODO: The child can be hooked up to `interactive.parameters` to avoid
            #  losing `opts`, but this requires i.e. understanding when to clear the
            #  cache, additional overhead, and some guarantees in base methods that
            #  don't yet exist. For now, consider additional options lost and simply
            #  add the value to `extra`
            extra.setdefault(name, value)

        if name in extra:
            return None
        return child

    def _resolveFunctionGroup(self, functionDict, interactiveFunction):
        # Possible for name to be overridden at the interactive level without
        # affecting the raw function name. In this case, prefer the interactive
        # name. Note in all cases where `interactiveFunc.__name__ == function.__name__`,
        # this is basically an inexpensive no-op.
        functionDict["name"] = interactiveFunction.__name__
        if self.titleFormat is not None:
            functionDict["title"] = self._nameToTitle(
                functionDict["name"], forwardStringTitle=True
            )

        return super()._resolveFunctionGroup(functionDict, interactiveFunction)


class ParameterlessInteractor(QtExtrasInteractor):
    """
    Places every key in "extra" instead of making parameters
    """

    def interact(self, function, *, ignores=None, **kwargs):
        if ignores is None:
            ignores = []
        ignores = set(ignores)
        funcDict = self.functionToParameterDict(function, **kwargs.get("overrides", {}))
        ignores.update(ch["name"] for ch in funcDict["children"])
        return super().interact(function, ignores=ignores, **kwargs)


class DocstringInteractor(QtExtrasInteractor):
    def functionToParameterDict(self, function, **overrides):
        out = super().functionToParameterDict(function, **overrides)
        names = [ch["name"] for ch in out["children"]]
        docDict = parseDocstringTips(function.__doc__, names)
        for child in out["children"]:
            if childDoc := docDict.get(child["name"]):
                child.setdefault("tip", childDoc)
        if tip := docDict.get("function-tip"):
            out.setdefault("tip", tip)
        return out


def parseDocstringTips(doc: str, parameter_names: list[str] | None = None):
    # Use docstring parser if it's available, otherwise basic parsing
    if find_spec("docstring_parser") is not None:
        return _parseTipsUsingDocstringParser(doc, parameter_names)
    else:
        return _parseTipsUsingIndentation(doc, parameter_names)


def _parseTipsUsingDocstringParser(doc, parameter_names: list[str] | None = None):
    import docstring_parser

    out = {}
    parsed = docstring_parser.parse(doc)
    # Give a name with a hyphen since this cannot override a real parameter name
    out["function-tip"] = "\n".join(
        [
            desc
            for desc in [parsed.short_description, parsed.long_description]
            if desc is not None
        ]
    )
    if parameter_names is None:
        parameter_names = [param.arg_name for param in parsed.params]
    for param in parsed.params:
        if param.arg_name not in parameter_names:
            continue
        # Construct mini ini file around each parameter
        descr = param.description
        if not descr:
            continue
        out[param.arg_name] = descr
    return out


def _parseTipsUsingIndentation(doc, parameter_names: list[str] | None = None):
    if not doc:
        return {}
    dedented = inspect.cleandoc(doc)
    # Assume each parameter is unindented and its description is indented
    if parameter_names is None:
        raise ValueError(
            "Must provide parameter names if using indentation-baseddocumetation parsing"
        )
    synopsis, dedented = pydoc.splitdoc(dedented)
    out = {"function-tip": synopsis}
    lines = dedented.splitlines()
    unparsed = set(parameter_names)
    while lines and unparsed:
        line = lines.pop(0)
        rstripped = line.rstrip()
        to_parse: set[str] = {name for name in unparsed if rstripped.startswith(name)}
        if not to_parse:
            continue
        # if multiple names are found, the longest match should be used
        name = sorted(to_parse, key=len, reverse=True)[0]
        unparsed.remove(name)
        try:
            descr = _getIndentedDescription(lines)
            out[name] = descr
        except ValueError:
            # No indented description found, all bets are off
            return out
    return out


def _getIndentedDescription(lines: list[str]):
    if not (lines and lines[0] and lines[0][0].isspace()):
        raise ValueError(
            "Can only parse docstrings whose parameter descriptions are " "indented"
        )
    descr = []
    while lines:
        line = lines[0]
        if not line or not line[0].isspace():
            break
        descr.append(line.strip())
        lines.pop(0)
    return "\n".join(descr)
