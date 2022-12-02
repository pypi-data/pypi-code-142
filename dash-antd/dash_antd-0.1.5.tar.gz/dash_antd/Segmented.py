# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Segmented(Component):
    """A Segmented component.
Segmented component

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- block (boolean; optional):
    Option to fit width to its parent\'s width.

- class_name (string; optional):
    Often used with CSS to style elements with common properties.

- disabled (boolean; optional):
    Disable all segments.

- key (string; optional):
    A unique identifier for the component, used to improve performance
    by React.js while rendering components See
    https://reactjs.org/docs/lists-and-keys.html for more info.

- options (list of strings | list of numbers; required):
    Set children optional.

- size (a value equal to: 'small', 'middle', 'large'; optional):
    The size of the Segmented.

- style (dict; optional):
    Defines CSS styles which will override styles previously set.

- value (string | number; optional):
    The input content value."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_antd'
    _type = 'Segmented'
    @_explicitize_args
    def __init__(self, block=Component.UNDEFINED, disabled=Component.UNDEFINED, options=Component.REQUIRED, size=Component.UNDEFINED, value=Component.UNDEFINED, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, class_name=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'block', 'class_name', 'disabled', 'key', 'options', 'size', 'style', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'block', 'class_name', 'disabled', 'key', 'options', 'size', 'style', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['options']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Segmented, self).__init__(**args)
