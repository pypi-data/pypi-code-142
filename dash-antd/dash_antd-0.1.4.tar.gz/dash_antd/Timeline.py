# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Timeline(Component):
    """A Timeline component.
Timeline component

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this component.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- class_name (string; optional):
    Often used with CSS to style elements with common properties.

- key (string; optional):
    A unique identifier for the component, used to improve performance
    by React.js while rendering components See
    https://reactjs.org/docs/lists-and-keys.html for more info.

- mode (a value equal to: 'left', 'alternate', 'right'; optional):
    By sending alternate the timeline will distribute the nodes to the
    left and right.

- pending (boolean; optional):
    Set the last ghost node's existence or its content.

- reverse (boolean; optional):
    Whether reverse nodes or not.

- style (dict; optional):
    Defines CSS styles which will override styles previously set."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_antd'
    _type = 'Timeline'
    @_explicitize_args
    def __init__(self, children=None, mode=Component.UNDEFINED, pending=Component.UNDEFINED, reverse=Component.UNDEFINED, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, class_name=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'class_name', 'key', 'mode', 'pending', 'reverse', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'class_name', 'key', 'mode', 'pending', 'reverse', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Timeline, self).__init__(children=children, **args)
