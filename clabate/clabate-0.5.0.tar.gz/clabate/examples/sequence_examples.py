'''
Sequence example.

Copyright 2021-2022 AXY axy@declassed.art
License: BSD, see LICENSE for details.
'''

from . import assert_equal
from ..core import Template
from ..extras.sequence import SequenceMixin

class Example(Template, SequenceMixin('seq')):

    snippet = '''
        Initialize the sequence, i.e. start from 5:
        {seq:first(5)}

        Generate numbers 6, 7, 8, 10, 9:
        {seq:next()},
        {seq:next()},
        {seq:next()}
        {seq:next(10)}
        {seq:prev()}
    '''

def sequence_example():
    template = Example()
    context = template.render()
    expected_result = Template.dedent('''
        Initialize the sequence, i.e. start from 5:
        5

        Generate numbers 6, 7, 8, 10, 9:
        6,
        7,
        8
        10
        9
    ''')
    assert_equal(context.snippet, expected_result)
