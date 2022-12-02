# ./emllib/eml220/eml220.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:b1e6ff345bc882e2a6794087436ebb2312818ec0
# Generated 2022-06-27 15:56:32.587542 by PyXB version 1.2.6 using Python 3.8.10.final.0
# Namespace https://eml.ecoinformatics.org/eml-2.2.0

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
import pyxb.binding.xml_

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('https://eml.ecoinformatics.org/eml-2.2.0', create_if_missing=True)
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
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 195, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'annotation'), 'annotation', '__httpseml_ecoinformatics_orgeml_2_2_0_CTD_ANON_annotation', True, pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 197, 5), )

    
    annotation = property(__annotation.value, __annotation.set, None, '')

    _ElementMap.update({
        __annotation.name() : __annotation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 288, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 118, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element access uses Python identifier access
    __access = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'access'), 'access', '__httpseml_ecoinformatics_orgeml_2_2_0_CTD_ANON_2_access', False, pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 120, 8), )

    
    access = property(__access.value, __access.set, None, '')

    
    # Element dataset uses Python identifier dataset
    __dataset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dataset'), 'dataset', '__httpseml_ecoinformatics_orgeml_2_2_0_CTD_ANON_2_dataset', False, pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 130, 10), )

    
    dataset = property(__dataset.value, __dataset.set, None, '')

    
    # Element citation uses Python identifier citation
    __citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'citation'), 'citation', '__httpseml_ecoinformatics_orgeml_2_2_0_CTD_ANON_2_citation', False, pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 143, 10), )

    
    citation = property(__citation.value, __citation.set, None, '')

    
    # Element software uses Python identifier software
    __software = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'software'), 'software', '__httpseml_ecoinformatics_orgeml_2_2_0_CTD_ANON_2_software', False, pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 155, 10), )

    
    software = property(__software.value, __software.set, None, '')

    
    # Element protocol uses Python identifier protocol
    __protocol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'protocol'), 'protocol', '__httpseml_ecoinformatics_orgeml_2_2_0_CTD_ANON_2_protocol', False, pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 168, 10), )

    
    protocol = property(__protocol.value, __protocol.set, None, '')

    
    # Element annotations uses Python identifier annotations
    __annotations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'annotations'), 'annotations', '__httpseml_ecoinformatics_orgeml_2_2_0_CTD_ANON_2_annotations', False, pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 181, 2), )

    
    annotations = property(__annotations.value, __annotations.set, None, '')

    
    # Element additionalMetadata uses Python identifier additionalMetadata
    __additionalMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'additionalMetadata'), 'additionalMetadata', '__httpseml_ecoinformatics_orgeml_2_2_0_CTD_ANON_2_additionalMetadata', True, pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 232, 8), )

    
    additionalMetadata = property(__additionalMetadata.value, __additionalMetadata.set, None, '')

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpseml_ecoinformatics_orgeml_2_2_0_CTD_ANON_2_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 352, 6)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute packageId uses Python identifier packageId
    __packageId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'packageId'), 'packageId', '__httpseml_ecoinformatics_orgeml_2_2_0_CTD_ANON_2_packageId', pyxb.binding.datatypes.string, required=True)
    __packageId._DeclarationLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 319, 6)
    __packageId._UseLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 319, 6)
    
    packageId = property(__packageId.value, __packageId.set, None, '')

    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'system'), 'system', '__httpseml_ecoinformatics_orgeml_2_2_0_CTD_ANON_2_system', _ImportedBinding_emllib_eml220__nsgroup.SystemType, required=True)
    __system._DeclarationLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 337, 6)
    __system._UseLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 337, 6)
    
    system = property(__system.value, __system.set, None, None)

    
    # Attribute scope uses Python identifier scope
    __scope = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'scope'), 'scope', '__httpseml_ecoinformatics_orgeml_2_2_0_CTD_ANON_2_scope', _ImportedBinding_emllib_eml220__nsgroup.ScopeType, fixed=True, unicode_default='system')
    __scope._DeclarationLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 338, 6)
    __scope._UseLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 338, 6)
    
    scope = property(__scope.value, __scope.set, None, '')

    _ElementMap.update({
        __access.name() : __access,
        __dataset.name() : __dataset,
        __citation.name() : __citation,
        __software.name() : __software,
        __protocol.name() : __protocol,
        __annotations.name() : __annotations,
        __additionalMetadata.name() : __additionalMetadata
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __packageId.name() : __packageId,
        __system.name() : __system,
        __scope.name() : __scope
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 246, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element describes uses Python identifier describes
    __describes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'describes'), 'describes', '__httpseml_ecoinformatics_orgeml_2_2_0_CTD_ANON_3_describes', True, pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 248, 14), )

    
    describes = property(__describes.value, __describes.set, None, '')

    
    # Element metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'metadata'), 'metadata', '__httpseml_ecoinformatics_orgeml_2_2_0_CTD_ANON_3_metadata', False, pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 265, 14), )

    
    metadata = property(__metadata.value, __metadata.set, None, '')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpseml_ecoinformatics_orgeml_2_2_0_CTD_ANON_3_id', _ImportedBinding_emllib_eml220__nsgroup.IDType)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 315, 12)
    __id._UseLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 315, 12)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __describes.name() : __describes,
        __metadata.name() : __metadata
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (_ImportedBinding_emllib_eml220__nsgroup.SemanticAnnotation):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 221, 6)
    _ElementMap = _ImportedBinding_emllib_eml220__nsgroup.SemanticAnnotation._ElementMap.copy()
    _AttributeMap = _ImportedBinding_emllib_eml220__nsgroup.SemanticAnnotation._AttributeMap.copy()
    # Base type is _ImportedBinding_emllib_eml220__nsgroup.SemanticAnnotation
    
    # Element propertyURI (propertyURI) inherited from {https://eml.ecoinformatics.org/semantics-2.2.0}SemanticAnnotation
    
    # Element valueURI (valueURI) inherited from {https://eml.ecoinformatics.org/semantics-2.2.0}SemanticAnnotation
    
    # Attribute references uses Python identifier references
    __references = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'references'), 'references', '__httpseml_ecoinformatics_orgeml_2_2_0_CTD_ANON_4_references', pyxb.binding.datatypes.string, required=True)
    __references._DeclarationLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 224, 9)
    __references._UseLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 224, 9)
    
    references = property(__references.value, __references.set, None, None)

    
    # Attribute id inherited from {https://eml.ecoinformatics.org/semantics-2.2.0}SemanticAnnotation
    
    # Attribute system inherited from {https://eml.ecoinformatics.org/semantics-2.2.0}SemanticAnnotation
    
    # Attribute scope inherited from {https://eml.ecoinformatics.org/semantics-2.2.0}SemanticAnnotation
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __references.name() : __references
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


eml = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eml'), CTD_ANON_2, documentation='', location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 98, 2))
Namespace.addCategoryObject('elementBinding', eml.name().localName(), eml)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'annotation'), CTD_ANON_4, scope=CTD_ANON, documentation='', location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 197, 5)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'annotation')), pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 197, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 290, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'access'), _ImportedBinding_emllib_eml220__nsgroup.AccessType, scope=CTD_ANON_2, documentation='', location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 120, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dataset'), _ImportedBinding_emllib_eml220__nsgroup.DatasetType, scope=CTD_ANON_2, documentation='', location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 130, 10)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'citation'), _ImportedBinding_emllib_eml220__nsgroup.CitationType, scope=CTD_ANON_2, documentation='', location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 143, 10)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'software'), _ImportedBinding_emllib_eml220__nsgroup.SoftwareType, scope=CTD_ANON_2, documentation='', location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 155, 10)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'protocol'), _ImportedBinding_emllib_eml220__nsgroup.ProtocolType, scope=CTD_ANON_2, documentation='', location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 168, 10)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'annotations'), CTD_ANON, scope=CTD_ANON_2, documentation='', location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 181, 2)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'additionalMetadata'), CTD_ANON_3, scope=CTD_ANON_2, documentation='', location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 232, 8)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 120, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 181, 2))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 232, 8))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'access')), pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 120, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'dataset')), pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 130, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'citation')), pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 143, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'software')), pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 155, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'protocol')), pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 168, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'annotations')), pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 181, 2))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'additionalMetadata')), pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 232, 8))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'describes'), _ImportedBinding_emllib_eml220__nsgroup.NonEmptyStringType, scope=CTD_ANON_3, documentation='', location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 248, 14)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'metadata'), CTD_ANON_, scope=CTD_ANON_3, documentation='', location=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 265, 14)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 248, 14))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'describes')), pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 248, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'metadata')), pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml.xsd', 265, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'propertyURI')), pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-semantics.xsd', 71, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'valueURI')), pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-semantics.xsd', 141, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()

