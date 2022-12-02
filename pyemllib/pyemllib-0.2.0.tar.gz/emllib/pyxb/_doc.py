# ./emllib/eml220/_doc.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:3829be4b409d48694a2d078861caa4f572af9024
# Generated 2022-06-27 15:56:32.587421 by PyXB version 1.2.6 using Python 3.8.10.final.0
# Namespace https://eml.ecoinformatics.org/documentation-2.2.0 [xmlns:doc]

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
import pyxb.binding.datatypes
import emllib.eml220._nsgroup as _ImportedBinding_emllib_eml220__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('https://eml.ecoinformatics.org/documentation-2.2.0', create_if_missing=True)
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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 46, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {https://eml.ecoinformatics.org/documentation-2.2.0}moduleName uses Python identifier moduleName
    __moduleName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'moduleName'), 'moduleName', '__httpseml_ecoinformatics_orgdocumentation_2_2_0_CTD_ANON_httpseml_ecoinformatics_orgdocumentation_2_2_0moduleName', False, pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 48, 8), )

    
    moduleName = property(__moduleName.value, __moduleName.set, None, None)

    
    # Element {https://eml.ecoinformatics.org/documentation-2.2.0}moduleDescription uses Python identifier moduleDescription
    __moduleDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'moduleDescription'), 'moduleDescription', '__httpseml_ecoinformatics_orgdocumentation_2_2_0_CTD_ANON_httpseml_ecoinformatics_orgdocumentation_2_2_0moduleDescription', False, pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 49, 8), )

    
    moduleDescription = property(__moduleDescription.value, __moduleDescription.set, None, None)

    
    # Element {https://eml.ecoinformatics.org/documentation-2.2.0}recommendedUsage uses Python identifier recommendedUsage
    __recommendedUsage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recommendedUsage'), 'recommendedUsage', '__httpseml_ecoinformatics_orgdocumentation_2_2_0_CTD_ANON_httpseml_ecoinformatics_orgdocumentation_2_2_0recommendedUsage', False, pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 50, 8), )

    
    recommendedUsage = property(__recommendedUsage.value, __recommendedUsage.set, None, None)

    
    # Element {https://eml.ecoinformatics.org/documentation-2.2.0}standAlone uses Python identifier standAlone
    __standAlone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'standAlone'), 'standAlone', '__httpseml_ecoinformatics_orgdocumentation_2_2_0_CTD_ANON_httpseml_ecoinformatics_orgdocumentation_2_2_0standAlone', False, pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 51, 8), )

    
    standAlone = property(__standAlone.value, __standAlone.set, None, None)

    _ElementMap.update({
        __moduleName.name() : __moduleName,
        __moduleDescription.name() : __moduleDescription,
        __recommendedUsage.name() : __recommendedUsage,
        __standAlone.name() : __standAlone
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


tooltip = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tooltip'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 55, 2))
Namespace.addCategoryObject('elementBinding', tooltip.name().localName(), tooltip)

summary = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'summary'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 56, 2))
Namespace.addCategoryObject('elementBinding', summary.name().localName(), summary)

lineage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lineage'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 59, 2))
Namespace.addCategoryObject('elementBinding', lineage.name().localName(), lineage)

module = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'module'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 60, 2))
Namespace.addCategoryObject('elementBinding', module.name().localName(), module)

moduleDocs = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'moduleDocs'), CTD_ANON, location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 45, 2))
Namespace.addCategoryObject('elementBinding', moduleDocs.name().localName(), moduleDocs)

description = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), _ImportedBinding_emllib_eml220__nsgroup.TextType, location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 57, 2))
Namespace.addCategoryObject('elementBinding', description.name().localName(), description)

example = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'example'), _ImportedBinding_emllib_eml220__nsgroup.TextType, location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 58, 2))
Namespace.addCategoryObject('elementBinding', example.name().localName(), example)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'moduleName'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 48, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'moduleDescription'), _ImportedBinding_emllib_eml220__nsgroup.TextType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 49, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recommendedUsage'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 50, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'standAlone'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 51, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleName')), pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 48, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleDescription')), pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 49, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recommendedUsage')), pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 50, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'standAlone')), pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-documentation.xsd', 51, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()

