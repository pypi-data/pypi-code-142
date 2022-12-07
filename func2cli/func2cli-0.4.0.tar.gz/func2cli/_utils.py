import builtins
import functools
import inspect

from typing import Union, get_args, get_origin, get_type_hints

def default_parse_func(func):
    """
    Parse a function and its docstring, and return data for argument parsing.

    The default parse assumes that the docstring has a single-line summary of
    func, followed by a blank line, and then a series of parameter descriptions
    following ten dashes (as below). The parameter descriptions should consist
    of the parameter name and type, separated by a colon, on one line, followed
    by an indented description of the parameter. The parameter list should be
    separated from the rest of the docstring by a blank line.

    Parameters
    ----------
    func : function
        The function to be parsed.

    Returns
    -------
    name : str
        A sanitized version of func.__name__.
    description : str
        A description of the behavior of func.
    params : list of dict
        A list of keyword argument dictionaries that can be passed to successive
        calls to add_argument.

    """

    name = func.__name__.replace('_', '-')
    docstring = func.__doc__

    start = docstring.index('\n') + 1
    end = docstring.index('\n\n')
    description = docstring[start:end].strip()

    header = 'Parameters\n    ----------\n'
    docstring = docstring[(docstring.index(header) + len(header)):]
    docstring = docstring[:docstring.index('\n\n')]

    casters = {k : _get_caster(t) for k, t in get_type_hints(func).items()}
    defaults = _get_defaults(func)
    params = _get_params(docstring, casters, defaults)

    return name, description, params

def _get_caster(t):
    origin = get_origin(t)

    if origin is list:
        return functools.partial(_parse_list, cast=get_args(t)[0])

    if origin is Union:
        return _get_caster(get_args(t)[0])

    if t is bool:
        return _parse_bool

    return t

def _get_defaults(func):
    defaults = {}
    for k, v in inspect.signature(func).parameters.items():
        if v.default is not inspect.Parameter.empty:
            defaults[k] = v.default

    return defaults

def _get_params(docstring, casters, defaults):
    params = []
    for line in [s[4:] for s in docstring.split('\n')]:
        if not line.startswith('    '):
            param_name, help = line.strip().split(' : ')
            prefix = '--' if param_name in defaults else ''

            caster = casters[param_name]
            default = defaults.get(param_name, None)
            
            if prefix:
                param_name = param_name.replace('_', '-')

            params.append({
                'param_name' : prefix + param_name,
                'metavar' : param_name.replace('_', '-'),
                'type' : caster,
                'default' : default,
                'help' : [help]
            })

        else:
            params[-1]['help'].append(line.strip())

    for param in params:
        param['help'] = ' '.join(param['help']).replace('_', '-')

    return params

def _parse_bool(s):
    return {'True' : True, 'False' : False}[s]

def _parse_list(s, cast):
    return [cast(v) for v in s.split(',')]
