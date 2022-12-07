# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class SelectableBoxList(Component):
    """A SelectableBoxList component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:

- id (string; optional)

- className (string; optional)

- optionChildren (list of a list of or a singular dash component, string or numbers; required)

- optionValues (list of string | numbers; required)

- value (string | number; optional)"""
    _children_props = ['optionChildren']
    _base_nodes = ['optionChildren', 'children']
    _namespace = 'selectable_box_list'
    _type = 'SelectableBoxList'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, optionChildren=Component.REQUIRED, optionValues=Component.REQUIRED, value=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'optionChildren', 'optionValues', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'optionChildren', 'optionValues', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['optionChildren', 'optionValues']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(SelectableBoxList, self).__init__(**args)
