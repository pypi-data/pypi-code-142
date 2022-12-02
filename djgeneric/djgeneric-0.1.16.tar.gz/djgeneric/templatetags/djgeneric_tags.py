from django import template
from django.conf import settings
from django.utils.formats import number_format
from django.utils.translation import ugettext as _

register = template.Library()


@register.simple_tag(takes_context=True)
def querystring(context, **kwargs):
    args = context["request"].GET.copy()
    for k, v in kwargs.items():
        args[k] = v
    return args.urlencode()


SORT_FIELD = getattr(settings, "SORT_FIELD", "o")

SORT_FIELD = getattr(settings, "SORT_FIELD", "o")


SORT_ICON = getattr(settings, "SORT_ICON", '<i class="fa fa-sort"></i>')
SORT_ASC_ICON = getattr(
    settings, "SORT_ASC_ICON", '<i class="fa fa-sort-amount-asc"></i>'
)
SORT_DESC_ICON = getattr(
    settings, "SORT_DESC_ICON", '<i class="fa fa-sort-amount-desc"></i>'
)

SORTANCHOR_TEMPLATE = '<a href="%(url)s">%(text)s</a>'

CRISPY_TEMPLATE_PACK = getattr(settings, "CRISPY_TEMPLATE_PACK")
if CRISPY_TEMPLATE_PACK == "bootstrap4":
    SORTANCHOR_TEMPLATE = '<a class="text-nowrap text-decoration-none" href="%(url)s">%(text)s <small>%(icon)s</small></a>'

if CRISPY_TEMPLATE_PACK == "bootstrap5":
    SORTANCHOR_TEMPLATE = '<a class="text-nowrap text-decoration-none" href="%(url)s">%(text)s <small>%(icon)s</small></a>'


SORTANCHOR_TEMPLATE = getattr(settings, "SORANCHOR_TEMPLATE", SORTANCHOR_TEMPLATE)


def sortanchor(parser, token):
    """
    Parses a tag that's supposed to be in this format
        '{% sortanchor field title [default] %}'
    Title may be a "string", _("trans string"), or variable
    """
    bits = [b for b in token.split_contents()]
    if len(bits) < 2:
        raise template.TemplateSyntaxError("anchor tag takes at least 1 argument.")

    try:
        title = bits[2]
    except IndexError:
        title = bits[1].capitalize()

    if len(bits) > 3:
        default = bits[3]
    else:
        default = False

    return SortAnchorNode(bits[1].strip(), title, default)


class SortAnchorNode(template.Node):
    """
    Renders an <a> HTML tag with a link which href attribute
    includes the field on which we sort and the direction.
    and adds an up or down arrow if the field is the one
    currently being sorted on.

    Eg.
        {% sortanchor name Name %} generates
        <a href="/the/current/path/?sort=name" title="Name">Name</a>

    """

    def __init__(self, field, title, is_default):
        self.field = field
        self.title = title
        self.is_default = is_default

    def render(self, context):

        title = self.title

        if title[0] in ('"', "'"):
            if title[0] == title[-1]:
                title = title[1:-1]
            else:
                raise template.TemplateSyntaxError(
                    "sortanchor tag title "
                    'must be a "string", _("trans string"), or variable'
                )
        elif title.startswith('_("') or title.startswith("_('"):
            title = _(title[3:-2])
        else:
            #  Title is var
            title = context[title]

        request = context["request"]
        getvars = request.GET.copy()

        currentsort = ""
        sortby = self.field
        icon = SORT_ICON

        def invert_order(fields):
            res = []
            for field in fields.split(","):
                if field.startswith("-"):
                    res.append(field[1:])
                else:
                    res.append("-" + field)
            return ",".join(res)

        if SORT_FIELD in getvars:
            currentsort = getvars[SORT_FIELD]
        else:
            if self.is_default:
                if self.is_default == "-":
                    currentsort = invert_order(self.field)
                else:
                    currentsort = self.field

        if currentsort == self.field:
            sortby = invert_order(self.field)
            icon = SORT_ASC_ICON

        if invert_order(currentsort) == self.field:
            icon = SORT_DESC_ICON

        getvars[SORT_FIELD] = sortby

        url = "%s?%s" % (request.path, getvars.urlencode())
        return SORTANCHOR_TEMPLATE % {"url": url, "text": title, "icon": icon}


sortanchor = register.tag(sortanchor)


@register.filter
def money_format(num):
    if num is None:
        return ""
    if isinstance(num, str):
        return num
    return number_format(num, decimal_pos=2, force_grouping=True)
