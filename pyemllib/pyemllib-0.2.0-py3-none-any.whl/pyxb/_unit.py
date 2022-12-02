# ./emllib/eml220/_unit.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:f374ec92bd81d21148c6a930b0dee591e9a76a6f
# Generated 2022-06-27 15:56:32.583142 by PyXB version 1.2.6 using Python 3.8.10.final.0
# Namespace https://eml.ecoinformatics.org/units-2.2.0 [xmlns:unit]

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

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('https://eml.ecoinformatics.org/units-2.2.0', create_if_missing=True)
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


# Atomic simple type: {https://eml.ecoinformatics.org/units-2.2.0}LengthUnitType
class LengthUnitType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LengthUnitType')
    _XSDLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-unitTypeDefinitions.xsd', 56, 2)
    _Documentation = ''
LengthUnitType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LengthUnitType, enum_prefix=None)
LengthUnitType.meter = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='meter', tag='meter')
LengthUnitType.nanometer = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='nanometer', tag='nanometer')
LengthUnitType.micrometer = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='micrometer', tag='micrometer')
LengthUnitType.micron = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='micron', tag='micron')
LengthUnitType.millimeter = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='millimeter', tag='millimeter')
LengthUnitType.centimeter = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='centimeter', tag='centimeter')
LengthUnitType.decimeter = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='decimeter', tag='decimeter')
LengthUnitType.dekameter = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='dekameter', tag='dekameter')
LengthUnitType.hectometer = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='hectometer', tag='hectometer')
LengthUnitType.kilometer = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='kilometer', tag='kilometer')
LengthUnitType.megameter = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='megameter', tag='megameter')
LengthUnitType.angstrom = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='angstrom', tag='angstrom')
LengthUnitType.inch = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='inch', tag='inch')
LengthUnitType.Foot_US = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='Foot_US', tag='Foot_US')
LengthUnitType.foot = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='foot', tag='foot')
LengthUnitType.Foot_Gold_Coast = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='Foot_Gold_Coast', tag='Foot_Gold_Coast')
LengthUnitType.fathom = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='fathom', tag='fathom')
LengthUnitType.nauticalMile = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='nauticalMile', tag='nauticalMile')
LengthUnitType.yard = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='yard', tag='yard')
LengthUnitType.Yard_Indian = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='Yard_Indian', tag='Yard_Indian')
LengthUnitType.Link_Clarke = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='Link_Clarke', tag='Link_Clarke')
LengthUnitType.Yard_Sears = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='Yard_Sears', tag='Yard_Sears')
LengthUnitType.mile = LengthUnitType._CF_enumeration.addEnumeration(unicode_value='mile', tag='mile')
LengthUnitType._InitializeFacetMap(LengthUnitType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LengthUnitType', LengthUnitType)
_module_typeBindings.LengthUnitType = LengthUnitType

# Atomic simple type: {https://eml.ecoinformatics.org/units-2.2.0}MassUnitType
class MassUnitType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MassUnitType')
    _XSDLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-unitTypeDefinitions.xsd', 102, 2)
    _Documentation = ''
MassUnitType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MassUnitType, enum_prefix=None)
MassUnitType.kilogram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='kilogram', tag='kilogram')
MassUnitType.nanogram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='nanogram', tag='nanogram')
MassUnitType.microgram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='microgram', tag='microgram')
MassUnitType.milligram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='milligram', tag='milligram')
MassUnitType.centigram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='centigram', tag='centigram')
MassUnitType.decigram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='decigram', tag='decigram')
MassUnitType.gram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='gram', tag='gram')
MassUnitType.dekagram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='dekagram', tag='dekagram')
MassUnitType.hectogram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='hectogram', tag='hectogram')
MassUnitType.megagram = MassUnitType._CF_enumeration.addEnumeration(unicode_value='megagram', tag='megagram')
MassUnitType.tonne = MassUnitType._CF_enumeration.addEnumeration(unicode_value='tonne', tag='tonne')
MassUnitType.pound = MassUnitType._CF_enumeration.addEnumeration(unicode_value='pound', tag='pound')
MassUnitType.ton = MassUnitType._CF_enumeration.addEnumeration(unicode_value='ton', tag='ton')
MassUnitType._InitializeFacetMap(MassUnitType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MassUnitType', MassUnitType)
_module_typeBindings.MassUnitType = MassUnitType

# Atomic simple type: {https://eml.ecoinformatics.org/units-2.2.0}otherUnitType
class otherUnitType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'otherUnitType')
    _XSDLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-unitTypeDefinitions.xsd', 138, 2)
    _Documentation = ''
otherUnitType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=otherUnitType, enum_prefix=None)
otherUnitType.acre = otherUnitType._CF_enumeration.addEnumeration(unicode_value='acre', tag='acre')
otherUnitType.ampere = otherUnitType._CF_enumeration.addEnumeration(unicode_value='ampere', tag='ampere')
otherUnitType.amperePerMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='amperePerMeter', tag='amperePerMeter')
otherUnitType.amperePerMeterSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='amperePerMeterSquared', tag='amperePerMeterSquared')
otherUnitType.amperePerSquareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='amperePerSquareMeter', tag='amperePerSquareMeter')
otherUnitType.are = otherUnitType._CF_enumeration.addEnumeration(unicode_value='are', tag='are')
otherUnitType.atmosphere = otherUnitType._CF_enumeration.addEnumeration(unicode_value='atmosphere', tag='atmosphere')
otherUnitType.bar = otherUnitType._CF_enumeration.addEnumeration(unicode_value='bar', tag='bar')
otherUnitType.becquerel = otherUnitType._CF_enumeration.addEnumeration(unicode_value='becquerel', tag='becquerel')
otherUnitType.britishThermalUnit = otherUnitType._CF_enumeration.addEnumeration(unicode_value='britishThermalUnit', tag='britishThermalUnit')
otherUnitType.bushel = otherUnitType._CF_enumeration.addEnumeration(unicode_value='bushel', tag='bushel')
otherUnitType.bushelPerAcre = otherUnitType._CF_enumeration.addEnumeration(unicode_value='bushelPerAcre', tag='bushelPerAcre')
otherUnitType.bushelsPerAcre = otherUnitType._CF_enumeration.addEnumeration(unicode_value='bushelsPerAcre', tag='bushelsPerAcre')
otherUnitType.calorie = otherUnitType._CF_enumeration.addEnumeration(unicode_value='calorie', tag='calorie')
otherUnitType.candela = otherUnitType._CF_enumeration.addEnumeration(unicode_value='candela', tag='candela')
otherUnitType.candelaPerMeterSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='candelaPerMeterSquared', tag='candelaPerMeterSquared')
otherUnitType.candelaPerSquareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='candelaPerSquareMeter', tag='candelaPerSquareMeter')
otherUnitType.celsius = otherUnitType._CF_enumeration.addEnumeration(unicode_value='celsius', tag='celsius')
otherUnitType.centimeterCubed = otherUnitType._CF_enumeration.addEnumeration(unicode_value='centimeterCubed', tag='centimeterCubed')
otherUnitType.centimeterPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='centimeterPerSecond', tag='centimeterPerSecond')
otherUnitType.centimeterPerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='centimeterPerYear', tag='centimeterPerYear')
otherUnitType.centimeterSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='centimeterSquared', tag='centimeterSquared')
otherUnitType.centimetersPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='centimetersPerSecond', tag='centimetersPerSecond')
otherUnitType.centisecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='centisecond', tag='centisecond')
otherUnitType.coulomb = otherUnitType._CF_enumeration.addEnumeration(unicode_value='coulomb', tag='coulomb')
otherUnitType.cubicCentimetersPerCubicCentimeters = otherUnitType._CF_enumeration.addEnumeration(unicode_value='cubicCentimetersPerCubicCentimeters', tag='cubicCentimetersPerCubicCentimeters')
otherUnitType.cubicFeetPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='cubicFeetPerSecond', tag='cubicFeetPerSecond')
otherUnitType.cubicInch = otherUnitType._CF_enumeration.addEnumeration(unicode_value='cubicInch', tag='cubicInch')
otherUnitType.cubicMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='cubicMeter', tag='cubicMeter')
otherUnitType.cubicMeterPerKilogram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='cubicMeterPerKilogram', tag='cubicMeterPerKilogram')
otherUnitType.cubicMetersPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='cubicMetersPerSecond', tag='cubicMetersPerSecond')
otherUnitType.cubicMicrometersPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='cubicMicrometersPerGram', tag='cubicMicrometersPerGram')
otherUnitType.decibar = otherUnitType._CF_enumeration.addEnumeration(unicode_value='decibar', tag='decibar')
otherUnitType.decisecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='decisecond', tag='decisecond')
otherUnitType.dekasecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='dekasecond', tag='dekasecond')
otherUnitType.dimensionless = otherUnitType._CF_enumeration.addEnumeration(unicode_value='dimensionless', tag='dimensionless')
otherUnitType.equivalentPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='equivalentPerLiter', tag='equivalentPerLiter')
otherUnitType.fahrenheit = otherUnitType._CF_enumeration.addEnumeration(unicode_value='fahrenheit', tag='fahrenheit')
otherUnitType.farad = otherUnitType._CF_enumeration.addEnumeration(unicode_value='farad', tag='farad')
otherUnitType.feetPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='feetPerDay', tag='feetPerDay')
otherUnitType.feetPerHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value='feetPerHour', tag='feetPerHour')
otherUnitType.feetPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='feetPerSecond', tag='feetPerSecond')
otherUnitType.feetSquaredPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='feetSquaredPerDay', tag='feetSquaredPerDay')
otherUnitType.footCubedPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='footCubedPerSecond', tag='footCubedPerSecond')
otherUnitType.footPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='footPerDay', tag='footPerDay')
otherUnitType.footPerHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value='footPerHour', tag='footPerHour')
otherUnitType.footPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='footPerSecond', tag='footPerSecond')
otherUnitType.footPound = otherUnitType._CF_enumeration.addEnumeration(unicode_value='footPound', tag='footPound')
otherUnitType.footSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='footSquared', tag='footSquared')
otherUnitType.footSquaredPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='footSquaredPerDay', tag='footSquaredPerDay')
otherUnitType.gallon = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gallon', tag='gallon')
otherUnitType.gramPerCentimeterCubed = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramPerCentimeterCubed', tag='gramPerCentimeterCubed')
otherUnitType.gramPerCentimeterSquaredPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramPerCentimeterSquaredPerSecond', tag='gramPerCentimeterSquaredPerSecond')
otherUnitType.gramPerDayPerHectare = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramPerDayPerHectare', tag='gramPerDayPerHectare')
otherUnitType.gramPerDayPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramPerDayPerLiter', tag='gramPerDayPerLiter')
otherUnitType.gramPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramPerGram', tag='gramPerGram')
otherUnitType.gramPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramPerLiter', tag='gramPerLiter')
otherUnitType.gramPerMeterSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramPerMeterSquared', tag='gramPerMeterSquared')
otherUnitType.gramPerMeterSquaredPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramPerMeterSquaredPerDay', tag='gramPerMeterSquaredPerDay')
otherUnitType.gramPerMeterSquaredPerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramPerMeterSquaredPerYear', tag='gramPerMeterSquaredPerYear')
otherUnitType.gramPerMilliliter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramPerMilliliter', tag='gramPerMilliliter')
otherUnitType.gramPerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramPerYear', tag='gramPerYear')
otherUnitType.gramPercentimeterSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramPercentimeterSquared', tag='gramPercentimeterSquared')
otherUnitType.gramsPerCentimeterSquaredPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerCentimeterSquaredPerSecond', tag='gramsPerCentimeterSquaredPerSecond')
otherUnitType.gramsPerCubicCentimeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerCubicCentimeter', tag='gramsPerCubicCentimeter')
otherUnitType.gramsPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerGram', tag='gramsPerGram')
otherUnitType.gramsPerHectarePerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerHectarePerDay', tag='gramsPerHectarePerDay')
otherUnitType.gramsPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerLiter', tag='gramsPerLiter')
otherUnitType.gramsPerLiterPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerLiterPerDay', tag='gramsPerLiterPerDay')
otherUnitType.gramsPerMeterSquaredPerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerMeterSquaredPerYear', tag='gramsPerMeterSquaredPerYear')
otherUnitType.gramsPerMilliliter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerMilliliter', tag='gramsPerMilliliter')
otherUnitType.gramsPerSquareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerSquareMeter', tag='gramsPerSquareMeter')
otherUnitType.gramsPerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gramsPerYear', tag='gramsPerYear')
otherUnitType.gray = otherUnitType._CF_enumeration.addEnumeration(unicode_value='gray', tag='gray')
otherUnitType.hectare = otherUnitType._CF_enumeration.addEnumeration(unicode_value='hectare', tag='hectare')
otherUnitType.hectopascal = otherUnitType._CF_enumeration.addEnumeration(unicode_value='hectopascal', tag='hectopascal')
otherUnitType.hectosecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='hectosecond', tag='hectosecond')
otherUnitType.henry = otherUnitType._CF_enumeration.addEnumeration(unicode_value='henry', tag='henry')
otherUnitType.hertz = otherUnitType._CF_enumeration.addEnumeration(unicode_value='hertz', tag='hertz')
otherUnitType.hour = otherUnitType._CF_enumeration.addEnumeration(unicode_value='hour', tag='hour')
otherUnitType.inchCubed = otherUnitType._CF_enumeration.addEnumeration(unicode_value='inchCubed', tag='inchCubed')
otherUnitType.inchPerHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value='inchPerHour', tag='inchPerHour')
otherUnitType.inverseCentimeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='inverseCentimeter', tag='inverseCentimeter')
otherUnitType.inverseMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='inverseMeter', tag='inverseMeter')
otherUnitType.joule = otherUnitType._CF_enumeration.addEnumeration(unicode_value='joule', tag='joule')
otherUnitType.katal = otherUnitType._CF_enumeration.addEnumeration(unicode_value='katal', tag='katal')
otherUnitType.kelvin = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kelvin', tag='kelvin')
otherUnitType.kilogramPerCubicMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramPerCubicMeter', tag='kilogramPerCubicMeter')
otherUnitType.kilogramPerHectare = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramPerHectare', tag='kilogramPerHectare')
otherUnitType.kilogramPerHectarePerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramPerHectarePerYear', tag='kilogramPerHectarePerYear')
otherUnitType.kilogramPerMeterCubed = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramPerMeterCubed', tag='kilogramPerMeterCubed')
otherUnitType.kilogramPerMeterSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramPerMeterSquared', tag='kilogramPerMeterSquared')
otherUnitType.kilogramPerMeterSquaredPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramPerMeterSquaredPerDay', tag='kilogramPerMeterSquaredPerDay')
otherUnitType.kilogramPerMeterSquaredPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramPerMeterSquaredPerSecond', tag='kilogramPerMeterSquaredPerSecond')
otherUnitType.kilogramPerMeterSquaredPerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramPerMeterSquaredPerYear', tag='kilogramPerMeterSquaredPerYear')
otherUnitType.kilogramPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramPerSecond', tag='kilogramPerSecond')
otherUnitType.kilogramsPerHectare = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramsPerHectare', tag='kilogramsPerHectare')
otherUnitType.kilogramsPerHectarePerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramsPerHectarePerYear', tag='kilogramsPerHectarePerYear')
otherUnitType.kilogramsPerMeterSquaredPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramsPerMeterSquaredPerSecond', tag='kilogramsPerMeterSquaredPerSecond')
otherUnitType.kilogramsPerMeterSquaredPerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramsPerMeterSquaredPerYear', tag='kilogramsPerMeterSquaredPerYear')
otherUnitType.kilogramsPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramsPerSecond', tag='kilogramsPerSecond')
otherUnitType.kilogramsPerSquareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilogramsPerSquareMeter', tag='kilogramsPerSquareMeter')
otherUnitType.kilohertz = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilohertz', tag='kilohertz')
otherUnitType.kiloliter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kiloliter', tag='kiloliter')
otherUnitType.kilometerPerHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilometerPerHour', tag='kilometerPerHour')
otherUnitType.kilometerSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilometerSquared', tag='kilometerSquared')
otherUnitType.kilometersPerHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilometersPerHour', tag='kilometersPerHour')
otherUnitType.kilopascal = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilopascal', tag='kilopascal')
otherUnitType.kilosecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilosecond', tag='kilosecond')
otherUnitType.kilovolt = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilovolt', tag='kilovolt')
otherUnitType.kilowatt = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilowatt', tag='kilowatt')
otherUnitType.kilowattPerMeterSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='kilowattPerMeterSquared', tag='kilowattPerMeterSquared')
otherUnitType.knot = otherUnitType._CF_enumeration.addEnumeration(unicode_value='knot', tag='knot')
otherUnitType.knots = otherUnitType._CF_enumeration.addEnumeration(unicode_value='knots', tag='knots')
otherUnitType.langley = otherUnitType._CF_enumeration.addEnumeration(unicode_value='langley', tag='langley')
otherUnitType.langleyPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='langleyPerDay', tag='langleyPerDay')
otherUnitType.liter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='liter', tag='liter')
otherUnitType.literPerHectare = otherUnitType._CF_enumeration.addEnumeration(unicode_value='literPerHectare', tag='literPerHectare')
otherUnitType.literPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='literPerLiter', tag='literPerLiter')
otherUnitType.literPerMeterSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='literPerMeterSquared', tag='literPerMeterSquared')
otherUnitType.literPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='literPerSecond', tag='literPerSecond')
otherUnitType.litersPerHectare = otherUnitType._CF_enumeration.addEnumeration(unicode_value='litersPerHectare', tag='litersPerHectare')
otherUnitType.litersPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='litersPerSecond', tag='litersPerSecond')
otherUnitType.litersPerSquareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='litersPerSquareMeter', tag='litersPerSquareMeter')
otherUnitType.lumen = otherUnitType._CF_enumeration.addEnumeration(unicode_value='lumen', tag='lumen')
otherUnitType.lux = otherUnitType._CF_enumeration.addEnumeration(unicode_value='lux', tag='lux')
otherUnitType.megagramPerMeterCubed = otherUnitType._CF_enumeration.addEnumeration(unicode_value='megagramPerMeterCubed', tag='megagramPerMeterCubed')
otherUnitType.megahertz = otherUnitType._CF_enumeration.addEnumeration(unicode_value='megahertz', tag='megahertz')
otherUnitType.megajoulePerMeterSquaredPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='megajoulePerMeterSquaredPerDay', tag='megajoulePerMeterSquaredPerDay')
otherUnitType.megapascal = otherUnitType._CF_enumeration.addEnumeration(unicode_value='megapascal', tag='megapascal')
otherUnitType.megasecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='megasecond', tag='megasecond')
otherUnitType.megavolt = otherUnitType._CF_enumeration.addEnumeration(unicode_value='megavolt', tag='megavolt')
otherUnitType.megawatt = otherUnitType._CF_enumeration.addEnumeration(unicode_value='megawatt', tag='megawatt')
otherUnitType.meterCubed = otherUnitType._CF_enumeration.addEnumeration(unicode_value='meterCubed', tag='meterCubed')
otherUnitType.meterCubedPerHectare = otherUnitType._CF_enumeration.addEnumeration(unicode_value='meterCubedPerHectare', tag='meterCubedPerHectare')
otherUnitType.meterCubedPerKilogram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='meterCubedPerKilogram', tag='meterCubedPerKilogram')
otherUnitType.meterCubedPerMeterCubed = otherUnitType._CF_enumeration.addEnumeration(unicode_value='meterCubedPerMeterCubed', tag='meterCubedPerMeterCubed')
otherUnitType.meterCubedPerMeterSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='meterCubedPerMeterSquared', tag='meterCubedPerMeterSquared')
otherUnitType.meterCubedPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='meterCubedPerSecond', tag='meterCubedPerSecond')
otherUnitType.meterPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='meterPerDay', tag='meterPerDay')
otherUnitType.meterPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='meterPerGram', tag='meterPerGram')
otherUnitType.meterPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='meterPerSecond', tag='meterPerSecond')
otherUnitType.meterPerSecondSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='meterPerSecondSquared', tag='meterPerSecondSquared')
otherUnitType.meterSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='meterSquared', tag='meterSquared')
otherUnitType.meterSquaredPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='meterSquaredPerDay', tag='meterSquaredPerDay')
otherUnitType.meterSquaredPerHectare = otherUnitType._CF_enumeration.addEnumeration(unicode_value='meterSquaredPerHectare', tag='meterSquaredPerHectare')
otherUnitType.meterSquaredPerKilogram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='meterSquaredPerKilogram', tag='meterSquaredPerKilogram')
otherUnitType.meterSquaredPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='meterSquaredPerSecond', tag='meterSquaredPerSecond')
otherUnitType.metersPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='metersPerDay', tag='metersPerDay')
otherUnitType.metersPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='metersPerGram', tag='metersPerGram')
otherUnitType.metersPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='metersPerSecond', tag='metersPerSecond')
otherUnitType.metersPerSecondSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='metersPerSecondSquared', tag='metersPerSecondSquared')
otherUnitType.metersSquaredPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='metersSquaredPerDay', tag='metersSquaredPerDay')
otherUnitType.metersSquaredPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='metersSquaredPerSecond', tag='metersSquaredPerSecond')
otherUnitType.microequivalentPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='microequivalentPerLiter', tag='microequivalentPerLiter')
otherUnitType.microgramPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='microgramPerGram', tag='microgramPerGram')
otherUnitType.microgramPerGramPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='microgramPerGramPerDay', tag='microgramPerGramPerDay')
otherUnitType.microgramPerGramPerHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value='microgramPerGramPerHour', tag='microgramPerGramPerHour')
otherUnitType.microgramPerGramPerWeek = otherUnitType._CF_enumeration.addEnumeration(unicode_value='microgramPerGramPerWeek', tag='microgramPerGramPerWeek')
otherUnitType.microgramPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='microgramPerLiter', tag='microgramPerLiter')
otherUnitType.microgramsPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='microgramsPerGram', tag='microgramsPerGram')
otherUnitType.microgramsPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='microgramsPerLiter', tag='microgramsPerLiter')
otherUnitType.microliter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='microliter', tag='microliter')
otherUnitType.microliterPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='microliterPerLiter', tag='microliterPerLiter')
otherUnitType.micrometerCubedPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='micrometerCubedPerGram', tag='micrometerCubedPerGram')
otherUnitType.micromolePerCentimeterSquaredPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='micromolePerCentimeterSquaredPerSecond', tag='micromolePerCentimeterSquaredPerSecond')
otherUnitType.micromolePerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='micromolePerGram', tag='micromolePerGram')
otherUnitType.micromolePerGramPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='micromolePerGramPerDay', tag='micromolePerGramPerDay')
otherUnitType.micromolePerGramPerHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value='micromolePerGramPerHour', tag='micromolePerGramPerHour')
otherUnitType.micromolePerGramPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='micromolePerGramPerSecond', tag='micromolePerGramPerSecond')
otherUnitType.micromolePerKilogram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='micromolePerKilogram', tag='micromolePerKilogram')
otherUnitType.micromolePerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='micromolePerLiter', tag='micromolePerLiter')
otherUnitType.micromolePerMeterSquaredPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='micromolePerMeterSquaredPerSecond', tag='micromolePerMeterSquaredPerSecond')
otherUnitType.micromolePerMole = otherUnitType._CF_enumeration.addEnumeration(unicode_value='micromolePerMole', tag='micromolePerMole')
otherUnitType.microsecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='microsecond', tag='microsecond')
otherUnitType.microwattPerCentimeterSquaredPerNanometer = otherUnitType._CF_enumeration.addEnumeration(unicode_value='microwattPerCentimeterSquaredPerNanometer', tag='microwattPerCentimeterSquaredPerNanometer')
otherUnitType.microwattPerCentimeterSquaredPerNanometerPerSteradian = otherUnitType._CF_enumeration.addEnumeration(unicode_value='microwattPerCentimeterSquaredPerNanometerPerSteradian', tag='microwattPerCentimeterSquaredPerNanometerPerSteradian')
otherUnitType.microwattPerCentimeterSquaredPerSteradian = otherUnitType._CF_enumeration.addEnumeration(unicode_value='microwattPerCentimeterSquaredPerSteradian', tag='microwattPerCentimeterSquaredPerSteradian')
otherUnitType.milePerHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milePerHour', tag='milePerHour')
otherUnitType.milePerMinute = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milePerMinute', tag='milePerMinute')
otherUnitType.milePerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milePerSecond', tag='milePerSecond')
otherUnitType.mileSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='mileSquared', tag='mileSquared')
otherUnitType.milesPerHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milesPerHour', tag='milesPerHour')
otherUnitType.milesPerMinute = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milesPerMinute', tag='milesPerMinute')
otherUnitType.milesPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milesPerSecond', tag='milesPerSecond')
otherUnitType.milliGramsPerMilliLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milliGramsPerMilliLiter', tag='milliGramsPerMilliLiter')
otherUnitType.millibar = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millibar', tag='millibar')
otherUnitType.milliequivalentPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milliequivalentPerLiter', tag='milliequivalentPerLiter')
otherUnitType.milligramPerKilogram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milligramPerKilogram', tag='milligramPerKilogram')
otherUnitType.milligramPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milligramPerLiter', tag='milligramPerLiter')
otherUnitType.milligramPerMeterCubed = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milligramPerMeterCubed', tag='milligramPerMeterCubed')
otherUnitType.milligramPerMeterCubedPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milligramPerMeterCubedPerDay', tag='milligramPerMeterCubedPerDay')
otherUnitType.milligramPerMeterSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milligramPerMeterSquared', tag='milligramPerMeterSquared')
otherUnitType.milligramPerMeterSquaredPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milligramPerMeterSquaredPerDay', tag='milligramPerMeterSquaredPerDay')
otherUnitType.milligramPerMilliliter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milligramPerMilliliter', tag='milligramPerMilliliter')
otherUnitType.milligramsPerCubicMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milligramsPerCubicMeter', tag='milligramsPerCubicMeter')
otherUnitType.milligramsPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milligramsPerLiter', tag='milligramsPerLiter')
otherUnitType.milligramsPerSquareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milligramsPerSquareMeter', tag='milligramsPerSquareMeter')
otherUnitType.millihertz = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millihertz', tag='millihertz')
otherUnitType.milliliter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milliliter', tag='milliliter')
otherUnitType.milliliterPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milliliterPerLiter', tag='milliliterPerLiter')
otherUnitType.millimeterPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millimeterPerDay', tag='millimeterPerDay')
otherUnitType.millimeterPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millimeterPerSecond', tag='millimeterPerSecond')
otherUnitType.millimeterSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millimeterSquared', tag='millimeterSquared')
otherUnitType.millimetersPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millimetersPerSecond', tag='millimetersPerSecond')
otherUnitType.millimolePerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millimolePerGram', tag='millimolePerGram')
otherUnitType.millimolePerKilogram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millimolePerKilogram', tag='millimolePerKilogram')
otherUnitType.millimolePerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millimolePerLiter', tag='millimolePerLiter')
otherUnitType.millimolePerMeterCubed = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millimolePerMeterCubed', tag='millimolePerMeterCubed')
otherUnitType.millimolePerMole = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millimolePerMole', tag='millimolePerMole')
otherUnitType.millimolesPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millimolesPerGram', tag='millimolesPerGram')
otherUnitType.millisecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millisecond', tag='millisecond')
otherUnitType.millivolt = otherUnitType._CF_enumeration.addEnumeration(unicode_value='millivolt', tag='millivolt')
otherUnitType.milliwatt = otherUnitType._CF_enumeration.addEnumeration(unicode_value='milliwatt', tag='milliwatt')
otherUnitType.minute = otherUnitType._CF_enumeration.addEnumeration(unicode_value='minute', tag='minute')
otherUnitType.molality = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molality', tag='molality')
otherUnitType.molarity = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molarity', tag='molarity')
otherUnitType.mole = otherUnitType._CF_enumeration.addEnumeration(unicode_value='mole', tag='mole')
otherUnitType.molePerCubicMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molePerCubicMeter', tag='molePerCubicMeter')
otherUnitType.molePerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molePerGram', tag='molePerGram')
otherUnitType.molePerKilogram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molePerKilogram', tag='molePerKilogram')
otherUnitType.molePerKilogram_ = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molePerKilogram', tag='molePerKilogram_')
otherUnitType.molePerKilogramPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molePerKilogramPerSecond', tag='molePerKilogramPerSecond')
otherUnitType.molePerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molePerLiter', tag='molePerLiter')
otherUnitType.molePerMeterCubed = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molePerMeterCubed', tag='molePerMeterCubed')
otherUnitType.molePerMeterSquaredPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molePerMeterSquaredPerSecond', tag='molePerMeterSquaredPerSecond')
otherUnitType.molePerMole = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molePerMole', tag='molePerMole')
otherUnitType.molesPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molesPerGram', tag='molesPerGram')
otherUnitType.molesPerKilogram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molesPerKilogram', tag='molesPerKilogram')
otherUnitType.molesPerKilogramPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='molesPerKilogramPerSecond', tag='molesPerKilogramPerSecond')
otherUnitType.nanogramPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nanogramPerGram', tag='nanogramPerGram')
otherUnitType.nanogramPerGramPerHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nanogramPerGramPerHour', tag='nanogramPerGramPerHour')
otherUnitType.nanoliterPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nanoliterPerLiter', tag='nanoliterPerLiter')
otherUnitType.nanomolePerGramPerDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nanomolePerGramPerDay', tag='nanomolePerGramPerDay')
otherUnitType.nanomolePerGramPerHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nanomolePerGramPerHour', tag='nanomolePerGramPerHour')
otherUnitType.nanomolePerGramPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nanomolePerGramPerSecond', tag='nanomolePerGramPerSecond')
otherUnitType.nanomolePerKilogram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nanomolePerKilogram', tag='nanomolePerKilogram')
otherUnitType.nanomolePerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nanomolePerLiter', tag='nanomolePerLiter')
otherUnitType.nanomolePerMole = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nanomolePerMole', tag='nanomolePerMole')
otherUnitType.nanomolesPerGramPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nanomolesPerGramPerSecond', tag='nanomolesPerGramPerSecond')
otherUnitType.nanosecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nanosecond', tag='nanosecond')
otherUnitType.newton = otherUnitType._CF_enumeration.addEnumeration(unicode_value='newton', tag='newton')
otherUnitType.nominalDay = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nominalDay', tag='nominalDay')
otherUnitType.nominalHour = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nominalHour', tag='nominalHour')
otherUnitType.nominalLeapYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nominalLeapYear', tag='nominalLeapYear')
otherUnitType.nominalMinute = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nominalMinute', tag='nominalMinute')
otherUnitType.nominalWeek = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nominalWeek', tag='nominalWeek')
otherUnitType.nominalYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='nominalYear', tag='nominalYear')
otherUnitType.number = otherUnitType._CF_enumeration.addEnumeration(unicode_value='number', tag='number')
otherUnitType.numberPerGram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='numberPerGram', tag='numberPerGram')
otherUnitType.numberPerHectare = otherUnitType._CF_enumeration.addEnumeration(unicode_value='numberPerHectare', tag='numberPerHectare')
otherUnitType.numberPerKilometerSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='numberPerKilometerSquared', tag='numberPerKilometerSquared')
otherUnitType.numberPerLiter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='numberPerLiter', tag='numberPerLiter')
otherUnitType.numberPerMeterCubed = otherUnitType._CF_enumeration.addEnumeration(unicode_value='numberPerMeterCubed', tag='numberPerMeterCubed')
otherUnitType.numberPerMeterSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='numberPerMeterSquared', tag='numberPerMeterSquared')
otherUnitType.numberPerMilliliter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='numberPerMilliliter', tag='numberPerMilliliter')
otherUnitType.ohm = otherUnitType._CF_enumeration.addEnumeration(unicode_value='ohm', tag='ohm')
otherUnitType.ohmMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='ohmMeter', tag='ohmMeter')
otherUnitType.pascal = otherUnitType._CF_enumeration.addEnumeration(unicode_value='pascal', tag='pascal')
otherUnitType.percent = otherUnitType._CF_enumeration.addEnumeration(unicode_value='percent', tag='percent')
otherUnitType.permil = otherUnitType._CF_enumeration.addEnumeration(unicode_value='permil', tag='permil')
otherUnitType.pint = otherUnitType._CF_enumeration.addEnumeration(unicode_value='pint', tag='pint')
otherUnitType.poundPerAcre = otherUnitType._CF_enumeration.addEnumeration(unicode_value='poundPerAcre', tag='poundPerAcre')
otherUnitType.poundPerInchSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='poundPerInchSquared', tag='poundPerInchSquared')
otherUnitType.poundsPerSquareInch = otherUnitType._CF_enumeration.addEnumeration(unicode_value='poundsPerSquareInch', tag='poundsPerSquareInch')
otherUnitType.quart = otherUnitType._CF_enumeration.addEnumeration(unicode_value='quart', tag='quart')
otherUnitType.second = otherUnitType._CF_enumeration.addEnumeration(unicode_value='second', tag='second')
otherUnitType.siemen = otherUnitType._CF_enumeration.addEnumeration(unicode_value='siemen', tag='siemen')
otherUnitType.siemens = otherUnitType._CF_enumeration.addEnumeration(unicode_value='siemens', tag='siemens')
otherUnitType.siemensPerCentimeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='siemensPerCentimeter', tag='siemensPerCentimeter')
otherUnitType.siemensPerMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='siemensPerMeter', tag='siemensPerMeter')
otherUnitType.sievert = otherUnitType._CF_enumeration.addEnumeration(unicode_value='sievert', tag='sievert')
otherUnitType.squareCentimeters = otherUnitType._CF_enumeration.addEnumeration(unicode_value='squareCentimeters', tag='squareCentimeters')
otherUnitType.squareFoot = otherUnitType._CF_enumeration.addEnumeration(unicode_value='squareFoot', tag='squareFoot')
otherUnitType.squareKilometers = otherUnitType._CF_enumeration.addEnumeration(unicode_value='squareKilometers', tag='squareKilometers')
otherUnitType.squareMeter = otherUnitType._CF_enumeration.addEnumeration(unicode_value='squareMeter', tag='squareMeter')
otherUnitType.squareMeterPerKilogram = otherUnitType._CF_enumeration.addEnumeration(unicode_value='squareMeterPerKilogram', tag='squareMeterPerKilogram')
otherUnitType.squareMile = otherUnitType._CF_enumeration.addEnumeration(unicode_value='squareMile', tag='squareMile')
otherUnitType.squareMillimeters = otherUnitType._CF_enumeration.addEnumeration(unicode_value='squareMillimeters', tag='squareMillimeters')
otherUnitType.squareYard = otherUnitType._CF_enumeration.addEnumeration(unicode_value='squareYard', tag='squareYard')
otherUnitType.tesla = otherUnitType._CF_enumeration.addEnumeration(unicode_value='tesla', tag='tesla')
otherUnitType.tonnePerHectare = otherUnitType._CF_enumeration.addEnumeration(unicode_value='tonnePerHectare', tag='tonnePerHectare')
otherUnitType.tonnePerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='tonnePerYear', tag='tonnePerYear')
otherUnitType.tonnesPerYear = otherUnitType._CF_enumeration.addEnumeration(unicode_value='tonnesPerYear', tag='tonnesPerYear')
otherUnitType.volt = otherUnitType._CF_enumeration.addEnumeration(unicode_value='volt', tag='volt')
otherUnitType.watt = otherUnitType._CF_enumeration.addEnumeration(unicode_value='watt', tag='watt')
otherUnitType.wattPerMeterSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='wattPerMeterSquared', tag='wattPerMeterSquared')
otherUnitType.wattPerMeterSquaredPerNanometer = otherUnitType._CF_enumeration.addEnumeration(unicode_value='wattPerMeterSquaredPerNanometer', tag='wattPerMeterSquaredPerNanometer')
otherUnitType.wattPerMeterSquaredPerNanometerPerSteradian = otherUnitType._CF_enumeration.addEnumeration(unicode_value='wattPerMeterSquaredPerNanometerPerSteradian', tag='wattPerMeterSquaredPerNanometerPerSteradian')
otherUnitType.wattPerMeterSquaredPerSteradian = otherUnitType._CF_enumeration.addEnumeration(unicode_value='wattPerMeterSquaredPerSteradian', tag='wattPerMeterSquaredPerSteradian')
otherUnitType.waveNumber = otherUnitType._CF_enumeration.addEnumeration(unicode_value='waveNumber', tag='waveNumber')
otherUnitType.weber = otherUnitType._CF_enumeration.addEnumeration(unicode_value='weber', tag='weber')
otherUnitType.yardPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='yardPerSecond', tag='yardPerSecond')
otherUnitType.yardSquared = otherUnitType._CF_enumeration.addEnumeration(unicode_value='yardSquared', tag='yardSquared')
otherUnitType.yardsPerSecond = otherUnitType._CF_enumeration.addEnumeration(unicode_value='yardsPerSecond', tag='yardsPerSecond')
otherUnitType._InitializeFacetMap(otherUnitType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'otherUnitType', otherUnitType)
_module_typeBindings.otherUnitType = otherUnitType

# Atomic simple type: {https://eml.ecoinformatics.org/units-2.2.0}angleUnitType
class angleUnitType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'angleUnitType')
    _XSDLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-unitTypeDefinitions.xsd', 461, 2)
    _Documentation = ''
angleUnitType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=angleUnitType, enum_prefix=None)
angleUnitType.radian = angleUnitType._CF_enumeration.addEnumeration(unicode_value='radian', tag='radian')
angleUnitType.degree = angleUnitType._CF_enumeration.addEnumeration(unicode_value='degree', tag='degree')
angleUnitType.grad = angleUnitType._CF_enumeration.addEnumeration(unicode_value='grad', tag='grad')
angleUnitType.steradian = angleUnitType._CF_enumeration.addEnumeration(unicode_value='steradian', tag='steradian')
angleUnitType._InitializeFacetMap(angleUnitType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'angleUnitType', angleUnitType)
_module_typeBindings.angleUnitType = angleUnitType

# Union simple type: {https://eml.ecoinformatics.org/units-2.2.0}StandardUnitDictionary
# superclasses pyxb.binding.datatypes.anySimpleType
class StandardUnitDictionary (pyxb.binding.basis.STD_union):

    """Simple type that is a union of LengthUnitType, MassUnitType, angleUnitType, otherUnitType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StandardUnitDictionary')
    _XSDLocation = pyxb.utils.utility.Location('/home/jumnhn/dev/pndb/pyeml/schemas/eml/eml-2.2.0/eml-unitTypeDefinitions.xsd', 34, 2)
    _Documentation = ''

    _MemberTypes = ( LengthUnitType, MassUnitType, angleUnitType, otherUnitType, )
StandardUnitDictionary.meter = 'meter'            # originally LengthUnitType.meter
StandardUnitDictionary.nanometer = 'nanometer'    # originally LengthUnitType.nanometer
StandardUnitDictionary.micrometer = 'micrometer'  # originally LengthUnitType.micrometer
StandardUnitDictionary.micron = 'micron'          # originally LengthUnitType.micron
StandardUnitDictionary.millimeter = 'millimeter'  # originally LengthUnitType.millimeter
StandardUnitDictionary.centimeter = 'centimeter'  # originally LengthUnitType.centimeter
StandardUnitDictionary.decimeter = 'decimeter'    # originally LengthUnitType.decimeter
StandardUnitDictionary.dekameter = 'dekameter'    # originally LengthUnitType.dekameter
StandardUnitDictionary.hectometer = 'hectometer'  # originally LengthUnitType.hectometer
StandardUnitDictionary.kilometer = 'kilometer'    # originally LengthUnitType.kilometer
StandardUnitDictionary.megameter = 'megameter'    # originally LengthUnitType.megameter
StandardUnitDictionary.angstrom = 'angstrom'      # originally LengthUnitType.angstrom
StandardUnitDictionary.inch = 'inch'              # originally LengthUnitType.inch
StandardUnitDictionary.Foot_US = 'Foot_US'        # originally LengthUnitType.Foot_US
StandardUnitDictionary.foot = 'foot'              # originally LengthUnitType.foot
StandardUnitDictionary.Foot_Gold_Coast = 'Foot_Gold_Coast'# originally LengthUnitType.Foot_Gold_Coast
StandardUnitDictionary.fathom = 'fathom'          # originally LengthUnitType.fathom
StandardUnitDictionary.nauticalMile = 'nauticalMile'# originally LengthUnitType.nauticalMile
StandardUnitDictionary.yard = 'yard'              # originally LengthUnitType.yard
StandardUnitDictionary.Yard_Indian = 'Yard_Indian'# originally LengthUnitType.Yard_Indian
StandardUnitDictionary.Link_Clarke = 'Link_Clarke'# originally LengthUnitType.Link_Clarke
StandardUnitDictionary.Yard_Sears = 'Yard_Sears'  # originally LengthUnitType.Yard_Sears
StandardUnitDictionary.mile = 'mile'              # originally LengthUnitType.mile
StandardUnitDictionary.kilogram = 'kilogram'      # originally MassUnitType.kilogram
StandardUnitDictionary.nanogram = 'nanogram'      # originally MassUnitType.nanogram
StandardUnitDictionary.microgram = 'microgram'    # originally MassUnitType.microgram
StandardUnitDictionary.milligram = 'milligram'    # originally MassUnitType.milligram
StandardUnitDictionary.centigram = 'centigram'    # originally MassUnitType.centigram
StandardUnitDictionary.decigram = 'decigram'      # originally MassUnitType.decigram
StandardUnitDictionary.gram = 'gram'              # originally MassUnitType.gram
StandardUnitDictionary.dekagram = 'dekagram'      # originally MassUnitType.dekagram
StandardUnitDictionary.hectogram = 'hectogram'    # originally MassUnitType.hectogram
StandardUnitDictionary.megagram = 'megagram'      # originally MassUnitType.megagram
StandardUnitDictionary.tonne = 'tonne'            # originally MassUnitType.tonne
StandardUnitDictionary.pound = 'pound'            # originally MassUnitType.pound
StandardUnitDictionary.ton = 'ton'                # originally MassUnitType.ton
StandardUnitDictionary.radian = 'radian'          # originally angleUnitType.radian
StandardUnitDictionary.degree = 'degree'          # originally angleUnitType.degree
StandardUnitDictionary.grad = 'grad'              # originally angleUnitType.grad
StandardUnitDictionary.steradian = 'steradian'    # originally angleUnitType.steradian
StandardUnitDictionary.acre = 'acre'              # originally otherUnitType.acre
StandardUnitDictionary.ampere = 'ampere'          # originally otherUnitType.ampere
StandardUnitDictionary.amperePerMeter = 'amperePerMeter'# originally otherUnitType.amperePerMeter
StandardUnitDictionary.amperePerMeterSquared = 'amperePerMeterSquared'# originally otherUnitType.amperePerMeterSquared
StandardUnitDictionary.amperePerSquareMeter = 'amperePerSquareMeter'# originally otherUnitType.amperePerSquareMeter
StandardUnitDictionary.are = 'are'                # originally otherUnitType.are
StandardUnitDictionary.atmosphere = 'atmosphere'  # originally otherUnitType.atmosphere
StandardUnitDictionary.bar = 'bar'                # originally otherUnitType.bar
StandardUnitDictionary.becquerel = 'becquerel'    # originally otherUnitType.becquerel
StandardUnitDictionary.britishThermalUnit = 'britishThermalUnit'# originally otherUnitType.britishThermalUnit
StandardUnitDictionary.bushel = 'bushel'          # originally otherUnitType.bushel
StandardUnitDictionary.bushelPerAcre = 'bushelPerAcre'# originally otherUnitType.bushelPerAcre
StandardUnitDictionary.bushelsPerAcre = 'bushelsPerAcre'# originally otherUnitType.bushelsPerAcre
StandardUnitDictionary.calorie = 'calorie'        # originally otherUnitType.calorie
StandardUnitDictionary.candela = 'candela'        # originally otherUnitType.candela
StandardUnitDictionary.candelaPerMeterSquared = 'candelaPerMeterSquared'# originally otherUnitType.candelaPerMeterSquared
StandardUnitDictionary.candelaPerSquareMeter = 'candelaPerSquareMeter'# originally otherUnitType.candelaPerSquareMeter
StandardUnitDictionary.celsius = 'celsius'        # originally otherUnitType.celsius
StandardUnitDictionary.centimeterCubed = 'centimeterCubed'# originally otherUnitType.centimeterCubed
StandardUnitDictionary.centimeterPerSecond = 'centimeterPerSecond'# originally otherUnitType.centimeterPerSecond
StandardUnitDictionary.centimeterPerYear = 'centimeterPerYear'# originally otherUnitType.centimeterPerYear
StandardUnitDictionary.centimeterSquared = 'centimeterSquared'# originally otherUnitType.centimeterSquared
StandardUnitDictionary.centimetersPerSecond = 'centimetersPerSecond'# originally otherUnitType.centimetersPerSecond
StandardUnitDictionary.centisecond = 'centisecond'# originally otherUnitType.centisecond
StandardUnitDictionary.coulomb = 'coulomb'        # originally otherUnitType.coulomb
StandardUnitDictionary.cubicCentimetersPerCubicCentimeters = 'cubicCentimetersPerCubicCentimeters'# originally otherUnitType.cubicCentimetersPerCubicCentimeters
StandardUnitDictionary.cubicFeetPerSecond = 'cubicFeetPerSecond'# originally otherUnitType.cubicFeetPerSecond
StandardUnitDictionary.cubicInch = 'cubicInch'    # originally otherUnitType.cubicInch
StandardUnitDictionary.cubicMeter = 'cubicMeter'  # originally otherUnitType.cubicMeter
StandardUnitDictionary.cubicMeterPerKilogram = 'cubicMeterPerKilogram'# originally otherUnitType.cubicMeterPerKilogram
StandardUnitDictionary.cubicMetersPerSecond = 'cubicMetersPerSecond'# originally otherUnitType.cubicMetersPerSecond
StandardUnitDictionary.cubicMicrometersPerGram = 'cubicMicrometersPerGram'# originally otherUnitType.cubicMicrometersPerGram
StandardUnitDictionary.decibar = 'decibar'        # originally otherUnitType.decibar
StandardUnitDictionary.decisecond = 'decisecond'  # originally otherUnitType.decisecond
StandardUnitDictionary.dekasecond = 'dekasecond'  # originally otherUnitType.dekasecond
StandardUnitDictionary.dimensionless = 'dimensionless'# originally otherUnitType.dimensionless
StandardUnitDictionary.equivalentPerLiter = 'equivalentPerLiter'# originally otherUnitType.equivalentPerLiter
StandardUnitDictionary.fahrenheit = 'fahrenheit'  # originally otherUnitType.fahrenheit
StandardUnitDictionary.farad = 'farad'            # originally otherUnitType.farad
StandardUnitDictionary.feetPerDay = 'feetPerDay'  # originally otherUnitType.feetPerDay
StandardUnitDictionary.feetPerHour = 'feetPerHour'# originally otherUnitType.feetPerHour
StandardUnitDictionary.feetPerSecond = 'feetPerSecond'# originally otherUnitType.feetPerSecond
StandardUnitDictionary.feetSquaredPerDay = 'feetSquaredPerDay'# originally otherUnitType.feetSquaredPerDay
StandardUnitDictionary.footCubedPerSecond = 'footCubedPerSecond'# originally otherUnitType.footCubedPerSecond
StandardUnitDictionary.footPerDay = 'footPerDay'  # originally otherUnitType.footPerDay
StandardUnitDictionary.footPerHour = 'footPerHour'# originally otherUnitType.footPerHour
StandardUnitDictionary.footPerSecond = 'footPerSecond'# originally otherUnitType.footPerSecond
StandardUnitDictionary.footPound = 'footPound'    # originally otherUnitType.footPound
StandardUnitDictionary.footSquared = 'footSquared'# originally otherUnitType.footSquared
StandardUnitDictionary.footSquaredPerDay = 'footSquaredPerDay'# originally otherUnitType.footSquaredPerDay
StandardUnitDictionary.gallon = 'gallon'          # originally otherUnitType.gallon
StandardUnitDictionary.gramPerCentimeterCubed = 'gramPerCentimeterCubed'# originally otherUnitType.gramPerCentimeterCubed
StandardUnitDictionary.gramPerCentimeterSquaredPerSecond = 'gramPerCentimeterSquaredPerSecond'# originally otherUnitType.gramPerCentimeterSquaredPerSecond
StandardUnitDictionary.gramPerDayPerHectare = 'gramPerDayPerHectare'# originally otherUnitType.gramPerDayPerHectare
StandardUnitDictionary.gramPerDayPerLiter = 'gramPerDayPerLiter'# originally otherUnitType.gramPerDayPerLiter
StandardUnitDictionary.gramPerGram = 'gramPerGram'# originally otherUnitType.gramPerGram
StandardUnitDictionary.gramPerLiter = 'gramPerLiter'# originally otherUnitType.gramPerLiter
StandardUnitDictionary.gramPerMeterSquared = 'gramPerMeterSquared'# originally otherUnitType.gramPerMeterSquared
StandardUnitDictionary.gramPerMeterSquaredPerDay = 'gramPerMeterSquaredPerDay'# originally otherUnitType.gramPerMeterSquaredPerDay
StandardUnitDictionary.gramPerMeterSquaredPerYear = 'gramPerMeterSquaredPerYear'# originally otherUnitType.gramPerMeterSquaredPerYear
StandardUnitDictionary.gramPerMilliliter = 'gramPerMilliliter'# originally otherUnitType.gramPerMilliliter
StandardUnitDictionary.gramPerYear = 'gramPerYear'# originally otherUnitType.gramPerYear
StandardUnitDictionary.gramPercentimeterSquared = 'gramPercentimeterSquared'# originally otherUnitType.gramPercentimeterSquared
StandardUnitDictionary.gramsPerCentimeterSquaredPerSecond = 'gramsPerCentimeterSquaredPerSecond'# originally otherUnitType.gramsPerCentimeterSquaredPerSecond
StandardUnitDictionary.gramsPerCubicCentimeter = 'gramsPerCubicCentimeter'# originally otherUnitType.gramsPerCubicCentimeter
StandardUnitDictionary.gramsPerGram = 'gramsPerGram'# originally otherUnitType.gramsPerGram
StandardUnitDictionary.gramsPerHectarePerDay = 'gramsPerHectarePerDay'# originally otherUnitType.gramsPerHectarePerDay
StandardUnitDictionary.gramsPerLiter = 'gramsPerLiter'# originally otherUnitType.gramsPerLiter
StandardUnitDictionary.gramsPerLiterPerDay = 'gramsPerLiterPerDay'# originally otherUnitType.gramsPerLiterPerDay
StandardUnitDictionary.gramsPerMeterSquaredPerYear = 'gramsPerMeterSquaredPerYear'# originally otherUnitType.gramsPerMeterSquaredPerYear
StandardUnitDictionary.gramsPerMilliliter = 'gramsPerMilliliter'# originally otherUnitType.gramsPerMilliliter
StandardUnitDictionary.gramsPerSquareMeter = 'gramsPerSquareMeter'# originally otherUnitType.gramsPerSquareMeter
StandardUnitDictionary.gramsPerYear = 'gramsPerYear'# originally otherUnitType.gramsPerYear
StandardUnitDictionary.gray = 'gray'              # originally otherUnitType.gray
StandardUnitDictionary.hectare = 'hectare'        # originally otherUnitType.hectare
StandardUnitDictionary.hectopascal = 'hectopascal'# originally otherUnitType.hectopascal
StandardUnitDictionary.hectosecond = 'hectosecond'# originally otherUnitType.hectosecond
StandardUnitDictionary.henry = 'henry'            # originally otherUnitType.henry
StandardUnitDictionary.hertz = 'hertz'            # originally otherUnitType.hertz
StandardUnitDictionary.hour = 'hour'              # originally otherUnitType.hour
StandardUnitDictionary.inchCubed = 'inchCubed'    # originally otherUnitType.inchCubed
StandardUnitDictionary.inchPerHour = 'inchPerHour'# originally otherUnitType.inchPerHour
StandardUnitDictionary.inverseCentimeter = 'inverseCentimeter'# originally otherUnitType.inverseCentimeter
StandardUnitDictionary.inverseMeter = 'inverseMeter'# originally otherUnitType.inverseMeter
StandardUnitDictionary.joule = 'joule'            # originally otherUnitType.joule
StandardUnitDictionary.katal = 'katal'            # originally otherUnitType.katal
StandardUnitDictionary.kelvin = 'kelvin'          # originally otherUnitType.kelvin
StandardUnitDictionary.kilogramPerCubicMeter = 'kilogramPerCubicMeter'# originally otherUnitType.kilogramPerCubicMeter
StandardUnitDictionary.kilogramPerHectare = 'kilogramPerHectare'# originally otherUnitType.kilogramPerHectare
StandardUnitDictionary.kilogramPerHectarePerYear = 'kilogramPerHectarePerYear'# originally otherUnitType.kilogramPerHectarePerYear
StandardUnitDictionary.kilogramPerMeterCubed = 'kilogramPerMeterCubed'# originally otherUnitType.kilogramPerMeterCubed
StandardUnitDictionary.kilogramPerMeterSquared = 'kilogramPerMeterSquared'# originally otherUnitType.kilogramPerMeterSquared
StandardUnitDictionary.kilogramPerMeterSquaredPerDay = 'kilogramPerMeterSquaredPerDay'# originally otherUnitType.kilogramPerMeterSquaredPerDay
StandardUnitDictionary.kilogramPerMeterSquaredPerSecond = 'kilogramPerMeterSquaredPerSecond'# originally otherUnitType.kilogramPerMeterSquaredPerSecond
StandardUnitDictionary.kilogramPerMeterSquaredPerYear = 'kilogramPerMeterSquaredPerYear'# originally otherUnitType.kilogramPerMeterSquaredPerYear
StandardUnitDictionary.kilogramPerSecond = 'kilogramPerSecond'# originally otherUnitType.kilogramPerSecond
StandardUnitDictionary.kilogramsPerHectare = 'kilogramsPerHectare'# originally otherUnitType.kilogramsPerHectare
StandardUnitDictionary.kilogramsPerHectarePerYear = 'kilogramsPerHectarePerYear'# originally otherUnitType.kilogramsPerHectarePerYear
StandardUnitDictionary.kilogramsPerMeterSquaredPerSecond = 'kilogramsPerMeterSquaredPerSecond'# originally otherUnitType.kilogramsPerMeterSquaredPerSecond
StandardUnitDictionary.kilogramsPerMeterSquaredPerYear = 'kilogramsPerMeterSquaredPerYear'# originally otherUnitType.kilogramsPerMeterSquaredPerYear
StandardUnitDictionary.kilogramsPerSecond = 'kilogramsPerSecond'# originally otherUnitType.kilogramsPerSecond
StandardUnitDictionary.kilogramsPerSquareMeter = 'kilogramsPerSquareMeter'# originally otherUnitType.kilogramsPerSquareMeter
StandardUnitDictionary.kilohertz = 'kilohertz'    # originally otherUnitType.kilohertz
StandardUnitDictionary.kiloliter = 'kiloliter'    # originally otherUnitType.kiloliter
StandardUnitDictionary.kilometerPerHour = 'kilometerPerHour'# originally otherUnitType.kilometerPerHour
StandardUnitDictionary.kilometerSquared = 'kilometerSquared'# originally otherUnitType.kilometerSquared
StandardUnitDictionary.kilometersPerHour = 'kilometersPerHour'# originally otherUnitType.kilometersPerHour
StandardUnitDictionary.kilopascal = 'kilopascal'  # originally otherUnitType.kilopascal
StandardUnitDictionary.kilosecond = 'kilosecond'  # originally otherUnitType.kilosecond
StandardUnitDictionary.kilovolt = 'kilovolt'      # originally otherUnitType.kilovolt
StandardUnitDictionary.kilowatt = 'kilowatt'      # originally otherUnitType.kilowatt
StandardUnitDictionary.kilowattPerMeterSquared = 'kilowattPerMeterSquared'# originally otherUnitType.kilowattPerMeterSquared
StandardUnitDictionary.knot = 'knot'              # originally otherUnitType.knot
StandardUnitDictionary.knots = 'knots'            # originally otherUnitType.knots
StandardUnitDictionary.langley = 'langley'        # originally otherUnitType.langley
StandardUnitDictionary.langleyPerDay = 'langleyPerDay'# originally otherUnitType.langleyPerDay
StandardUnitDictionary.liter = 'liter'            # originally otherUnitType.liter
StandardUnitDictionary.literPerHectare = 'literPerHectare'# originally otherUnitType.literPerHectare
StandardUnitDictionary.literPerLiter = 'literPerLiter'# originally otherUnitType.literPerLiter
StandardUnitDictionary.literPerMeterSquared = 'literPerMeterSquared'# originally otherUnitType.literPerMeterSquared
StandardUnitDictionary.literPerSecond = 'literPerSecond'# originally otherUnitType.literPerSecond
StandardUnitDictionary.litersPerHectare = 'litersPerHectare'# originally otherUnitType.litersPerHectare
StandardUnitDictionary.litersPerSecond = 'litersPerSecond'# originally otherUnitType.litersPerSecond
StandardUnitDictionary.litersPerSquareMeter = 'litersPerSquareMeter'# originally otherUnitType.litersPerSquareMeter
StandardUnitDictionary.lumen = 'lumen'            # originally otherUnitType.lumen
StandardUnitDictionary.lux = 'lux'                # originally otherUnitType.lux
StandardUnitDictionary.megagramPerMeterCubed = 'megagramPerMeterCubed'# originally otherUnitType.megagramPerMeterCubed
StandardUnitDictionary.megahertz = 'megahertz'    # originally otherUnitType.megahertz
StandardUnitDictionary.megajoulePerMeterSquaredPerDay = 'megajoulePerMeterSquaredPerDay'# originally otherUnitType.megajoulePerMeterSquaredPerDay
StandardUnitDictionary.megapascal = 'megapascal'  # originally otherUnitType.megapascal
StandardUnitDictionary.megasecond = 'megasecond'  # originally otherUnitType.megasecond
StandardUnitDictionary.megavolt = 'megavolt'      # originally otherUnitType.megavolt
StandardUnitDictionary.megawatt = 'megawatt'      # originally otherUnitType.megawatt
StandardUnitDictionary.meterCubed = 'meterCubed'  # originally otherUnitType.meterCubed
StandardUnitDictionary.meterCubedPerHectare = 'meterCubedPerHectare'# originally otherUnitType.meterCubedPerHectare
StandardUnitDictionary.meterCubedPerKilogram = 'meterCubedPerKilogram'# originally otherUnitType.meterCubedPerKilogram
StandardUnitDictionary.meterCubedPerMeterCubed = 'meterCubedPerMeterCubed'# originally otherUnitType.meterCubedPerMeterCubed
StandardUnitDictionary.meterCubedPerMeterSquared = 'meterCubedPerMeterSquared'# originally otherUnitType.meterCubedPerMeterSquared
StandardUnitDictionary.meterCubedPerSecond = 'meterCubedPerSecond'# originally otherUnitType.meterCubedPerSecond
StandardUnitDictionary.meterPerDay = 'meterPerDay'# originally otherUnitType.meterPerDay
StandardUnitDictionary.meterPerGram = 'meterPerGram'# originally otherUnitType.meterPerGram
StandardUnitDictionary.meterPerSecond = 'meterPerSecond'# originally otherUnitType.meterPerSecond
StandardUnitDictionary.meterPerSecondSquared = 'meterPerSecondSquared'# originally otherUnitType.meterPerSecondSquared
StandardUnitDictionary.meterSquared = 'meterSquared'# originally otherUnitType.meterSquared
StandardUnitDictionary.meterSquaredPerDay = 'meterSquaredPerDay'# originally otherUnitType.meterSquaredPerDay
StandardUnitDictionary.meterSquaredPerHectare = 'meterSquaredPerHectare'# originally otherUnitType.meterSquaredPerHectare
StandardUnitDictionary.meterSquaredPerKilogram = 'meterSquaredPerKilogram'# originally otherUnitType.meterSquaredPerKilogram
StandardUnitDictionary.meterSquaredPerSecond = 'meterSquaredPerSecond'# originally otherUnitType.meterSquaredPerSecond
StandardUnitDictionary.metersPerDay = 'metersPerDay'# originally otherUnitType.metersPerDay
StandardUnitDictionary.metersPerGram = 'metersPerGram'# originally otherUnitType.metersPerGram
StandardUnitDictionary.metersPerSecond = 'metersPerSecond'# originally otherUnitType.metersPerSecond
StandardUnitDictionary.metersPerSecondSquared = 'metersPerSecondSquared'# originally otherUnitType.metersPerSecondSquared
StandardUnitDictionary.metersSquaredPerDay = 'metersSquaredPerDay'# originally otherUnitType.metersSquaredPerDay
StandardUnitDictionary.metersSquaredPerSecond = 'metersSquaredPerSecond'# originally otherUnitType.metersSquaredPerSecond
StandardUnitDictionary.microequivalentPerLiter = 'microequivalentPerLiter'# originally otherUnitType.microequivalentPerLiter
StandardUnitDictionary.microgramPerGram = 'microgramPerGram'# originally otherUnitType.microgramPerGram
StandardUnitDictionary.microgramPerGramPerDay = 'microgramPerGramPerDay'# originally otherUnitType.microgramPerGramPerDay
StandardUnitDictionary.microgramPerGramPerHour = 'microgramPerGramPerHour'# originally otherUnitType.microgramPerGramPerHour
StandardUnitDictionary.microgramPerGramPerWeek = 'microgramPerGramPerWeek'# originally otherUnitType.microgramPerGramPerWeek
StandardUnitDictionary.microgramPerLiter = 'microgramPerLiter'# originally otherUnitType.microgramPerLiter
StandardUnitDictionary.microgramsPerGram = 'microgramsPerGram'# originally otherUnitType.microgramsPerGram
StandardUnitDictionary.microgramsPerLiter = 'microgramsPerLiter'# originally otherUnitType.microgramsPerLiter
StandardUnitDictionary.microliter = 'microliter'  # originally otherUnitType.microliter
StandardUnitDictionary.microliterPerLiter = 'microliterPerLiter'# originally otherUnitType.microliterPerLiter
StandardUnitDictionary.micrometerCubedPerGram = 'micrometerCubedPerGram'# originally otherUnitType.micrometerCubedPerGram
StandardUnitDictionary.micromolePerCentimeterSquaredPerSecond = 'micromolePerCentimeterSquaredPerSecond'# originally otherUnitType.micromolePerCentimeterSquaredPerSecond
StandardUnitDictionary.micromolePerGram = 'micromolePerGram'# originally otherUnitType.micromolePerGram
StandardUnitDictionary.micromolePerGramPerDay = 'micromolePerGramPerDay'# originally otherUnitType.micromolePerGramPerDay
StandardUnitDictionary.micromolePerGramPerHour = 'micromolePerGramPerHour'# originally otherUnitType.micromolePerGramPerHour
StandardUnitDictionary.micromolePerGramPerSecond = 'micromolePerGramPerSecond'# originally otherUnitType.micromolePerGramPerSecond
StandardUnitDictionary.micromolePerKilogram = 'micromolePerKilogram'# originally otherUnitType.micromolePerKilogram
StandardUnitDictionary.micromolePerLiter = 'micromolePerLiter'# originally otherUnitType.micromolePerLiter
StandardUnitDictionary.micromolePerMeterSquaredPerSecond = 'micromolePerMeterSquaredPerSecond'# originally otherUnitType.micromolePerMeterSquaredPerSecond
StandardUnitDictionary.micromolePerMole = 'micromolePerMole'# originally otherUnitType.micromolePerMole
StandardUnitDictionary.microsecond = 'microsecond'# originally otherUnitType.microsecond
StandardUnitDictionary.microwattPerCentimeterSquaredPerNanometer = 'microwattPerCentimeterSquaredPerNanometer'# originally otherUnitType.microwattPerCentimeterSquaredPerNanometer
StandardUnitDictionary.microwattPerCentimeterSquaredPerNanometerPerSteradian = 'microwattPerCentimeterSquaredPerNanometerPerSteradian'# originally otherUnitType.microwattPerCentimeterSquaredPerNanometerPerSteradian
StandardUnitDictionary.microwattPerCentimeterSquaredPerSteradian = 'microwattPerCentimeterSquaredPerSteradian'# originally otherUnitType.microwattPerCentimeterSquaredPerSteradian
StandardUnitDictionary.milePerHour = 'milePerHour'# originally otherUnitType.milePerHour
StandardUnitDictionary.milePerMinute = 'milePerMinute'# originally otherUnitType.milePerMinute
StandardUnitDictionary.milePerSecond = 'milePerSecond'# originally otherUnitType.milePerSecond
StandardUnitDictionary.mileSquared = 'mileSquared'# originally otherUnitType.mileSquared
StandardUnitDictionary.milesPerHour = 'milesPerHour'# originally otherUnitType.milesPerHour
StandardUnitDictionary.milesPerMinute = 'milesPerMinute'# originally otherUnitType.milesPerMinute
StandardUnitDictionary.milesPerSecond = 'milesPerSecond'# originally otherUnitType.milesPerSecond
StandardUnitDictionary.milliGramsPerMilliLiter = 'milliGramsPerMilliLiter'# originally otherUnitType.milliGramsPerMilliLiter
StandardUnitDictionary.millibar = 'millibar'      # originally otherUnitType.millibar
StandardUnitDictionary.milliequivalentPerLiter = 'milliequivalentPerLiter'# originally otherUnitType.milliequivalentPerLiter
StandardUnitDictionary.milligramPerKilogram = 'milligramPerKilogram'# originally otherUnitType.milligramPerKilogram
StandardUnitDictionary.milligramPerLiter = 'milligramPerLiter'# originally otherUnitType.milligramPerLiter
StandardUnitDictionary.milligramPerMeterCubed = 'milligramPerMeterCubed'# originally otherUnitType.milligramPerMeterCubed
StandardUnitDictionary.milligramPerMeterCubedPerDay = 'milligramPerMeterCubedPerDay'# originally otherUnitType.milligramPerMeterCubedPerDay
StandardUnitDictionary.milligramPerMeterSquared = 'milligramPerMeterSquared'# originally otherUnitType.milligramPerMeterSquared
StandardUnitDictionary.milligramPerMeterSquaredPerDay = 'milligramPerMeterSquaredPerDay'# originally otherUnitType.milligramPerMeterSquaredPerDay
StandardUnitDictionary.milligramPerMilliliter = 'milligramPerMilliliter'# originally otherUnitType.milligramPerMilliliter
StandardUnitDictionary.milligramsPerCubicMeter = 'milligramsPerCubicMeter'# originally otherUnitType.milligramsPerCubicMeter
StandardUnitDictionary.milligramsPerLiter = 'milligramsPerLiter'# originally otherUnitType.milligramsPerLiter
StandardUnitDictionary.milligramsPerSquareMeter = 'milligramsPerSquareMeter'# originally otherUnitType.milligramsPerSquareMeter
StandardUnitDictionary.millihertz = 'millihertz'  # originally otherUnitType.millihertz
StandardUnitDictionary.milliliter = 'milliliter'  # originally otherUnitType.milliliter
StandardUnitDictionary.milliliterPerLiter = 'milliliterPerLiter'# originally otherUnitType.milliliterPerLiter
StandardUnitDictionary.millimeterPerDay = 'millimeterPerDay'# originally otherUnitType.millimeterPerDay
StandardUnitDictionary.millimeterPerSecond = 'millimeterPerSecond'# originally otherUnitType.millimeterPerSecond
StandardUnitDictionary.millimeterSquared = 'millimeterSquared'# originally otherUnitType.millimeterSquared
StandardUnitDictionary.millimetersPerSecond = 'millimetersPerSecond'# originally otherUnitType.millimetersPerSecond
StandardUnitDictionary.millimolePerGram = 'millimolePerGram'# originally otherUnitType.millimolePerGram
StandardUnitDictionary.millimolePerKilogram = 'millimolePerKilogram'# originally otherUnitType.millimolePerKilogram
StandardUnitDictionary.millimolePerLiter = 'millimolePerLiter'# originally otherUnitType.millimolePerLiter
StandardUnitDictionary.millimolePerMeterCubed = 'millimolePerMeterCubed'# originally otherUnitType.millimolePerMeterCubed
StandardUnitDictionary.millimolePerMole = 'millimolePerMole'# originally otherUnitType.millimolePerMole
StandardUnitDictionary.millimolesPerGram = 'millimolesPerGram'# originally otherUnitType.millimolesPerGram
StandardUnitDictionary.millisecond = 'millisecond'# originally otherUnitType.millisecond
StandardUnitDictionary.millivolt = 'millivolt'    # originally otherUnitType.millivolt
StandardUnitDictionary.milliwatt = 'milliwatt'    # originally otherUnitType.milliwatt
StandardUnitDictionary.minute = 'minute'          # originally otherUnitType.minute
StandardUnitDictionary.molality = 'molality'      # originally otherUnitType.molality
StandardUnitDictionary.molarity = 'molarity'      # originally otherUnitType.molarity
StandardUnitDictionary.mole = 'mole'              # originally otherUnitType.mole
StandardUnitDictionary.molePerCubicMeter = 'molePerCubicMeter'# originally otherUnitType.molePerCubicMeter
StandardUnitDictionary.molePerGram = 'molePerGram'# originally otherUnitType.molePerGram
StandardUnitDictionary.molePerKilogram = 'molePerKilogram'# originally otherUnitType.molePerKilogram
StandardUnitDictionary.molePerKilogram_ = 'molePerKilogram'# originally otherUnitType.molePerKilogram_
StandardUnitDictionary.molePerKilogramPerSecond = 'molePerKilogramPerSecond'# originally otherUnitType.molePerKilogramPerSecond
StandardUnitDictionary.molePerLiter = 'molePerLiter'# originally otherUnitType.molePerLiter
StandardUnitDictionary.molePerMeterCubed = 'molePerMeterCubed'# originally otherUnitType.molePerMeterCubed
StandardUnitDictionary.molePerMeterSquaredPerSecond = 'molePerMeterSquaredPerSecond'# originally otherUnitType.molePerMeterSquaredPerSecond
StandardUnitDictionary.molePerMole = 'molePerMole'# originally otherUnitType.molePerMole
StandardUnitDictionary.molesPerGram = 'molesPerGram'# originally otherUnitType.molesPerGram
StandardUnitDictionary.molesPerKilogram = 'molesPerKilogram'# originally otherUnitType.molesPerKilogram
StandardUnitDictionary.molesPerKilogramPerSecond = 'molesPerKilogramPerSecond'# originally otherUnitType.molesPerKilogramPerSecond
StandardUnitDictionary.nanogramPerGram = 'nanogramPerGram'# originally otherUnitType.nanogramPerGram
StandardUnitDictionary.nanogramPerGramPerHour = 'nanogramPerGramPerHour'# originally otherUnitType.nanogramPerGramPerHour
StandardUnitDictionary.nanoliterPerLiter = 'nanoliterPerLiter'# originally otherUnitType.nanoliterPerLiter
StandardUnitDictionary.nanomolePerGramPerDay = 'nanomolePerGramPerDay'# originally otherUnitType.nanomolePerGramPerDay
StandardUnitDictionary.nanomolePerGramPerHour = 'nanomolePerGramPerHour'# originally otherUnitType.nanomolePerGramPerHour
StandardUnitDictionary.nanomolePerGramPerSecond = 'nanomolePerGramPerSecond'# originally otherUnitType.nanomolePerGramPerSecond
StandardUnitDictionary.nanomolePerKilogram = 'nanomolePerKilogram'# originally otherUnitType.nanomolePerKilogram
StandardUnitDictionary.nanomolePerLiter = 'nanomolePerLiter'# originally otherUnitType.nanomolePerLiter
StandardUnitDictionary.nanomolePerMole = 'nanomolePerMole'# originally otherUnitType.nanomolePerMole
StandardUnitDictionary.nanomolesPerGramPerSecond = 'nanomolesPerGramPerSecond'# originally otherUnitType.nanomolesPerGramPerSecond
StandardUnitDictionary.nanosecond = 'nanosecond'  # originally otherUnitType.nanosecond
StandardUnitDictionary.newton = 'newton'          # originally otherUnitType.newton
StandardUnitDictionary.nominalDay = 'nominalDay'  # originally otherUnitType.nominalDay
StandardUnitDictionary.nominalHour = 'nominalHour'# originally otherUnitType.nominalHour
StandardUnitDictionary.nominalLeapYear = 'nominalLeapYear'# originally otherUnitType.nominalLeapYear
StandardUnitDictionary.nominalMinute = 'nominalMinute'# originally otherUnitType.nominalMinute
StandardUnitDictionary.nominalWeek = 'nominalWeek'# originally otherUnitType.nominalWeek
StandardUnitDictionary.nominalYear = 'nominalYear'# originally otherUnitType.nominalYear
StandardUnitDictionary.number = 'number'          # originally otherUnitType.number
StandardUnitDictionary.numberPerGram = 'numberPerGram'# originally otherUnitType.numberPerGram
StandardUnitDictionary.numberPerHectare = 'numberPerHectare'# originally otherUnitType.numberPerHectare
StandardUnitDictionary.numberPerKilometerSquared = 'numberPerKilometerSquared'# originally otherUnitType.numberPerKilometerSquared
StandardUnitDictionary.numberPerLiter = 'numberPerLiter'# originally otherUnitType.numberPerLiter
StandardUnitDictionary.numberPerMeterCubed = 'numberPerMeterCubed'# originally otherUnitType.numberPerMeterCubed
StandardUnitDictionary.numberPerMeterSquared = 'numberPerMeterSquared'# originally otherUnitType.numberPerMeterSquared
StandardUnitDictionary.numberPerMilliliter = 'numberPerMilliliter'# originally otherUnitType.numberPerMilliliter
StandardUnitDictionary.ohm = 'ohm'                # originally otherUnitType.ohm
StandardUnitDictionary.ohmMeter = 'ohmMeter'      # originally otherUnitType.ohmMeter
StandardUnitDictionary.pascal = 'pascal'          # originally otherUnitType.pascal
StandardUnitDictionary.percent = 'percent'        # originally otherUnitType.percent
StandardUnitDictionary.permil = 'permil'          # originally otherUnitType.permil
StandardUnitDictionary.pint = 'pint'              # originally otherUnitType.pint
StandardUnitDictionary.poundPerAcre = 'poundPerAcre'# originally otherUnitType.poundPerAcre
StandardUnitDictionary.poundPerInchSquared = 'poundPerInchSquared'# originally otherUnitType.poundPerInchSquared
StandardUnitDictionary.poundsPerSquareInch = 'poundsPerSquareInch'# originally otherUnitType.poundsPerSquareInch
StandardUnitDictionary.quart = 'quart'            # originally otherUnitType.quart
StandardUnitDictionary.second = 'second'          # originally otherUnitType.second
StandardUnitDictionary.siemen = 'siemen'          # originally otherUnitType.siemen
StandardUnitDictionary.siemens = 'siemens'        # originally otherUnitType.siemens
StandardUnitDictionary.siemensPerCentimeter = 'siemensPerCentimeter'# originally otherUnitType.siemensPerCentimeter
StandardUnitDictionary.siemensPerMeter = 'siemensPerMeter'# originally otherUnitType.siemensPerMeter
StandardUnitDictionary.sievert = 'sievert'        # originally otherUnitType.sievert
StandardUnitDictionary.squareCentimeters = 'squareCentimeters'# originally otherUnitType.squareCentimeters
StandardUnitDictionary.squareFoot = 'squareFoot'  # originally otherUnitType.squareFoot
StandardUnitDictionary.squareKilometers = 'squareKilometers'# originally otherUnitType.squareKilometers
StandardUnitDictionary.squareMeter = 'squareMeter'# originally otherUnitType.squareMeter
StandardUnitDictionary.squareMeterPerKilogram = 'squareMeterPerKilogram'# originally otherUnitType.squareMeterPerKilogram
StandardUnitDictionary.squareMile = 'squareMile'  # originally otherUnitType.squareMile
StandardUnitDictionary.squareMillimeters = 'squareMillimeters'# originally otherUnitType.squareMillimeters
StandardUnitDictionary.squareYard = 'squareYard'  # originally otherUnitType.squareYard
StandardUnitDictionary.tesla = 'tesla'            # originally otherUnitType.tesla
StandardUnitDictionary.tonnePerHectare = 'tonnePerHectare'# originally otherUnitType.tonnePerHectare
StandardUnitDictionary.tonnePerYear = 'tonnePerYear'# originally otherUnitType.tonnePerYear
StandardUnitDictionary.tonnesPerYear = 'tonnesPerYear'# originally otherUnitType.tonnesPerYear
StandardUnitDictionary.volt = 'volt'              # originally otherUnitType.volt
StandardUnitDictionary.watt = 'watt'              # originally otherUnitType.watt
StandardUnitDictionary.wattPerMeterSquared = 'wattPerMeterSquared'# originally otherUnitType.wattPerMeterSquared
StandardUnitDictionary.wattPerMeterSquaredPerNanometer = 'wattPerMeterSquaredPerNanometer'# originally otherUnitType.wattPerMeterSquaredPerNanometer
StandardUnitDictionary.wattPerMeterSquaredPerNanometerPerSteradian = 'wattPerMeterSquaredPerNanometerPerSteradian'# originally otherUnitType.wattPerMeterSquaredPerNanometerPerSteradian
StandardUnitDictionary.wattPerMeterSquaredPerSteradian = 'wattPerMeterSquaredPerSteradian'# originally otherUnitType.wattPerMeterSquaredPerSteradian
StandardUnitDictionary.waveNumber = 'waveNumber'  # originally otherUnitType.waveNumber
StandardUnitDictionary.weber = 'weber'            # originally otherUnitType.weber
StandardUnitDictionary.yardPerSecond = 'yardPerSecond'# originally otherUnitType.yardPerSecond
StandardUnitDictionary.yardSquared = 'yardSquared'# originally otherUnitType.yardSquared
StandardUnitDictionary.yardsPerSecond = 'yardsPerSecond'# originally otherUnitType.yardsPerSecond
StandardUnitDictionary._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'StandardUnitDictionary', StandardUnitDictionary)
_module_typeBindings.StandardUnitDictionary = StandardUnitDictionary
