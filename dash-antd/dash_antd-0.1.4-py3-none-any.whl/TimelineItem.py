# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class TimelineItem(Component):
    """A TimelineItem component.
An item in the timeline

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- class_name (string; optional):
    Often used with CSS to style elements with common properties.

- color (string; optional):
    Set the circle's color to blue, red, green, gray or other custom
    colors string.

- key (string; optional):
    A unique identifier for the component, used to improve performance
    by React.js while rendering components See
    https://reactjs.org/docs/lists-and-keys.html for more info.

- label (string; optional):
    Set the label.

- position (a value equal to: 'left', 'right'; optional):
    Customize node position.

- style (dict; optional):
    Defines CSS styles which will override styles previously set."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_antd'
    _type = 'TimelineItem'
    @_explicitize_args
    def __init__(self, color=Component.UNDEFINED, label=Component.UNDEFINED, position=Component.UNDEFINED, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, class_name=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'class_name', 'color', 'key', 'label', 'position', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'class_name', 'color', 'key', 'label', 'position', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(TimelineItem, self).__init__(**args)
