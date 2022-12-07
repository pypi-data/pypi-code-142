import copy

import requests

from .. import OperatorType
from ..universe import Universe


class UniverseError(RuntimeError):

    def __init__(self, *args):
        super(FetchError, self).__init__(self, *args)


class FetchError(RuntimeError):

    def __init__(self, *args):
        super(FetchError, self).__init__(self, *args)


class ParsingError(RuntimeError):

    def __init__(self, *args):
        super(ParsingError, self).__init__(self, *args)


class Pipe:

    def __init__(self, definition: str, backend='https://api.vyze.io'):
        self._definition = definition

        self._model = None
        self._object = None
        self._model_node = None
        self._node_type = None
        self._orders = []
        self._filters = []

        self._backend: str = backend

    def model(self, model_id):
        new_pipe = copy.deepcopy(self)
        new_pipe._model = model_id
        return new_pipe

    def object(self, obj):
        new_pipe = copy.deepcopy(self)
        new_pipe._object = obj
        return new_pipe

    def filter(self, path: str, operator: OperatorType, value: any):
        new_pipe = copy.deepcopy(self)
        new_pipe._filters.append({
            'path': path,
            'operator': operator.value,
            'value': value,
        })
        return new_pipe

    def equal(self, path: str, value: any):
        return self.filter(path, OperatorType.EQUALS, value)

    def greater_than(self, path: str, value: any):
        return self.filter(path, OperatorType.GREATER, value)

    def less_than(self, path: str, value: any):
        return self.filter(path, OperatorType.LESS, value)

    def order(self, path: str, asc=True):
        new_pipe = copy.deepcopy(self)
        new_pipe._orders.append({
            'path': path,
            'descending': not asc,
        })
        return new_pipe

    def list_node(self):
        node = {
            'type': 'list',
            'list': {
                'entry': self._model_node,
            }
        }

        for o in self._orders:
            node = {
                'type': 'sort',
                'sort': {
                    'order': {
                        'source': self._path_source(o['path']),
                        'descending': o['descending'],
                    },
                    'node': node,
                }
            }

        for f in self._filters:
            node = {
                'type': 'filter',
                'filter': {
                    'filter': {
                        'source': self._path_source(f['path']),
                        'operator': f['operator'],
                        'value': f['value'],
                    },
                    'node': node,
                }
            }

        node = {
            'type': 'context',
            'context': {
                'context': {
                    'environment': {
                        'type': 'primitive',
                    },
                    'value': self._model,
                },
                'node': {
                    'type': 'specials',
                    'specials': {
                        'type': 'list',
                        'direct': True,
                        'indirect': True,
                        'node': node,
                    }
                }
            }
        }

        return node

    def object_node(self):
        if self._object:
            return {
                'type': 'context',
                'context': {
                    'context': {
                        'environment': {
                            'type': 'primitive',
                        },
                        'value': self._object,
                    },
                    'node': self._model_node,
                }
            }

        elif self._model:
            return {
                'type': 'context',
                'context': {
                    'context': {
                        'environment': {
                            'type': 'primitive',
                        },
                        'value': self._model,
                    },
                    'node': {
                        'type': 'specials',
                        'specials': {
                            'type': 'primitive',
                            'direct': True,
                            'indirect': True,
                            'node': self._model_node,
                        }
                    }
                }
            }

        else:
            return None

    def _path_source(self, path: str):
        source_node, format = _cut_map_nodes(path.split('.'), self._model_node)

        return {
            'type': 'node',
            'format': format,
            'node': source_node
        }

    def load_pipe(self, universe: Universe) -> None:
        if self._definition.startswith('$'):
            endpoint_node = universe.get_pipe(self._definition[1:])
            if not endpoint_node:
                raise UniverseError(f'Endpoint not found: {self._definition[1:]}')

            self._model_node = endpoint_node['node']
            self._node_type = endpoint_node['type']

            if endpoint_node['context']['value']:
                self._model = endpoint_node['context']['value']
            elif endpoint_node['context']['environment'].get('model'):
                self._model = endpoint_node['context']['environment']['model']

        else:
            req = {
                'universe': universe.definition.decode(encoding='utf-8', errors='strict'),
                'pipe': self._definition,
            }
            resp = requests.post(f'{self._backend}/pipe', json=req).json()
            if resp.get('parseErrors') is not None and len(resp['parseErrors']) != 0:
                raise ParsingError(resp['parseErrors'][0]['error'])
            if resp.get('error'):
                raise FetchError(resp['error'])
            self._model_node = resp['node']
            self._model = resp['model']

    def __copy__(self):
        new_pipe = Pipe(self._definition)
        new_pipe._model = self._model
        new_pipe._object = self._object
        new_pipe._model_node = copy.deepcopy(self._model_node)
        new_pipe._node_type = self._node_type
        return new_pipe


def _cut_map_nodes(path: list[str], iter_node: any) -> [any, str]:
    iter_type = iter_node['type']

    if iter_type == 'map':
        if len(path) == 0:
            raise RuntimeError('Path leads to a map. Add a field by attaching it with a dot (.)')

        for e in iter_node['map']['entries']:
            if e['name'] == path[0]:
                return _cut_map_nodes(path[1:], e['node'])
        raise RuntimeError(f'Entry not found: {path[0]}')

    elif iter_type == 'value':
        if len(path) != 0:
            raise RuntimeError(f'Path exceeds the node structure. Leftover path: ...{".".join(path)}')
        return copy.deepcopy(iter_node), iter_node['value']['format']

    elif iter_type == 'relation':
        return_node, format = _cut_map_nodes(path, iter_node['relation']['node'])
        iter_node = copy.deepcopy(iter_node)
        iter_node['relation']['node'] = return_node
        return iter_node, format

    elif iter_type == 'specials':
        return_node, format = _cut_map_nodes(path, iter_node['specials']['node'])
        iter_node = copy.deepcopy(iter_node)
        iter_node['specials']['node'] = return_node
        return iter_node, format

    raise RuntimeError(f'Unsupported node type: {iter_type}')
