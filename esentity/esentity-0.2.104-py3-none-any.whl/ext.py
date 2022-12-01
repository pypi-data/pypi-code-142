#coding: utf-8
from flask import current_app, g, request, abort
from flask_login import current_user
from itsdangerous import exc
from jinja2 import TemplateNotFound, TemplateSyntaxError
from jinja2.ext import Extension
from jinja2.nodes import List, CallBlock
from esentity.models import Page, Activity
from loguru import logger
from json import dumps, loads
import html
import math
from urllib.parse import unquote
from babel.numbers import format_decimal
import pendulum
import pycountry
import random

class HtmlExtension(Extension):
    tags = set(['html'])

    def __init__(self, environment):
        super(HtmlExtension, self).__init__(environment)

    def _render(self, caller):
        rv = caller()
        return html.unescape(rv)

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        body = parser.parse_statements(['name:endhtml'], drop_needle=True)
        args = []

        return CallBlock(self.call_method("_render", args), [], [], body).set_lineno(lineno)


# class LicencesExtension(Extension):
#     tags = set(['licences'])

#     def __init__(self, environment):
#         super(LicencesExtension, self).__init__(environment)

#     def _render(self, caller):
#         pages, _ = Page.get(
#             category='collection',
#             is_active=True,
#             is_searchable=True,
#             is_redirect=False,  
#             locale=g.language, 
#             _source=['title', 'path', 'alt_title'],
#             collection_mode='CasinoLicence',
#             _count=100,
#             _sort=[
#                 {'alt_title.keyword': {'order': 'asc'}}
#             ]
#         )
#         t = current_app.jinja_env.get_template('_table-licences.html')
#         s = t.render(pages=pages)
#         return s

#     def parse(self, parser):
#         lineno = next(parser.stream).lineno

#         body = ''
#         args = []

#         return CallBlock(self.call_method("_render", args), [], [], body).set_lineno(lineno)


class CollectionsExtension(Extension):
    tags = set(['collections'])

    def __init__(self, environment):
        super(CollectionsExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info('collections Args IN: {0}'.format(args))

        default = ['collections', 'CasinoSoftware', 100, None, 500, []]
        _ca = len(default)
        args = args[:_ca] + default[len(args):] + args[_ca:]

        logger.info('collections Args OUT: {0}'.format(args))

        template = args[0]
        mode = args[1]
        count = int(args[2])
        aggs_key = args[3]
        aggs_count = int(args[4])
        exclude = args[5]

        items, _ = Page.get(
            category='collection',
            is_active=True,
            is_searchable=True,
            is_redirect=False,  
            locale=g.language, 
            _source=['title', 'path', 'alt_title', 'custom_text', 'logo', 'theme_color'],
            collection_mode=mode,
            _count=count,
            _exclude=exclude,
            _sort=[
                {'alt_title.keyword': {'order': 'asc'}}
            ]
        )

        aggs = []
        if aggs_key:
            filter_list =  [ 
                {"term": {"is_active": True}},
                {"term": {"is_draft": False}},
                {"term": {"is_sandbox": False}},
                {"term": {"is_searchable": True}},
                {"term": {"is_redirect": False}},
                {"term": {"category.keyword": 'provider'}},
                {"term": {"locale.keyword": g.language}},
            ]

            _aggs = {
                aggs_key: {
                    "terms": {
                        "field": f"{aggs_key}.keyword",
                        "size": aggs_count,
                        "order": {"_count": "desc"}
                    },
                    # "aggs": {
                    #     "casinos": {
                    #         "top_hits": {
                    #             "sort": [
                    #                 {
                    #                     "rating": {
                    #                         "order": "desc"
                    #                     }
                    #                 }
                    #             ],
                    #             "_source": {
                    #                 "includes": ["title", "path", "alt_title", "rating"]
                    #             },
                    #             "size": 3
                    #         }
                    #     }                
                    # }
                }
            }

            q = {
                "query": {
                    "bool": {
                        "must": filter_list,
                    }
                },
                "aggs": _aggs,
                "size": 0,
                "_source": False,
            }

            resp = current_app.es.search(index=Page._table(), body=q, request_timeout=60, ignore=[400, 404])
            aggs = resp['aggregations'][aggs_key]['buckets']

        logger.info(aggs)

        t = current_app.jinja_env.get_template(f'_ext-{template}.html')
        s = t.render(
            items=items, 
            aggs={item['key']: item['doc_count'] for item in aggs}
        )

        return s


    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
            parser.stream.skip_if('comma')

        return CallBlock(self.call_method("_render", args=[List(args)]), [], [], []).set_lineno(lineno)          


# class CollectionsExtension(Extension):
#     tags = set(['collections'])

#     def __init__(self, environment):
#         super(CollectionsExtension, self).__init__(environment)

#     def _render(self, caller):
#         pages, _ = Page.get(
#             category='collection',
#             is_active=True,
#             is_searchable=True,
#             is_redirect=False,  
#             locale=g.language, 
#             _source=['title', 'path', 'alt_title', 'custom_text', 'logo'],
#             collection_mode='CasinoSoftware',
#             _count=100,
#             _sort=[
#                 {'alt_title.keyword': {'order': 'asc'}}
#             ]
#         )
#         pages = {item.alt_title: item for item in pages}

#         # v2 (with aggs)

#         filter_list =  [ 
#             {"term": {"is_active": True}},
#             {"term": {"is_draft": False}},
#             {"term": {"is_sandbox": False}},
#             {"term": {"is_searchable": True}},
#             {"term": {"is_redirect": False}},
#             {"term": {"category.keyword": 'provider'}},
#             {"term": {"locale.keyword": g.language}},
#         ]

#         _aggs = {
#             "software": {
#                 "terms": {
#                     "field": "software.keyword",
#                     "size": 500,
#                     "order": {"_count": "desc"}
#                 },
#                 # "aggs": {
#                 #     "casinos": {
#                 #         "top_hits": {
#                 #             "sort": [
#                 #                 {
#                 #                     "rating": {
#                 #                         "order": "desc"
#                 #                     }
#                 #                 }
#                 #             ],
#                 #             "_source": {
#                 #                 "includes": ["title", "path", "alt_title", "rating"]
#                 #             },
#                 #             "size": 3
#                 #         }
#                 #     }                
#                 # }
#             }
#         }

#         q = {
#             "query": {
#                 "bool": {
#                     "must": filter_list,
#                 }
#             },
#             "aggs": _aggs,
#             "size": 0,
#             "_source": False,
#         }

#         resp = current_app.es.search(index=Page._table(), body=q, request_timeout=60, ignore=[400, 404])

#         if 'status' in resp and resp['status'] in [400, 404]:
#             return ''

#         t = current_app.jinja_env.get_template('_table-simple.html')
#         s = t.render(pages=pages, title='Software', items=resp['aggregations']['software']['buckets'])

#         return s

#     def parse(self, parser):
#         lineno = next(parser.stream).lineno

#         body = ''
#         args = []

#         return CallBlock(self.call_method("_render", args), [], [], body).set_lineno(lineno)


# class CountriesExtension(Extension):
#     tags = set(['countries'])

#     def __init__(self, environment):
#         super(CountriesExtension, self).__init__(environment)

#     def _render(self, caller):
#         pages, _ = Page.get(
#             category='collection',
#             is_active=True,
#             is_searchable=True,
#             is_redirect=False,  
#             locale=g.language, 
#             _source=['title', 'path', 'alt_title'],
#             collection_mode='CasinoCountry',
#             _count=100,
#             _sort=[
#                 {'alt_title.keyword': {'order': 'asc'}}
#             ]
#         )
#         t = current_app.jinja_env.get_template('_table-countries.html')
#         s = t.render(pages=pages)
#         return s

#     def parse(self, parser):
#         lineno = next(parser.stream).lineno

#         body = ''
#         args = []

#         return CallBlock(self.call_method("_render", args), [], [], body).set_lineno(lineno)        


# class BankingExtension(Extension):
#     tags = set(['banking'])

#     def __init__(self, environment):
#         super(BankingExtension, self).__init__(environment)

#     def _render(self, caller):
#         pages, _ = Page.get(
#             category='collection',
#             is_active=True,
#             is_searchable=True,
#             is_redirect=False,  
#             locale=g.language, 
#             _source=['title', 'path', 'alt_title', 'custom_text', 'logo'],
#             collection_mode=['CasinoBanking', 'CasinoBankingLimits'],
#             _count=100,
#             _sort=[
#                 {'alt_title.keyword': {'order': 'asc'}}
#             ]
#         )
#         pages = {item.alt_title: item for item in pages}

#         # v2 (with aggs)

#         filter_list =  [ 
#             {"term": {"is_active": True}},
#             {"term": {"is_draft": False}},
#             {"term": {"is_sandbox": False}},
#             {"term": {"is_searchable": True}},
#             {"term": {"is_redirect": False}},
#             {"term": {"category.keyword": 'provider'}},
#             {"term": {"locale.keyword": g.language}},
#         ]

#         _aggs = {
#             "deposits": {
#                 "terms": {
#                     "field": "deposits.keyword",
#                     "size": 500,
#                     "order": {"_count": "desc"}
#                 },
#                 # "aggs": {
#                 #     "casinos": {
#                 #         "top_hits": {
#                 #             "sort": [
#                 #                 {
#                 #                     "rating": {
#                 #                         "order": "desc"
#                 #                     }
#                 #                 }
#                 #             ],
#                 #             "_source": {
#                 #                 "includes": ["title", "path", "alt_title", "rating"]
#                 #             },
#                 #             "size": 3
#                 #         }
#                 #     }                
#                 # }
#             }
#         }

#         q = {
#             "query": {
#                 "bool": {
#                     "must": filter_list,
#                 }
#             },
#             "aggs": _aggs,
#             "size": 0,
#             "_source": False,
#         }

#         resp = current_app.es.search(index=Page._table(), body=q, request_timeout=60, ignore=[400, 404])

#         if 'status' in resp and resp['status'] in [400, 404]:
#             return ''

#         t = current_app.jinja_env.get_template('_table-simple.html')
#         s = t.render(pages=pages, title='Payment Method', items=resp['aggregations']['deposits']['buckets'])

#         return s

#     def parse(self, parser):
#         lineno = next(parser.stream).lineno

#         body = ''
#         args = []

#         return CallBlock(self.call_method("_render", args), [], [], body).set_lineno(lineno)  


class RatingExtension(Extension):
    tags = set(['rating'])

    def __init__(self, environment):
        super(RatingExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info(f'Casinos Args IN: {args}')

        default = ['casino', True, 10, False]
        _ca = len(default)
        args = args[:_ca] + default[len(args):] + args[_ca:]

        logger.info('Casinos Args OUT: {0}'.format(args))

        service = args[0]
        has_filters = args[1]
        count = int(args[2])
        row_mode = bool(args[3])

        tags = args[4:]
        logger.info('Casinos Tags: {0}'.format(tags))

        _afields = ['software', 'licences', 'deposits', 'withdrawal', 'games']
        _aggs = {
            item: {
                "terms": {
                    "field": "{0}.keyword".format(item),
                    "size": 500,
                    "order": {"_key": "asc"}
                }
            } for item in _afields
        }

        # args: service
        pages, found, aggs, id = Page.provider_by_context(
            is_searchable=True,
            is_redirect=False,
            country=current_user.country_full,
            services=service,
            provider_tags=tags,
            _locale=g.language,
            _source = [
                "title", 
                "alias", 
                "logo", 
                "logo_white",
                "logo_small",
                "external_id", 
                "theme_color", 
                "welcome_package", 
                "welcome_package_note",
                "provider_pros",
                "services",
                "welcome_package_max_bonus",
                "welcome_package_fs",
                "default_currency",
                "rating",
                "rank",
                "user_rating",
                "is_sponsored",
                "website",
                "provider_pros",
                "licences",
                "ref_link",
                "geo",
            ] + _afields, 
            _count=count,
            _aggs = _aggs
        )
        if id and has_filters:
            _c = dumps(aggs)
            current_app.redis.hset('aggs', id, _c)
            logger.info('Cache aggs {0}: {1}'.format(id, len(_c)))

        deposits_primary = ['Visa', 'Trustly', 'PayPal', 'Skrill', 'Neteller']

        t = current_app.jinja_env.get_template('_ext-rating_casinos.html')
        s = t.render(
            pages=pages, 
            has_filters=has_filters, 
            found=found, 
            service=service, 
            id=id, 
            count=count,
            tags=tags,
            deposits_primary=deposits_primary,
            row_mode=row_mode
        )
        return s

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
            parser.stream.skip_if('comma')

        return CallBlock(self.call_method("_render", args=[List(args)]), [], [], []).set_lineno(lineno)          


class TopSlotsExtension(Extension):
    tags = set(['top_slots'])

    def __init__(self, environment):
        super(TopSlotsExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info('Top Slots IN Args: {0}'.format(args))

        default = ['NetEnt', 8, 4, False, True]
        args = args[:4] + default[len(args):] + args[4:]

        logger.info('Top Slots OUT Args: {0}'.format(args))

        provider = args[0]
        count = int(args[1])
        in_row = int(args[2])
        random = bool(args[3])
        show_provider = bool(args[4])

        # args: service
        slots, found = Page.get(
            is_active=True, 
            is_searchable=True, 
            is_redirect=False,
            locale=g.language, 
            _source=True, 
            _count=count,
            _random=random,
            category='slot',
            software=provider, 
        )

        t = current_app.jinja_env.get_template('_ext-slots_list.html')
        s = t.render(
            slots=slots,
            in_row=in_row,
            show_provider=show_provider,
        )
        return s

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
            parser.stream.skip_if('comma')

        return CallBlock(self.call_method("_render", args=[List(args)]), [], [], []).set_lineno(lineno)          


class GuideExtension(Extension):
    tags = set(['guides'])

    def __init__(self, environment):
        super(GuideExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info('Guide args: {0}'.format(args))

        guides, found = Page.get(
            is_active=True, 
            is_searchable=True, 
            is_redirect=False, 
            tags=args[0],
            locale=g.language, 
            _source=['path', 'title'], 
            _count=500,
            _sort=[
                {'publishedon': {'order': 'desc'}}
            ]
        )
        t = current_app.jinja_env.get_template('_table-guides.html')
        s = t.render(pages=guides, found=found)
        return s

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
            parser.stream.skip_if('comma')

        return CallBlock(self.call_method("_render", args=[List(args)]), [], [], []).set_lineno(lineno)          


class TopCasinosExtension(Extension):
    tags = set(['top_casinos'])

    def __init__(self, environment):
        super(TopCasinosExtension, self).__init__(environment)

    def _render(self, caller=None):
        top, found = Page.provider_by_context(
            country=current_user.country_full,
            is_searchable=True,
            is_redirect=False,
            _locale=g.language,
            _source = [
                "title", 
                "alias", 
                "logo", 
                "logo_white",
                "logo_small",
                "external_id", 
                "theme_color", 
                "welcome_package", 
                "welcome_package_note",
                "provider_pros",
                "services",
                "welcome_package_max_bonus",
                "welcome_package_fs",
                "default_currency",
                "rating",
                "rank",
                "user_rating",
                "is_sponsored",
                "website",
                "provider_pros",
                "licences",
                "ref_link",
                "geo",
            ], 
            _count=3
        )    
        t = current_app.jinja_env.get_template('_top-casinos.html')
        s = t.render(top=top, found=found)
        return s

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        body = ''
        args = []
        return CallBlock(self.call_method("_render", args), [], [], body).set_lineno(lineno)


class CasinoAppsExtension(Extension):
    tags = set(['casino_apps'])

    def __init__(self, environment):
        super(CasinoAppsExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info('CasinoApps IN Args: {0}'.format(args))

        default = [True]
        args = args[:len(default)-1] + default[len(args):] + args[len(default)-1:] # TODO (-1 ??)

        logger.info('CasinoApps OUT Args: {0}'.format(args))

        t = current_app.jinja_env.get_template('_ext-casino-apps.html')
        s = t.render()
        return s

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
            parser.stream.skip_if('comma')

        return CallBlock(self.call_method("_render", args=[List(args)]), [], [], []).set_lineno(lineno)          


class SlotPlayExtension(Extension):
    tags = set(['slot_play'])

    def __init__(self, environment):
        super(SlotPlayExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info('SlotPlay IN Args: {0}'.format(args))

        title = args[0]
        alias = args[1]
        screen = args[2]

        t = current_app.jinja_env.get_template('_ext-slot-play.html')
        s = t.render(screen=screen, alias=alias, title=title)
        return s

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
            parser.stream.skip_if('comma')

        return CallBlock(self.call_method("_render", args=[List(args)]), [], [], []).set_lineno(lineno)          


class AuthorExtension(Extension):
    tags = set(['author_badge'])

    def __init__(self, environment):
        super(AuthorExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info('Author IN Args: {0}'.format(args))

        author = args[0]

        t = current_app.jinja_env.get_template('_ext-author.html')
        s = t.render(author=author)
        return s

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
            parser.stream.skip_if('comma')

        return CallBlock(self.call_method("_render", args=[List(args)]), [], [], []).set_lineno(lineno)          


class TopAlexaExtension(Extension):
    tags = set(['top_alexa'])

    def __init__(self, environment):
        super(TopAlexaExtension, self).__init__(environment)

    def _render(self, caller=None):
        pages, _ = Page.get(
            category='provider',
            is_active=True,
            is_searchable=True,
            is_redirect=False,  
            locale=g.language, 
            _source=['title', 'path', 'alias', 'alt_title', 'rank_alexa', 'geo'],
            _count=30,
            _sort=[
                {'rank_alexa': {'order': 'asc'}}
            ]
        )
   
        t = current_app.jinja_env.get_template('_ext-top_alexa.html')
        s = t.render(pages=pages)
        return s

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        body = ''
        args = []
        return CallBlock(self.call_method("_render", args), [], [], body).set_lineno(lineno)


class CasinosExtension(Extension):
    tags = set(['casinos'])

    def __init__(self, environment):
        super(CasinosExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info('casinos Args IN: {0}'.format(args))

        default = [10, 'casinos_top', True, False, None] # cnt, template, has_geo, has_append, sort, [tags...]
        _ca = len(default)
        args = args[:_ca] + default[len(args):] + args[_ca:]

        logger.info('casinos Args OUT: {0}'.format(args))

        count = int(args[0])
        template = args[1]
        has_geo = bool(args[2])
        has_append = bool(args[3])
        sorting = args[4]

        tags = args[len(default):]
        logger.info('casinos Tags: {0}'.format(tags))

        kwargs = {
            'is_searchable': True,
            'is_redirect': False,
            'country': current_user.country_full if has_geo else None,
            'provider_tags': tags,
            '_source': True, 
            '_count': count,
            '_sorting': sorting,
        }
        if len(current_app.config['AVAILABLE_LOCALE']) > 1:
            kwargs['locale_available'] = g.language

        pages, found = Page.provider_by_context(**kwargs)
        logger.info(f'Casinos found: {found}')

        if has_append and has_geo and found < count and tags:
            kwargs = {
                'is_searchable': True,
                'is_redirect': False,
                'country': None,
                'country': current_user.country_full if has_geo else None,
                '_source': True, 
                '_count': count - found,
                '_exclude': [casino._id for casino in pages],
            }
            if len(current_app.config['AVAILABLE_LOCALE']) > 1:
                kwargs['locale_available'] = g.language

            pages_level_2, found_level_2 = Page.provider_by_context(**kwargs)
            logger.info(f'Casinos level-2 found: {found_level_2}')
            pages += pages_level_2

        now = pendulum.now('UTC')

        s = str(args)
        try:
            t = current_app.jinja_env.get_template('_ext-{0}.html'.format(template))
            s = t.render(
                pages=pages, 
                found=found, 
                count=count,
                my=now.format('MMMM YYYY'),
            )
        except TemplateNotFound:
            pass

        return s

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
            parser.stream.skip_if('comma')

        return CallBlock(self.call_method("_render", args=[List(args)]), [], [], []).set_lineno(lineno)          


class SlotsExtension(Extension):
    tags = set(['slots'])

    def __init__(self, environment):
        super(SlotsExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info(f'Slots Args IN: {args}')

        default = [10, 'rating_slots', False] # cnt, template, has_filters, [tags...]
        _ca = len(default)
        args = args[:_ca] + default[len(args):] + args[_ca:]

        logger.info('Slots Args OUT: {0}'.format(args))

        count = int(args[0])
        template = args[1]
        has_filters = bool(args[2])

        tags = args[3:]
        logger.info('Slots Tags: {0}'.format(tags))

        _afields = ['software', 'volatility', 'themes', 'slot_features']
        _aggs = {
            item: {
                "terms": {
                    "field": "{0}.keyword".format(item),
                    "size": 500,
                    "order": {"_key": "asc"}
                }
            } for item in _afields
        }

        slots, found, aggs, id = Page.slots_by_context(
            is_searchable=True, 
            is_redirect=False, 
            _locale=g.language, 
            _source=[
                'alias', 
                'title', 
                'cover', 
                'software'
            ] + _afields, 
            _count=count,
            _aggs=_aggs,
        )            

        if id and has_filters:
            _c = dumps(aggs)
            current_app.redis.hset('aggs', id, _c)
            logger.info('Cache aggs {0}: {1}'.format(id, len(_c)))

        t = current_app.jinja_env.get_template('_ext-{0}.html'.format(template))
        s = t.render(
            slots=slots, 
            has_filters=has_filters, 
            found=found, 
            id=id, 
            count=count,
            tags=tags,
        )
        return s

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
            parser.stream.skip_if('comma')

        return CallBlock(self.call_method("_render", args=[List(args)]), [], [], []).set_lineno(lineno)          


class TicketExtension(Extension):
    tags = set(['ticket'])

    def __init__(self, environment):
        super(TicketExtension, self).__init__(environment)

    def _render(self, caller):
        t = current_app.jinja_env.get_template('_ext-ticket.html')
        return t.render()

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        return CallBlock(self.call_method("_render", []), [], [], '').set_lineno(lineno)


class CookiesExtension(Extension):
    tags = set(['cookies'])

    def __init__(self, environment):
        super(CookiesExtension, self).__init__(environment)

    def _render(self, caller):
        t = current_app.jinja_env.get_template('_ext-cookies.html')
        return t.render()

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        return CallBlock(self.call_method("_render", []), [], [], '').set_lineno(lineno)


class PromoExtension(Extension):
    tags = set(['promo'])

    def __init__(self, environment):
        super(PromoExtension, self).__init__(environment)

    def _render(self, caller):
        t = current_app.jinja_env.get_template('_ext-promo.html')
        return t.render()

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        return CallBlock(self.call_method("_render", []), [], [], '').set_lineno(lineno)


class AuthExtension(Extension):
    tags = set(['auth'])

    def __init__(self, environment):
        super(AuthExtension, self).__init__(environment)

    def _render(self, caller):
        t = current_app.jinja_env.get_template('_ext-auth.html')
        return t.render()

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        return CallBlock(self.call_method("_render", []), [], [], '').set_lineno(lineno)


class AgeExtension(Extension):
    tags = set(['age'])

    def __init__(self, environment):
        super(AgeExtension, self).__init__(environment)

    def _render(self, caller):
        t = current_app.jinja_env.get_template('_ext-age.html')
        return t.render()

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        return CallBlock(self.call_method("_render", []), [], [], '').set_lineno(lineno)


class GeoCountriesExtension(Extension):
    tags = set(['geo_countries'])

    def __init__(self, environment):
        super(GeoCountriesExtension, self).__init__(environment)

    def _render(self, caller):
        t = current_app.jinja_env.get_template('_ext-geo_countries.html')
        countries = g.countries
        if not current_user.location_iso in [i for c, i in countries]:
            countries = [(current_user.location, current_user.location_iso)] + countries

        return t.render(countries=countries, current=current_user.location_iso)

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        return CallBlock(self.call_method("_render", []), [], [], '').set_lineno(lineno)


class CompareButtonExtension(Extension):
    tags = set(['compare_button'])

    def __init__(self, environment):
        super(CompareButtonExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info('Args: {0}'.format(args))

        t = current_app.jinja_env.get_template('_ext-compare_button.html')
        s = t.render(uid=Page.get_urlsafe_string(6), alias=args[0], title=args[1], logo=args[2])
        return s

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
            parser.stream.skip_if('comma')

        return CallBlock(self.call_method("_render", args=[List(args)]), [], [], []).set_lineno(lineno)          


class ComparatorExtension(Extension):
    tags = set(['comparator'])

    def __init__(self, environment):
        super(ComparatorExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info('Args: {0}'.format(args))

        try:
            casinos = []
            casinos = []
            select_enable = False

            if request.cookies.get('comparator'):
                cmp_list = loads(unquote(request.cookies.get('comparator')))
                logger.info(f'Casinos for compare: {cmp_list}')

                casinos, _ = Page.get(
                    category='provider',
                    alias=[item['alias'] for item in cmp_list],
                    is_active=True,
                    is_searchable=True,
                    is_redirect=False,  
                    locale=g.language, 
                    _count=3,
                )

            if len(casinos) <= 3:
                recommended, _ = Page.provider_by_context(
                    country=current_user.country_full,
                    is_searchable=True,
                    is_redirect=False,
                    _locale=g.language,
                    _source=[
                        'alias', 
                        'title', 
                        'theme_color', 
                        'logo', 
                    ], 
                    _exclude=[casino._id for casino in casinos],
                    _count=6
                )

                def process_casino(i):
                    obj = Page({
                        'title': 'Casino ' + str(i + 1),
                        'logo': '/static/media/images/default-cover.png',
                        'theme_color': '#1b114d'
                    }, Page.get_urlsafe_string(6))
                    return obj

                if len(casinos) < 3:
                    select_enable = True

                casinos = casinos + [process_casino(i) for i in range(0, 3 - len(casinos))]

            t = current_app.jinja_env.get_template('_ext-comparator.html')
            attrs = {
                'General': [
                    'logo', 
                    'path', 
                    'establishedon',
                    'website',
                    'languages',
                    'services',
                    'licences',
                    'provider_pros',
                    'provider_cons',
                    'rating',
                    'user_rating',
                    'rank_alexa',
                    'geo',
                    'path',
                ],
                'Support': [
                    'support_languages',
                    'support_livechat',
                    'support_email',
                    'support_phone',
                    'support_worktime',
                    'logo',
                    'path',
                ],
                'Banking': [
                    'currencies',
                    'deposits',
                    'withdrawal',
                    'min_deposit',
                    'min_withdrawal',
                    # 'withdrawal_time',
                    'withdrawal_monthly',
                    'kyc_deposit',
                    'kyc_withdrawal',
                    'path',
                ],
                'Games': [
                    'games',
                    'software',
                    'games_count',
                    'path',
                ],
                'Promotions': [
                    'welcome_package',
                    'welcome_package_note',
                    'welcome_package_wager',
                    'path',
                ],
            }

            names = {
                'logo': '',
                'establishedon': 'Launched',
                'website': 'Website',
                'languages': 'Interface',
                'services': 'Services',
                'licences': 'Licences',
                'path': '',
                'provider_pros': 'Pros',
                'provider_cons': 'Cons',
                'rating': 'Editor Rating',
                'user_rating': 'Players Rating',
                'rank_alexa': 'Alexa Rank',
                'geo': 'Acceptable Countries',
                'support_languages': 'Support Languages',
                'support_livechat': 'Livechat Available',
                'support_email': 'Support E-mail',
                'support_phone': 'Support Phone',
                'support_worktime': 'Support Worktime',
                'currencies': 'Currencies',
                'deposits': 'Deposit Methods',
                'withdrawal': 'Withdrawal Methods',
                'min_deposit': 'Minimal Deposit',
                'min_withdrawal': 'Minimal Withdrawal',
                'withdrawal_time': 'Withdrawal Time',
                'withdrawal_monthly': 'Withdrawal Monthly Limit',
                'kyc_deposit': 'KYC Deposit',
                'kyc_withdrawal': 'KYC Withdrawal',
                'games': 'Games types',
                'software': 'Game Providers',
                'games_count': 'Games count',
                'welcome_package': 'Welcome Package',
                'welcome_package_note': 'Requirements',
                'welcome_package_wager': 'Wager',
            }

            s = t.render(
                casinos=casinos, 
                attrs=attrs, 
                names=names, 
                currency_geo=g.currency_geo,
                select_enable=select_enable,
                recommended=recommended
            )
            return s
        except Exception as e:
            logger.error(f'Comparator Exception: {e}')

        return ''

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
            parser.stream.skip_if('comma')

        return CallBlock(self.call_method("_render", args=[List(args)]), [], [], []).set_lineno(lineno)          


class BlogExtension(Extension):
    tags = set(['blog'])

    def __init__(self, environment):
        super(BlogExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info('blog Args: {0}'.format(args))

        default = [12, 3, True]
        _ca = len(default)
        args = args[:_ca] + default[len(args):] + args[_ca:]

        _cpp = int(args[0])
        _row = int(args[1])
        _paging = bool(args[2])

        page = 1
        p = request.args.get('page')
        if p:
            if p.isdigit():
                page = int(request.args.get('page'))
            else:
                abort(404)

        pages, total = Page.get(
            is_active=True,
            is_searchable=True, 
            is_redirect=False, 
            locale=g.language, 
            tags='Blog',
            _source=['path', 'title', 'publishedon', 'cover'],
            _count=_cpp,
            _offset=(page - 1) * _cpp,
            _sort=[
                {'publishedon': {'order': 'desc'}}
            ]
        )

        logger.debug('Page: {0}'.format(page))
        logger.debug('Total: {0}'.format(total))

        if (page - 1) * _cpp > total or (request.args.get('page') and page < 2):
            abort(404)

        paging = []
        if _paging:
            paging = [{'page': item, 'value': item} for item in range(1, math.ceil(total / _cpp) + 1)]

        t = current_app.jinja_env.get_template('_ext-blog.html')
        return t.render(pages=pages, paging=paging, current=page, row=_row)

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
            parser.stream.skip_if('comma')

        return CallBlock(self.call_method("_render", args=[List(args)]), [], [], []).set_lineno(lineno)          


class TopPromoExtension(Extension):
    tags = set(['top_promo'])

    def __init__(self, environment):
        super(TopPromoExtension, self).__init__(environment)

    def _render(self, caller=None):
        logger.info(f'Generate (top_promo) for {current_user.country_full}')

        casinos, found = Page.provider_by_context(
            country=current_user.country_full,
            is_searchable=True,
            is_redirect=False,
            provider_tags='TopPromo',
            _locale=g.language,
            _source = [
                "title", 
                "alias", 
                "path",
            ], 
            _count=3
        )    
        t = current_app.jinja_env.get_template('_ext-promo.html')
        s = t.render(casinos=casinos, found=found)
        return s

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        body = ''
        args = []
        return CallBlock(self.call_method("_render", args), [], [], body).set_lineno(lineno)


class TabMenuExtension(Extension):
    tags = set(['tab_menu'])

    def __init__(self, environment):
        super(TabMenuExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info('tab_menu Args: {0}'.format(args))

        path = str(args[0])

        _aggs = {
            item: {
                "terms": {
                    "field": "{0}.keyword".format(item),
                    "size": 500,
                    "order": {"_key": "asc"}
                }
            } for item in ['provider_tags', 'deposits', 'games']
        }

        _, _, aggs, _ = Page.provider_by_context(
            country=current_user.country_full,
            is_searchable=True,
            is_redirect=False,
            services=['casino'],
            _locale=g.language,
            _count=0,
            _aggs=_aggs
        )    

        def process_count(_items, _key):
            for item in _items:
                if item['item'] == _key:
                    return item['count']
            return None

        pages = [
            {'path': '/casino/casino-knowledge-base/essential-guide-to-live-dealer-online-casino.html', 'title': 'Live Casinos', 'count': process_count(aggs['games'], 'Live Games')},
            {'path': '/casino/established-online-casinos/', 'title': 'Big Brand Casinos', 'count': process_count(aggs['provider_tags'], 'Big')},
            {'path': '/collections/25-licensed-casinos-with-fastest-withdrawals.html', 'title': 'Fast Payout Casinos', 'count': process_count(aggs['provider_tags'], 'Sponsored')},
            {'path': '/casino/high-traffic-casinos/', 'title': 'High Traffic Casinos', 'count': 30},
            {'path': '/casino/casino-payment-methods/bitcoin-online-casinos.html', 'title': 'Bitcoin Casinos', 'count': process_count(aggs['deposits'], 'Bitcoin')},
            {'path': '/casino/casino-payment-methods/casinos-that-use-paypal.html', 'title': 'Paypal Casinos', 'count': process_count(aggs['deposits'], 'PayPal')},
        ]

        t = current_app.jinja_env.get_template('_ext-tab_menu.html')
        s = t.render(pages=pages, path=path)
        return s

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
            parser.stream.skip_if('comma')

        return CallBlock(self.call_method("_render", args=[List(args)]), [], [], []).set_lineno(lineno)          


class RelatedPagesExtension(Extension):
    tags = set(['related_pages'])

    def __init__(self, environment):
        super(RelatedPagesExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info(f'related_pages Args IN: {args}')

        default = ['RelatedBlog', None, 10]
        _ca = len(default)
        args = args[:_ca] + default[len(args):] + args[_ca:]

        logger.info('related_pages Args OUT: {0}'.format(args))

        tag = args[0]
        eid = args[1]
        count = int(args[2])

        pages, _ = Page.get(
            is_active=True, 
            is_searchable=True, 
            is_redirect=False, 
            tags=tag,
            locale=g.language, 
            _source=['path', 'title'], 
            _count=count,
            _exclude=[eid],
            _sort=[
                {'publishedon': {'order': 'desc'}}
            ]
        )

        t = current_app.jinja_env.get_template('_ext-related_pages.html')
        s = t.render(pages=pages)
        return s

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
            parser.stream.skip_if('comma')

        return CallBlock(self.call_method("_render", args=[List(args)]), [], [], []).set_lineno(lineno)          


class ComplaintAddExtension(Extension):
    tags = set(['complaint_add'])

    def __init__(self, environment):
        super(ComplaintAddExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info('complaint_add Args: {0}'.format(args))

        t = current_app.jinja_env.get_template('_ext-complaint_add.html')
        s = t.render()
        return s

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
            parser.stream.skip_if('comma')

        return CallBlock(self.call_method("_render", args=[List(args)]), [], [], []).set_lineno(lineno)          


class CryptoRatesExtension(Extension):
    tags = set(['crypto_rates'])

    def __init__(self, environment):
        super(CryptoRatesExtension, self).__init__(environment)

    def _render(self, caller):
        t = current_app.jinja_env.get_template('_ext-crypto_rates.html')
        crypto_rates = {k.decode(): format_decimal(v.decode(), locale=g.language) for k, v in current_app.redis.hgetall('crypto_rates').items()}
        s = t.render(crypto_rates=crypto_rates)
        return s

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        return CallBlock(self.call_method("_render", []), [], [], '').set_lineno(lineno)


class SidebarExtension(Extension):
    tags = set(['sidebar'])

    def __init__(self, environment):
        super(SidebarExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info('sidebar Args: {0}'.format(args))

        default = ['casinos', 3, 10, 'Online Casinos']
        _ca = len(default)
        args = args[:_ca] + default[len(args):] + args[_ca:]

        _service = args[0]
        _primary = int(args[1])
        _secondary = int(args[2])
        _title = args[3]

        _total = _primary + _secondary

        _items, _count = Page.provider_by_context(
            country=current_user.country_full,
            is_searchable=True,
            is_redirect=False,
            services=_service,
            _source=["title", "alias", "logo", "path", "logo_small", "ref_link", "welcome_package", "welcome_package_note"],
            _locale=g.language,
            _count=_total,
        )

        logger.info(f'We found {_count} items for sidebar')    

        t = current_app.jinja_env.get_template('_ext-sidebar.html')
        return t.render(items=_items, service=_service, primary=_primary, total=_total, title=_title)

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
            parser.stream.skip_if('comma')

        return CallBlock(self.call_method("_render", args=[List(args)]), [], [], []).set_lineno(lineno)          


class PagesExtension(Extension):
    tags = set(['pages'])

    def __init__(self, environment):
        super(PagesExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info(f'pages Args IN: {args}')

        default = ['page', 10]
        _ca = len(default)
        args = args[:_ca] + default[len(args):] + args[_ca:]

        logger.info('pages Args OUT: {0}'.format(args))

        category = args[0]
        count = int(args[1])

        kwargs = {}

        if 'provider' in category:
            kwargs = {
                'provider_tags': 'Bottom',
                '_sort': [{'rating': {'order': 'desc'}}]
            }
        elif 'page' in category:
            kwargs = {
                'tags': 'Blog',
                '_exclude_params': {'tags': 'Promo'},
                '_sort': [{'publishedon': {'order': 'desc'}}]
            }

        pages, found = Page.get(
            is_active=True,
            is_searchable=True,
            is_redirect=False,
            category=category,
            **kwargs,
            _source = [
                "title", 
                "alt_title",
                "path", 
            ], 
            _count=count,
        )

        t = current_app.jinja_env.get_template('_ext-pages.html')
        s = t.render(
            pages=pages, 
        )
        return s

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
            parser.stream.skip_if('comma')

        return CallBlock(self.call_method("_render", args=[List(args)]), [], [], []).set_lineno(lineno)          


class PagesListExtension(Extension):
    tags = set(['pages_list'])

    def __init__(self, environment):
        super(PagesListExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info(f'pages_list Args IN: {args}')

        default = [20, 4, 'pages_list', [], {'tags': 'Promo'}, None]
        _ca = len(default)
        args = args[:_ca] + default[len(args):] + args[_ca:]

        logger.info('pages_list Args OUT: {0}'.format(args))

        count = int(args[0])
        cols = int(args[1])
        template = args[2]
        tags = args[3]
        exclude = args[4]
        css = args[5]

        pages, found = Page.get(
            is_active=True,
            is_searchable=True,
            is_redirect=False,
            category=['page', 'collection'],
            tags=tags or ['Blog'],
            _exclude_params=exclude,
            _sort=[{'publishedon': {'order': 'desc'}}],
            _source = [
                "title", 
                "alt_title",
                "path", 
                "cover",
                "publishedon"
            ], 
            _count=count,
        )

        t = current_app.jinja_env.get_template(f'_ext-{template}.html')
        s = t.render(
            pages=pages, 
            cols=cols,
            css=css,
        )
        return s

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
            parser.stream.skip_if('comma')

        return CallBlock(self.call_method("_render", args=[List(args)]), [], [], []).set_lineno(lineno)          


# class PromoPagesExtension(Extension):
#     tags = set(['promo_pages'])

#     def __init__(self, environment):
#         super(PromoPagesExtension, self).__init__(environment)

#     def _render(self, caller):
#         t = current_app.jinja_env.get_template('_ext-promo_pages.html')
#         s = t.render()
#         return s

#     def parse(self, parser):
#         lineno = next(parser.stream).lineno
#         return CallBlock(self.call_method("_render", []), [], [], '').set_lineno(lineno)


# class TocExtension(Extension):
#     tags = set(['toc'])

#     def __init__(self, environment):
#         super(TocExtension, self).__init__(environment)

#     def _render(self, caller):
#         rv = caller()

#         def parse_item(s):
#             v, k = s.split('#')
#             return {'anchor': f'#{k}', 'title': v}

#         items = [parse_item(item) for item in rv.strip().split(';')]

#         t = current_app.jinja_env.get_template('_ext-toc.html')
#         s = t.render(items=items)

#         return s

#     def parse(self, parser):
#         lineno = next(parser.stream).lineno

#         body = parser.parse_statements(['name:endtoc'], drop_needle=True)
#         args = []

#         return CallBlock(self.call_method("_render", args), [], [], body).set_lineno(lineno)


class UIExtension(Extension):
    tags = set(['ui'])

    def __init__(self, environment):
        super(UIExtension, self).__init__(environment)

    def _render(self, args, caller):
        logger.info(f'ui Args IN: {args}')

        default = ['features', False]
        _ca = len(default)
        args = args[:_ca] + default[len(args):] + args[_ca:]

        logger.info('ui Args OUT: {0}'.format(args))

        template = args[0]
        logger.info(f'ui template: {template}')

        parse_content = bool(args[1])

        rv = caller().strip()
        items = []

        if parse_content:
            def parse_item(s):
                _d = s.split(':')
                if len(_d) >= 2:
                    _res = {'key': _d[0], 'value': _d[1], }
                    _res.update({f'args_{idx}': item for idx, item in enumerate(_d[2:])})
                    return _res
            try:
                items = [parse_item(item) for item in rv.split('|')]
            except:
                logger.warning(f'ui extension parse error: {rv}')

        s = rv
        try:
            t = current_app.jinja_env.get_template(f'_ext-ui_{template}.html')
            s = t.render(items=items, rv=html.unescape(rv), args=args)
        except TemplateNotFound:
            pass

        return s

    def parse(self, parser):
        tag = parser.stream.__next__()

        args = []
        try:
            while parser.stream.current.type != 'block_end':
                args.append(parser.parse_expression())
                parser.stream.skip_if('comma')
        except TemplateSyntaxError:
            pass

        body = parser.parse_statements(['name:endui'], drop_needle=True)

        callback = self.call_method('_render', args=[List(args)])
        return CallBlock(callback, [], [], body).set_lineno(tag.lineno)


class ComplaintsExtension(Extension):
    tags = set(['complaints'])

    def __init__(self, environment):
        super(ComplaintsExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info(f'ComplaintsExtension Args IN: {args}')

        default = [10]
        _ca = len(default)
        args = args[:_ca] + default[len(args):] + args[_ca:]

        logger.info('ComplaintsExtension Args OUT: {0}'.format(args))

        count = int(args[0])

        complaints, total = Activity.get(
            activity='complaint',
            is_active=True,
            status=['opened', 'not_solved', 'solved', 'rejected'],
            _sort=[{'createdon': 'desc'}],
            _count=count,
        ) 

        casinos, _ = Page.get(
            category='provider',
            _all=True,
            _process=False,
            _count=1000,
            _source=[
                'path', 
            ]
        )
        casinos = {item['_id']: item['_source']['path'] for item in casinos}

        t = current_app.jinja_env.get_template('_ext-complaints.html')
        s = t.render(
            items=complaints, 
            cpp=count,
            total=total,
            count=count,
            percent=int((count / total) * 100) if total else 0,
            casinos=casinos,
        )
        return s

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = []
        while parser.stream.current.type != 'block_end':
            args.append(parser.parse_expression())
            parser.stream.skip_if('comma')

        return CallBlock(self.call_method("_render", args=[List(args)]), [], [], []).set_lineno(lineno)          


def process_aggs(_a, _k, _t):
    if _k in _a:
        _r = []
        for _i in _a[_k]:
            if _i['item'] in _t:
                _r.append(_i)
        _a[_k] = _r
    return _a

class RatingV2Extension(Extension):
    tags = set(['rating'])

    def __init__(self, environment):
        super(RatingV2Extension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info(f'rating_v2 Args IN: {args}')

        default = ['casino', 10, False, ['software', 'provider_tags', 'deposits', 'games', 'licences'], 1000, []]
        _ca = len(default)
        args = args[:_ca] + default[len(args):] + args[_ca:]

        logger.info('rating_v2 Args OUT: {0}'.format(args))

        service = args[0]
        count = int(args[1])
        parse_kwargs = bool(args[2])
        aggs_fields = args[3]
        aggs_count = int(args[4])
        tags_enabled = args[5]

        tags = args[len(default):]
        logger.info('rating_v2 Casinos Tags: {0}'.format(tags))

        _aggs = {
            item: {
                "terms": {
                    "field": "{0}.keyword".format(item),
                    "size": aggs_count,
                    "order": {"_key": "asc"}
                }
            } for item in aggs_fields
        }

        # args: service
        items, total, aggs, _ = Page.provider_by_context(
            is_searchable=True,
            is_redirect=False,
            country=current_user.country_full,
            services=service,
            provider_tags=tags,
            _locale=g.language,
            _source=True,
            _count=count,
            _aggs=_aggs,
        )

        kw = {}
        if parse_kwargs:
            rv = caller()
            try:
                for s in rv.split('|'):
                    k, v = s.split(':')
                    kw[str(k)] = str(v)
            except:
                logger.warning(f'rating_v2 kwargs parse error: {rv}')

        t = current_app.jinja_env.get_template('_ext-rating_casinos.html')
        s = t.render(
            items=items, 
            total=total, 
            count=len(items),
            cpp=count,
            percent=int((count / total) * 100) if total else 0,
            service=service, 
            tags=tags,
            aggs=process_aggs(aggs, 'provider_tags', tags_enabled),
            **kw
        )
        return s

    def parse(self, parser):
        tag = parser.stream.__next__()

        args = []
        try:
            while parser.stream.current.type != 'block_end':
                args.append(parser.parse_expression())
                parser.stream.skip_if('comma')
        except TemplateSyntaxError:
            pass

        body = parser.parse_statements(['name:endrating'], drop_needle=True)

        callback = self.call_method('_render', args=[List(args)])
        return CallBlock(callback, [], [], body).set_lineno(tag.lineno)


class MapExtension(Extension):
    tags = set(['map'])

    def __init__(self, environment):
        super(MapExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info(f'map Args IN: {args}')

        default = [[], True]
        _ca = len(default)
        args = args[:_ca] + default[len(args):] + args[_ca:]

        logger.info('map Args OUT: {0}'.format(args))

        geo = args[0]
        has_legend = bool(args[1])

        locations = {
            "kalimantan": "M781.68,324.4l-2.31,8.68l-12.53,4.23l-3.75-4.4l-1.82,0.5l3.4,13.12l5.09,0.57l6.79,2.57v2.57l3.11-0.57l4.53-6.27v-5.13l2.55-5.13l2.83,0.57l-3.4-7.13l-0.52-4.59L781.68,324.4L781.68,324.4z",
            "papua new guinea": "M852.76,348.29l-0.37,24.44l3.52-0.19l4.63-5.41l3.89,0.19l2.5,2.24l0.83,6.9l7.96,4.2l2.04-0.75v-2.52l-6.39-5.32l-3.15-7.28l2.5-1.21l-1.85-4.01l-3.7-0.09l-0.93-4.29l-9.81-6.62L852.76,348.29L852.76,348.29z",
            "mexico": "M137.49,225.43l4.83,15.21l-2.25,1.26l0.25,3.02l4.25,3.27v6.05l5.25,5.04l-2.25-14.86l-3-9.83l0.75-6.8l2.5,0.25l1,2.27l-1,5.79l13,25.44v9.07l10.5,12.34l11.5,5.29l4.75-2.77l6.75,5.54l4-4.03l-1.75-4.54l5.75-1.76l1.75,1.01l1.75-1.76h2.75l5-8.82l-2.5-2.27l-9.75,2.27l-2.25,6.55l-5.75,1.01l-6.75-2.77l-3-9.57l2.27-12.07l-4.64-2.89l-2.21-11.59l-1.85-0.79l-3.38,3.43l-3.88-2.07l-1.52-7.73l-15.37-1.61l-7.94-5.97L137.49,225.43L137.49,225.43z",
            "estonia": "M517.77,143.66l-5.6-0.2l-3.55,2.17l-0.05,1.61l2.3,2.17l7.15,1.21L517.77,143.66L517.77,143.66z",
            "algeria": "M473.88,227.49l-4.08-1.37l-16.98,3.19l-3.7,2.81l2.26,11.67l-6.75,0.27l-4.06,6.53l-9.67,2.32l0.03,4.75l31.85,24.35l5.43,0.46l18.11-14.15l-1.81-2.28l-3.4-0.46l-2.04-3.42v-14.15l-1.36-1.37l0.23-3.65l-3.62-3.65l-0.45-3.88l1.58-1.14l-0.68-4.11L473.88,227.49L473.88,227.49z",
            "morocco": "M448.29,232.28h-11.55l-2.26,5.02l-5.21,2.51l-4.3,11.64l-8.38,5.02l-11.77,19.39l11.55-0.23l0.45-5.7h2.94v-7.76h10.19l0.23-10.04l9.74-2.28l4.08-6.62l6.34-0.23L448.29,232.28L448.29,232.28z",
            "mauretania": "M404.9,276.66l2.18,2.85l-0.45,12.32l3.17-2.28l2.26-0.46l3.17,1.14l3.62,5.02l3.4-2.28l16.53-0.23l-4.08-27.61l4.38-0.02l-8.16-6.25l0.01,4.06l-10.33,0.01l-0.05,7.75l-2.97-0.01l-0.38,5.72L404.9,276.66L404.9,276.66z",
            "senegal": "M410.12,290.32l-3.94,2.86l-0.9,1.6l-0.28,1.6l1.45,1.04l4.84-0.07l3.11-0.84l0.35,1.53l-0.28,2.02l2.97,1.46l0.62,0.7l3.94,0.14l0.14-1.74l-3.6-4.32l-4.01-5.43l-2.49-1.04L410.12,290.32L410.12,290.32z",
            "gambia": "M406.89,298.34l-0.13,1.11l6.92-0.1l0.35-1.03l-0.15-1.04l-1.99,0.81L406.89,298.34L406.89,298.34z",
            "casamance": "M406.79,300.22l1.24,3.01l0.69-1.86l8.41,0.88l-3.64-1.87L406.79,300.22L406.79,300.22z",
            "bissau": "M408.6,304.53l1.4,2.77l3.93-3.38l0.04-1.04l-4.63-0.67L408.6,304.53L408.6,304.53z",
            "guinee": "M410.42,307.94l3.04,4.68l3.96-3.44l4.06-0.18l3.38,4.49l2.87,1.89l1.08-2.1l0.96-0.54l-0.07-4.62l-1.91-5.48l-5.86,0.65l-7.25-0.58l-0.04,1.86L410.42,307.94L410.42,307.94z",
            "sierra leone": "M413.93,313.13l5.65,5.46l4.03-4.89l-2.52-3.95l-3.47,0.35L413.93,313.13L413.93,313.13z",
            "liberia": "M420.17,319.19l10.98,7.34l-0.26-5.56l-3.32-3.91l-3.24-2.87L420.17,319.19L420.17,319.19z",
            "ivoire": "M432.07,326.75l4.28-3.03l5.32-0.93l5.43,1.17l-2.77-4.19l-0.81-2.56l0.81-7.57l-4.85,0.23l-2.2-2.1l-4.62,0.12l-2.2,0.35l0.23,5.12l-1.16,0.47l-1.39,2.56l3.58,4.19L432.07,326.75L432.07,326.75z",
            "mali": "M419.46,295.84l3.08-2.11l17.12-0.1l-3.96-27.54l4.52-0.13l21.87,16.69l2.94,0.42l-1.11,9.28l-13.75,1.25l-10.61,7.92l-1.93,5.42l-7.37,0.31l-1.88-5.41l-5.65,0.4l0.22-1.77L419.46,295.84L419.46,295.84z",
            "burkina": "M450.59,294.28l3.64-0.29l5.97,8.44l-5.54,4.18l-4.01-1.03l-5.39,0.07l-0.87,3.16l-4.52,0.22l-1.24-1.69l1.6-5.14L450.59,294.28L450.59,294.28z",
            "niger": "M460.89,302l2.55-0.06l2.3-3.45l3.86-0.69l4.11,2.51l8.77,0.25l6.78-2.76l2.55-2.19l0.19-2.88l4.73-4.77l1.25-10.53l-3.11-6.52l-7.96-1.94l-18.42,14.36l-2.61-0.25l-1.12,9.97l-9.4,0.94L460.89,302L460.89,302z",
            "ghana": "M444.34,317.05l1.12,2.63l2.92,4.58l1.62-0.06l4.42-2.51l-0.31-14.29l-3.42-1l-4.79,0.13L444.34,317.05L444.34,317.05z",
            "togo": "M455.22,321.25l2.68-1.57l-0.06-10.35l-1.74-2.82l-1.12,0.94L455.22,321.25L455.22,321.25z",
            "benin": "M458.71,319.49h2.12l0.12-6.02l2.68-3.89l-0.12-6.77l-2.43-0.06l-4.17,3.26l1.74,3.32L458.71,319.49L458.71,319.49z",
            "nigeria": "M461.57,319.37l3.92,0.19l4.73,5.27l2.3,0.63l1.8-0.88l2.74-0.38l0.93-3.82l3.73-2.45l4.04-0.19l7.4-13.61l-0.12-3.07l-3.42-2.63l-6.84,3.01l-9.15-0.13l-4.36-2.76l-3.11,0.69l-1.62,2.82l-0.12,7.96l-2.61,3.7L461.57,319.37L461.57,319.37z",
            "tunisia": "M474.91,227.33l5.53-2.23l1.82,1.18l0.07,1.44l-0.85,1.11l0.13,1.97l0.85,0.46v3.54l-0.98,1.64l0.13,1.05l3.71,1.31l-2.99,4.65l-1.17-0.07l-0.2,3.74l-1.3,0.2l-1.11-0.98l0.26-3.8l-3.64-3.54l-0.46-3.08l1.76-1.38L474.91,227.33L474.91,227.33z",
            "libya": "M480.05,248.03l1.56-0.26l0.46-3.6h0.78l3.19-5.24l7.87,2.29l2.15,3.34l7.74,3.54l4.03-1.7l-0.39-1.7l-1.76-1.7l0.2-1.18l2.86-2.42h5.66l2.15,2.88l4.55,0.66l0.59,36.89l-3.38-0.13l-20.42-10.62l-2.21,1.25l-8.39-2.1l-2.28-3.01l-3.32-0.46l-1.69-3.01L480.05,248.03L480.05,248.03z",
            "egypt": "M521.93,243.06l2.67,0.07l5.2,1.44l2.47,0.07l3.06-2.56h1.43l2.6,1.44h3.29l0.59-0.04l2.08,5.98l0.59,1.93l0.55,2.89l-0.98,0.72l-1.69-0.85l-1.95-6.36l-1.76-0.13l-0.13,2.16l1.17,3.74l9.37,11.6l0.2,4.98l-2.73,3.15L522.32,273L521.93,243.06L521.93,243.06z",
            "chad": "M492.79,296l0.13-2.95l4.74-4.61l1.27-11.32l-3.16-6.04l2.21-1.13l21.4,11.15l-0.13,10.94l-3.77,3.21v5.64l2.47,4.78h-4.36l-7.22,7.14l-0.19,2.16l-5.33-0.07l-0.07,0.98l-3.04-0.4l-2.08-3.93l-1.56-0.77l0.2-1.2l1.96-1.5v-7.02l-2.71-0.42l-3.27-2.43L492.79,296L492.79,296L492.79,296z",
            "south_sudan": "M 549.08398 310.33984 L 546.14062 305.39648 L 545.83203 301.80078 L 545.125 301.93555 L 544.93359 303.04297 L 541.07617 308.67773 L 537.99805 307.20898 L 534.92773 309.78125 L 528.57617 309.41602 L 525.76562 307.16992 L 521.73242 309.23438 L 521.58008 310.60938 L 520.34961 311.34961 L 532.66992 324.0293 L 539.38086 324.41016 L 540.35938 325.90039 L 549.96094 326.07031 L 550.03906 323.91992 L 550.85938 322.42969 L 554.06055 322.01953 L 550.07031 316.23047 L 547.13086 316.23047 L 546.38086 312.11914 L 548.74023 311.08008 L 549.08398 310.33984 z ",
            "sudan": "M 552 270.60938 L 548.31055 274.33008 L 522.50977 274.09961 L 522.78906 280.66992 L 520.33008 280.59961 L 520.15039 292.42969 L 516.41992 295.64062 L 516.26953 300.58008 L 518.96094 305.89062 L 521.91016 307.63086 L 521.86523 308.04492 L 525.88477 305.98633 L 528.95117 308.43555 L 534.58984 308.75977 L 537.84766 306.03125 L 540.73438 307.40625 L 543.98438 302.6582 L 544.25781 301.08203 L 546.73438 300.61133 L 547.11914 305.08203 L 549.5957 309.24219 L 555.59961 296.33008 L 555.59961 288.48047 L 559.96094 283.33984 L 552 270.60938 z ",
            "cameroon": "M477.82,324.28l3.22,2.96l-0.23,4.58l17.66-0.41l1.44-1.62l-5.06-5.45l-0.75-1.97l3.22-6.03l-2.19-4l-1.84-0.99v-2.03l2.13-1.39l0.12-6.32l-1.69-0.19l-0.03,3.32l-7.42,13.85l-4.54,0.23l-3.11,2.14L477.82,324.28L477.82,324.28z",
            "eritrea": "M556.71,294.7l-0.25-5.89l3.96-4.62l1.07,0.82l1.95,6.52l9.36,6.97l-1.7,2.09l-6.85-5.89H556.71L556.71,294.7z",
            "djibouti": "M571.48,301.54l-0.57,3.36l3.96-0.06l0.06-4.94l-1.45-0.89L571.48,301.54L571.48,301.54z",
            "ethiopia": "M549.49,311.76l7.28-16.2l7.23,0.04l6.41,5.57l-0.45,4.59h4.97l0.51,2.76l8.04,4.81l4.96,0.25l-9.43,10.13l-12.95,3.99h-3.21l-5.72-4.88l-2.26-0.95l-4.38-6.45l-2.89,0.04l-0.34-2.96L549.49,311.76L549.49,311.76z",
            "somaliland": "M575.74,305.04l4.08,2.78l1.21-0.06l10.13-3.48l1.15,3.71l-0.81,3.13l-2.19,1.74l-5.47-0.35l-7.83-4.81L575.74,305.04L575.74,305.04z",
            "soqotra": "M599.62,299.65l2.13,2.38l2.88-1.74l1.04-0.35l-1.32-1.28l-2.53,0.75L599.62,299.65L599.62,299.65z",
            "somalia": "M591.97,304.05l4.37-1.68l1.55,0.93l-0.17,3.88l-4.03,11.48l-21.81,23.36l-2.53-1.74l-0.17-9.86l3.28-3.77l6.96-2.15l10.21-10.78l2.67-2.38l0.75-3.48L591.97,304.05L591.97,304.05z",
            "centrafrique": "M495.66,324.05l4.66,5.04l1.84-2.38l2.93,0.12l0.63-2.32l2.88-1.8l5.98,4.12l3.45-3.42l13.39,0.59L519,311.18l1.67-1.04l0.23-2.26l-2.82-1.33h-4.14l-6.67,6.61l-0.23,2.72l-5.29-0.17l-0.17,1.16l-3.45-0.35l-3.11,5.91L495.66,324.05L495.66,324.05z",
            "sao tome": "M470.74,337.15l1.15-0.58l0.86,0.7l-0.86,1.33l-1.04-0.41L470.74,337.15L470.74,337.15z",
            "principe": "M473.05,333.5l1.73-0.29l0.58,1.1l-0.86,0.93l-0.86-0.12L473.05,333.5L473.05,333.5z",
            "bioko": "M476.84,327.41l-0.46,1.97l1.38,0.75l1.32-0.99l-0.46-2.03L476.84,327.41L476.84,327.41z",
            "gabon": "M486.39,332.63l-0.12,2.49l-5.64-0.12l-3.45,6.67l8.11,8.87l2.01-1.68l-0.06-1.74l-1.38-0.64v-1.22l3.11-1.97l2.76,2.09l3.05,0.06l-0.06-10.49l-4.83-0.23l-0.06-2.2L486.39,332.63L486.39,332.63z",
            "equatorial guinea": "M480.99,332.69l-0.06,1.39l4.54,0.23l-0.06-1.57L480.99,332.69L480.99,332.69z",
            "congo": "M491,332.52l-0.06,1.45l4.78,0.12l0.17,12.41l-4.37-0.12l-2.53-1.97l-1.96,1.1l-0.09,0.55l1.01,0.49l0.29,2.55l-2.7,2.32l0.58,1.22l2.99-2.32h1.44l0.46,1.39l1.9,0.81l6.1-5.16l-0.12-3.77l1.27-3.07l3.91-2.9l1.05-9.81l-2.78,0.01l-3.22,4.41L491,332.52L491,332.52z",
            "cabinda": "M486.55,353.23l1.74,2.26l2.25-2.13l-0.66-2.21l-0.56-0.04L486.55,353.23L486.55,353.23z",
            "drc": "M489.38,355.71l10.31-0.18l2.09,2.97l-0.08,2.19l0.77,0.7h5.12l1.47-2.89h2.09l0.85,0.86l2.87-0.08l0.85,10.08l4.96,0.16v0.78l13.33,6.01l0.62,1.17h2.79l-0.31-4.22l-5.04-2.42l0.31-3.2l2.17-5.08l4.96-0.16l-4.26-14.14l0.08-6.01l6.74-10.54l0.08-1.48l-1.01-0.55l0.04-2.86l-1.23-0.11l-1.24-1.58l-20.35-0.92l-3.73,3.63l-6.11-4.02l-2.15,1.32l-1.56,13.13l-3.86,2.98l-1.16,2.64l0.21,3.91l-6.96,5.69l-1.85-0.84l0.25,1.09L489.38,355.71L489.38,355.71z",
            "rwanda": "M537.82,339.9l2.81,2.59l-0.12,2.77l-4.36,0.09v-3.06L537.82,339.9L537.82,339.9z",
            "burundi": "M536.21,346.21l4.27-0.09l-1.11,3.74l-1.08,0.94h-1.32l-0.94-2.53L536.21,346.21L536.21,346.21z",
            "uganda": "M538.3,339.09l3.03,2.84l1.9-1.21l5.14-0.84l0.88,0.09l0.33-1.95l2.9-6.1l-2.44-5.08l-7.91,0.05l-0.05,2.09l1.06,1.02l-0.16,2.09L538.3,339.09L538.3,339.09z",
            "kenya": "M550.83,326.52l2.66,5.19l-3.19,6.69l-0.42,2.03l15.93,9.85l4.94-7.76l-2.5-2.03l-0.05-10.22l3.13-3.42l-4.99,1.66l-3.77,0.05l-5.9-4.98l-1.86-0.8l-3.45,0.32l-0.61,1.02L550.83,326.52L550.83,326.52z",
            "tanzania": "M550.57,371.42l17.47-2.14l-3.93-7.6l-0.21-7.28l1.27-3.48l-16.62-10.44l-5.21,0.86l-1.81,1.34l-0.16,3.05l-1.17,4.23l-1.22,1.45l-1.75,0.16l3.35,11.61l5.47,2.57l3.77,0.11L550.57,371.42L550.57,371.42z",
            "zambia": "M514.55,384.7l3.17,4.4l4.91,0.3l1.74,0.96l5.14,0.06l4.43-6.21l12.38-5.54l1.08-4.88l-1.44-6.99l-6.46-3.68l-4.31,0.3l-2.15,4.76l0.06,2.17l5.08,2.47l0.3,5.37l-4.37,0.24l-1.08-1.81l-12.14-5.18l-0.36,3.98l-5.74,0.18L514.55,384.7L514.55,384.7z",
            "angola": "M488.62,356.71l3.41,12.73l-0.08,4.02l-4.99,5.36l-0.75,8.71l19.2,0.17l6.24,2.26l5.15-0.67l-3-3.76l0.01-10.74l5.9-0.25v-4.19l-4.79-0.2l-0.96-9.92l-2.02,0.03l-1.09-0.98l-1.19,0.06l-1.58,3.06H502l-1.41-1.42l0.42-2.01l-1.66-2.43L488.62,356.71L488.62,356.71z",
            "malawi": "M547.16,379.4l3.11,3.25l-0.06,4.16l0.6,1.75l4.13-4.46l-0.48-5.67l-2.21-1.69l-1.97-9.95l-3.41-0.12l1.55,7.17L547.16,379.4L547.16,379.4z",
            "mozambique": "M541.17,413.28l2.69,2.23l6.34-3.86l1.02-5.73v-9.46l10.17-8.32l1.74,0.06l6.16-5.91l-0.96-12.18L552,372.17l0.48,3.68l2.81,2.17l0.66,6.63l-5.5,5.37l-1.32-3.01l0.24-3.98l-3.17-3.44l-7.78,3.62l7.24,3.68l0.24,10.73l-4.79,7.11L541.17,413.28L541.17,413.28z",
            "zimbabwe": "M524.66,392.3l8.97,10.13l6.88,1.75l4.61-7.23l-0.36-9.58l-7.48-3.86l-2.81,1.27l-4.19,6.39l-5.8-0.06L524.66,392.3L524.66,392.3z",
            "namibia": "M496.55,421.96l3.35,0.24l1.97,1.99l4.67,0.06l1.14-13.26v-8.68l2.99-0.6l1.14-9.1l7.6-0.24l2.69-2.23l-4.55-0.18l-6.16,0.84l-6.64-2.41h-18.66l0.48,5.3l6.22,9.16l-1.08,4.7l0.06,2.47L496.55,421.96L496.55,421.96z",
            "botswana": "M508.51,411.23l2.15,0.66l-0.3,6.15l2.21,0.3l5.08-4.58l6.1,0.66l1.62-4.1l7.72-7.05l-9.27-10.67l-0.12-1.75l-1.02-0.3l-2.81,2.59l-7.3,0.18l-1.02,9.1l-2.87,0.66L508.51,411.23L508.51,411.23z",
            "swaziland": "M540.87,414l-2.51,0.42l-1.08,2.95l1.92,1.75h2.33l1.97-2.83L540.87,414L540.87,414z",
            "lesotho": "M527.41,425.39l3.05-2.35l1.44,0.06l1.74,2.17l-0.18,2.17l-2.93,1.08v0.84l-3.23-0.18l-0.78-2.35L527.41,425.39L527.41,425.39z",
            "south africa": "M534.16,403.63l-7.9,7.3l-1.88,4.51l-6.26-0.78l-5.21,4.63l-3.46-0.34l0.28-6.4l-1.23-0.43l-0.86,13.09l-6.14-0.06l-1.85-2.18l-2.71-0.03l2.47,7.09l4.41,4.17l-3.15,3.67l2.04,4.6l4.72,1.8l3.76-3.2l10.77,0.06l0.77-0.96l4.78-0.84l16.17-16.1l-0.06-5.07l-1.73,2.24h-2.59l-3.15-2.64l1.6-3.98l2.75-0.56l-0.25-8.18L534.16,403.63L534.16,403.63z M530.37,422.13l1.51-0.06l2.45,2.66l-0.07,3.08l-2.87,1.45l-0.18,1.02l-4.38,0.05l-1.37-3.3l1.25-2.42L530.37,422.13L530.37,422.13z",
            "greenland": "M321.13,50.07l-1.36,2.17l2.45,2.45l-1.09,2.45l3.54,4.62l4.35-1.36l5.71-0.54l6.53,7.07l4.35,11.69l-3.53,7.34l4.89-0.82l2.72,1.63l0.27,3.54l-5.98,0.27l3.26,3.26l4.08,0.82l-8.97,11.96l-1.09,7.34l1.9,5.98l-1.36,3.54l2.45,7.61l4.62,5.17l1.36-0.27l2.99-0.82l0.27,4.35l1.9,2.72l3.53-0.27l2.72-10.06l8.16-10.06l12.24-4.89l7.61-9.52l3.53,1.63h7.34l5.98-5.98l7.34-2.99l0.82-4.62l-4.62-4.08l-4.08-1.36l-2.18-5.71l5.17-2.99l8.16,4.35l2.72-2.99l-4.35-2.45l9.25-12.51l-1.63-5.44l-4.35-0.27l1.63-4.89l5.44-2.45l11.15-9.79l-3.26-3.53l-12.51,1.09l-6.53,6.53l3.81-8.43l-4.35-1.09l-2.45,4.35l-3.53-2.99l-9.79,1.09l2.72-4.35l16.04-0.54l-4.08-5.44l-17.4-3.26l-7.07,1.09l0.27,3.54l-7.34-2.45l0.27-2.45l-5.17,1.09l-1.09,2.72l5.44,1.9l-5.71,4.08l-4.08-4.62l-5.71-1.63l-0.82,4.35h-5.71l-2.18-4.62l-8.97-1.36l-4.89,2.45l-0.27,3.26l-6.25-0.82l-3.81,1.63l0.27,3.81v1.9l-7.07,1.36l-3.26-2.17l-2.18,3.53l3.26,3.54l6.8-0.82l0.54,2.18l-5.17,2.45L321.13,50.07L321.13,50.07z",
            "disko": "M342.89,92.49l1.63,2.45l-0.82,2.99h-1.63l-2.18-2.45l0.54-1.9L342.89,92.49L342.89,92.49z",
            "milne": "M410.87,85.69l4.62,1.36l-0.27,3.81l-4.89-2.45l-1.09-1.36L410.87,85.69L410.87,85.69z",
            "east antarctica": "M388.52,622.99l3.83-5.11l14.89-7.66l2.55-5.53l6.38-1.28l5.96-7.66l5.96-0.43l1.28-5.96l5.11-3.83l4.26,1.28l12.34-3.83l2.98,2.98l5.53,0.43l5.11-2.55l30.64-0.43l11.06,2.98l14.04-2.98l4.68,0.43l1.28-4.26h4.68l6.38,6.81l11.92-7.66l13.19-3.83l4.68,2.98l0.43-5.96l6.81-0.85l7.23,3.4v3.4l18.3,7.66l5.11-0.43l2.13,2.55l-5.96,6.81v4.68l5.53,2.98l1.28-2.98l25.11-9.79l18.3-1.7l3.83,2.13l14.47,2.13l3.4,1.28l4.68-2.55l6.81-0.43l6.38,4.68l0.43,5.11l14.47-2.98l2.13,0.85l0.85,4.68l13.19,4.26l4.26-2.98l0.43,3.83l4.68,0.43l6.38,5.11l5.96-2.55l5.11,0.43h3.83l2.55-0.43l0.43,6.81l8.51,5.11L388.52,622.99L388.52,622.99z",
            "antarctic peninsula": "M260.01,622.99l13.62-3.83l0.85-3.83l14.47-3.4l8.51,2.13l18.72-7.66l-0.43-8.08l-5.53-8.51l1.28-2.13l-2.13-5.53v-5.96h3.4l-2.13-4.26l15.32-13.19l-0.43,5.96l-2.98,0.85l-2.98,5.11l2.98,1.28l-2.98,4.26l-3.4-0.85l-1.7,3.83l0.43,5.11l5.11-0.43l3.4,4.68l1.28,5.96l6.81,8.51l0.43,10.64l-2.55,1.28l2.13,5.53l-1.28,2.13L260.01,622.99L260.01,622.99z",
            "thurston": "M250.22,615.33l5.11-0.85l2.13,1.7l-0.85,2.13l-0.43,2.55l-2.98,1.28l-2.13-2.55h-8.51v-1.7l3.83-0.85L250.22,615.33L250.22,615.33z",
            "alexander": "M304.69,587.67l-4.26,0.85l2.55,4.68l2.98,1.28l-1.28,2.55v1.7l-8.09,2.13l0.85,2.55l3.4,1.28l3.83-2.98l3.4,0.85l-2.13,3.4l1.28,0.85l3.83-1.7l2.98-5.53L304.69,587.67L304.69,587.67z",
            "smyley": "M295.75,606.82l-3.4,2.98l2.98,0.85l3.83,0.85l3.83-2.55l-3.83-0.85L295.75,606.82L295.75,606.82z",
            "robert": "M319.57,556.47l-2.49,0.5l-0.55,2.55l4.76-0.7L319.57,556.47L319.57,556.47z",
            "king george": "M323.59,552.54l-2.99,0.57l0.57,2.31l3.64-0.13L323.59,552.54L323.59,552.54z",
            "james ross": "M328.34,557.17l0.02,3.56l2.05,0.09l1.66-2.64L328.34,557.17L328.34,557.17z",
            "elephant": "M329.33,547.24l-2.16,0.85l-0.55,2.04l1.87,0.68l3.14-2.16L329.33,547.24L329.33,547.24z",
            "australia": "M761.17,427.98l-0.35,25.38l-3.9,2.86l-0.35,2.5l5.32,3.57l13.13-2.5h6.74l2.48-3.58l14.9-2.86l10.64,3.22l-0.71,4.29l1.42,4.29l8.16-1.43l0.35,2.14l-5.32,3.93l1.77,1.43l3.9-1.43l-1.06,11.8l7.45,5.72l4.26-1.43l2.13,2.14l12.42-1.79l11.71-18.95l4.26-1.07l8.51-15.73l2.13-13.58l-5.32-6.79l2.13-1.43l-4.26-13.23l-4.61-3.22l0.71-17.87l-4.26-3.22l-1.06-10.01h-2.13l-7.1,23.59l-3.9,0.36l-8.87-8.94l4.97-13.23l-9.22-1.79l-10.29,2.86l-2.84,8.22l-4.61,1.07l-0.35-5.72l-18.8,11.44l0.35,4.29l-2.84,3.93h-7.1l-15.26,6.43L761.17,427.98L761.17,427.98z",
            "tasmania": "M825.74,496.26l-1.77,7.15l0.35,5l5.32-0.36l6.03-9.29L825.74,496.26L825.74,496.26z",
            "new zealand north island": "M913.02,481.96l1.06,11.8l-1.42,5.36l-5.32,3.93l0.35,4.65v5l1.42,1.79l14.55-12.51v-2.86h-3.55l-4.97-16.8L913.02,481.96L913.02,481.96z",
            "new zealand south island": "M902.38,507.7l2.84,5.36l-7.81,7.51l-0.71,3.93l-5.32,0.71l-8.87,8.22l-8.16-3.93l-0.71-2.86l14.9-6.43L902.38,507.7L902.38,507.7z",
            "new caledonia": "M906.64,420.47l-0.35,1.79l4.61,6.43l2.48,1.07l0.35-2.5L906.64,420.47L906.64,420.47z",
            "sumatra": "M722.48,317.57l-0.28,2.28l6.79,11.41h1.98l14.15,23.67l5.66,0.57l2.83-8.27l-4.53-2.85l-0.85-4.56L722.48,317.57L722.48,317.57z",
            "east malaysia": "M764.14,332.92l3.02,3.49l11.58-4.01l2.29-8.84l5.16-0.37l4.72-3.42l-6.12-4.46l-1.4-2.45l-3.02,5.57l1.11,3.2l-1.84,2.67l-3.47-0.89l-8.41,6.17l0.22,3.57L764.14,332.92L764.14,332.92z",
            "brunei": "M779.77,319.25l-2.88,3.49l2.36,0.74l1.33-1.86L779.77,319.25L779.77,319.25z",
            "sulawesi": "M789.53,349.11l2.26,2.77l-1.47,4.16v0.79h3.34l1.18-10.4l1.08,0.3l1.96,9.5l1.87,0.5l1.77-4.06l-1.77-6.14l-1.47-2.67l4.62-3.37l-1.08-1.49l-4.42,2.87h-1.18l-2.16-3.17l0.69-1.39l3.64-1.78l5.5,1.68l1.67-0.1l4.13-3.86l-1.67-1.68l-3.83,2.97h-2.46l-3.73-1.78l-2.65,0.1l-2.95,4.75l-1.87,8.22L789.53,349.11L789.53,349.11z",
            "maluku": "M814.19,330.5l-1.87,4.55l2.95,3.86h0.98l1.28-2.57l0.69-0.89l-1.28-1.39l-1.87-0.69L814.19,330.5L814.19,330.5z",
            "seram": "M819.99,345.45l-4.03,0.89l-1.18,1.29l0.98,1.68l2.65-0.99l1.67-0.99l2.46,1.98l1.08-0.89l-1.96-2.38L819.99,345.45L819.99,345.45z",
            "java": "M753.17,358.32l-2.75,1.88l0.59,1.58l8.75,1.98l4.42,0.79l1.87,1.98l5.01,0.4l2.36,1.98l2.16-0.5l1.97-1.78l-3.64-1.68l-3.14-2.67l-8.16-1.98L753.17,358.32L753.17,358.32z",
            "bali": "M781.77,366.93l-2.16,1.19l1.28,1.39l3.14-1.19L781.77,366.93L781.77,366.93z",
            "lombok": "M785.5,366.04l0.39,1.88l2.26,0.59l0.88-1.09l-0.98-1.49L785.5,366.04L785.5,366.04z",
            "sumba": "M790.91,370.99l-2.75,0.4l2.46,2.08h1.96L790.91,370.99L790.91,370.99z",
            "flores": "M791.69,367.72l-0.59,1.19l4.42,0.69l3.44-1.98l-1.96-0.59l-3.14,0.89l-1.18-0.99L791.69,367.72L791.69,367.72z",
            "timor": "M806.14,368.42l-5.11,4.26l0.49,1.09l2.16-0.4l2.55-2.38l5.01-0.69l-0.98-1.68L806.14,368.42L806.14,368.42z",
            "new ireland": "M880.48,349l-0.88,1.25l4.81,4.26l0.66,2.5l1.31-0.15l0.15-2.57l-1.46-1.32L880.48,349L880.48,349z",
            "new britain": "M882.89,355.03l-0.95,0.22l-0.58,2.57l-1.82,1.18l-5.47,0.96l0.22,2.06l5.76-0.29l3.65-2.28l-0.22-3.97L882.89,355.03L882.89,355.03z",
            "bougainville": "M889.38,359.51l1.24,3.45l2.19,2.13l0.66-0.59l-0.22-2.28l-2.48-3.01L889.38,359.51L889.38,359.51z",
            "choiseul": "M895.43,364.65l0.15,2.28l1.39,1.32l1.31-0.81l-1.17-2.43L895.43,364.65L895.43,364.65z",
            "new georgia": "M897.18,370.31l-1.17,1.25l1.24,2.28l1.46,0.44l-0.07-1.54L897.18,370.31L897.18,370.31z",
            "santa isabel": "M900.03,368.99l1.02,2.5l1.97,2.35l1.09-1.76l-1.46-2.5L900.03,368.99L900.03,368.99z",
            "malaita": "M905.14,372.74l0.58,3.09l1.39,1.91l1.17-2.42L905.14,372.74L905.14,372.74z",
            "santa ana": "M906.74,379.65l-0.51,0.88l1.68,2.21l1.17,0.07l-0.73-2.87L906.74,379.65L906.74,379.65z",
            "rennell": "M903.02,384.05l-1.75,0.81l1.53,2.13l1.31-0.74L903.02,384.05L903.02,384.05z",
            "espiritu santo": "M920.87,397.22l-1.24,1.66l0.52,1.87l0.62,0.42l1.13-1.46L920.87,397.22L920.87,397.22z",
            "malakula": "M921.49,402.31l0.1,1.35l1.34,0.42l0.93-0.52l-0.93-1.46L921.49,402.31L921.49,402.31z",
            "efate": "M923.45,414.37l-0.62,0.94l0.93,1.04l1.55-0.52L923.45,414.37L923.45,414.37z",
            "fiji": "M948.62,412.29l-1.24,1.66l-0.1,1.87l1.44,1.46L948.62,412.29L948.62,412.29z",
            "palawan": "M789.37,297.53l-0.86,1.64l-0.48,2.02l-4.78,6.07l0.29,1.25l2.01-0.29l6.21-6.94L789.37,297.53L789.37,297.53z",
            "negros": "M797.11,295.22l-0.1,5.01l1.82,1.83l0.67,3.56l1.82,0.39l0.86-2.22l-1.43-1.06l-0.38-6.26L797.11,295.22L797.11,295.22z",
            "cebu": "M802.28,297.15l-0.1,4.43l1.05,1.73l1.82-2.12l-0.48-3.85L802.28,297.15L802.28,297.15z",
            "samar": "M803.42,293.29l1.82,2.41l0.86,2.31h1.63l-0.29-3.95l-1.82-1.25L803.42,293.29L803.42,293.29z",
            "dabaw": "M806.96,302.35l0.38,2.89l-3.35,2.7l-2.77,0.29l-2.96,3.18l0.1,1.45l2.77-0.87l1.91-1.25l1.63,4.14l2.87,2.02l1.15-0.39l1.05-1.25l-2.29-2.31l1.34-1.06l1.53,1.25l1.05-1.73l-1.05-2.12l-0.19-4.72L806.96,302.35L806.96,302.35z",
            "luzon": "M791.38,272.97l-2.58,1.83l-0.29,5.78l4.02,7.8l1.34,1.06l1.72-1.16l2.96,0.48l0.57,2.6l2.2,0.19l1.05-1.44l-1.34-1.83l-1.63-1.54l-3.44-0.38l-1.82-2.99l2.1-3.18l0.19-2.79l-1.43-3.56L791.38,272.97L791.38,272.97z",
            "mindoro": "M792.72,290.21l0.76,2.7l1.34,0.87l0.96-1.25l-1.53-2.12L792.72,290.21L792.72,290.21z",
            "hainan": "M759.83,270.17l-2.39,0.67l-1.72,2.12l1.43,2.79l2.1,0.19l2.39-2.12l0.57-2.79L759.83,270.17L759.83,270.17z",
            "taiwan": "M787.46,248.31l-3.54,2.7l-0.19,5.2l3.06,3.56l0.76-0.67L787.46,248.31L787.46,248.31z",
            "kyushu": "M803.23,216.42l-1.63,1.64l0.67,2.31l1.43,0.1l0.96,5.01l1.15,1.25l2.01-1.83l0.86-3.28l-2.49-3.56L803.23,216.42L803.23,216.42z",
            "shikoku": "M812.03,213.15l-2.77,2.6l-0.1,2.99l0.67,0.87l3.73-3.18l-0.29-3.18L812.03,213.15L812.03,213.15z",
            "honshu": "M808.2,206.98l-4.88,5.59l0.86,1.35l2.39,0.29l4.49-3.47l3.16-0.58l2.87,3.37l2.2-0.77l0.86-3.28l4.11-0.1l4.02-4.82l-2.1-8l-0.96-4.24l2.1-1.73l-4.78-7.22l-1.24,0.1l-2.58,2.89v2.41l1.15,1.35l0.38,6.36l-2.96,3.66l-1.72-1.06l-1.34,2.99l-0.29,2.79l1.05,1.64l-0.67,1.25l-2.2-1.83h-1.53l-1.34,0.77L808.2,206.98L808.2,206.98z",
            "hokkaido": "M816.43,163.44l-1.53,1.35l0.77,2.89l1.34,1.35l-0.1,4.43l-1.72,0.67l-1.34,2.99l3.92,5.39l2.58-0.87l0.48-1.35l-2.77-2.5l1.72-2.22l1.82,0.29l1.43,1.54l0.1-3.18l3.92-3.18l2.2-0.58l-1.82-3.08l-0.86-1.35l-1.43,0.96l-1.24,1.54l-2.68-0.58l-2.77-1.83L816.43,163.44L816.43,163.44z",
            "iturup": "M830.86,160.45l-2.68,3.76l0.19,1.83l1.34-0.58l3.15-3.95L830.86,160.45L830.86,160.45z",
            "urup": "M834.4,154.96l-0.96,2.6l0.1,1.73l1.63-1.06l1.53-3.08V154L834.4,154.96L834.4,154.96z",
            "paramushir": "M840.04,132.03l-1.24,1.54l0.1,2.41l1.15-0.1l1.91-3.37L840.04,132.03L840.04,132.03z",
            "onekotan": "M837.75,137.91v4.24l1.34,0.48l0.96-1.54v-3.27L837.75,137.91L837.75,137.91z",
            "sakhalin": "M798.64,122.59l-0.09,6.17l7.74,11.95l2.77,10.4l4.88,9.25l1.91,0.67l1.63-1.35l0.76-2.22l-6.98-7.61l0.19-3.95l1.53-0.67l0.38-2.31l-13.67-19.36L798.64,122.59L798.64,122.59z",
            "bering island": "M852.57,103.42l-1.91,0.19l1.15,1.64l2.39,1.64l0.67-0.77L852.57,103.42L852.57,103.42z",
            "medny": "M856.29,104.58l0.29,1.64l2.96,0.87l0.29-1.16L856.29,104.58L856.29,104.58z",
            "attu": "M872.54,110.87l1.25,2.24l2.08-0.14l0.42-1.54L872.54,110.87L872.54,110.87z",
            "amchitka": "M893.51,114.37l1.67,3.08l1.25-1.4v-2.1L893.51,114.37L893.51,114.37z",
            "adak": "M907.81,104.57l-2.36,3.08l0.55,1.4l2.92-1.82l0.28-1.82L907.81,104.57L907.81,104.57z",
            "umnak": "M919.61,94.92l-2.08,2.52l2.22,0.84L919.61,94.92L919.61,94.92z",
            "unalaska": "M922.53,90.72l-1.39,2.24l0.14,2.24l1.94-0.84L922.53,90.72L922.53,90.72z",
            "st. lawrence island": "M881.29,38.39l-2.36,1.54l-0.56,1.96l1.11,1.26l2.5-0.84l2.5,0.84l1.39,0.42l-0.14-4.62L881.29,38.39L881.29,38.39z",
            "st. lawrence island west": "M69.17,53.35l3.46,6.47l2.22-0.5v-2.24L69.17,53.35L69.17,53.35z",
            "alaska": "M883.4,17.54l-4.22,7.57l8.08,5.11l9.05-7.59l5.5,9.17l-5.74,1.18l-2.27,5.88l12.71,17.22l7.65,1.27l11.03,2.17l1.36-4L930.4,57l0.73,16.75L924,85.62l3.44,0.75l8.98-18.92l2.73-14.16l-5.54-2.59l-0.89-19l4.27,0.83l-0.04,11.43l4.66,4.07l2.72-9.93l-2.18-5.9l6.58,3.15l0.69-34.99L873.66,0.5l-4.36,3.35l0.59,6.77l13.43,1.84l10.31-2.35l-3.7,6.92L883.4,17.54L883.4,17.54z",
            "chukotka": "M1.17,54.95l14.01,1.57l2.34,4.84l11.16-6.54l18.68-2.61l1.3-9.67l9.34-3.4l6.1-5.75v7.84l6.23,8.5L83.3,41.5l-6.23-7.06L69.29,13.4L59.94,2.67l-6.62-0.52L53.06,7.9l-5.45,2.75l-1.69-3.4l3.24-6.93L1.3,0.45L1.17,54.95L1.17,54.95z",
            "wrangel-w": "M78.49,3.32L74.6,6.85l1.17,2.61l2.08-1.44l1.17,1.31L82.9,7.9l-0.13-2.22L78.49,3.32L78.49,3.32z",
            "unalaska west": "M49.66,110.26l-0.17,3.01l2.16-0.5v-1.34L49.66,110.26L49.66,110.26z",
            "umnak west": "M46.34,111.6l-4.32,2.18l0.67,2.34l1.66-1.34l3.32-1.51L46.34,111.6L46.34,111.6z",
            "another aleutian west": "M28.39,114.44l-2.99-0.67l-0.5,1.34l0.33,2.51L28.39,114.44L28.39,114.44z",
            "adak west": "M22.07,114.28l-2.83-1.17l-1,1.84l1.83,1.84L22.07,114.28L22.07,114.28z",
            "amchitka west": "M12.27,111.6l-1.33-1.84l-1.33,0.5v2.51l1.5,1L12.27,111.6L12.27,111.6z",
            "attu west": "M1.47,99.71l1.66,1.17l-0.5,1.34H1.47V99.71L1.47,99.71z",
            "kerguelen": "M622.76,499.62l-0.15,4.29l5.94,1.38l1.37-3.53l-2.13,0.61l-2.74,0.61l-0.76-3.22L622.76,499.62L622.76,499.62z",
            "mauritius": "M613.01,398.99l-1.52,1.99l0.3,2.15l3.2-2.61L613.01,398.99L613.01,398.99z",
            "reunion": "M607.38,402.37l-2.28,0.15l-0.15,1.99l1.52,0.31l2.28-1.07L607.38,402.37L607.38,402.37z",
            "madagascar": "M592.3,372.92l-2.13,5.06l-3.65,6.44l-6.39,0.46l-2.74,3.22l0.46,9.82l-3.96,4.6l0.46,7.82l3.35,3.83l3.96-0.46l3.96-2.92l-0.91-4.6l9.13-15.8l-1.83-1.99l1.83-3.83l1.98,0.61l0.61-1.53l-1.83-7.82l-1.07-3.22L592.3,372.92L592.3,372.92z",
            "grande comore": "M577.69,371.23l0.46,1.53l1.98,0.31l0.76-1.99L577.69,371.23L577.69,371.23z",
            "mayotte": "M580.58,374.3l0.76,1.69h1.22l0.61-2.15L580.58,374.3L580.58,374.3z",
            "aldabra": "M602.35,358.34l-0.61,1.23l1.67,1.38l1.22-1.38L602.35,358.34L602.35,358.34z",
            "praslin": "M610.88,349.14l-1.83,1.23l1.37,2.15h1.83L610.88,349.14L610.88,349.14z",
            "mahe": "M611.64,354.51l-1.22,1.38l0.91,1.38l1.67,0.31l0.15-2.92L611.64,354.51L611.64,354.51z",
            "male": "M656.4,320.76l0.3,2.61l1.67,0.61l0.3-2.3L656.4,320.76L656.4,320.76z",
            "maldive": "M658.53,326.28l-0.15,3.22l1.22,0.61l1.07-2.15L658.53,326.28L658.53,326.28z",
            "gan": "M658.84,332.57l-1.07,1.07l1.22,1.07l1.52-1.07L658.84,332.57L658.84,332.57z",
            "path151": "M372.64,217.02l-1.36,1.37l2.44,1.37l0.27-1.91L372.64,217.02L372.64,217.02z",
            "terceira": "M379.97,216.2l-1.63,1.09l1.36,1.09l2.17-0.55L379.97,216.2L379.97,216.2z",
            "pico": "M381.05,220.03l-0.81,2.19l1.08,1.37l1.36-1.09L381.05,220.03L381.05,220.03z",
            "sao miguel": "M387.56,224.4l-0.54,1.37l0.81,0.82l2.17-1.37L387.56,224.4L387.56,224.4z",
            "madeira": "M408.18,236.42l-1.08,1.37l1.08,1.37l1.63-0.82L408.18,236.42L408.18,236.42z",
            "lanzarote": "M415.62,253.73l-1.75,1.01l0.81,0.82L415.62,253.73L415.62,253.73z",
            "gran canaria": "M409.54,253.92l-2.17,0.55l1.08,1.64h1.63L409.54,253.92L409.54,253.92z",
            "tenerife": "M404.38,252.28l-1.36,1.37l1.9,1.64l1.08-2.46L404.38,252.28L404.38,252.28z",
            "santo antao": "M387.56,290.54l-1.9,1.09l1.36,1.09l1.63-0.82L387.56,290.54L387.56,290.54z",
            "boa vista": "M392.23,292.74l-1.24,1.1l0.88,1.63l2.12-0.95L392.23,292.74L392.23,292.74z",
            "santiago": "M389.52,295.83l-1.59,0.95l1.71,2.29l1.35-0.71L389.52,295.83L389.52,295.83z",
            "kauai": "M10,248.7l-0.14,2.33l2.04,1.37l1.22-1.09L10,248.7L10,248.7z",
            "oahu": "M15.29,252.13l-1.9,1.37l1.63,2.05l1.9-1.64L15.29,252.13L15.29,252.13z",
            "kahului": "M19.1,255.41l-1.63,2.19l0.54,1.37l2.31-1.09L19.1,255.41L19.1,255.41z",
            "hawaii": "M21.81,259.65l-0.95,5.47l0.95,2.05l3.12-0.96l1.63-2.74l-3.4-3.15L21.81,259.65L21.81,259.65z",
            "raiatea": "M27.25,402.68l-1.9-0.14l-0.14,1.78l1.49,0.96l1.77-1.09L27.25,402.68L27.25,402.68z",
            "tahiti": "M33.77,404.6l-2.72,1.78l2.04,2.46l1.77-0.41l0.95-1.23L33.77,404.6L33.77,404.6z",
            "guadeloupe": "M276.6,283.37l-1.5,0.62l0.53,1.33l1.76-1.15l-0.35-0.36L276.6,283.37L276.6,283.37z",
            "dominica": "M279.07,284.88l-0.88,1.87l1.06,1.42l1.32-1.15L279.07,284.88L279.07,284.88z",
            "martinique": "M282.07,290.03l-1.06,0.98l0.79,1.6l1.5-0.44L282.07,290.03L282.07,290.03z",
            "st. lucia": "M281.98,294.03l-0.71,1.51l1.15,1.24l1.5-0.8L281.98,294.03L281.98,294.03z",
            "st. vincent": "M282.07,297.85l-1.23,0.89l0.97,1.78l1.59-0.89L282.07,297.85L282.07,297.85z",
            "grenada": "M280.57,301.31l-1.15,1.15l0.44,0.71h1.41l0.44-1.16L280.57,301.31L280.57,301.31z",
            "trinidad": "M282.24,304.78l-1.06,0.98l-1.15,0.18v1.42l2.12,1.95l0.88-1.42l0.53-1.6l-0.18-1.33L282.24,304.78L282.24,304.78z",
            "puerto rico": "M271.05,281.06l-2.64-0.89l-2.12,1.33l1.06,1.24l3.61,0.53L271.05,281.06L271.05,281.06z",
            "haiti-dominican border": "M250.87,275.38l-1.67,1.71l1.91,0.78l0.28,2.39l-4.23,0.37l0.43,2.3l1.23,0.09l0.71-1.06l4.94,0.16l0.89,1.71l1.14-1.34l3.33-0.9l2.93,0.62l0.34-1.77l-5.28-3.45l-3.42-1.28L250.87,275.38L250.87,275.38z",
            "domincan republic": "M263.11,280.44l-5.29-3.46l-2.5-0.85l-0.84,6l0.88,1.69l1.15-1.33l3.35-0.89l2.91,0.62L263.11,280.44L263.11,280.44z",
            "haiti": "M250.86,275.38l3.44,0.36l-0.41,4.22l-0.34,2.22l-4.01-0.22l-0.71,1.07l-1.23-0.09l-0.44-2.31l4.23-0.35l-0.26-2.4l-1.94-0.8L250.86,275.38L250.86,275.38z",
            "falklands west": "M307.95,508.18l-2.63-0.29l-2.62,1.76l1.9,2.06L307.95,508.18L307.95,508.18z",
            "falklands east": "M310.57,506.86l-0.87,2.79l-2.48,2.2l0.15,0.73l4.23-1.62l1.75-2.2L310.57,506.86L310.57,506.86z",
            "iceland": "M406.36,117.31l-1.96-1.11l-2.64,1.67l-2.27,2.1l0.06,1.17l2.94,0.37l-0.18,2.1l-1.04,1.05l0.25,0.68l2.94,0.19v3.4l4.23,0.74l2.51,1.42l2.82,0.12l4.84-2.41l3.74-4.94l0.06-3.34l-2.27-1.92l-1.9-1.61l-0.86,0.62l-1.29,1.67l-1.47-0.19l-1.47-1.61l-1.9,0.18l-2.76,2.29l-1.66,1.79l-0.92-0.8l-0.06-1.98l0.92-0.62L406.36,117.31L406.36,117.31z",
            "spitsbergen": "M488.26,53.96l-1.65-1.66l-3.66,1.78h-6.72L475.17,58l3.77,3.33l1.65-0.24l2.36-4.04l2,1.43l-1.42,2.85l-0.71,4.16l1.65,2.61l3.54-5.94l4.6-5.59l-1.77-1.54L488.26,53.96L488.26,53.96z",
            "nordaustlandet": "M490.26,46.83l-2.95,2.73l1.77,2.73h3.18l1.3,1.78l3.89,2.02l4.48-2.61l3.07-2.61l-1.06-2.14l-3.07-1.78l-2.24,2.02l-1.53-1.9l-1.18,0.12l-1.53,3.33l-2.24-2.26l-0.24-1.54L490.26,46.83L490.26,46.83z",
            "edgeoya": "M496.98,59.07l-2.36,2.14l-2,1.54l0.94,1.66l1.89,0.59l3.07-1.43l1.42-1.78l-1.3-2.14L496.98,59.07L496.98,59.07z",
            "prince george": "M547.82,38.79l1.72,0.69l-1.21,2.08v2.95l-2.58,1.56H543l-1.55-1.91l0.17-2.08l1.21-1.56h2.41L547.82,38.79L547.82,38.79z",
            "salisbury": "M554.36,36.88v2.08l1.72,1.39l2.41-0.17l2.07-1.91v-1.39h-1.89l-1.55,0.52l-1.21-1.39L554.36,36.88L554.36,36.88z",
            "wilczek": "M564.18,37.06l1.21,2.6l2.41,0.17l1.72-0.69l-0.86-2.43l-2.24-0.52L564.18,37.06L564.18,37.06z",
            "bell": "M573.99,33.59l-1.89-0.35l-1.72,1.74l0.86,1.56l0.52,2.43l2.24-1.73l0.52-1.91L573.99,33.59L573.99,33.59z",
            "novaya zemlya north": "M584.49,51.98l-0.52,2.43l-3.96,3.47l-8.44,1.91l-6.89,11.45l-1.21,3.3l6.89,1.74l1.03-4.16l2.07-6.42l5.34-2.78l4.48-3.47l3.27-1.39h1.72v-4.68L584.49,51.98L584.49,51.98z",
            "novaya zemlya south": "M562.28,77.31l4.65,0.52l1.55,5.38l3.96,4.16l-1.38,2.78h-2.41l-2.24-2.6l-4.99-0.17l-2.07-2.78v-1.91l3.1-0.87L562.28,77.31L562.28,77.31z",
            "komsomolets": "M634.95,18.15l-2.24-1.39h-2.58l-0.52,1.56l-2.75,1.56l-2.07,0.69l-0.34,2.08l4.82,0.35L634.95,18.15L634.95,18.15z",
            "october": "M640.28,18.67l-1.21,2.6l-2.41-0.17l-3.79,2.78l-1.03,3.47h2.41l1.38-2.26l3.27,2.43l3.1-1.39l2.24-1.91l-0.86-2.95l-1.21-2.08L640.28,18.67L640.28,18.67z",
            "bolshevik": "M645.28,20.58l1.21,4.86l1.89,4.51l2.07-3.64l3.96-0.87v-2.6l-2.58-1.91L645.28,20.58L645.28,20.58z",
            "kotelny": "M739.76,12.8l2.69,2.26l1.91-0.79l0.56-3.17L741,8.39l-2.58,1.7l-6.28,0.57v2.83l-6.62,0.11v4.63l7.74,5.76l2.02-1.47l-0.45-4.07l4.94-1.24l-1.01-1.92l-1.79-1.81L739.76,12.8L739.76,12.8z",
            "novaya sibir": "M746.94,10.09l1.79,3.39l6.96-0.79l1.91-2.49l-0.45-2.15l-1.91-0.79l-1.79,1.36l-5.16,1.13L746.94,10.09L746.94,10.09z",
            "lyakhovsky": "M746.49,23.31l-3.48-0.9L741,24.56l-0.9,2.94l4.71-0.45l3.59-1.81L746.49,23.31L746.49,23.31z",
            "wrangel": "M836.68,3.76l-2.92-0.9L830.4,4.1l-1.68,2.49l2.13,2.83l5.61-2.49l1.12-1.24L836.68,3.76L836.68,3.76z",
            "sri lanka": "M680.54,308.05l0.25,2.72l0.25,1.98l-1.47,0.25l0.74,4.45l2.21,1.24l3.43-1.98l-0.98-4.69l0.25-1.73l-3.19-2.96L680.54,308.05L680.54,308.05z",
            "cuba": "M220.85,266.92v1.27l5.32,0.1l2.51-1.46l0.39,1.07l5.22,1.27l4.64,4.19l-1.06,1.46l0.19,1.66l3.87,0.97l3.87-1.75l1.74-1.75l-2.51-1.27l-12.95-7.6l-4.54-0.49L220.85,266.92L220.85,266.92z",
            "bimini": "M239.61,259.13l-1.26-0.39l-0.1,2.43l1.55,1.56l1.06-1.56L239.61,259.13L239.61,259.13z",
            "andros": "M242.12,262.93l-1.74,0.97l1.64,2.34l0.87-1.17L242.12,262.93L242.12,262.93z",
            "inagua": "M247.73,264.68l-1.84-0.1l0.19,1.17l1.35,1.95l1.16-1.27L247.73,264.68L247.73,264.68z",
            "eleuthera": "M246.86,262.35l-3-1.27l-0.58-3.02l1.16-0.49l1.16,2.34l1.16,0.88L246.86,262.35L246.86,262.35z",
            "grand bahama": "M243.96,256.21l-1.55-0.39l-0.29-1.95l-1.64-0.58l1.06-1.07l1.93,0.68l1.45,0.88L243.96,256.21L243.96,256.21z",
            "jamaica": "M238.93,279.59l-3.48,0.88v0.97l2.03,1.17h2.13l1.35-1.56L238.93,279.59L238.93,279.59z",
            "irian jaya": "M831.93,339.34l-4.17,0.47l-2.68,1.96l1.11,2.24l4.54,0.84v0.84l-2.87,2.33l1.39,4.85l1.39,0.09l1.2-4.76h2.22l0.93,4.66l10.83,8.96l0.28,7l3.7,4.01l1.67-0.09l0.37-24.72l-6.29-4.38l-5.93,4.01l-2.13,1.31l-3.52-2.24l-0.09-7.09L831.93,339.34L831.93,339.34z",
            "alaska-westcopy": "M93.11,44.89l-8.39,1.99l1.73,9.45l9.13,2.49l0.49,1.99L82.5,65.04l-7.65,12.68l2.71,13.43L82,94.13l3.46-3.23l0.99,1.99l-4.2,4.97l-16.29,7.46l-10.37,2.49l-0.25,3.73l23.94-6.96l9.87-2.74l9.13-11.19l10.12-6.71l-5.18,8.7l5.68,0.75l9.63-4.23l1.73,6.96l6.66,1.49l6.91,6.71l0.49,4.97l-0.99,1.24l1.23,4.72h1.73l0.25-7.96h1.97l0.49,19.64l4.94-4.23l-3.46-20.39h-5.18l-5.68-7.21l27.89-47.25l-27.64-21.63l-30.85,5.97l-1.23,9.45l6.66,3.98l-2.47,6.47L93.11,44.89L93.11,44.89z",
            "galapagos": "M194.97,338.18l-0.62,2.75l-1.15,1.16l0.79,1.42l2.03-0.8l0.97-1.69l-0.62-1.78L194.97,338.18L194.97,338.18z",
            "banks": "M203.73,35.89l0.22,4.02l-7.98,8.27l2,6.7l5.76-1.56l3.33-4.92l8.42-3.13l6.87-0.45l-5.32-5.81l-2.66,2.01l-2-0.67l-1.11-2.46l-2.44-2.46L203.73,35.89L203.73,35.89z",
            "prince patrick": "M214.15,24.05l-1.77,3.13l8.65,3.13l3.1-4.69l1.33,3.13h2.22l4.21-4.69l-5.1-1.34l-2-1.56l-2.66,2.68L214.15,24.05L214.15,24.05z",
            "eglinton": "M229.23,30.31l-6.87,2.9v2.23l8.87,3.35l-2,2.23l1.33,2.9l5.54-2.46h4.66l2.22,3.57l3.77-3.8l-0.89-3.58l-3.1,1.12l-0.44-4.47l1.55-2.68h-1.55l-2.44,1.56l-1.11,0.89l0.67,3.13l-1.77,1.34l-2.66-0.22l-0.67-4.02L229.23,30.31L229.23,30.31z",
            "mackenzie king": "M238.32,23.38l-0.67,2.23l4.21,2.01l3.1-1.79l-0.22-1.34L238.32,23.38L238.32,23.38z",
            "king christian": "M241.64,19.58l-3.1,1.12l0.22,1.56l6.87-0.45l-0.22-1.56L241.64,19.58L241.64,19.58z",
            "ellef ringnes": "M256.5,23.38l-0.44,1.56l-1.11,1.56v2.23l4.21-0.67l4.43,3.8h1.55v-3.8l-4.43-4.92L256.5,23.38L256.5,23.38z",
            "amund ringnes": "M267.81,27.85l1.77,2.01l-1.55,2.68l1.11,2.9l4.88-2.68v-2.01l-2.88-3.35L267.81,27.85L267.81,27.85z",
            "axel heiberg": "M274.24,22.71l0.22,3.57h5.99l1.55,1.34l-0.22,1.56l-5.32,0.67l3.77,5.14l5.1,0.89l7.09-3.13l-10.2-15.42l-3.1,2.01l0.22,2.68l-3.55-1.34L274.24,22.71L274.24,22.71z",
            "victoria": "M222.58,47.96l-8.42,2.23l-4.88,4.25l0.44,4.69l8.87,2.68l-2,4.47l-6.43-4.02l-1.77,3.35l4.21,2.9l-0.22,4.69l6.43,1.79l7.76-0.45l1.33-2.46l5.76,6.48l3.99-1.34l0.67-4.47l2.88,2.01l0.44-4.47l-3.55-2.23l0.22-14.07l-3.1-2.46L231.89,56L222.58,47.96L222.58,47.96z",
            "prince of wales": "M249.63,57.79l-2.88-1.34l-1.55,2.01l3.1,4.92l0.22,4.69l6.65-4.02v-5.81l2.44-2.46l-2.44-1.79h-3.99L249.63,57.79L249.63,57.79z",
            "prescott": "M263.82,55.78l-4.66,3.8l1.11,4.69h2.88l1.33-2.46l2,2.01l2-0.22l5.32-4.47L263.82,55.78L263.82,55.78z",
            "cornwallis": "M263.37,48.4l-1.11,2.23l4.88,1.79l1.33-2.01L263.37,48.4L263.37,48.4z",
            "bathurst": "M260.49,39.91l-4.88,0.67l-2.88,2.68l5.32,0.22l-1.55,4.02l1.11,1.79l1.55-0.22l3.77-6.03L260.49,39.91L260.49,39.91z",
            "devon": "M268.92,38.35l-2.66,0.89l0.44,3.57l4.43,2.9l0.22,2.23l-1.33,1.34l0.67,4.47l17.07,5.58l4.66,1.56l4.66-4.02l-5.54-4.47l-5.1,1.34l-7.09-0.67l-2.66-2.68l-0.67-7.37l-4.43-2.23L268.92,38.35L268.92,38.35z",
            "baffin": "M282.88,61.59L278,61.14l-5.76,2.23l-3.1,4.24l0.89,11.62l9.53,0.45l9.09,4.47l6.43,7.37l4.88-0.22l-1.33,6.92l-4.43,7.37l-4.88,2.23l-3.55-0.67l-1.77-1.56l-2.66,3.57l1.11,3.57l3.77,0.22l4.66-2.23l3.99,10.28l9.98,6.48l6.87-8.71l-5.76-9.38l3.33-3.8l4.66,7.82l8.42-7.37l-1.55-3.35l-5.76,1.79l-3.99-10.95l3.77-6.25l-7.54-8.04l-4.21,2.9l-3.99-8.71l-8.42,1.12l-2.22-10.5l-6.87,4.69l-0.67,5.81h-3.77l0.44-5.14L282.88,61.59L282.88,61.59z",
            "bylot": "M292.86,65.61l-1.77,1.79l1.55,2.46l7.32,0.89l-4.66-4.92L292.86,65.61L292.86,65.61z",
            "ellesmere": "M285.77,40.36v2.01l-4.88,1.12l1.33,2.23l5.54,2.23l6.21,0.67l4.43,3.13l4.43-2.46l-3.1-3.13h3.99l2.44-2.68l5.99-0.89v-1.34l-3.33-2.23l0.44-2.46l9.31,1.56l13.75-5.36l-5.1-1.56l1.33-1.79h10.64l1.77-1.79l-21.51-7.6l-5.1-1.79l-5.54,4.02l-6.21-5.14l-3.33-0.22l-0.67,4.25l-4.21-3.8l-4.88,1.56l0.89,2.46l7.32,1.56l-0.44,3.57l3.99,2.46l9.76-2.46l0.22,3.35l-7.98,3.8l-4.88-3.8l-4.43,0.45l4.43,6.26l-2.22,1.12l-3.33-2.9l-2.44,1.56l2.22,4.24h3.77l-0.89,4.02l-3.1-0.45l-3.99-4.25L285.77,40.36L285.77,40.36z",
            "southhampton": "M266.01,101.85l-4.23,5.32l-0.26,5.86l3.7-2.13h4.49l3.17,2.93l2.91-2.4L266.01,101.85L266.01,101.85z",
            "newfoundland": "M317.52,171.05l-10.57,10.12l1.06,2.4l12.94,4.79l1.85-3.19l-1.06-5.32l-4.23,0.53l-2.38-2.66l3.96-3.99L317.52,171.05L317.52,171.05z",
            "canada": "M158.22,48.66l1.99,3.01l1,4.02l4.98,1.25l3.49-3.76l2.99,1.51l8.47,0.75l5.98-2.51l1,8.28h3.49V57.7l3.49,0.25l8.72,10.29l5.73,3.51l-2.99,4.77l1.25,1.25L219,80.03l0.25,5.02l2.99,0.5l0.75-7.53l4.73-1.25l3.49,5.27l7.47,3.51l3.74,0.75l2.49-3.01l0.25-4.77l4.48-2.76l1.49,4.02l-3.99,7.03l0.5,3.51l2.24-3.51l4.48-4.02l0.25-5.27l-2.49-4.02l0.75-3.26l5.98-3.01l2.74,2.01l0.5,17.57l4.23-3.76l2.49,1.51l-3.49,6.02l4.48,1l6.48-10.04l5.48,5.77l-2.24,10.29l-5.48,3.01l-5.23-2.51l-9.46,2.01l1,3.26l-2.49,4.02l-7.72,1.76l-8.72,6.78l-7.72,10.29l-1,3.26l5.23,2.01l1.99,5.02l7.22,7.28l11.46,5.02l-2.49,11.54l-0.25,3.26l2.99,2.01l3.99-5.27l0.5-10.04l6.23-0.25l2.99-5.77l0.5-8.78l7.97-15.56l9.96,3.51l5.23,7.28l-2.24,7.28l3.99,2.26l9.71-6.53l2.74,17.82l8.97,10.79l0.25,5.52l-9.96,2.51l-4.73,5.02l-9.96-2.26l-4.98-0.25l-8.72,6.78l5.23-1.25l6.48-1.25l1.25,1.51l-1.74,5.52l0.25,5.02l2.99,2.01l2.99-0.75l1.5-2.26h1.99l-3.24,6.02l-6.23,0.25l-2.74,4.02h-3.49l-1-3.01l4.98-5.02l-5.98,2.01l-0.27-8.53l-1.72-1l-5.23,2.26l-0.5,4.27h-11.96l-10.21,7.03l-13.7,4.52l-1.49-2.01l6.9-10.3l-3.92-3.77l-2.49-4.78l-5.07-3.87l-5.44-0.45l-9.75-6.83l-70.71-11.62l-1.17-4.79l-6.48-6.02v-5.02l1-4.52l-0.5-2.51l-2.49-2.51l-0.5-4.02l6.48-4.52l-3.99-21.58l-5.48-0.25l-4.98-6.53L158.22,48.66L158.22,48.66z",
            "usa": "M148.76,158.34l-1,4.02l-3.49-2.26h-1.74l-1,4.27l-12.21,27.36l3.24,23.84l3.99,2.01l0.75,6.53h8.22l7.97,6.02l15.69,1.51l1.74,8.03l2.49,1.76l3.49-3.51l2.74,1.25l2.49,11.54l4.23,2.76l3.49-6.53l10.71-7.78l6.97,3.26l5.98,0.5l0.25-3.76l12.45,0.25l2.49,2.76l0.5,6.27l-1.49,3.51l1.74,6.02h3.74l3.74-5.77l-1.49-2.76l-1.49-6.02l2.24-6.78l10.21-8.78l7.72-2.26l-1-7.28l10.71-11.55l10.71-1.76L272.8,199l10.46-6.02v-8.03l-1-0.5l-3.74,1.25l-0.5,4.92l-12.43,0.15l-9.74,6.47l-15.29,5l-2.44-2.99l6.94-10.5l-3.43-3.27l-2.33-4.44l-4.83-3.88l-5.25-0.44l-9.92-6.77L148.76,158.34L148.76,158.34z",
            "haida gwaii": "M133.83,128.41l-1.7,3.26l0.59,2.31l1.11,0.69l-0.26,0.94l-1.19,0.34l0.34,3.43l1.28,1.29l1.02-1.11l-1.28-3.34l0.76-2.66l1.87-2.49l-1.36-2.31L133.83,128.41L133.83,128.41z",
            "vancouver": "M139.45,147.95l-1.53,0.6l2.81,3.26l0.68,3.86l2.81,3l2.38-0.43v-3.94l-2.89-1.8L139.45,147.95L139.45,147.95z",
            "guatemala": "M194.88,291.52l5.93,4.34l5.98-7.43l-1.02-1.54l-2.04-0.07v-4.35l-1.53-0.93l-4.63,1.38l1.77,4.08L194.88,291.52L194.88,291.52z",
            "honduras": "M207.55,288.78l9.24-0.35l2.74,3.26l-1.71-0.39l-3.29,0.14l-4.3,4.04l-1.84,4.09l-1.21-0.64l-0.01-4.48l-2.66-1.78L207.55,288.78L207.55,288.78z",
            "el salvador": "M201.65,296.27l4.7,2.34l-0.07-3.71l-2.41-1.47L201.65,296.27L201.65,296.27z",
            "nicaragua": "M217.74,292.11l2.19,0.44l0.07,4.49l-2.55,7.28l-6.87-0.68l-1.53-3.51l2.04-4.26l3.87-3.6L217.74,292.11L217.74,292.11z",
            "costa rica": "M217.38,304.98l1.39,2.72l1.13,1.5l-1.52,4.51l-2.9-2.04l-4.74-4.34v-2.87L217.38,304.98L217.38,304.98z",
            "panama": "M220.59,309.61l-1.46,4.56l4.82,1.25l2.99,0.59l0.51-3.53l3.21-1.62l2.85,1.47l1.12,1.79l1.36-0.16l1.07-3.25l-3.56-1.47l-2.7-1.47l-2.7,1.84l-3.21,1.62l-3.28-1.32L220.59,309.61L220.59,309.61z",
            "colombia": "M253.73,299.78l-2.06-0.21l-13.62,11.23l-1.44,3.95l-1.86,0.21l0.83,8.73l-4.75,11.65l5.16,4.37l6.61,0.42l4.54,6.66l6.6,0.21l-0.21,4.99H256l2.68-9.15l-2.48-3.12l0.62-5.82l5.16-0.42l-0.62-13.52l-11.56-3.74l-2.68-7.28L253.73,299.78L253.73,299.78z",
            "venezuela": "M250.46,305.92l0.44,2.59l3.25,1.03l0.74-4.77l3.43-3.55l3.43,4.02l7.89,2.15l6.68-1.4l4.55,5.61l3.43,2.15l-3.76,5.73l1.26,4.34l-2.15,2.66l-2.23,1.87l-4.83-2.43l-1.11,1.12v3.46l3.53,1.68l-2.6,2.81l-2.6,2.81l-3.43-0.28l-3.45-3.79l-0.73-14.26l-11.78-4.02l-2.14-6.27L250.46,305.92L250.46,305.92z",
            "guyana": "M285.05,314.13l7.22,6.54l-2.87,3.32l-0.23,1.97l3.77,3.89l-0.09,3.74l-6.56,2.5l-3.93-5.31l0.84-6.38l-1.68-4.75L285.05,314.13L285.05,314.13z",
            "suriname": "M293.13,321.14l2.04,1.87l3.16-1.96l2.88,0.09l-0.37,1.12l-1.21,2.52l-0.19,6.27l-5.75,2.34l0.28-4.02l-3.71-3.46l0.19-1.78L293.13,321.14L293.13,321.14z",
            "guyane": "M302.13,321.8l5.85,3.65l-3.06,6.08l-1.11,1.4l-3.25-1.87l0.09-6.55L302.13,321.8L302.13,321.8z",
            "ecuador": "M230.2,335.85l-4.73,2.94l-0.34,4.36l-0.95,1.43l2.98,2.86l-1.29,1.41l0.3,3.6l5.33,1.27l8.07-9.55l-0.02-3.33l-3.87-0.25L230.2,335.85L230.2,335.85z",
            "peru": "M225.03,349.52l-1.94,1.96l0.13,3.13l16.94,30.88l17.59,11.34l2.72-4.56l0.65-10.03l-1.42-6.25l-4.79-8.08l-2.85,0.91l-1.29,1.43l-5.69-6.52l1.42-7.69l6.6-4.3l-0.52-4.04l-6.72-0.26l-3.49-5.86l-1.94-0.65l0.13,3.52l-8.66,10.29l-6.47-1.56L225.03,349.52L225.03,349.52z",
            "bolivia": "M258.71,372.79l8.23-3.59l2.72,0.26l1.81,7.56l12.54,4.17l2.07,6.39l5.17,0.65l2.2,5.47l-1.55,4.95l-8.41,0.65l-3.1,7.95l-6.6-0.13l-2.07-0.39l-3.81,3.7l-1.88-0.18l-6.47-14.99l1.79-2.68l0.63-10.6l-1.6-6.31L258.71,372.79L258.71,372.79z",
            "paraguay": "M291.76,399.51l2.2,2.4l-0.26,5.08l6.34-0.39l4.79,6.13l-0.39,5.47l-3.1,4.69l-6.34,0.26l-0.26-2.61l1.81-4.3l-6.21-3.91h-5.17l-3.88-4.17l2.82-8.06L291.76,399.51L291.76,399.51z",
            "uruguay": "M300.36,431.93l-2.05,2.19l0.85,11.78l6.44,1.87l8.19-8.21L300.36,431.93L300.36,431.93z",
            "argentina": "M305.47,418.2l1.94,1.82l-7.37,10.95l-2.59,2.87l0.9,12.51l5.69,6.91l-4.78,8.34l-3.62,1.56h-4.14l1.16,6.51l-6.47,2.22l1.55,5.47l-3.88,12.38l4.79,3.91l-2.59,6.38l-4.4,6.91l2.33,4.82l-5.69,0.91l-4.66-5.73l-0.78-17.85l-7.24-30.32l2.19-10.6l-4.66-13.55l3.1-17.59l2.85-3.39l-0.7-2.57l3.66-3.34l8.16,0.56l4.56,4.87l5.27,0.09l5.4,3.3l-1.59,3.72l0.38,3.76l7.65-0.36L305.47,418.2L305.47,418.2z",
            "tierra del fuego chile": "M285.04,514.1l-4.27,9.38l7.37,0.78l0.13-6.25L285.04,514.1L285.04,514.1z",
            "tierra del fuego argentina": "M288.92,518.79l0.26,5.73l4.4-0.39l3.75-2.48l-6.34-1.3L288.92,518.79L288.92,518.79z",
            "chile": "M283.59,512.63l-3.21,3.55l-0.39,4.17l-6.21-3.52l-6.6-9.51l-1.94-3.39l2.72-3.52l-0.26-4.43l-3.1-1.3l-2.46-1.82l0.52-2.48l3.23-0.91l0.65-14.33l-5.04-2.87l-3.29-74.59l0.85-1.48l6.44,14.85l2.06,0.04l0.67,2.37l-2.74,3.32l-3.15,17.87l4.48,13.76l-2.07,10.42l7.3,30.64l0.77,17.92l5.23,6.05L283.59,512.63L283.59,512.63z",
            "chiloe": "M262.28,475.14l-1.29,1.95l0.65,3.39l1.29,0.13l0.65-4.3L262.28,475.14L262.28,475.14z",
            "brazil": "M314.24,438.85l6.25-12.02l0.23-10.1l11.66-7.52h6.53l5.13-8.69l0.93-16.68l-2.1-4.46l12.36-11.28l0.47-12.45l-16.79-8.22l-20.28-6.34l-9.56-0.94l2.57-5.4l-0.7-8.22l-2.09-0.69l-3.09,6.14l-1.62,2.03l-4.16-1.84l-13.99,4.93l-4.66-5.87l0.75-6.13l-4.4,4.48l-4.86-2.62l-0.49,0.69l0.01,2.13l4.19,2.25l-6.29,6.63l-3.97-0.04l-4.02-4.09l-4.55,0.14l-0.56,4.86l2.61,3.17l-3.08,9.87l-3.6,0.28l-5.73,3.62l-1.4,7.11l4.97,5.32l0.91-1.03l3.49-0.94l2.98,5.02l8.53-3.66l3.31,0.19l2.28,8.07l12.17,3.86l2.1,6.44l5.18,0.62l2.47,6.15l-1.67,5.47l2.18,2.86l-0.32,4.26l5.84-0.55l5.35,6.76l-0.42,4.75l3.17,2.68l-7.6,11.51L314.24,438.85L314.24,438.85z",
            "belize": "M204.56,282.4l-0.05,3.65h0.84l2.86-5.34h-1.94L204.56,282.4L204.56,282.4z",
            "russia": "M817.97,72.93l1.76,6.08l3.52,1.01l3.52-5.57l-2.01-3.8l0.75-3.29h5.28l-1.26,2.53l0.5,9.12l-7.54,18.74l0.75,4.05l-0.25,6.84l14.07,20.51l2.76,0.76l0.25-16.71l2.76-2.53l-3.02-6.58l2.51-2.79l-5.53-7.34l-3.02,0.25l-1-12.15l7.79-2.03l0.5-3.55l4.02-1.01l2.26,2.03l2.76-11.14l4.77-8.1l3.77-2.03l3.27,0.25v-3.8l-5.28-1.01l-7.29-6.08l3.52-4.05l-3.02-6.84l2.51-2.53l3.02,4.05l7.54,2.79l8.29,0.76l1.01-3.54l-4.27-4.3l4.77-6.58l-10.81-3.8l-2.76,5.57l-3.52-4.56l-19.85-6.84l-18.85,3.29l-2.76,1.52v1.52l4.02,2.03l-0.5,4.81l-7.29-3.04l-16.08,6.33l-2.76-5.82h-11.06l-5.03,5.32l-17.84-4.05l-16.33,3.29l-2.01,5.06l2.51,0.76l-0.25,3.8l-15.83,1.77l1.01,5.06l-14.58-2.53l3.52-6.58l-14.83-0.76l1.26,6.84l-4.77,2.28l-4.02-3.8l-16.33,2.79l-6.28,5.82l-0.25,3.54l-4.02,0.25l-0.5-4.05l12.82-11.14v-7.6l-8.29-2.28l-10.81,3.54l-4.52-4.56h-2.01l-2.51,5.06l2.01,2.28l-14.33,7.85l-12.31,9.37l-7.54,10.38v4.3l8.04,3.29l-4.02,3.04l-8.54-3.04l-3.52,3.04l-5.28-6.08l-1.01,2.28l5.78,18.23l1.51,0.51l4.02-2.03l2.01,1.52v3.29l-3.77-1.52l-2.26,1.77l1.51,3.29l-1.26,8.61l-7.79,0.76l-0.5-2.79l4.52-2.79l1.01-7.6l-5.03-6.58l-1.76-11.39l-8.04-1.27l-0.75,4.05l1.51,2.03l-3.27,2.79l1.26,7.6l4.77,2.03l1.01,5.57l-4.78-3.04l-12.31-2.28l-1.51,4.05l-9.8,3.54l-1.51-2.53l-12.82,7.09l-0.25,4.81l-5.03,0.76l1.51-3.54v-3.54l-5.03-1.77l-3.27,1.27l2.76,5.32l2.01,3.54v2.79l-3.77-0.76l-0.75-0.76l-3.77,4.05l2.01,3.54l-8.54-0.25l2.76,3.55l-0.75,1.52h-4.52l-3.27-2.28l-0.75-6.33l-5.28-2.03v-2.53l11.06,2.28l6.03,0.51l2.51-3.8l-2.26-4.05l-16.08-6.33l-5.55,1.38l-1.9,1.63l0.59,3.75l2.36,0.41l-0.55,5.9l7.28,17.1l-5.26,8.34l-0.36,1.88l2.67,1.88l-2.41,1.59l-1.6,0.03l0.3,7.35l2.21,3.13l0.03,3.04l2.83,0.26l4.33,1.65l4.58,6.3l0.05,1.66l-1.49,2.55l3.42-0.19l3.33,0.96l4.5,6.37l11.08,1.01l-0.48,7.58l-3.82,3.27l0.79,1.28l-3.77,4.05l-1,3.8l2.26,3.29l7.29,2.53l3.02-1.77l19.35,7.34l0.75-2.03l-4.02-3.8v-4.81l-2.51-0.76l0.5-4.05l4.02-4.81l-7.21-5.4l0.5-7.51l7.71-5.07l9.05,0.51l1.51,2.79l9.3,0.51l6.79-3.8l-3.52-3.8l0.75-7.09l17.59-8.61l13.53,6.1l4.52-4.05l13.32,12.66l10.05-1.01l3.52,3.54l9.55,1.01l6.28-8.61l8.04,3.55l4.27,0.76l4.27-3.8l-3.77-2.53l3.27-5.06l9.3,3.04l2.01,4.05l4.02,0.25l2.51-1.77l6.79-0.25l0.75,1.77l7.79,0.51l5.28-5.57l10.81,1.27l3.27-1.27l1-6.08l-3.27-7.34l3.27-2.79h10.3l9.8,11.65l12.56,7.09h3.77l0.5-3.04l4.52-2.79l0.5,16.46l-4.02,0.25v4.05l2.26,2.79l-0.42,3.62l1.67,0.69l1.01-2.53l1.51,0.51l1,1.01l4.52-1.01l4.52-13.17l0.5-16.46l-5.78-13.17l-7.29-8.86l-3.52,0.51v2.79l-8.54-3.29l3.27-7.09l2.76-18.74l11.56-3.54l5.53-3.54h6.03L805.86,96l1.51,2.53l5.28-5.57l3.02,0.25l-0.5-3.29l-4.78-1.01l3.27-11.9L817.97,72.93L817.97,72.93z",
            "china": "M670.4,170.07l-3.46,8.7l-4.77-0.25l-5.03,11.01l4.27,5.44l-8.8,12.15l-4.52-0.76l-3.02,3.8l0.75,2.28l3.52,0.25l1.76,4.05l3.52,0.76l10.81,13.93v7.09l5.28,3.29l5.78-1.01l7.29,4.3l8.8,2.53l4.27-0.51l4.78-0.51l10.05-6.58l3.27,0.51l1.25,2.97l2.77,0.83l3.77,5.57l-2.51,5.57l1.51,3.8l4.27,1.52l0.75,4.56l5.03,0.51l0.75-2.28l7.29-3.8l4.52,0.25l5.28,5.82l3.52-1.52l2.26,0.25l1.01,2.79l1.76,0.25l2.51-3.54l10.05-3.8l9.05-10.89l3.02-10.38l-0.25-6.84l-3.77-0.76l2.26-2.53l-0.5-4.05l-9.55-9.62v-4.81l2.76-3.54l2.76-1.27l0.25-2.79h-7.04l-1.26,3.8l-3.27-0.76l-4.02-4.3l2.51-6.58l3.52-3.8l3.27,0.25l-0.5,5.82l1.76,1.52l4.27-4.3l1.51-0.25l-0.5-3.29l4.02-4.81l3.02,0.25l1.76-5.57l2.06-1.09l0.21-3.47l-2-2.1l-0.17-5.48l3.85-0.25l-0.25-14.13l-2.7,1.62l-1.01,3.62l-4.51-0.01l-13.07-7.35l-9.44-11.38l-9.58-0.1l-2.44,2.12l3.1,7.1l-1.08,6.66l-3.86,1.6l-2.17-0.17l-0.16,6.59l2.26,0.51l4.02-1.77l5.28,2.53v2.53l-3.77,0.25l-3.02,6.58l-2.76,0.25l-9.8,12.91l-10.3,4.56l-7.04,0.51l-4.77-3.29l-6.79,3.55l-7.29-2.28l-1.76-4.81l-12.31-0.76l-6.53-10.63h-2.76l-2.22-4.93L670.4,170.07z",
            "mongolia": "M673.8,170.17l5.82-7.72l6.99,3.23l4.75,1.27l5.82-5.34l-3.95-2.91l2.6-3.67l7.76,2.74l2.69,4.41l4.86,0.13l2.54-1.89l5.23-0.21l1.14,1.94l8.69,0.44l5.5-5.61l7.61,0.8l-0.44,7.64l3.33,0.76l4.09-1.86l4.33,2.14l-0.1,1.08l-3.14,0.09l-3.27,6.86l-2.54,0.25l-9.88,12.91l-10.09,4.45l-6.31,0.49l-5.24-3.38l-6.7,3.58l-6.6-2.05l-1.87-4.79l-12.5-0.88l-6.4-10.85l-3.11-0.2L673.8,170.17L673.8,170.17z",
            "north korea": "M778.28,194.27l1.84,0.77l0.56,6.44l3.65,0.21l3.44-4.03l-1.19-1.06l0.14-4.32l3.16-3.82l-1.61-2.9l1.05-1.2l0.58-3l-1.83-0.83l-1.56,0.79l-1.93,5.86l-3.12-0.27l-3.61,4.26L778.28,194.27L778.28,194.27z",
            "south korea": "M788.34,198.2l6.18,5.04l1.05,4.88l-0.21,2.62l-3.02,3.4l-2.6,0.14l-2.95-6.37l-1.12-3.04l1.19-0.92l-0.28-1.27l-1.47-0.66L788.34,198.2L788.34,198.2z",
            "kazakhstan": "M576.69,188.62l4.1-1.75l4.58-0.16l0.32,7h-2.68l-2.05,3.34l2.68,4.45l3.95,2.23l0.36,2.55l1.45-0.48l1.34-1.59l2.21,0.48l1.11,2.23h2.84v-2.86l-1.74-5.09l-0.79-4.13l5.05-2.23l6.79,1.11l4.26,4.29l9.63-0.95l5.37,7.63l6.31,0.32l1.74-2.86l2.21-0.48l0.32-3.18l3.31-0.16l1.74,2.07l1.74-4.13l14.99,2.07l2.52-3.34l-4.26-5.25l5.68-12.4l4.58,0.32l3.16-7.63l-6.31-0.64l-3.63-3.5l-10,1.16l-12.88-12.45l-4.54,4.03l-13.77-6.25l-16.89,8.27l-0.47,5.88l3.95,4.61l-7.7,4.35l-9.99-0.22l-2.09-3.07l-7.83-0.43l-7.42,4.77l-0.16,6.52L576.69,188.62L576.69,188.62z",
            "turkmenistan": "M593.85,207.59l-0.62,2.63h-4.15v3.56l4.46,2.94l-1.38,4.03v1.86l1.85,0.31l2.46-3.25l5.54-1.24l11.84,4.49l0.15,3.25l6.61,0.62l7.38-7.75l-0.92-2.48l-4.92-1.08l-13.84-8.99l-0.62-3.25h-5.23l-2.31,4.34h-2.31L593.85,207.59L593.85,207.59z",
            "uzbekistan": "M628.92,219.06l3.08,0.16v-5.27l-2.92-1.7l4.92-6.2h2l2,2.33l5.23-2.01l-7.23-2.48l-0.28-1.5l-1.72,0.42l-1.69,2.94l-7.29-0.24l-5.35-7.57l-9.4,0.93l-4.48-4.44l-6.2-1.05l-4.5,1.83l2.61,8.68l0.03,2.92l1.9,0.04l2.33-4.44l6.2,0.08l0.92,3.41l13.29,8.82l5.14,1.18L628.92,219.06L628.92,219.06z",
            "tajikistan": "M630.19,211.84l4.11-5.1h1.55l0.54,1.14l-1.9,1.38v1.14l1.25,0.9l6.01,0.36l1.96-0.84l0.89,0.18l0.6,1.92l3.57,0.36l1.79,3.78l-0.54,1.14l-0.71,0.06l-0.71-1.44l-1.55-0.12l-2.68,0.36l-0.18,2.52l-2.68-0.18l0.12-3.18l-1.96-1.92l-2.98,2.46l0.06,1.62l-2.62,0.9h-1.55l0.12-5.58L630.19,211.84L630.19,211.84z",
            "kirgizstan": "M636.81,199.21l-0.31,2.53l0.25,1.56l8.7,2.92l-7.64,3.08l-0.87-0.72l-1.65,1.06l0.08,0.58l0.88,0.4l5.36,0.14l2.72-0.82l3.49-4.4l4.37,0.76l5.27-7.3l-14.1-1.92l-1.95,4.73l-2.46-2.64L636.81,199.21L636.81,199.21z",
            "afghanistan": "M614.12,227.05l1.59,12.46l3.96,0.87l0.37,2.24l-2.84,2.37l5.29,4.27l10.28-3.7l0.82-4.38l6.47-4.04l2.48-9.36l1.85-1.99l-1.92-3.34l6.26-3.87l-0.8-1.12l-2.89,0.18l-0.26,2.66l-3.88-0.04l-0.07-3.55l-1.25-1.49l-2.1,1.91l0.06,1.75l-3.17,1.2l-5.85-0.37l-7.6,7.96L614.12,227.05L614.12,227.05z",
            "pakistan": "M623.13,249.84l2.6,3.86l-0.25,1.99l-3.46,1.37l-0.25,3.24h3.96l1.36-1.12h7.54l6.8,5.98l0.87-2.87h5.07l0.12-3.61l-5.19-4.98l1.11-2.74l5.32-0.37l7.17-14.95l-3.96-3.11l-1.48-5.23l9.64-0.87l-5.69-8.1l-3.03-0.82l-1.24,1.5l-0.93,0.07l-5.69,3.61l1.86,3.12l-2.1,2.24l-2.6,9.59l-6.43,4.11l-0.87,4.49L623.13,249.84L623.13,249.84z",
            "india": "M670.98,313.01l4.58-2.24l2.72-9.84l-0.12-12.08l15.58-16.82v-3.99l3.21-1.25l-0.12-4.61l-3.46-6.73l1.98-3.61l4.33,3.99l5.56,0.25v2.24l-1.73,1.87l0.37,1l2.97,0.12l0.62,3.36h0.87l2.23-3.99l1.11-10.46l3.71-2.62l0.12-3.61l-1.48-2.87l-2.35-0.12l-9.2,6.08l0.58,3.91l-6.46-0.02l-2.28-2.79l-1.24,0.16l0.42,3.88l-13.97-1l-8.66-3.86l-0.46-4.75l-5.77-3.58l-0.07-7.37l-3.96-4.53l-9.1,0.87l0.99,3.96l4.46,3.61l-7.71,15.78l-5.16,0.39l-0.85,1.9l5.08,4.7l-0.25,4.75l-5.19-0.08l-0.56,2.36l4.31-0.19l0.12,1.87l-3.09,1.62l1.98,3.74l3.83,1.25l2.35-1.74l1.11-3.11l1.36-0.62l1.61,1.62l-0.49,3.99l-1.11,1.87l0.25,3.24L670.98,313.01L670.98,313.01z",
            "nepal": "M671.19,242.56l0.46,4.27l8.08,3.66l12.95,0.96l-0.49-3.13l-8.65-2.38l-7.34-4.37L671.19,242.56L671.19,242.56z",
            "bhutan": "M695.4,248.08l1.55,2.12l5.24,0.04l-0.53-2.9L695.4,248.08L695.4,248.08z",
            "bangladesh": "M695.57,253.11l-1.31,2.37l3.4,6.46l0.1,5.04l0.62,1.35l3.99,0.07l2.26-2.17l1.64,0.99l0.33,3.07l1.31-0.82l0.08-3.92l-1.1-0.13l-0.69-3.33l-2.78-0.1l-0.69-1.85l1.7-2.27l0.03-1.12h-4.94L695.57,253.11L695.57,253.11z",
            "burma": "M729.44,303.65l-2.77-4.44l2.01-2.82l-1.9-3.49l-1.79-0.34l-0.34-5.86l-2.68-5.19l-0.78,1.24l-1.79,3.04l-2.24,0.34l-1.12-1.47l-0.56-3.95l-1.68-3.16l-6.84-6.45l1.68-1.11l0.31-4.67l2.5-4.2l1.08-10.45l3.62-2.47l0.12-3.81l2.17,0.72l3.42,4.95l-2.54,5.44l1.71,4.27l4.23,1.66l0.77,4.65l5.68,0.88l-1.57,2.71l-7.16,2.82l-0.78,4.62l5.26,6.76l0.22,3.61l-1.23,1.24l0.11,1.13l3.92,5.75l0.11,5.97L729.44,303.65L729.44,303.65z",
            "thailand": "M730.03,270.47l3.24,4.17v5.07l1.12,0.56l5.15-2.48l1.01,0.34l6.15,7.1l-0.22,4.85l-2.01-0.34l-1.79-1.13l-1.34,0.11l-2.35,3.94l0.45,2.14l1.9,1.01l-0.11,2.37l-1.34,0.68l-4.59-3.16v-2.82l-1.9-0.11l-0.78,1.24l-0.4,12.62l2.97,5.42l5.26,5.07l-0.22,1.47l-2.8-0.11l-2.57-3.83h-2.69l-3.36-2.71l-1.01-2.82l1.45-2.37l0.5-2.14l1.58-2.8l-0.07-6.44l-3.86-5.58l-0.16-0.68l1.25-1.26l-0.29-4.43l-5.14-6.51l0.6-3.75L730.03,270.47L730.03,270.47z",
            "malaysia": "M732.71,315.45l2.01,4.51l0.45,5.86l2.69,4.17l6.49,3.94l2.46,0.23l-0.45-4.06l-2.13-5.18l-3.12-6.63l-0.26,1.16l-3.76-0.17l-2.7-3.88L732.71,315.45L732.71,315.45z",
            "cambodia": "M740.48,299.47l4.09,4.37l7.61-5.64l0.67-8.9l-3.93,2.71l-2.04-1.14l-2.77-0.37l-1.55-1.09l-0.75,0.04l-2.03,3.33l0.33,1.54l2.06,1.15l-0.25,3.13L740.48,299.47L740.48,299.47z",
            "laos": "M735.47,262.93l-2.42,1.23l-2.01,5.86l3.36,4.28l-0.56,4.73l0.56,0.23l5.59-2.71l7.5,8.38l-0.18,5.28l1.63,0.88l4.03-3.27l-0.33-2.59l-11.63-11.05l0.11-1.69l1.45-1.01l-1.01-2.82l-4.81-0.79L735.47,262.93L735.47,262.93z",
            "vietnam": "M745.06,304.45l1.19,1.87l0.22,2.14l3.13,0.34l3.8-5.07l3.58-1.01l1.9-5.18l-0.89-8.34l-3.69-5.07l-3.89-3.11l-4.95-8.5l3.55-5.94l-5.08-5.83l-4.07-0.18l-3.66,1.97l1.09,4.71l4.88,0.86l1.31,3.63l-1.72,1.12l0.11,0.9l11.45,11.2l0.45,3.29l-0.69,10.4L745.06,304.45L745.06,304.45z",
            "georgia": "M555.46,204.16l3.27,4.27l4.08,1.88l2.51-0.01l4.31-1.17l1.08-1.69l-12.75-4.77L555.46,204.16L555.46,204.16z",
            "armenia": "M569.72,209.89l4.8,6.26l-1.41,1.65l-3.4-0.59l-4.22-3.78l0.23-2.48L569.72,209.89L569.72,209.89z",
            "azerbaijan": "M571.41,207.72l-1.01,1.72l4.71,6.18l1.64-0.53l2.7,2.83l1.17-4.96l2.93,0.47l-0.12-1.42l-4.82-4.22l-0.92,2.48L571.41,207.72L571.41,207.72z",
            "iran": "M569.65,217.95l-1.22,1.27l0.12,2.01l1.52,2.13l5.39,5.9l-0.82,2.36h-0.94l-0.47,2.36l3.05,3.9l2.81,0.24l5.63,7.79l3.16,0.24l2.46,1.77l0.12,3.54l9.73,5.67h3.63l2.23-1.89l2.81-0.12l1.64,3.78l10.51,1.46l0.31-3.86l3.48-1.26l0.16-1.38l-2.77-3.78l-6.17-4.96l3.24-2.95l-0.23-1.3l-4.06-0.63l-1.72-13.7l-0.2-3.15l-11.01-4.21l-4.88,1.1l-2.73,3.35l-2.42-0.16l-0.7,0.59l-5.39-0.35l-6.8-4.96l-2.53-2.77l-1.16,0.28l-2.09,2.39L569.65,217.95L569.65,217.95z",
            "turkey": "M558.7,209.19l-2.23,2.36l-8.2-0.24l-4.92-2.95l-4.8-0.12l-5.51,3.9l-5.16,0.24l-0.47,2.95h-5.86l-2.34,2.13v1.18l1.41,1.18v1.3l-0.59,1.54l0.59,1.3l1.88-0.94l1.88,2.01l-0.47,1.42l-0.7,0.95l1.05,1.18l5.16,1.06l3.63-1.54v-2.24l1.76,0.35l4.22,2.48l4.57-0.71l1.99-1.89l1.29,0.47v2.13h1.76l1.52-2.95l13.36-1.42l5.83-0.71l-1.54-2.02l-0.03-2.73l1.17-1.4l-4.26-3.42l0.23-2.95h-2.34L558.7,209.19L558.7,209.19z",
            "yemen": "M571.99,289.23l1.44,4.28v4.18l3.46,3.14l24.38-9.93l0.23-2.73l-3.91-7.02l-9.81,3.13l-5.63,5.54l-6.53-3.86L571.99,289.23L571.99,289.23z",
            "oman": "M598.38,280.84l7.39-4.26l1.31-6.25l-1.62-0.93l0.67-6.7l1.41-0.82l1.51,2.37l8.99,4.7v2.61l-10.89,16.03l-5.01,0.17L598.38,280.84L598.38,280.84z",
            "emirates": "M594.01,264.94l0.87,3.48l9.86,0.87l0.69-7.14l1.9-1.04l0.52-2.61l-3.11,0.87l-3.46,5.23L594.01,264.94L594.01,264.94z",
            "qatar": "M592.63,259.02l-0.52,4.01l1.54,1.17l1.4-0.13l0.52-5.05l-1.21-0.87L592.63,259.02L592.63,259.02z",
            "kuwait": "M583.29,247.17l-2.25-1.22l-1.56,1.57l0.17,3.14l3.63,1.39L583.29,247.17L583.29,247.17z",
            "saudi": "M584,253.24l7.01,9.77l2.26,1.8l1.01,4.38l10.79,0.85l1.22,0.64l-1.21,5.4l-7.09,4.18l-10.37,3.14l-5.53,5.4l-6.57-3.83l-3.98,3.48L566,279.4l-3.8-1.74l-1.38-2.09v-4.53l-13.83-16.72l-0.52-2.96h3.98l4.84-4.18l0.17-2.09l-1.38-1.39l2.77-2.26l5.88,0.35l10.03,8.36l5.92-0.27l0.38,1.46L584,253.24L584,253.24z",
            "syria": "M546.67,229.13l-0.35,2.54l2.82,1.18l-0.12,7.04l2.82-0.06l2.82-2.13l1.06-0.18l6.4-5.09l1.29-7.39l-12.79,1.3l-1.35,2.96L546.67,229.13L546.67,229.13z",
            "iraq": "M564.31,225.03l-1.56,7.71l-6.46,5.38l0.41,2.54l6.31,0.43l10.05,8.18l5.62-0.16l0.15-1.89l2.06-2.21l2.88,1.63l0.38-0.36l-5.57-7.41l-2.64-0.16l-3.51-4.51l0.7-3.32l1.07-0.14l0.37-1.47l-4.78-5.03L564.31,225.03L564.31,225.03z",
            "jordan": "M548.9,240.78l-2.46,8.58l-0.11,1.31h3.87l4.33-3.82l0.11-1.45l-1.77-1.81l3.17-2.63l-0.46-2.44l-0.87,0.2l-2.64,1.89L548.9,240.78L548.9,240.78z",
            "lebanon": "M546.2,232.44l0.06,1.95l-0.82,2.96l2.82,0.24l0.18-4.2L546.2,232.44L546.2,232.44z",
            "israel": "M545.32,238.06l-1.58,5.03l2.05,6.03l2.35-8.81v-1.89L545.32,238.06L545.32,238.06z",
            "cyprus": "M543.21,229.84l1.23,0.89l-3.81,3.61l-1.82-0.06l-1.35-0.95l0.18-1.77l2.76-0.18L543.21,229.84L543.21,229.84z",
            "norway": "M515.46,102.14l2.02-1.48L517.3,99l-1.28-0.74l0.18-2.03h1.1v-1.11l-4.77-1.29l-7.15,0.74l-0.73,3.14L503,97.16l-1.1-1.85l-3.49,0.18L498.04,99l-1.65,0.74l-0.92-1.85l-7.34,5.91l1.47,1.66l-2.75,1.29l-6.24,12.38l-2.2,1.48l0.18,1.11l2.2,1.11l-0.55,2.4l-3.67-0.19l-1.1-1.29l-2.38,2.77l-1.47,1.11l-0.37,2.59l-1.28,0.74l-3.3,0.74l-1.65,5.18l1.1,8.5l1.28,3.88l1.47,1.48l3.3-0.18l4.77-4.62l1.83-3.14l0.55,4.62l3.12-5.54l0.18-15.53l2.54-1.6l0.76-8.57l7.7-11.09l3.67-1.29l1.65-2.03l5.5,1.29l2.75,1.66l0.92-4.62l4.59-2.77L515.46,102.14L515.46,102.14z",
            "britain": "M446.12,149.08l-1.83,2.77l0.73,1.11h4.22v1.85l-1.1,1.48l0.73,3.88l2.38,4.62l1.83,4.25l2.93,1.11l1.28,2.22l-0.18,2.03l-1.83,1.11l-0.18,0.92l1.28,0.74l-1.1,1.48l-2.57,1.11l-4.95-0.55l-7.71,3.51l-2.57-1.29l7.34-4.25l-0.92-0.55l-3.85-0.37l2.38-3.51l0.37-2.96l3.12-0.37l-0.55-5.73l-3.67-0.18l-1.1-1.29l0.18-4.25l-2.2,0.18l2.2-7.39l4.04-2.96L446.12,149.08L446.12,149.08z",
            "ulster": "M438.42,161.47l-3.3,0.37l-0.18,2.96l2.2,1.48l2.38-0.55l0.92-1.66L438.42,161.47L438.42,161.47z",
            "ireland": "M439.51,166.55l-0.91,6l-8.07,2.96h-2.57l-1.83-1.29v-1.11l4.04-2.59l-1.1-2.22l0.18-3.14l3.49,0.18l1.6-3.76l-0.21,3.34l2.71,2.15L439.51,166.55L439.51,166.55z",
            "sweden": "M497.72,104.58l1.96,1.81h3.67l2.02,3.88l0.55,6.65l-4.95,3.51v3.51l-3.49,4.81l-2.02,0.18l-2.75,4.62l0.18,4.44l4.77,3.51l-0.37,2.03l-1.83,2.77l-2.75,2.4l0.18,7.95l-4.22,1.48l-1.47,3.14h-2.02l-1.1-5.54l-4.59-7.04l3.77-6.31l0.26-15.59l2.6-1.43l0.63-8.92l7.41-10.61L497.72,104.58L497.72,104.58z",
            "finland": "M506.79,116.94l2.07,0.91l1.28,2.4l-1.28,1.66l-6.42,7.02l-1.1,3.7l1.47,5.36l4.95,3.7l6.6-3.14l5.32-0.74l4.95-7.95l-3.67-8.69l-3.49-8.32l0.55-5.36l-2.2-0.37l-0.57-3.91l-2.96-4.83l-3.28,2.27l-1.29,5.27l-3.48-2.09l-4.84-1.18l-1.08,1.26l1.86,1.68l3.39-0.06l2.73,4.41L506.79,116.94L506.79,116.94z",
            "latvia": "M518.07,151.37l-6.85-1.11l0.15,3.83l6.35,3.88l2.6-0.76l-0.15-2.92L518.07,151.37L518.07,151.37z",
            "hiumaa": "M506.76,147.64l-1.55-0.05l-0.9,0.91l0.65,0.96l1.55,0.1l0.8-1.16L506.76,147.64L506.76,147.64z",
            "saaremaa": "M506.61,151.72l-1.5-0.15l-2.7,3.23v1.51l0.9,0.35l1.75,0.05l2.9-2.37l0.4-0.81L506.61,151.72L506.61,151.72z",
            "lithuania": "M510.81,154.7l-2.15-0.05l-2.95,2.82h-2.5l0.15,3.53l-1.5,2.77l5.4,0.05l1.55-0.2l1.55,1.87l3.55-0.15l3.4-4.33l-0.2-2.57L510.81,154.7L510.81,154.7z",
            "belarus": "M510.66,166.29l1.5,2.47l-0.6,1.97l0.1,1.56l0.55,1.87l3.1-1.76l3.85,0.1l2.7,1.11h6.85l2-4.79l1.2-1.81v-1.21l-4.3-6.05l-3.8-1.51l-3.1-0.35l-2.7,0.86l0.1,2.72l-3.75,4.74L510.66,166.29L510.66,166.29z",
            "poland": "M511.46,174.76l0.85,1.56l0.2,1.66l-0.7,1.61l-1.6,3.08l-1.35,0.61l-1.75-0.76l-1.05,0.05l-2.55,0.96l-2.9-0.86l-4.7-3.33l-4.6-2.47l-1.85-2.82l-0.35-6.65l3.6-3.13l4.7-1.56l1.75-0.2l-0.7,1.41l0.45,0.55l7.91,0.15l1.7-0.05l2.8,4.29l-0.7,1.76l0.3,2.07L511.46,174.76L511.46,174.76z",
            "spain": "M448.36,205h-12.74l-2.57-1.16l-1.24,0.09l-1.5,3.12l0.53,3.21l4.87,0.45l0.62,2.05l-2.12,11.95l0.09,2.14l3.45,1.87l3.98,0.27l7.96-1.96l3.89-4.9l0.09-4.99l6.9-6.24l0.35-2.76l-6.28-0.09L448.36,205L448.36,205z",
            "portugal": "M430.93,211.24l-0.62,8.65l-1.77,1.6l0.18,0.98l1.24,2.05l-0.8,2.5l1.33,0.45l3.1-0.36l-0.18-2.5l2.03-11.59l-0.44-1.6L430.93,211.24L430.93,211.24z",
            "majorca": "M461.1,217.21l-1.59,0.54l0.35,1.43h2.3l0.97-1.07L461.1,217.21L461.1,217.21z",
            "sardinia": "M477.56,213.38l-2.65,1.34l0.35,5.17l2.12,0.36l1.59-1.52v-4.9L477.56,213.38L477.56,213.38z",
            "corsica": "M477.83,206.96l-1.95,1.96l-0.18,1.78l1.59,0.98l0.62-0.09l0.35-2.59L477.83,206.96L477.83,206.96z",
            "france": "M460.4,178.7l-2.21,0.54l-4.42,4.81l-1.33,0.09l-1.77-1.25l-1.15,0.27l-0.88,2.76l-6.46,0.18l0.18,1.43l4.42,2.94l5.13,4.1l-0.09,4.9l-2.74,4.81l5.93,2.85l6.02,0.18l1.86-2.14l3.8,0.09l1.06,0.98l3.8-0.27l1.95-2.5l-2.48-2.94l-0.18-1.87l0.53-2.05l-1.24-1.78l-2.12,0.62l-0.27-1.6l4.69-5.17v-3.12l-3.1-1.78l-1.59-0.27L460.4,178.7L460.4,178.7z",
            "netherlands": "M470.09,168.27l-4.53,2.23l0.96,0.87l0.1,2.23l-0.96-0.19l-1.06-1.65l-2.53,4.01l3.89,0.81l1.45,1.53l0.77,0.02l0.51-3.46l2.45-1.03L470.09,168.27L470.09,168.27z",
            "belgium": "M461.61,176.52l-0.64,1.6l6.88,4.54l1.98,0.47l0.07-2.15l-1.73-1.94h-1.06l-1.45-1.65L461.61,176.52L461.61,176.52z",
            "germany": "M471.14,167.88l3.57-0.58v-2.52l2.99-0.49l1.64,1.65l1.73,0.19l2.7-1.17l2.41,0.68l2.12,1.84l0.29,6.89l2.12,2.82l-2.79,0.39l-4.63,2.91l0.39,0.97l4.14,3.88l-0.29,1.94l-3.85,1.94l-3.57,0.1l-0.87,1.84h-1.83l-0.87-1.94l-3.18-0.78l-0.1-3.2l-2.7-1.84l0.29-2.33l-1.83-2.52l0.48-3.3l2.5-1.17L471.14,167.88L471.14,167.88z",
            "denmark": "M476.77,151.5l-4.15,4.59l-0.15,2.99l1.89,4.93l2.96-0.56l-0.37-4.03l2.04-2.28l-0.04-1.79l-1.44-3.73L476.77,151.5L476.77,151.5z",
            "sjælland": "M481.44,159.64l-0.93-0.04l-1.22,1.12l0.15,1.75l2.89,0.08l0.15-1.98L481.44,159.64L481.44,159.64z",
            "gotland": "M498.49,150.17l-2.11,1.67l1.06,2.45l1.87-1.82L498.49,150.17L498.49,150.17z",
            "switzerland": "M472.91,189.38l-4.36,4.64l0.09,0.47l1.79-0.56l1.61,2.24l2.72-0.96l1.88,1.46l0.77-0.44l2.32-3.64l-0.59-0.56l-2.29-0.06l-1.11-2.27L472.91,189.38L472.91,189.38z",
            "czech": "M488.43,184.87h2.97h1.46l2.37,1.69l4.39-3.65l-4.26-3.04l-4.22-2.04l-2.89,0.52l-3.92,2.52L488.43,184.87L488.43,184.87z",
            "slovakia": "M495.84,187.13l0.69,0.61l0.09,1.04l7.63-0.17l5.64-2.43l-0.09-2.47l-1.08,0.48l-1.55-0.83l-0.95-0.04l-2.5,1l-3.4-0.82L495.84,187.13L495.84,187.13z",
            "austria": "M480.63,190.12l-0.65,1.35l0.56,0.96l2.33-0.48h1.98l2.15,1.82l4.57-0.83l3.36-2l0.86-1.35l-0.13-1.74l-3.02-2.26l-4.05,0.04l-0.34,2.3l-4.26,2.08L480.63,190.12L480.63,190.12z",
            "hungary": "M496.74,189.6l-1.16,1.82l0.09,2.78l1.85,0.95l5.69,0.17l7.93-6.68l0.04-1.48l-0.86-0.43l-5.73,2.6L496.74,189.6L496.74,189.6z",
            "slovenia": "M494.8,191.99l-2.54,1.52l-4.74,1.04l0.95,2.74l3.32,0.04l3.06-2.56L494.8,191.99L494.8,191.99z",
            "croatia": "M495.62,195.16l-3.53,2.91h-3.58l-0.43,2.52l1.64,0.43l0.82-1.22l1.29,1.13l1.03,3.6l7.07,3.3l0.7-0.8l-7.17-7.4l0.73-1.35l6.81-0.26l0.69-2.17l-4.44,0.13L495.62,195.16L495.62,195.16z",
            "bosnia": "M494.8,198.94l-0.37,0.61l6.71,6.92l2.46-3.62l-0.09-1.43l-2.15-2.61L494.8,198.94L494.8,198.94z",
            "italy": "M472.27,196.98l-0.62,1.57l0.17,1.71l2.39,2.79l3.76-0.13l8.3,9.64l5.18,1.5l3.06,2.89l0.73,6.59l1.64-0.96l1.42-3.59l-0.35-2.58l2.43-0.22l0.35-1.46l-6.85-3.28l-6.5-6.39l-2.59-3.82l-0.63-3.63l3.31-0.79l-0.85-2.39l-2.03-1.71l-1.75-0.08l-2.44,0.67l-2.3,3.22l-1.39,0.92l-2.15-1.32L472.27,196.98L472.27,196.98z",
            "sicily": "M492.44,223.02l-1.45-0.78l-4.95,0.78l0.17,1.34l4.45,2.24l0.67,0.73l1.17,0.17L492.44,223.02L492.44,223.02z",
            "malta": "M492.61,230.47l-1.67,0.34l0.06,1.85l1.5,0.5l0.67-0.56L492.61,230.47L492.61,230.47z",
            "ukraine": "M515.57,173.15l-2.9,1.63l0.72,3.08l-2.68,5.65l0.02,2.49l1.26,0.8l8.08,0.4l2.26-1.87l2.42,0.81l3.47,4.63l-2.54,4.56l3.02,0.88l3.95-4.55l2.26,0.41l2.1,1.46l-1.85,2.44l2.5,3.9h2.66l1.37-2.6l2.82-0.57l0.08-2.11l-5.24-0.81l0.16-2.27h5.08l5.48-4.39l2.42-2.11l0.4-6.66l-10.8-0.97l-4.43-6.25l-3.06-1.05l-3.71,0.16l-1.67,4.13l-7.6,0.1l-2.47-1.14L515.57,173.15L515.57,173.15z",
            "moldova": "M520.75,187.71l3.1,4.77l-0.26,2.7l1.11,0.05l2.63-4.45l-3.16-3.92l-1.79-0.74L520.75,187.71L520.75,187.71z",
            "romania": "M512.18,187.6l-0.26,1.48l-5.79,4.82l4.84,7.1l3.1,2.17h5.58l1.84-1.54l2.47-0.32l1.84,1.11l3.26-3.71l-0.63-1.86l-3.31-0.85l-2.26-0.11l0.11-3.18l-3-4.72L512.18,187.6L512.18,187.6z",
            "montenegro": "M 504.90234 207.24805 L 504.85742 206.3125 L 503.53711 204.45898 L 501.40039 207.48047 L 501.82031 208.75 L 503.56055 209.07031 L 504.90234 207.24805 z ",
            "serbia": "M 505.55078 194.53906 L 503.5 196.08008 L 502.5 196.08008 L 501.82031 198.19922 L 504.24023 201.00977 L 504.40039 203.24023 L 504.05859 203.72266 L 505.69531 206.02148 L 505.75195 207.24023 L 506.92969 208.38086 L 510.76953 207.21094 L 510.44922 201.75 L 505.55078 194.53906 z ",
            "bulgaria": "M511.44,202.39l0.16,4.98l1.68,3.5l6.31,0.11l2.84-2.01l2.79-1.11l-0.68-3.18l0.63-1.7l-1.42-0.74l-1.95,0.16l-1.53,1.54l-6.42,0.05L511.44,202.39L511.44,202.39z",
            "albania": "M504.02,209.76v4.61l1.32,2.49l0.95-0.11l1.63-2.97l-0.95-1.33l-0.37-3.29l-1.26-1.17L504.02,209.76L504.02,209.76z",
            "macedonia": "M510.92,208.01l-3.37,1.11l0.16,2.86l0.79,1.01l4-1.86L510.92,208.01L510.92,208.01z",
            "greece": "M506.71,217.6l-0.11,1.33l4.63,2.33l2.21,0.85l-1.16,1.22l-2.58,0.26l-0.37,1.17l0.89,2.01l2.89,1.54l1.26,0.11l0.16-3.45l1.89-2.28l-5.16-6.1l0.68-2.07l1.21-0.05l1.84,1.48l1.16-0.58l0.37-2.07l5.42,0.05l0.21-3.18l-2.26,1.59l-6.63-0.16l-4.31,2.23L506.71,217.6L506.71,217.6z",
            "thrace": "M523.02,209.7l-0.16,3.55l3.1-0.95l1.42-0.95l-0.42-1.54l-1.47-1.17L523.02,209.7L523.02,209.7z",
            "crete": "M516.76,230.59l1.63,0.05l0.68,1.01h2.37l1.58-0.58l0.53,0.64l-1.05,1.38l-4.63,0.16l-0.84-1.11l-0.89-0.53L516.76,230.59L516.76,230.59z",            
        }

        loc_mapping = {
            'russian federation': [
                'russia', 
                'chukotka', 
                'sakhalin',
                'novaya zemlya north',
                'novaya zemlya south',
                'komsomolets',
                'october',
                'bolshevik',
                'kotelny',
                'novaya sibir',
                'lyakhovsky',
                'wrangel',
            ],
            'united states': ['usa', 'alaska', 'alaska-westcopy', 'kauai', 'oahu', 'kahului', 'hawaii'],
            'italy': ['sicily', 'sardinia'],
            'portugal': ['madeira'],
            'antarctica': ['east antarctica', 'antarctic peninsula'],
            'united kingdom': ['britain', 'ulster'],
            'australia': ['tasmania'],
            'united arab emirates': ['emirates'],
            'saudi arabia': ['saudi'],
            'new zealand': ['new zealand north island', 'new zealand south island'],
            'bolivia, plurinational state of': ['bolivia'],
            'somalia': ['somaliland'],
            'ecuador': ['galapagos'],
            'canada': [
                'banks', 
                'prince patrick', 
                'eglinton', 
                'mackenzie king', 
                'king christian',
                'ellef ringnes',
                'amund ringnes',
                'axel heiberg',
                'victoria',
                'prince of wales',
                'prescott',
                'cornwallis',
                'bathurst',
                'devon',
                'baffin',
                'bylot',
                'ellesmere',
                'southhampton',
                'newfoundland'
            ],
            'chile': ['tierra del fuego chile'],
            'argentina': ['tierra del fuego argentina'],
            'iran, islamic republic of': ['iran'],
            'japan': [
                'kyushu',
                'shikoku',
                'honshu',
                'hokkaido',
            ],
            'korea, democratic people\'s republic of': ['north korea'],
            'korea, republic of': ['south korea'],
            'mauritania': ['mauretania'],
            'bahamas': ['grand bahama', 'bimini', 'andros', 'inagua', 'eleuthera'],
            'dominican republic': ['domincan republic'],
            'venezuela, bolivarian republic of': ['venezuela'],
            'french guiana': ['guyane'],
            'viet nam': ['vietnam'],
            'tanzania, united republic of': ['tanzania'],
            'taiwan, province of china': ['taiwan'],
            'syrian arab republic': ['syria'],
            'seychelles': ['aldabra', 'praslin', 'mahe'],
            'réunion': ['reunion'],
            'myanmar': ['burma'],
            'north macedonia': ['macedonia'],
            'maldives': ['maldive'],
            'moldova, republic of': ['moldova'],
            'lao people\'s democratic republic': ['laos'],
            'kyrgyzstan': ['kirgizstan'],
            'czechia': ['czech'],
            'guinea-bissau': ['bissau'],
            # 'gambia': ['gambia'],
            'guinea': ['guinee'],
            'burkina faso': ['burkina'],
            'comoros': ['grande comore'],
            'côte d\'ivoire': ['ivoire'],
            'central african republic': ['centrafrique'],
            'brunei darussalam': ['brunei'],
            'bosnia and herzegovina': ['bosnia'],
            'congo, the democratic republic of the': ['drc'],
            'south sudan': ['south_sudan'],
            'eswatini': ['swaziland'],
            'indonesia': ['irian jaya', 'kalimantan', 'sumatra', 'sulawesi', 'maluku', 'seram', 'java', 'bali', 'lombok', 'sumba', 'flores', ''],
            'philippines': [
                'palawan',
                'negros',
                'cebu',
                'samar',
                'luzon',
                'mindoro',
                'dabaw',
            ],
            'timor-leste': ['timor'],
            'malaysia': ['east malaysia'],
            'greece': ['crete'],
            'china': ['hainan'],
            'spain': ['majorca', 'lanzarote', 'gran canaria', 'tenerife'],
            'france': ['corsica'],
            'denmark': ['sjælland'],
        }

        res = []
        for item in pycountry.countries:
            c = item.name
            loc_list = loc_mapping.get(c.lower(), [])
            for loc in [c.lower()] + loc_list:
                if loc in locations:
                    res.append({
                        'id': loc,
                        'name': c,
                        'iso': item.alpha_2.lower(),
                        'path': locations[loc],
                        'class': 'a' if c in geo else 'r',
                    })
                else:
                    if loc not in loc_mapping:
                        logger.info(f'Country not found: {loc}')

        t = current_app.jinja_env.get_template('_ext-map.html')

        def func_black_geo(s):
            if isinstance(s, list):
                all = [item.name for item in pycountry.countries]
                return set(all) ^ set(s)
            return []

        s = t.render(
            countries = res,
            has_legend = has_legend,
            cnt_a = len(geo),
            cnt_r = len(func_black_geo(geo))
        )
        return s

    def parse(self, parser):
        tag = parser.stream.__next__()

        args = []
        try:
            while parser.stream.current.type != 'block_end':
                args.append(parser.parse_expression())
                parser.stream.skip_if('comma')
        except TemplateSyntaxError:
            pass

        body = parser.parse_statements(['name:endmap'], drop_needle=True)

        callback = self.call_method('_render', args=[List(args)])
        return CallBlock(callback, [], [], body).set_lineno(tag.lineno)


class PlayExtension(Extension):
    tags = set(['play'])

    def __init__(self, environment):
        super(PlayExtension, self).__init__(environment)

    def _render(self, args, caller=None):
        logger.info(f'play Args IN: {args}')

        title = args[0]
        software = args[1]
        count = int(args[2])
        priority = args[3:]

        @current_app.cache.cached(timeout=24*60*60, key_prefix=f'casinos_by_soft_geo:{software}:{current_user.country}')
        def get_casino():
            _casino = None
            kwargs = {
                'is_searchable': True,
                'is_redirect': False,
                'country': current_user.country_full,
                'software': software,
                '_source': True, 
                '_count': count,
            }
            if len(current_app.config['AVAILABLE_LOCALE']) > 1:
                kwargs['locale_available'] = g.language
            if priority:
                kwargs['title'] = priority

            while True:
                casinos, found = Page.provider_by_context(**kwargs)
                logger.info(f'Casinos for play found: {found}, kwargs: {kwargs}')
                logger.info(f'Casinos for play list: {[item.title for item in casinos]}')

                if found > 0:
                    _casino = random.choice(casinos)
                    break

                if 'title' in kwargs:
                    del kwargs['title']
                else:
                    break

            return {'visit_url': _casino.visit_url, 'title': _casino.title} if _casino else None

        rv = caller().strip()

        _res = ''
        try:
            screen, play_url = rv.split('|')

            t = current_app.jinja_env.get_template('_ext-play.html')
            _res = t.render(
                title=title,
                screen=screen,
                play_url=play_url,
                casino=get_casino(),
            )
        except Exception as _e:
            _res = rv
            logger.warning(f'Exception: {_e}')

        return _res

    def parse(self, parser):
        tag = parser.stream.__next__()

        args = []
        try:
            while parser.stream.current.type != 'block_end':
                args.append(parser.parse_expression())
                parser.stream.skip_if('comma')
        except TemplateSyntaxError:
            pass

        body = parser.parse_statements(['name:endplay'], drop_needle=True)

        callback = self.call_method('_render', args=[List(args)])
        return CallBlock(callback, [], [], body).set_lineno(tag.lineno)        