from ..client.pipe import _cut_map_nodes


def test__cut_map_nodes_value1():
    node, format = _cut_map_nodes([], {
        'type': 'value',
        'value': {'format': 'string', 'field': 'data'},
    })
    assert node['type'] == 'value'
    assert format == 'string'


def test__cut_map_nodes_map1():
    node, format = _cut_map_nodes(['a'], {
        'type': 'map',
        'map': {
            'entries': [
                {
                    'name': 'a',
                    'node': {
                        'type': 'value',
                        'value': {
                            'format': 'string',
                            'field': 'data',
                        },
                    },
                },
            ],
        },
    })
    assert node['type'] == 'value'
    assert format == 'string'


def test__cut_map_nodes_map2():
    node, format = _cut_map_nodes(['a'], {
        'type': 'map',
        'map': {
            'entries': [
                {
                    'name': 'a',
                    'node': {
                        'type': 'relation', 'relation': {
                            'type': 'list', 'relation': 'rel',
                            'node': {
                                'type': 'value',
                                'value': {
                                    'format': 'string',
                                    'field': 'data',
                                },
                            },
                        },
                    },
                },
            ],
        },
    })
    assert node['type'] == 'relation'
    assert node['relation']['node']['type'] == 'value'
    assert format == 'string'


def test__cut_map_nodes_map3():
    node, format = _cut_map_nodes(['a', 'b'], {
        'type': 'map',
        'map': {
            'entries': [
                {
                    'name': 'a',
                    'node': {
                        'type': 'map',
                        'map': {
                            'entries': [
                                {
                                    'name': 'b',
                                    'node': {
                                        'type': 'value',
                                        'value': {
                                            'format': 'string',
                                            'field': 'data',
                                        },
                                    },
                                },
                            ],
                        },
                    },
                },
            ],
        },
    })
    assert node['type'] == 'value'
    assert format == 'string'
