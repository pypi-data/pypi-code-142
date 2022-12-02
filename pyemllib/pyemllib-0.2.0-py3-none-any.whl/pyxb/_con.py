# ./emllib/eml220/_con.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:301c6c0904e7aa72110d44392a54f6fa61d59fdd
# Generated 2022-06-27 15:56:32.585469 by PyXB version 1.2.6 using Python 3.8.10.final.0
# Namespace https://eml.ecoinformatics.org/constraint-2.2.0 [xmlns:con]

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
Namespace = pyxb.namespace.NamespaceForURI('https://eml.ecoinformatics.org/constraint-2.2.0', create_if_missing=True)
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

from emllib.eml220._nsgroup import CTD_ANON_19 as CTD_ANON # None
from emllib.eml220._nsgroup import CTD_ANON_20 as CTD_ANON_ # None
from emllib.eml220._nsgroup import CTD_ANON_21 as CTD_ANON_2 # None
from emllib.eml220._nsgroup import CTD_ANON_22 as CTD_ANON_3 # None
from emllib.eml220._nsgroup import CTD_ANON_23 as CTD_ANON_4 # None
from emllib.eml220._nsgroup import CTD_ANON_24 as CTD_ANON_5 # None
from emllib.eml220._nsgroup import CTD_ANON_25 as CTD_ANON_6 # None
from emllib.eml220._nsgroup import CTD_ANON_26 as CTD_ANON_7 # None
from emllib.eml220._nsgroup import CTD_ANON_27 as CTD_ANON_8 # None
from emllib.eml220._nsgroup import CTD_ANON_28 as CTD_ANON_9 # None
from emllib.eml220._nsgroup import STD_ANON_4 as STD_ANON # None
from emllib.eml220._nsgroup import CTD_ANON_29 as CTD_ANON_10 # None
from emllib.eml220._nsgroup import STD_ANON_5 as STD_ANON_ # None
from emllib.eml220._nsgroup import CTD_ANON_30 as CTD_ANON_11 # None
from emllib.eml220._nsgroup import STD_ANON_6 as STD_ANON_2 # None
from emllib.eml220._nsgroup import ConstraintType # {https://eml.ecoinformatics.org/constraint-2.2.0}ConstraintType
from emllib.eml220._nsgroup import CardinalityChildOccurancesType # {https://eml.ecoinformatics.org/constraint-2.2.0}CardinalityChildOccurancesType
