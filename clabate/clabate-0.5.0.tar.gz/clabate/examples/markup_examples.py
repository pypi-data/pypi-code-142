'''
Markup examples.

Copyright 2021-2022 AXY axy@declassed.art
License: BSD, see LICENSE for details.
'''

from types import SimpleNamespace

from . import assert_equal
from ..markup import MarkupTemplate, Markup

class HtmlBoilerplate(MarkupTemplate):

    html = Markup('''
        <html>
        {head}
        {body}
        </html>
    ''')

    head = Markup('''
        <head>
            <title>{title}</title>
        </head>
    ''')

    title = 'Example'

    body = Markup('''
        <body>
            <header>
                {header}
            </header>
            <main>
                {main}
            </main>
            <footer>
                {footer}
            </footer>
        </body>
    ''')

    header = Markup('This is <strong>header</strong>.')

    main = Markup('Main content goes <strong>here</strong>.')

    footer = Markup('This is <strong>footer</strong>.')

def html_boilerplate_example():
    template = HtmlBoilerplate()
    context = template.render()
    expected_result = MarkupTemplate.dedent('''
        <html>
        <head>
            <title>Example</title>
        </head>
        <body>
            <header>
                This is <strong>header</strong>.
            </header>
            <main>
                Main content goes <strong>here</strong>.
            </main>
            <footer>
                This is <strong>footer</strong>.
            </footer>
        </body>
        </html>
    ''')
    assert_equal(context.html, expected_result)


class MarkupExample(MarkupTemplate):
    '''
    All values are escaped unless they are Markup.
    This applies to everything: complex data, properties, kwargs, and missing values.
    '''
    attr = 'String attributes are <strong>escaped</strong>'
    markup_attr = Markup('Markup attributes are <strong>unchanged</strong>')
    snippet1 = Markup('''
        {attr}
        {markup_attr}
        {prop}
        {markup_prop}
        {constructor_kwarg}
        {markup_constructor_kwarg}
        {render_kwarg}
        {markup_render_kwarg}
        What is <a.b[name].c[1].d>? It's {a.b[name].c[1].d}!
        What is <a.b[name].c[1].e>? It's {a.b[name].c[1].e} and it is escaped!
        And what is foo.bar? {foo.bar}
        Wait, what is bar[foo][1]? {bar[foo][1]}
    ''')

    a = SimpleNamespace(
        b = dict(
            name = SimpleNamespace(
                c = [
                    0,
                    SimpleNamespace(
                        d = Markup('<span style="color:green">wow</span>'),
                        e = '<span style="color:green">wow</span>'
                    )
                ]
            )
        )
    )

    @property
    def prop(self, context):
        return 'Property values are <strong>escaped</strong>'

    @property
    def markup_prop(self, context):
        return Markup('Markup property values are <strong>unchanged</strong>')

    def missing(self, name):
        return Markup(f'<span style="color:red">{name}</span> is missing from the rendering context!')

    # And values are escaped only once!
    snippet2 = Markup('''
        Values are escaped only once:
        {snippet1}
        Otherwise we'd get lots of &amp; instead of bare &
    ''')

def markup_example():
    '''
    Render MarkupExample template.
    '''
    template = MarkupExample(
        constructor_kwarg='Constructor kwargs are <strong>escaped</strong>',
        markup_constructor_kwarg=Markup('Markup constructor kwargs are <strong>unchanged</strong>')
    )
    context = template.render(
        render_kwarg='Render kwargs are <strong>escaped</strong>',
        markup_render_kwarg=Markup('Markup render kwargs are <strong>unchanged</strong>')
    )
    expected_result1 = MarkupTemplate.dedent('''
        String attributes are &lt;strong&gt;escaped&lt;/strong&gt;
        Markup attributes are <strong>unchanged</strong>
        Property values are &lt;strong&gt;escaped&lt;/strong&gt;
        Markup property values are <strong>unchanged</strong>
        Constructor kwargs are &lt;strong&gt;escaped&lt;/strong&gt;
        Markup constructor kwargs are <strong>unchanged</strong>
        Render kwargs are &lt;strong&gt;escaped&lt;/strong&gt;
        Markup render kwargs are <strong>unchanged</strong>
        What is <a.b[name].c[1].d>? It's <span style="color:green">wow</span>!
        What is <a.b[name].c[1].e>? It's &lt;span style="color:green"&gt;wow&lt;/span&gt; and it is escaped!
        And what is foo.bar? <span style="color:red">foo</span> is missing from the rendering context!
        Wait, what is bar[foo][1]? <span style="color:red">bar</span> is missing from the rendering context!
    ''')
    assert_equal(context.snippet1, expected_result1)

    expected_result2 = MarkupTemplate.dedent('''
        Values are escaped only once:
        String attributes are &lt;strong&gt;escaped&lt;/strong&gt;
        Markup attributes are <strong>unchanged</strong>
        Property values are &lt;strong&gt;escaped&lt;/strong&gt;
        Markup property values are <strong>unchanged</strong>
        Constructor kwargs are &lt;strong&gt;escaped&lt;/strong&gt;
        Markup constructor kwargs are <strong>unchanged</strong>
        Render kwargs are &lt;strong&gt;escaped&lt;/strong&gt;
        Markup render kwargs are <strong>unchanged</strong>
        What is <a.b[name].c[1].d>? It's <span style="color:green">wow</span>!
        What is <a.b[name].c[1].e>? It's &lt;span style="color:green"&gt;wow&lt;/span&gt; and it is escaped!
        And what is foo.bar? <span style="color:red">foo</span> is missing from the rendering context!
        Wait, what is bar[foo][1]? <span style="color:red">bar</span> is missing from the rendering context!
        Otherwise we'd get lots of &amp; instead of bare &
    ''')
    assert_equal(context.snippet2, expected_result2)


class TagAttributesExample(MarkupTemplate):
    '''
    Tag attributes.
    '''
    link1 = '<a href="https://declassed.art">declassed.art</a>'
    snippet1 = Markup('''
        <span data-link="{link1}">wrong attribute escaping</span>
    ''')

    link2 = Markup('<a href="https://declassed.art">declassed.art</a>')
    snippet2 = Markup('''
        <span data-link={escape:attr({link2!r})}>correct attribute escaping</span>
    ''')

    snippet3 = Markup('''
        Inline javascript attribute escaping
        <p onclick={escape:attr("""
            run("<script>this()</script>");
            run('<script>that()</script>');
        """)}>Click me!</p>
    ''')

def tag_attributes_example():
    '''
    Render TagAttributesExample template.
    '''
    template = TagAttributesExample()
    context = template.render()
    expected_result1 = MarkupTemplate.dedent('''
        <span data-link="&lt;a href="https://declassed.art"&gt;declassed.art&lt;/a&gt;">wrong attribute escaping</span>
    ''')
    assert_equal(context.snippet1, expected_result1)

    expected_result2 = MarkupTemplate.dedent('''
        <span data-link='&lt;a href="https://declassed.art"&gt;declassed.art&lt;/a&gt;'>correct attribute escaping</span>
    ''')
    assert_equal(context.snippet2, expected_result2)

    expected_result3 = MarkupTemplate.dedent('''
        Inline javascript attribute escaping
        <p onclick="run(&quot;&lt;script&gt;this()&lt;/script&gt;&quot;);&#10;    run('&lt;script&gt;that()&lt;/script&gt;');">Click me!</p>
    ''')
    assert_equal(context.snippet3, expected_result3)


class MarkupInsideNonMarkup(MarkupTemplate):
    '''
    What if we insert markup in a non-markup?
    Suppose we want to insert some markup in a text to be escaped.
    '''
    # Some markup. Escape marks it as Escaped.
    # No actual escaping is performed because it's already markup.
    some_markup = Markup("""<span style="color:red">your custom HTML</span>""")

    # First snippet. Literal text around substitution is escaped by formatter.
    # Substitution is already escaped so copied to the resulting string as is.
    # The result is marked as Escaped.
    snippet1 = '''
        When a text is going to be <escaped> but you need
        to insert {some_markup}
    '''

    # Another way to do the above. The result is exactly the same.
    snippet2 = '''
        When a text is going to be <escaped> but you need
        to insert {escape:markup("""<span style="color:red">your custom HTML</span>""")}
    '''

    snippet3 = '''
        When a text is going to be <escaped> but you need
        to insert {escape:markup({some_markup!r})}
    '''

    # Literal text around substitutions is escaped by formatter.
    # Substitutions are already escaped so copied to the resulting string as is.
    # No double escaping takes place for substitutions.
    snippet4 = '''
        Doubly escaped?
        {snippet1}
        {snippet2}
        {snippet3}
        -- No!
    '''

    # Same as previous one, the substitution is already escaped
    # and no triple escaping takes place.
    snippet5 = '''
        Triply escaped?
        {snippet4}
        -- No!
    '''

def markup_inside_non_markup_example():
    template = MarkupInsideNonMarkup()
    context = template.render()
    expected_result = MarkupTemplate.dedent('''
        When a text is going to be &lt;escaped&gt; but you need
        to insert <span style="color:red">your custom HTML</span>
    ''')
    print()
    print('=== here is snippet5 from MarkupInsideNonMarkup which demonstrates that values are escaped only once ===')
    print(context.snippet5)
    print()
    assert_equal(context.snippet1, expected_result)
    assert_equal(context.snippet2, expected_result)
    assert_equal(context.snippet3, expected_result)
    assert '&lt;span' not in context.snippet4
    assert '&amp' not in context.snippet5


class TagAttrInsideNonMarkup(MarkupTemplate):
    '''
    How about escaping tag attribute in a non-markup?
    '''
    snippet1 = """<span data-link={escape:attr('<a href="https://declassed.art">declassed.art</a>')}>"""\
               "inline attribute gets doubly escaped</span>"

    snippet2 = """<span data-link={escape:attr({link!r})}>correct attribute escaping</span>"""
    link = Markup('<a href="https://declassed.art">declassed.art</a>')

def tag_attr_inside_non_markup_example():
    '''
    Render TagAttrInsideNonMarkup template
    '''
    template = TagAttrInsideNonMarkup()
    context = template.render()
    expected_result1 = """&lt;span data-link='&amp;lt;a href="https://declassed.art"&amp;gt;declassed.art&amp;lt;/a&amp;gt;'&gt;""" \
                       "inline attribute gets doubly escaped&lt;/span&gt;"
    assert_equal(context.snippet1, expected_result1)

    expected_result2 = """&lt;span data-link='&lt;a href="https://declassed.art"&gt;declassed.art&lt;/a&gt;'&gt;""" \
                       "correct attribute escaping&lt;/span&gt;"
    assert_equal(context.snippet2, expected_result2)


class FormatSpecEscapeTemplate(MarkupTemplate):
    '''
    Format specification is escaped because of recursive nature of `string.Formatter.vformat()` method.
    That's why attributes gets doubly escaped in `TagAttrInsideNonMarkup.snippet1`.
    '''
    snippet = '''
        This is a <literal text> preceeding the {substitution: And this is a <literal text>
        for {nested_substitution: which gets <doubly escaped> if not a markup!}}
    '''

    class MarkupSubst:
        def __format__(self, format_spec):
            return Markup(format_spec)

    class PlainSubst:
        def __format__(self, format_spec):
            return format_spec

    substitution = MarkupSubst()
    nested_substitution = PlainSubst()


def format_spec_escape_example():
    template = FormatSpecEscapeTemplate()
    context = template.render()
    expected_result = MarkupTemplate.dedent('''
        This is a &lt;literal text&gt; preceeding the  And this is a &lt;literal text&gt;
        for  which gets &amp;lt;doubly escaped&amp;gt; if not a markup!
    ''')
    assert_equal(context.snippet, expected_result)


#-----------------------------------------------------------------------------------
# How to use render_str

class RenderStrExample(MarkupTemplate):
    '''
    Example how to use render_str
    '''

    table = Markup('''
        <table>
        <tbody>
            {table_rows}
        </tbody>
        </table>
    ''')

    # attributes with underscores are not collected by template system so they are not formatted
    _row = Markup('<tr><td>{row_data[a]}</td><td>{row_data[b]}</td></tr>')

    @property
    def table_rows(self, context):
        # use Markup.join('\n', ...) instead of '\n'.join(...)
        return Markup.join('\n', (
            self.render_str(context, self._row, row_data=value)
            for value in context.table_data
        ))

def render_str_example():

    template = RenderStrExample()
    context = template.render(
        table_data = [dict(a=1, b=2), dict(a=3, b=4), dict(a=5, b=6)]
    )
    expected_table = MarkupTemplate.dedent('''
        <table>
        <tbody>
            <tr><td>1</td><td>2</td></tr>
            <tr><td>3</td><td>4</td></tr>
            <tr><td>5</td><td>6</td></tr>
        </tbody>
        </table>
    ''')
    assert_equal(context.table, expected_table)
