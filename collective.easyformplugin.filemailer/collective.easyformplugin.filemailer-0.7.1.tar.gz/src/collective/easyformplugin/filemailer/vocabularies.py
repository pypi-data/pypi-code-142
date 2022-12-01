# CatalogVocab
from plone.app.layout.navigation.root import getNavigationRootObject
from plone.app.vocabularies.catalog import CatalogVocabulary
from plone.app.vocabularies.utils import parseQueryString
from plone.dexterity.interfaces import IDexterityContent

from plone.uuid.interfaces import IUUID
from Products.CMFCore.utils import getToolByName
from zope.component.hooks import getSite
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import ISource
from zope.schema.interfaces import IVocabularyFactory

import os
import six

# Example of a Vocabulary that can be used outside the normal Zope object context, 
# Like theEeasyform MailerAction context. It needs the context hack added below

@implementer(IVocabularyFactory)
class CatalogVocabularyFactory(object):
    def __call__(self, context, query=None):

        # Make sure we have a context if rendered inside a datagridfield Row
        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]  # pylint: disable=no-member

        parsed = {}
        if query:
            parsed = parseQueryString(context, query["criteria"])
            if "sort_on" in query:
                parsed["sort_on"] = query["sort_on"]
            if "sort_order" in query:
                parsed["sort_order"] = str(query["sort_order"])

        # If no path is specified check if we are in a sub-site and use that
        # as the path root for catalog searches
        if "path" not in parsed:
            site = getSite()
            nav_root = getNavigationRootObject(context, site)
            site_path = site.getPhysicalPath()
            if nav_root and nav_root.getPhysicalPath() != site_path:
                parsed["path"] = {
                    "query": "/".join(nav_root.getPhysicalPath()),
                    "depth": -1,
                }
        return CatalogVocabulary.fromItems(parsed, context)


