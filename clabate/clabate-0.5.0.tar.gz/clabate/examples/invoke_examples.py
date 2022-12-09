'''
Invocation examples.

Copyright 2019-2022 AXY axy@declassed.art
License: BSD, see LICENSE for details.
'''

from . import assert_equal
from ..markup import Invoke, Template

class IdeaTemplate(Template):
    '''
    This class demonstrates the idea of invoke.
    '''
    snippet = '''
        The idea behind invoke {invoke_idea:is that format_spec is passed as is
        to the __format__ method where we can compile and run it}
    '''

    class InvokeIdea:

        def __format__(self, format_spec):
            return format_spec

    invoke_idea = InvokeIdea()

def idea_example():
    template = IdeaTemplate()
    context = template.render()
    expected_result = Template.dedent('''
        The idea behind invoke is that format_spec is passed as is
        to the __format__ method where we can compile and run it
    ''')
    assert_equal(context.snippet, expected_result)

class RealExampleTemplate(Template):
    '''
    A real example.
    '''
    snippet = '''
        So Invoke class provides __format__ method that does the job.
        Anything after colon is evaluated as a pythonic expression.
        We need to subclass it and define our methods.
        {my_invoke:one()}
        {my_invoke:two()}
        {my_invoke:three}  (yes, this is an attribute of my_invoke)
    '''

    class MyInvoke(Invoke):

        def one(self):
            return '1'

        def two(self):
            return '2'

        three = '3'

    my_invoke = MyInvoke()

def real_example():
    template = RealExampleTemplate()
    context = template.render()
    expected_result = Template.dedent('''
        So Invoke class provides __format__ method that does the job.
        Anything after colon is evaluated as a pythonic expression.
        We need to subclass it and define our methods.
        1
        2
        3  (yes, this is an attribute of my_invoke)
    ''')
    assert_equal(context.snippet, expected_result)

class InvokeWithParamsTemplate(Template):
    '''
    Arguments example.
    '''
    snippet = '''
        Parameters may contain any built-in types supported in python syntax.
        Mind braces escaping.
        If parameters are substitutions that may contain arbitrary quotes, use !r
        {arguments:show(
            'string',
            {another_string!r},
            True, False,
            1, 2.0, 3.4,
            a_complex = 5.0+6j,
            a_dict = {{'foo': 'bar'}},
            a_set = {{'foo'}},
            a_list = [1, 2, 3]
        )}
    '''
    # XXX both a_set and a_dict have single element to avoid troubles with unpredictable order

    another_string = '"wow, \'quotes\'"'

    class Arguments(Invoke):

        def show(self, *args, **kwargs):
            return f'args: {args}\nkwargs: {kwargs}'

    arguments = Arguments()

def arguments_example():
    template = InvokeWithParamsTemplate()
    context = template.render()
    expected_result = Template.dedent('''
        Parameters may contain any built-in types supported in python syntax.
        Mind braces escaping.
        If parameters are substitutions that may contain arbitrary quotes, use !r
        args: ('string', '"wow, \\'quotes\\'"', True, False, 1, 2.0, 3.4)
        kwargs: {'a_complex': (5+6j), 'a_dict': {'foo': 'bar'}, 'a_set': {'foo'}, 'a_list': [1, 2, 3]}
    ''')
    assert_equal(context.snippet, expected_result)

class UnderscoresTemplate(Template):
    '''
    Names that start with underscore are treated as special by clabate.
    '''
    snippet = '''
        Names should not start with underscore.
        This won't work: {i_want_this:_working()}
    '''

    class IWantThis(Invoke):

        def _working(self):
            return 'It works!!!'

    i_want_this = IWantThis()

def underscores_example():
    template = UnderscoresTemplate()
    try:
        context = template.render()
        assert False, 'WTF??? This should fail!'
    except Exception as e:
        assert e.args[0] == 'Denied access to _working'

class RestrictionsExampleTemplate(Template):
    '''
    Invoke allows only basic values as arguments.
    '''
    snippet = '''
        No function calls are allowed in params.
        This won't work: {i_want_this:working(tuple(1,2,3))}
    '''

    class IWantThis(Invoke):

        def working(self, arg):
            return f'It works: {arg}!!!'

    i_want_this = IWantThis()

def restrictions_example():
    template = RestrictionsExampleTemplate()
    try:
        context = template.render()
        assert False, 'WTF??? This should fail!'
    except Exception as e:
        assert e.args[0] == 'Calls are not allowed in parameters: working(tuple(1,2,3))'
