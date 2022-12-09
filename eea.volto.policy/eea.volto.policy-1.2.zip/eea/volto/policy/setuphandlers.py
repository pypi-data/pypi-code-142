""" Custom setup
"""
# pylint: disable = C0301
import json
import logging

from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from plone import api

logger = logging.getLogger("eea.volto.policy")


@implementer(INonInstallable)
class HiddenProfiles(object):
    """ Hidden profiles
    """

    def getNonInstallableProfiles(self):
        """ Hide uninstall profile from site-creation and quickinstaller.
        """
        return [
            'eea.volto.policy:uninstall',
        ]


def post_install(context):
    """ Post install script
    """
    # Get default_page if any, then set blocks to plone root
    portal = api.portal.get()
    homepage = getattr(portal, 'default_page', None)
    if homepage:
        homepage = api.content.get('/' + homepage)
    create_root_homepage(portal, homepage)


def uninstall(context):
    """ Uninstall script
    """
    # Remove blocks information from portal
    portal = api.portal.get()
    portal._delProperty("blocks")
    portal._delProperty("blocks_layout")


def create_root_homepage(portal, default_home=None):
    """It takes a default object:
    {
        "title": "The title",
        "description": "The description",
        "blocks": {...},
        "blocks_layout": [...]
    }
    and sets it as default page in the Plone root object.
    """
    if default_home:
        blocks = getattr(default_home, "blocks", {})
        blocks_layout = getattr(default_home, "blocks_layout", {})
        portal.setTitle(default_home.title)
        portal.setDescription(default_home.description)

        logger.info(
            "Creating custom default homepage in Plone site root."
        )
    else:
        blocks = {
            "0358abe2-b4f1-463d-a279-a63ea80daf19": {"@type": "description"},
            "07c273fc-8bfc-4e7d-a327-d513e5a945bb": {"@type": "title"},
            "2dfe8e4c-5bf6-43f1-93e1-6c320ede7226": {
                "@type": "text",
                "text": {
                    "blocks": [
                        {
                            "data": {},
                            "depth": 0,
                            "entityRanges": [],
                            "inlineStyleRanges": [
                                {"length": 10, "offset": 0, "style": "BOLD"}
                            ],
                            "key": "6470b",
                            "text": "Disclaimer: This instance is reset every night, so all changes will be lost afterwards.",  # noqa
                            "type": "unstyled",
                        }
                    ],
                    "entityMap": {},
                },
            },
            "3c881f51-f75b-4959-834a-6e1d5edc32ae": {
                "@type": "text",
                "text": {
                    "blocks": [
                        {
                            "data": {},
                            "depth": 0,
                            "entityRanges": [],
                            "inlineStyleRanges": [
                                {"length": 5, "offset": 6, "style": "BOLD"}
                            ],
                            "key": "ekn3l",
                            "text": "user: admin",
                            "type": "unstyled",
                        }
                    ],
                    "entityMap": {},
                },
            },
            "5e1c30b1-ec6c-4dc0-9483-9768c3c416e4": {
                "@type": "text",
                "text": {
                    "blocks": [
                        {
                            "data": {},
                            "depth": 0,
                            "entityRanges": [
                                {"key": 0, "length": 5, "offset": 0},
                                {"key": 1, "length": 8, "offset": 455},
                            ],
                            "inlineStyleRanges": [],
                            "key": "behki",
                            "text": "Plone is a CMS built on Python with over 19 years of experience. Plone has very interesting features that appeal to developers and users alike, such as customizable content types, hierarchical URL object traversing and a sophisticated content workflow powered by a granular permissions model. This allows you to build anything from simple websites to enterprise-grade intranets. Volto exposes all these features and communicates with Plone via its mature REST API. Volto can be esily themed and is highly customizable.",  # noqa
                            "type": "unstyled",
                        }
                    ],
                    "entityMap": {
                        "0": {
                            "data": {
                                "href": "https://plone.org",
                                "rel": "nofollow",
                                "url": "https://plone.org/",
                            },
                            "mutability": "MUTABLE",
                            "type": "LINK",
                        },
                        "1": {
                            "data": {
                                "href": "https://github.com/plone/plone.restapi",  # noqa
                                "url": "https://github.com/plone/plone.restapi",   # noqa
                            },
                            "mutability": "MUTABLE",
                            "type": "LINK",
                        },
                    },
                },
            },
            "61cc1bc0-d4f5-4e2b-9152-79512045a4dd": {
                "@type": "text",
                "text": {
                    "blocks": [
                        {
                            "data": {},
                            "depth": 0,
                            "entityRanges": [],
                            "inlineStyleRanges": [],
                            "key": "9qsa4",
                            "text": "Demo",
                            "type": "header-two",
                        }
                    ],
                    "entityMap": {},
                },
            },
            "874049e7-629e-489a-b46c-1adf35ad40ee": {
                "@type": "text",
                "text": {
                    "blocks": [
                        {
                            "data": {},
                            "depth": 0,
                            "entityRanges": [],
                            "inlineStyleRanges": [],
                            "key": "9pnjr",
                            "text": "Happy hacking!",
                            "type": "unstyled",
                        }
                    ],
                    "entityMap": {},
                },
            },
            "942b6530-2407-420f-9c24-597adda6b2ce": {
                "@type": "text",
                "text": {
                    "blocks": [
                        {
                            "data": {},
                            "depth": 0,
                            "entityRanges": [{"key": 0, "length": 36, "offset": 39}],  # noqa
                            "inlineStyleRanges": [],
                            "key": "6a248",
                            "text": "Last but not least, it also supports a Volto Nodejs-based backend reference API implementation that demos how other systems could also use Volto to display and create content through it.",  # noqa
                            "type": "unstyled",
                        }
                    ],
                    "entityMap": {
                        "0": {
                            "data": {
                                "href": "https://github.com/plone/volto-reference-backend",  # noqa
                                "url": "https://github.com/plone/volto-reference-backend",   # noqa
                            },
                            "mutability": "MUTABLE",
                            "type": "LINK",
                        }
                    },
                },
            },
            "9a976b8e-72ba-468a-bea8-b37a31bb386b": {
                "@type": "text",
                "text": {
                    "blocks": [
                        {
                            "data": {},
                            "depth": 0,
                            "entityRanges": [],
                            "inlineStyleRanges": [
                                {"length": 12, "offset": 51, "style": "BOLD"}
                            ],
                            "key": "94arl",
                            "text": "You can log in and use it as admin user using these credentials:",  # noqa
                            "type": "unstyled",
                        }
                    ],
                    "entityMap": {},
                },
            },
            "b3717238-448f-406e-b06f-57a9715c3326": {
                "@type": "text",
                "text": {
                    "blocks": [
                        {
                            "data": {},
                            "depth": 0,
                            "entityRanges": [{"key": 0, "length": 5, "offset": 0}],  # noqa
                            "inlineStyleRanges": [],
                            "key": "1bnna",
                            "text": "Volto is a React-based frontend for content management systems, currently supporting three backend implementations: Plone, Guillotina and a NodeJS reference implementation.",  # noqa
                            "type": "unstyled",
                        }
                    ],
                    "entityMap": {
                        "0": {
                            "data": {
                                "href": "https://github.com/plone/volto",
                                "url": "https://github.com/plone/volto",
                            },
                            "mutability": "MUTABLE",
                            "type": "LINK",
                        }
                    },
                },
            },
            "c049ff8b-3e5a-4cfb-bca6-e4a6cca9be28": {
                "@type": "text",
                "text": {
                    "blocks": [
                        {
                            "data": {},
                            "depth": 0,
                            "entityRanges": [],
                            "inlineStyleRanges": [],
                            "key": "55n44",
                            "text": "You can use this site to test Volto. It runs on the master branch of Volto using latest Plone 5.2 Backend running on Python 3.",  # noqa
                            "type": "unstyled",
                        }
                    ],
                    "entityMap": {},
                },
            },
            "c91f0fe9-f2e9-4a17-84a5-8e4f2678ed3c": {
                "@type": "text",
                "text": {
                    "blocks": [
                        {
                            "data": {},
                            "depth": 0,
                            "entityRanges": [],
                            "inlineStyleRanges": [
                                {"length": 5, "offset": 10, "style": "BOLD"}
                            ],
                            "key": "buncq",
                            "text": "password: admin",
                            "type": "unstyled",
                        }
                    ],
                    "entityMap": {},
                },
            },
            "e0ca2fbc-7800-4b9b-afe5-8e42af9f5dd6": {
                "@type": "text",
                "text": {
                    "blocks": [
                        {
                            "data": {},
                            "depth": 0,
                            "entityRanges": [],
                            "inlineStyleRanges": [],
                            "key": "f0prj",
                            "text": "2020 - Volto Team - Plone Foundation",
                            "type": "unstyled",
                        }
                    ],
                    "entityMap": {},
                },
            },
            "effbdcdc-253c-41a7-841e-5edb3b56ce32": {
                "@type": "text",
                "text": {
                    "blocks": [
                        {
                            "data": {},
                            "depth": 0,
                            "entityRanges": [{"key": 0, "length": 10, "offset": 36}],  # noqa
                            "inlineStyleRanges": [],
                            "key": "68rve",
                            "text": "Volto also supports other APIs like Guillotina, a Python resource management system, inspired by Plone and using the same basic concepts like traversal, content types and permissions model.",  # noqa
                            "type": "unstyled",
                        }
                    ],
                    "entityMap": {
                        "0": {
                            "data": {
                                "href": "https://guillotina.io/",
                                "rel": "nofollow",
                                "url": "https://guillotina.io/",
                            },
                            "mutability": "MUTABLE",
                            "type": "LINK",
                        }
                    },
                },
            },
        }

        blocks_layout = {
            "items": [
                "07c273fc-8bfc-4e7d-a327-d513e5a945bb",
                "0358abe2-b4f1-463d-a279-a63ea80daf19",
                "b3717238-448f-406e-b06f-57a9715c3326",
                "5e1c30b1-ec6c-4dc0-9483-9768c3c416e4",
                "effbdcdc-253c-41a7-841e-5edb3b56ce32",
                "942b6530-2407-420f-9c24-597adda6b2ce",
                "61cc1bc0-d4f5-4e2b-9152-79512045a4dd",
                "c049ff8b-3e5a-4cfb-bca6-e4a6cca9be28",
                "9a976b8e-72ba-468a-bea8-b37a31bb386b",
                "3c881f51-f75b-4959-834a-6e1d5edc32ae",
                "c91f0fe9-f2e9-4a17-84a5-8e4f2678ed3c",
                "2dfe8e4c-5bf6-43f1-93e1-6c320ede7226",
                "874049e7-629e-489a-b46c-1adf35ad40ee",
                "e0ca2fbc-7800-4b9b-afe5-8e42af9f5dd6",
            ]
        }

        portal.setTitle("Welcome to Volto!")
        portal.setDescription("The React powered content management system")

        logger.info("Added blocks to Plone site root.")

    if not getattr(portal, "blocks", False):
        portal.manage_addProperty("blocks", json.dumps(blocks), "string")

    if not getattr(portal, "blocks_layout", False):
        portal.manage_addProperty(
            "blocks_layout", json.dumps(blocks_layout), "string"
        )  # noqa
