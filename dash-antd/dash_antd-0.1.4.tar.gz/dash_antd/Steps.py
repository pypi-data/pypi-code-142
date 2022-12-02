# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Steps(Component):
    """A Steps component.
Steps

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- class_name (string; optional):
    Often used with CSS to style elements with common properties.

- current (number; optional):
    To set the current step, counting from 0. You can overwrite this
    state by using status of Step.

- direction (a value equal to: 'horizontal', 'vertical'; optional):
    To specify the direction of the step bar, horizontal or vertical.

- initial (number; optional):
    Set the initial step, counting from 0.

- items (list of dicts; required):
    The children of this component.

    `items` is a list of dicts with keys:

    - description (string; optional):
        Description of the step.

    - disabled (boolean; optional):
        Disable click.

    - icon (a list of or a singular dash component, string or number; required):
        Icon of the step.

    - status (a value equal to: 'wait', 'process', 'finish', 'error'; optional):
        To specify the status. It will be automatically set by current
        of Steps if not configured.

    - subTitle (a list of or a singular dash component, string or number; optional):
        Subtitle of the step.

    - title (a list of or a singular dash component, string or number; optional):
        Title of the step.

- key (string; optional):
    A unique identifier for the component, used to improve performance
    by React.js while rendering components See
    https://reactjs.org/docs/lists-and-keys.html for more info.

- label_placement (a value equal to: 'horizontal', 'vertical'; optional):
    Place title and description with horizontal or vertical direction.

- percent (number; optional):
    Progress circle percentage of current step in process status (only
    works on basic Steps).

- progress_dot (boolean; optional):
    Steps with progress dot style.

- responsive (boolean; optional):
    Change to vertical direction when screen width smaller than 532px.

- size (a value equal to: 'default', 'small'; optional):
    To specify the size of the step bar.

- status (a value equal to: 'wait', 'process', 'finish', 'error'; optional):
    Specify the status of current step.

- style (dict; optional):
    Defines CSS styles which will override styles previously set.

- type (a value equal to: 'default', 'navigation'; optional):
    Type of steps."""
    _children_props = ['items[].icon', 'items[].subTitle', 'items[].title']
    _base_nodes = ['children']
    _namespace = 'dash_antd'
    _type = 'Steps'
    @_explicitize_args
    def __init__(self, children=None, items=Component.REQUIRED, current=Component.UNDEFINED, direction=Component.UNDEFINED, initial=Component.UNDEFINED, label_placement=Component.UNDEFINED, percent=Component.UNDEFINED, progress_dot=Component.UNDEFINED, responsive=Component.UNDEFINED, size=Component.UNDEFINED, status=Component.UNDEFINED, type=Component.UNDEFINED, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, class_name=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'class_name', 'current', 'direction', 'initial', 'items', 'key', 'label_placement', 'percent', 'progress_dot', 'responsive', 'size', 'status', 'style', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'class_name', 'current', 'direction', 'initial', 'items', 'key', 'label_placement', 'percent', 'progress_dot', 'responsive', 'size', 'status', 'style', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['items']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Steps, self).__init__(children=children, **args)
