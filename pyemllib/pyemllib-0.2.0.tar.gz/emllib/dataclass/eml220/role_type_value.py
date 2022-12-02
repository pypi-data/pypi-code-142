from enum import Enum

__NAMESPACE__ = "https://eml.ecoinformatics.org/party-2.2.0"


class RoleTypeValue(Enum):
    CONTENT_PROVIDER = "contentProvider"
    CUSTODIAN_STEWARD = "custodianSteward"
    OWNER = "owner"
    USER = "user"
    DISTRIBUTOR = "distributor"
    METADATA_PROVIDER = "metadataProvider"
    ORIGINATOR = "originator"
    POINT_OF_CONTACT = "pointOfContact"
    PRINCIPAL_INVESTIGATOR = "principalInvestigator"
    PROCESSOR = "processor"
    PUBLISHER = "publisher"
    AUTHOR = "author"
    EDITOR = "editor"
