from typing import Pattern
from selectolax.parser import Node

def ensure_str(x):
    if isinstance(x, str):
        return x

    if isinstance(x, Node):
        return x.text().strip()

    return str(x)

def maybe_int(x):
    try:
        return int(x)
    except:
        return None

def apply_eval(tree, node, selector, conversions):
    """Evaluate a set of instructions to node, returning its result."""

    rv = node

    if selector:
        if selector.startswith('html '):
            nodes = tree.css(selector[5:])
        else:
            nodes = rv.css(selector)

        if len(nodes) == 0:
            return None
        rv = nodes[0]

    for conversion in conversions or []:
        if isinstance(conversion, Pattern):
            m = conversion.search(ensure_str(rv))
            if m:
                if 'rv' in m.groupdict():
                    rv = m.group('rv')
            else:
                rv = None
        elif conversion == 'int':
            rv = maybe_int(ensure_str(rv))
        elif conversion.startswith('@'):
            attr_name = conversion[1:]

            if attr_name in rv.attrs:
                rv = rv.attrs[attr_name]
            else:
                rv = None
        else:
            raise Exception('unknown conversion: ' + conversion)

    if isinstance(rv, Node):
        return ensure_str(rv)

    return rv



def extract_rows(tree, instructions):
    if not 'selector' in instructions:
        raise Exception('expected top-level key `selector`, but was missing')

    selector = instructions['selector']
    if not isinstance(selector, str):
        raise Exception('expected top-level key `selector` to be str, but was: ' + str(selector))

    if not 'columns' in instructions:
        raise Exception('expected top-level key `columns`, but was missing')

    columns = instructions['columns']
    if not isinstance(columns, list):
        raise Exception('expected top-level key `columns` to be list, but was: ' + str(columns))

    if not columns:
        raise Exception('expected at least one value in `columns`, but was empty')

    rv = []

    for i in range(len(columns)):
        column = columns[i]
        if not isinstance(column, dict):
            raise Exception('expected `columns[' + str(i) + ']` to be a dict, but was ' + str(column))

        if not isinstance(column.get('selector', ''), str):
            raise Exception('expected `columns[' + str(i) + '].selector` to be str, but was ' + str(columns[i].selector))

        if not isinstance(column.get('optional', False), bool):
            raise Exception('expected columns[' + str(i) + '].optional to be absent or bool, but was ' + str(column['optional']))

        if not isinstance(column.get('conversions', []), list):
            raise Exception('expected `columns[' + str(i) + '].conversions` to be absent or list, but was ' + str(column['conversions']))

    for node in tree.css(selector):
        candidate = []

        ok = True

        for i, column in enumerate(columns):
            #print('Evaluating for key=' + k)
            value = apply_eval(tree, node, column.get('selector'), column.get('conversions', []))

            if value is None and not column.get('optional'):
                #print('  did not find value')
                ok = False
                continue

            candidate.append(value)

        if ok:
            rv.append(candidate)

    return rv


