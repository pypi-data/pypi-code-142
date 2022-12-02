import importlib.resources
import logging
from collections import namedtuple

from lxml import etree
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser

from emllib.dataclass.eml220 import Eml

logger = logging.getLogger(__name__)

EML_220_SCHEMA_LOCATION = "schemas/eml/eml-2.2.0/eml.xsd"


def validate(xml_doc) -> namedtuple:
    """Validates EML doc against EML 2.2.0 xsd and gives reason if not validated

    Args:
        xml_doc (etree): Etree but a path string should do

    Returns:
        namedtuple (bool, str): example (False, "attribute X is missing")
    """
    is_eml_valid = namedtuple("is_eml_valid", ["bool", "reason"])
    # XML DOM instance of EML document
    if not isinstance(xml_doc, etree._Element):
        try:
            xml_doc = etree.parse(xml_doc)
        except Exception as e:
            raise e

    # XML Schema validator instance for EML 2.2.0 schema - assumes local copy of schema
    pkg_res = importlib.resources.files(__package__)
    xml_validator = etree.XMLSchema(file=pkg_res / EML_220_SCHEMA_LOCATION)

    # Validate method returns a boolean
    is_valid = xml_validator.validate(xml_doc)

    if is_valid:
        return is_eml_valid(True, "Congrats!")
    else:
        msg = []
        for error in xml_validator.error_log:
            # logger.warning("Erreur sur la ligne %s: %s" % (error.line, error.message))
            msg.append("Erreur sur la ligne %s: %s" % (error.line, error.message))
        return is_eml_valid(False, "\n".join(msg))


def eml_from_filename(filename) -> Eml:
    """Returns Eml object from eml path

    Args:
        filename (str): path to eml xml file

    Returns:
        Eml: EML dataclass object
    """
    parser = XmlParser(context=XmlContext())
    eml = parser.parse(filename, Eml)
    return eml


def eml_from_string(eml_string) -> Eml:
    """Returns Eml object from eml path

    Args:
        eml_string (stringIO): path to eml xml file

    Returns:
        Eml: EML dataclass object
    """
    parser = XmlParser(context=XmlContext())
    eml = parser.from_string(eml_string, Eml)
    return eml


def datapaper_from_eml(eml: Eml):
    """Renvoie un objet markdown avec "toutes" les info pour dataPaper
    On se repose sur cette issue https://github.com/NCEAS/eml/issues/269 pour le mapping des champs à extraire

    Args:
        eml (Eml): Eml dataclass object
    """

    dataset = eml.dataset
    titles = [p.content[0] for p in dataset.title]
    authors = [
        " ".join(p.individual_name[0].given_name[0].content) + " " + p.individual_name[0].sur_name.content[0]
        for p in dataset.creator
    ]
    pub_date = dataset.pub_date  # noqa F841
    keywords = dataset.keyword_set  # noqa F841
    geo_cov = dataset.coverage.geographic_coverage[0]
    temporal_cov = dataset.coverage.temporal_coverage[0]
    abstract = dataset.abstract.content[0].text
    doi = eml.package_id  # noqa F841
    data_synopsis = dataset.purpose  # noqa F841
    data_package_struct = dataset.data_table  # noqa F841

    from mdutils.mdutils import MdUtils

    mdFile = MdUtils(file_name="eml_data_paper", title=" ; ".join(titles))
    mdFile.new_paragraph(" - ".join(authors))
    # mdFile.new_paragraph(pub_date)
    mdFile.new_header(level=1, title="Introduction")
    mdFile.new_paragraph(abstract)
    mdFile.new_header(level=1, title="Coverage")
    mdFile.new_header(level=1, title="Geographic Coverage")
    mdFile.new_paragraph(geo_cov.geographic_description)
    mdFile.new_header(level=1, title="Temporal Coverage")
    mdFile.new_paragraph(temporal_cov.geographic_description)

    mdFile.create_md_file()

    return mdFile


if __name__ == "__main__":  # pragma: no cover
    eml = eml_from_filename("tests/resources/eml-data-paper.xml")
    dp = datapaper_from_eml(eml)
