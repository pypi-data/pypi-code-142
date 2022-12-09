'''
Basic examples.

Copyright 2021-2022 AXY axy@declassed.art
License: BSD, see LICENSE for details.
'''

import time
from types import SimpleNamespace

from . import assert_equal
from .. import Template, LeanTemplate, escape_braces, depends_on

#-----------------------------------------------------------------------------------
# Template inheritance

class Fruit(Template):
    '''
    This is an abstract template for fruits.
    Some substitutions are not defined yet.
    For dynamic substitution a class property is used.
    '''
    snippet = 'This is {a} {fruit_name}. The {fruit_name} is {fruit_attribute}.'

    @property
    def a(self, context):
        '''
        Return correct article for fruit_name.
        Property getters have `context` argument so they
        can access all substitutions.
        '''
        # Simplified logic just for illistration:
        if context.fruit_name.lower()[0] in 'aeio':
            return 'an'
        else:
            return 'a'

def fruit_example():
    '''
    Rendering Fruit template must fail because some substitutions are missing.
    '''
    template = Fruit()
    try:
        context = template.render()
        print(context.snippet)
        assert False, 'WTF? Fruit should fail!'
    except AttributeError as e:
        assert any(s in e.args[0] for s in [
            'Fruit does not provide fruit_name',
            'Fruit does not provide fruit_attribute'
        ])


class Apple(Fruit):
    '''
    Let's provide one missing substitution.
    Other substitutions will be provided as keyword parameters
    to the constructor and `render` method.
    '''
    fruit_name = 'apple'

def apple_example():
    '''
    Render Apple template, providing fruit_color as a keyword parameter
    to the `render` method.

    Strings passed to the constructor are treated as template strings,
    so they may contain substitutions.

    However strings, passed to the `render` method are treated
    as bare strings and are not formatted.

    That's because all potential template strings are detected
    and their dependencies get resolved in the constructor.

    But the `render` method is designed to be simple and fast
    so it does not check whether provided strings are templates,
    nor it handles any additional dependencies.
    It simply populates rendering context with provided values
    and invokes `format` method for template strings in the right order.
    '''
    template = Apple(fruit_attribute = 'pretty {fruit_color}')
    context = template.render(fruit_color='red')
    expected_result = 'This is an apple. The apple is pretty red.'
    assert_equal(context.snippet, expected_result)

    # again, strings passed as arguments to the render method are not formatted:
    context = template.render(fruit_color='{red}')
    expected_result = 'This is an apple. The apple is pretty {red}.'
    assert_equal(context.snippet, expected_result)


class Orange(Fruit):
    '''
    Braces escaping example.
    '''
    fruit_name = 'orange'
    fruit_attribute = '{{orange}}, period'
    # or:
    fruit_attribute = escape_braces('{orange}, period')

def orange_example():
    template = Orange()
    context = template.render(fruit_color='orange')
    expected_result = "This is an orange. The orange is {orange}, period."
    assert_equal(context.snippet, expected_result)

#-----------------------------------------------------------------------------------
# Dependencies

class FormattingOrderExample(Template):

    snippet = 'This snippet depends on {substitution1}.'
    substitution1 = 'the first substitution which, in turn, depends on {substitution2}'
    substitution2 = 'the second substitution which, in turn, depends on {substitution3}'
    substitution3 = 'the third substitution'

    def render(self, *args, **kwargs):
        '''
        Override render method to take a look at some internals:
        '''
        print(f'{self.__class__.__name__}; looking into template internals:')
        print('  data attributes:')
        for a in self._data_attributes.items():
            print(f'    {a}')
        print('  formatting order:')
        for a in self._template_attributes:
            print(f'    {a}')
        print()
        return super().render(*args, **kwargs)

def formatting_order_example():
    template = FormattingOrderExample()
    context = template.render()
    expected_result = 'This snippet depends on the first substitution which,'\
        ' in turn, depends on the second substitution which,'\
        ' in turn, depends on the third substitution.'
    assert_equal(context.snippet, expected_result)


#-----------------------------------------------------------------------------------
# Substitutions examples

class SubstitutionsExample(Template):
    '''
    A bit more complex substitutions and missing values:
    '''
    snippet1 = '''
        What is a.b[name].c[1].d? It's {a.b[name].c[1].d}!
        And what is foo.bar? {foo.bar}
        Wait, what is bar[foo][1]? {bar[foo][1]}
    '''

    a = SimpleNamespace(
        b = dict(
            name = SimpleNamespace(
                c = [
                    0,
                    SimpleNamespace(
                        d = 'wow'
                    )
                ]
            )
        )
    )

    def missing(self, name):
        return f'{name} is missing from the rendering context!'

    # Specifically, this is the case where __format__ method is required for MissingValue, see clabate/core.py:
    snippet2 = 'Missing {{baz:my format spec}}? {baz:my format spec}'

def substitutions_example():
    template = SubstitutionsExample()
    context = template.render()
    expected_result1 = Template.dedent('''
        What is a.b[name].c[1].d? It's wow!
        And what is foo.bar? foo is missing from the rendering context!
        Wait, what is bar[foo][1]? bar is missing from the rendering context!
    ''')
    expected_result2 = 'Missing {baz:my format spec}? baz is missing from the rendering context!'
    print('==================')
    print(context.snippet1    )
    assert_equal(context.snippet1, expected_result1)
    assert_equal(context.snippet2, expected_result2)

#-----------------------------------------------------------------------------------
# Use of properties

class PropertiesExample(Template):
    '''
    This example illustrates ways to use properties.

    Before any value gets formatted, the rendering context is populated
    with class attributes and values passed as kwargs to the template
    constructor and the `render` method.

    Properties are evaluated lazily. Their getters are called once
    and values are cached in the rendering context.

    A property can use some value from the context, but
    clabate can't detect such dependencies.
    There's a workaround, `depends_on` decorator.
    '''
    snippet = 'I love {something_to_love} and hate {something_to_hate}'

    @property
    @depends_on('kind_of_freedom')
    def something_to_love(self, context):
        return f'{context.kind_of_freedom} freedom'

    @property
    def something_to_hate(self, context):
        value = f"{self.activist_type} activists"
        return value

    kind_of_freedom = 'absolute'

    @property
    def activist_type(self, context=None):
        # this property is invoked as usual, so the context is optional
        return 'open source'

def properties_example():
    template = PropertiesExample()
    context = template.render()
    assert_equal(context.snippet, 'I love absolute freedom and hate open source activists')

#-----------------------------------------------------------------------------------
# How to use render_str

class RenderStrExample(Template):
    '''
    Examples how to use `render_str`
    '''
    one = 1
    two = 2
    three = 3

    snippet = "Here's some math: {formatted_examples}"

    @property
    def formatted_examples(self, context):
        # Strings passed to render() as kwargs are not formatted,
        # but we can do that in properties using render_str.
        # Here, for example, we format context.examples
        # (see render(examples=...) call below:
        return self.render_str(context, context.examples)

    table = '''
        +--------+--------+
        {table_rows}
        +--------+--------+
    '''

    # attributes with underscores are not collected by template system so they are not formatted
    _row = '| {row_data[a]:^6} | {row_data[b]:^6} |'

    @property
    def table_rows(self, context):
        return '\n'.join(
            self.render_str(context, self._row, row_data=value)
            for value in context.table_data
        )

def render_str_example():
    template = RenderStrExample()
    context = template.render(
        examples='{one}+{two}={three}; {three}-{one}={two}',
        table_data=[dict(a=1, b=2), dict(a=3, b=4), dict(a=5, b=6)]
    )
    expected_result = "Here's some math: 1+2=3; 3-1=2"
    assert_equal(context.snippet, expected_result)

    expected_table = Template.dedent('''
        +--------+--------+
        |   1    |   2    |
        |   3    |   4    |
        |   5    |   6    |
        +--------+--------+
    ''')
    assert_equal(context.table, expected_table)

#-----------------------------------------------------------------------------------
# Indentation

class IndentationExample(Template):
    '''
    Demonstrate indentation.
    '''

    # All strings are dedented and the leading empty line is stripped.
    zone_config = '''
        $TTL    3600
        @   IN  SOA (
                    {primary_ns[0]}.{idna_domain}.  ; MNAME
                    {rname}  ; RNAME
                    {timestamp}  ; SERIAL
                    {cache_params}
                    )
        {nameservers}
        {resource_records}
    '''

    idna_domain = 'declassed.art'
    primary_ns = ('ns1', '1.2.3.4')
    secondary_ns = ('ns2', '5.6.7.8')

    rname = 'axy.{idna_domain}.'

    @property
    def timestamp(self, context):
        #return int(time.time())
        return 1654791702

    cache_params = '''
        3600  ; REFRESH
        60    ; RETRY
        1W    ; EXPIRY
        60    ; MINIMUM Negative Cache TTL
    '''

    @property
    def nameservers(self, context):
        # in properties dedent should be called explicitly
        tmpl = self.dedent('''
            @  IN  NS  {ns_name}.{idna_domain}.
            {ns_name}  IN  A  {ns_addr}
        ''')
        result = []
        for ns_name, ns_addr in [self.primary_ns, self.secondary_ns]:
            result.append(self.render_str(context, tmpl, ns_name=ns_name, ns_addr=ns_addr))
        return ''.join(result)

    resource_records = '''
        @  IN  A   {main_server_addr}
        *  IN  A   {main_server_addr}
    '''

    main_server_addr = '9.10.11.12'

def indentation_example():
    template = IndentationExample()
    context = template.render()
    expected_result = Template.dedent('''
        $TTL    3600
        @   IN  SOA (
                    ns1.declassed.art.  ; MNAME
                    axy.declassed.art.  ; RNAME
                    1654791702  ; SERIAL
                    3600  ; REFRESH
                    60    ; RETRY
                    1W    ; EXPIRY
                    60    ; MINIMUM Negative Cache TTL
                    )
        @  IN  NS  ns1.declassed.art.
        ns1  IN  A  1.2.3.4
        @  IN  NS  ns2.declassed.art.
        ns2  IN  A  5.6.7.8
        @  IN  A   9.10.11.12
        *  IN  A   9.10.11.12
    ''')
    assert_equal(context.zone_config, expected_result)

#-----------------------------------------------------------------------------------
# LeanTemplate

class LeanTemplateExample(LeanTemplate):
    '''
    How would IndentationExample look with LeanTemplate as the base class?
    Let's simply copy-paste the code and compare.
    '''

    # All strings are dedented and the leading empty line is stripped.
    zone_config = '''
        $TTL    3600
        @   IN  SOA (
                    {primary_ns[0]}.{idna_domain}.  ; MNAME
                    {rname}  ; RNAME
                    {timestamp}  ; SERIAL
                    3600  ; REFRESH
                    60    ; RETRY
                    1W    ; EXPIRY
                    60    ; MINIMUM Negative Cache TTL
                    )
        {nameservers}
        {resource_records}
    '''

    idna_domain = 'declassed.art'
    primary_ns = ('ns1', '1,2,3,4')
    secondary_ns = ('ns2', '5,6,7,8')

    rname = 'axy.{idna_domain}.'

    @property
    def timestamp(self, context):
        #return int(time.time())
        return 1654791702

    @property
    def nameservers(self, context):
        # in properties dedent should be called explicitly
        tmpl = self.dedent('''
            @  IN  NS  {ns_name}.{idna_domain}.
            {ns_name}  IN  A  {ns_addr}
        ''')
        result = []
        for ns_name, ns_addr in [self.primary_ns, self.secondary_ns]:
            result.append(self.render_str(context, tmpl, ns_name=ns_name, ns_addr=ns_addr))
        return ''.join(result)

    resource_records = '''
        @  IN  A   {main_server_addr}
        *  IN  A   {main_server_addr}
    '''

    main_server_addr = '9.10.11.12'

def lean_template_example():
    template = LeanTemplateExample()
    context = template.render()
    expected_result = '\n'\
    '        $TTL    3600\n'\
    '        @   IN  SOA (\n'\
    '                    ns1.declassed.art.  ; MNAME\n'\
    '                    axy.declassed.art.  ; RNAME\n'\
    '                    1654791702  ; SERIAL\n'\
    '                    3600  ; REFRESH\n'\
    '                    60    ; RETRY\n'\
    '                    1W    ; EXPIRY\n'\
    '                    60    ; MINIMUM Negative Cache TTL\n'\
    '                    )\n'\
    '        \n'\
    '            @  IN  NS  ns1.declassed.art.\n'\
    '            ns1  IN  A  1,2,3,4\n'\
    '        \n'\
    '            @  IN  NS  ns2.declassed.art.\n'\
    '            ns2  IN  A  5,6,7,8\n'\
    '        \n'\
    '        \n'\
    '        @  IN  A   9.10.11.12\n'\
    '        *  IN  A   9.10.11.12\n'\
    '    \n'\
    '    '
    assert_equal(context.zone_config, expected_result)

    # How about performance?
    indent_template = IndentationExample()

    start_time = time.monotonic()
    for i in range(1000):
        indent_template.render()
    indent_time = time.monotonic() - start_time

    start_time = time.monotonic()
    for i in range(1000):
        template.render()
    lean_time = time.monotonic() - start_time

    print(f'IndentedTemplate: {indent_time:.6f}s, LeanTemplate: {lean_time:.6f}')
    # on my laptop:
    # IndentedTemplate: 0.123696, LeanTemplate: 0.076246
