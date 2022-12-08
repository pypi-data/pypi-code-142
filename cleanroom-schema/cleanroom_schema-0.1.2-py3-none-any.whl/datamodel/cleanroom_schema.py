# Auto generated from cleanroom_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-12-07T19:37:37
# Schema: cleanroom-schema
#
# id: https://w3id.org/microbiomedata/cleanroom-schema
# description: Cleanroom reboot of NMDC schema
# license: MIT

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'https://purl.obolibrary.org/obo/BFO_')
GOLD = CurieNamespace('GOLD', 'http://identifiers.org/gold/')
OBI = CurieNamespace('OBI', 'https://purl.obolibrary.org/obo/OBI_')
OBO = CurieNamespace('OBO', 'https://purl.obolibrary.org/obo/')
BIOSAMPLE_RELATIONS = CurieNamespace('biosample_relations', 'https://example.com/biosample_relations')
CLEANROOM_SCHEMA = CurieNamespace('cleanroom_schema', 'https://example.com/biosample_relations/cleanroom-schema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
SCHEMA = CurieNamespace('schema', 'https://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CLEANROOM_SCHEMA


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class MaterialEntityId(NamedThingId):
    pass


class ImmaterialEntityId(NamedThingId):
    pass


class SpecimenId(MaterialEntityId):
    pass


class BiosampleId(NamedThingId):
    pass


class MaterialSampleId(SpecimenId):
    pass


class SiteId(ImmaterialEntityId):
    pass


class FieldResearchSiteId(SiteId):
    pass


class PlannedProcessId(NamedThingId):
    pass


class CollectingBiosamplesFromSiteId(PlannedProcessId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = CLEANROOM_SCHEMA.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class MaterialEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BFO["0000040"]
    class_class_curie: ClassVar[str] = "BFO:0000040"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = CLEANROOM_SCHEMA.MaterialEntity

    id: Union[str, MaterialEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ImmaterialEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BFO["0000141"]
    class_class_curie: ClassVar[str] = "BFO:0000141"
    class_name: ClassVar[str] = "ImmaterialEntity"
    class_model_uri: ClassVar[URIRef] = CLEANROOM_SCHEMA.ImmaterialEntity

    id: Union[str, ImmaterialEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImmaterialEntityId):
            self.id = ImmaterialEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Specimen(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0100051"]
    class_class_curie: ClassVar[str] = "OBI:0100051"
    class_name: ClassVar[str] = "Specimen"
    class_model_uri: ClassVar[URIRef] = CLEANROOM_SCHEMA.Specimen

    id: Union[str, SpecimenId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecimenId):
            self.id = SpecimenId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Biosample(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CLEANROOM_SCHEMA.Biosample
    class_class_curie: ClassVar[str] = "cleanroom_schema:Biosample"
    class_name: ClassVar[str] = "Biosample"
    class_model_uri: ClassVar[URIRef] = CLEANROOM_SCHEMA.Biosample

    id: Union[str, BiosampleId] = None
    collected_from: Optional[Union[str, FieldResearchSiteId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiosampleId):
            self.id = BiosampleId(self.id)

        if self.collected_from is not None and not isinstance(self.collected_from, FieldResearchSiteId):
            self.collected_from = FieldResearchSiteId(self.collected_from)

        super().__post_init__(**kwargs)


@dataclass
class MaterialSample(Specimen):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000747"]
    class_class_curie: ClassVar[str] = "OBI:0000747"
    class_name: ClassVar[str] = "MaterialSample"
    class_model_uri: ClassVar[URIRef] = CLEANROOM_SCHEMA.MaterialSample

    id: Union[str, MaterialSampleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialSampleId):
            self.id = MaterialSampleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Site(ImmaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BFO["0000029"]
    class_class_curie: ClassVar[str] = "BFO:0000029"
    class_name: ClassVar[str] = "Site"
    class_model_uri: ClassVar[URIRef] = CLEANROOM_SCHEMA.Site

    id: Union[str, SiteId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SiteId):
            self.id = SiteId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class FieldResearchSite(Site):
    """
    A site, outside of a laboratory, from which biosamples may be collected.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CLEANROOM_SCHEMA.FieldResearchSite
    class_class_curie: ClassVar[str] = "cleanroom_schema:FieldResearchSite"
    class_name: ClassVar[str] = "FieldResearchSite"
    class_model_uri: ClassVar[URIRef] = CLEANROOM_SCHEMA.FieldResearchSite

    id: Union[str, FieldResearchSiteId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FieldResearchSiteId):
            self.id = FieldResearchSiteId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PlannedProcess(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000011"]
    class_class_curie: ClassVar[str] = "OBI:0000011"
    class_name: ClassVar[str] = "PlannedProcess"
    class_model_uri: ClassVar[URIRef] = CLEANROOM_SCHEMA.PlannedProcess

    id: Union[str, PlannedProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlannedProcessId):
            self.id = PlannedProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CollectingBiosamplesFromSite(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000011"]
    class_class_curie: ClassVar[str] = "OBI:0000011"
    class_name: ClassVar[str] = "CollectingBiosamplesFromSite"
    class_model_uri: ClassVar[URIRef] = CLEANROOM_SCHEMA.CollectingBiosamplesFromSite

    id: Union[str, CollectingBiosamplesFromSiteId] = None
    site: Optional[Union[str, FieldResearchSiteId]] = None
    biosamples: Optional[Union[Union[str, BiosampleId], List[Union[str, BiosampleId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CollectingBiosamplesFromSiteId):
            self.id = CollectingBiosamplesFromSiteId(self.id)

        if self.site is not None and not isinstance(self.site, FieldResearchSiteId):
            self.site = FieldResearchSiteId(self.site)

        if not isinstance(self.biosamples, list):
            self.biosamples = [self.biosamples] if self.biosamples is not None else []
        self.biosamples = [v if isinstance(v, BiosampleId) else BiosampleId(v) for v in self.biosamples]

        super().__post_init__(**kwargs)


@dataclass
class ReifiedRelationship(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF.Statement
    class_class_curie: ClassVar[str] = "rdf:Statement"
    class_name: ClassVar[str] = "ReifiedRelationship"
    class_model_uri: ClassVar[URIRef] = CLEANROOM_SCHEMA.ReifiedRelationship

    subject: Optional[Union[str, NamedThingId]] = None
    predicate: Optional[str] = None
    object: Optional[Union[str, NamedThingId]] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.object is not None and not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass
class DataListCollection(YAMLRoot):
    """
    A datastructure that can contain lists of instances from any selected classes in the schema
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CLEANROOM_SCHEMA.DataListCollection
    class_class_curie: ClassVar[str] = "cleanroom_schema:DataListCollection"
    class_name: ClassVar[str] = "DataListCollection"
    class_model_uri: ClassVar[URIRef] = CLEANROOM_SCHEMA.DataListCollection

    biosample_list: Optional[Union[Dict[Union[str, BiosampleId], Union[dict, Biosample]], List[Union[dict, Biosample]]]] = empty_dict()
    frs_list: Optional[Union[Dict[Union[str, FieldResearchSiteId], Union[dict, FieldResearchSite]], List[Union[dict, FieldResearchSite]]]] = empty_dict()
    cbfs_list: Optional[Union[Dict[Union[str, CollectingBiosamplesFromSiteId], Union[dict, CollectingBiosamplesFromSite]], List[Union[dict, CollectingBiosamplesFromSite]]]] = empty_dict()
    relations_list: Optional[Union[Union[dict, ReifiedRelationship], List[Union[dict, ReifiedRelationship]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="biosample_list", slot_type=Biosample, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="frs_list", slot_type=FieldResearchSite, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="cbfs_list", slot_type=CollectingBiosamplesFromSite, key_name="id", keyed=True)

        if not isinstance(self.relations_list, list):
            self.relations_list = [self.relations_list] if self.relations_list is not None else []
        self.relations_list = [v if isinstance(v, ReifiedRelationship) else ReifiedRelationship(**as_dict(v)) for v in self.relations_list]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=CLEANROOM_SCHEMA.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=CLEANROOM_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=CLEANROOM_SCHEMA.description, domain=None, range=Optional[str])

slots.type = Slot(uri=CLEANROOM_SCHEMA.type, name="type", curie=CLEANROOM_SCHEMA.curie('type'),
                   model_uri=CLEANROOM_SCHEMA.type, domain=None, range=Optional[str])

slots.collected_from = Slot(uri=CLEANROOM_SCHEMA.collected_from, name="collected_from", curie=CLEANROOM_SCHEMA.curie('collected_from'),
                   model_uri=CLEANROOM_SCHEMA.collected_from, domain=Biosample, range=Optional[Union[str, FieldResearchSiteId]])

slots.biosamples = Slot(uri=CLEANROOM_SCHEMA.biosamples, name="biosamples", curie=CLEANROOM_SCHEMA.curie('biosamples'),
                   model_uri=CLEANROOM_SCHEMA.biosamples, domain=None, range=Optional[Union[Union[str, BiosampleId], List[Union[str, BiosampleId]]]])

slots.site = Slot(uri=CLEANROOM_SCHEMA.site, name="site", curie=CLEANROOM_SCHEMA.curie('site'),
                   model_uri=CLEANROOM_SCHEMA.site, domain=None, range=Optional[Union[str, FieldResearchSiteId]])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=CLEANROOM_SCHEMA.subject, domain=None, range=Optional[Union[str, NamedThingId]])

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=CLEANROOM_SCHEMA.predicate, domain=None, range=Optional[str])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=CLEANROOM_SCHEMA.object, domain=None, range=Optional[Union[str, NamedThingId]])

slots.notes = Slot(uri=CLEANROOM_SCHEMA.notes, name="notes", curie=CLEANROOM_SCHEMA.curie('notes'),
                   model_uri=CLEANROOM_SCHEMA.notes, domain=None, range=Optional[str])

slots.dataListCollection__biosample_list = Slot(uri=CLEANROOM_SCHEMA.biosample_list, name="dataListCollection__biosample_list", curie=CLEANROOM_SCHEMA.curie('biosample_list'),
                   model_uri=CLEANROOM_SCHEMA.dataListCollection__biosample_list, domain=None, range=Optional[Union[Dict[Union[str, BiosampleId], Union[dict, Biosample]], List[Union[dict, Biosample]]]])

slots.dataListCollection__frs_list = Slot(uri=CLEANROOM_SCHEMA.frs_list, name="dataListCollection__frs_list", curie=CLEANROOM_SCHEMA.curie('frs_list'),
                   model_uri=CLEANROOM_SCHEMA.dataListCollection__frs_list, domain=None, range=Optional[Union[Dict[Union[str, FieldResearchSiteId], Union[dict, FieldResearchSite]], List[Union[dict, FieldResearchSite]]]])

slots.dataListCollection__cbfs_list = Slot(uri=CLEANROOM_SCHEMA.cbfs_list, name="dataListCollection__cbfs_list", curie=CLEANROOM_SCHEMA.curie('cbfs_list'),
                   model_uri=CLEANROOM_SCHEMA.dataListCollection__cbfs_list, domain=None, range=Optional[Union[Dict[Union[str, CollectingBiosamplesFromSiteId], Union[dict, CollectingBiosamplesFromSite]], List[Union[dict, CollectingBiosamplesFromSite]]]])

slots.dataListCollection__relations_list = Slot(uri=CLEANROOM_SCHEMA.relations_list, name="dataListCollection__relations_list", curie=CLEANROOM_SCHEMA.curie('relations_list'),
                   model_uri=CLEANROOM_SCHEMA.dataListCollection__relations_list, domain=None, range=Optional[Union[Union[dict, ReifiedRelationship], List[Union[dict, ReifiedRelationship]]]])