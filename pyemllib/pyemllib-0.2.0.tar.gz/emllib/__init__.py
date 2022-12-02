import logging
from decimal import Decimal

from lxml import etree

from emllib.dataclass.eml220 import (
    Coverage,
    DatasetType,
    Eml,
    GeographicCoverage,
    I18NNonEmptyStringType,
    ParagraphType,
    Person,
    PhysicalDistributionType,
    PhysicalOnlineType,
    PhysicalType,
    ResponsibleParty,
    SingleDateTimeType,
    TemporalCoverage,
    TextType,
)

logger = logging.getLogger(__name__)


class EMLizer:
    """# Very simplistic class to build an EML doc from dataClass
    - with xsd validation
    - with XML serialization
    """

    def __init__(self, **kwargs) -> None:
        """any arbitrary kwargs are allowed (no enforcement)

        keyword args:
            package_id (str): package ID
            title (str): Titre du dataPackage
            lang (str): langue par défaut
            creator (str): créateur
            abstract (str): abstract

        """

        self.__dict__.update(kwargs)
        # self.mapper = self.get_mapper_class(**kwargs)

    # def get_mapper_class(self, **kwargs):
    #     if isinstance(self.source, MD_Metadata):
    #         return ISOMapper(source_obj=self.source, remote_system=kwargs['source_cat'])
    #     elif isinstance(self.source, dict):
    #         return DataverseJsonMapper(source_obj=self.source, remote_system=kwargs['source_cat'])
    #     else:StringIO
    #         typeobj = type(self.source)
    #         raise Exception("La source est d'un type (%s) non encore pris en charge !" % typeobj)

    def get_identification(self):
        pass

    def get_package_id(self):
        return self.package_id

    def get_default_system(self):
        return "PNDB"

    def get_default_lang(self):
        return self.lang

    def get_identifier(self):
        pass

    def get_alternate_identifier(self):
        pass

    def get_title(self):
        return self.title

    def get_abstract(self):
        return self.abstract

    def get_contact(self):
        return self.get_creator()

    def get_creator(self):
        return self.creator

    def get_party(self):
        pass

    def get_geo_coverage(self):
        geo_coverage = [GeographicCoverage()]
        geo_coverage[0].geographic_description = "Very nice place"
        geo_coverage[0].bounding_coordinates = GeographicCoverage.BoundingCoordinates()

        # arbitraty bbox !
        geo_coverage[0].bounding_coordinates.east_bounding_coordinate = Decimal("10.0")
        geo_coverage[0].bounding_coordinates.west_bounding_coordinate = Decimal("-5.0")
        geo_coverage[0].bounding_coordinates.north_bounding_coordinate = Decimal("50.0")
        geo_coverage[0].bounding_coordinates.south_bounding_coordinate = Decimal("40.0")

        return geo_coverage

    def get_temporal_coverage(self):
        temporal_coverage = [Coverage().TemporalCoverage()]

        # arbitrary range
        temporal_coverage[0].range_of_dates = TemporalCoverage.RangeOfDates()
        temporal_coverage[0].range_of_dates.begin_date = SingleDateTimeType("1970-01-01")
        temporal_coverage[0].range_of_dates.end_date = SingleDateTimeType("2022-01-01")

        return temporal_coverage

    def get_keyword_set(self):
        pass

    def get_intellectual_rights(self):
        ir = TextType()
        ir.content = [
            ParagraphType(
                content=[
                    "This work is licensed under the Creative Commons Attribution 4.0 International License.",
                    "To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.",
                ]
            )
        ]
        return ir

    def get_datatable(self):
        pass

    def get_spatialRaster(self):
        pass

    def get_spatialVector(self):
        pass

    def get_other_entity(self):
        pass

    def get_coverage(self):
        coverage = Coverage()
        coverage.geographic_coverage = self.get_geo_coverage()
        coverage.temporal_coverage = self.get_temporal_coverage()
        return coverage

    def build_eml(self) -> Eml:
        eml = Eml(system=self.get_default_system())
        eml.package_id = self.get_package_id()
        dataset = DatasetType()
        lang = self.get_default_lang()

        # Titre
        dataset.title = I18NNonEmptyStringType()
        dataset.title.lang = lang
        dataset.title.content = ["[PNDB] " + self.get_title()]

        # Abstract
        dataset.abstract = TextType()
        dataset.abstract.content = [ParagraphType(lang=lang, content=[self.get_abstract()])]

        # Contact
        dataset.contact = ResponsibleParty(individual_name=[Person(sur_name=self.get_contact())])

        # Creator
        dataset.creator = ResponsibleParty(individual_name=[Person(sur_name=self.get_contact())])

        # AP
        dataset.associated_party = self.get_party()

        # keywords
        dataset.keyword_set = self.get_keyword_set()

        # coverage
        dataset.coverage = self.get_coverage()

        # datafiles
        if self.get_spatialVector():
            dataset.spatial_vector = self.get_spatialVector()
        if self.get_spatialRaster():
            dataset.spatial_raster = self.get_spatialRaster()
        if self.get_other_entity():
            dataset.other_entity = self.get_other_entity()

        # intellectual rights
        dataset.intellectual_rights = self.get_intellectual_rights()

        eml.dataset = dataset
        return eml

    def to_string(self, xml_declaration=True):
        from xsdata.formats.dataclass.serializers import XmlSerializer
        from xsdata.formats.dataclass.serializers.config import SerializerConfig

        config = SerializerConfig(
            pretty_print=True,
            xml_declaration=xml_declaration,
            schema_location="https://eml.ecoinformatics.org/eml-2.2.0 xsd/eml.xsd",
        )
        serializer = XmlSerializer(config=config)
        ns_map = {
            "eml": "https://eml.ecoinformatics.org/eml-2.2.0",
            "xsi": "http://www.w3.org/2001/XMLSchema-instance",
            # "xsi": "http://www.w3.org/2001/XMLSchema-instance",
        }
        return serializer.render(self.build_eml(), ns_map=ns_map)

    def to_file(self, path="./eml.xml"):
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.to_string())

    def validate(self):
        from emllib.utils import validate

        return validate(etree.fromstring(self.to_string(xml_declaration=False)))


if __name__ == "__main__":  # pragma: no cover
    my_eml = EMLizer(package_id="ID", title="Mon titre", lang="fr", creator="Mon Createur", abstract="Mon abstract")
    print(my_eml.to_string())

    # my_eml.to_file()

    if my_eml.validate().bool:
        print("This EML file seems valid ;)")
    else:
        print("This EML file does not seem valid !")
        print(my_eml.validate().reason)
