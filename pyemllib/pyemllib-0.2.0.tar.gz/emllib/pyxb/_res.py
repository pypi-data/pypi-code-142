# ./emllib/eml220/_res.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e3f6cbfc3c34e9f9d6eb92b3fc95c25ca0776d7f
# Generated 2022-06-27 15:56:32.586916 by PyXB version 1.2.6 using Python 3.8.10.final.0
# Namespace https://eml.ecoinformatics.org/resource-2.2.0 [xmlns:res]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:f2f05a8a-f620-11ec-ae48-6d7493702e64')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import emllib.eml220._nsgroup as _ImportedBinding_emllib_eml220__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('https://eml.ecoinformatics.org/resource-2.2.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)

from emllib.eml220._nsgroup import CTD_ANON_63 as CTD_ANON # None
from emllib.eml220._nsgroup import KeyTypeCode # {https://eml.ecoinformatics.org/resource-2.2.0}KeyTypeCode
from emllib.eml220._nsgroup import yearDate # {https://eml.ecoinformatics.org/resource-2.2.0}yearDate
from emllib.eml220._nsgroup import IDType # {https://eml.ecoinformatics.org/resource-2.2.0}IDType
from emllib.eml220._nsgroup import SystemType # {https://eml.ecoinformatics.org/resource-2.2.0}SystemType
from emllib.eml220._nsgroup import ScopeType # {https://eml.ecoinformatics.org/resource-2.2.0}ScopeType
from emllib.eml220._nsgroup import FunctionType # {https://eml.ecoinformatics.org/resource-2.2.0}FunctionType
from emllib.eml220._nsgroup import CTD_ANON_64 as CTD_ANON_ # None
from emllib.eml220._nsgroup import InlineType # {https://eml.ecoinformatics.org/resource-2.2.0}InlineType
from emllib.eml220._nsgroup import OfflineType # {https://eml.ecoinformatics.org/resource-2.2.0}OfflineType
from emllib.eml220._nsgroup import OnlineType # {https://eml.ecoinformatics.org/resource-2.2.0}OnlineType
from emllib.eml220._nsgroup import CTD_ANON_65 as CTD_ANON_2 # None
from emllib.eml220._nsgroup import NonEmptyStringType # {https://eml.ecoinformatics.org/resource-2.2.0}NonEmptyStringType
from emllib.eml220._nsgroup import i18nNonEmptyStringType # {https://eml.ecoinformatics.org/resource-2.2.0}i18nNonEmptyStringType
from emllib.eml220._nsgroup import LicenseType # {https://eml.ecoinformatics.org/resource-2.2.0}LicenseType
from emllib.eml220._nsgroup import CTD_ANON_93 as CTD_ANON_3 # None
from emllib.eml220._nsgroup import CTD_ANON_94 as CTD_ANON_4 # None
from emllib.eml220._nsgroup import CTD_ANON_95 as CTD_ANON_5 # None
from emllib.eml220._nsgroup import DistributionType # {https://eml.ecoinformatics.org/resource-2.2.0}DistributionType
from emllib.eml220._nsgroup import ConnectionDefinitionType # {https://eml.ecoinformatics.org/resource-2.2.0}ConnectionDefinitionType
from emllib.eml220._nsgroup import CTD_ANON_96 as CTD_ANON_6 # None
from emllib.eml220._nsgroup import UrlType # {https://eml.ecoinformatics.org/resource-2.2.0}UrlType
from emllib.eml220._nsgroup import ConnectionType # {https://eml.ecoinformatics.org/resource-2.2.0}ConnectionType
from emllib.eml220._nsgroup import CTD_ANON_97 as CTD_ANON_7 # None
from emllib.eml220._nsgroup import CTD_ANON_106 as CTD_ANON_8 # None
