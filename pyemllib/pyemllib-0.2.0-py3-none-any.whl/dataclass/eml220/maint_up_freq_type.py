from enum import Enum

__NAMESPACE__ = "https://eml.ecoinformatics.org/dataset-2.2.0"


class MaintUpFreqType(Enum):
    ANNUALLY = "annually"
    AS_NEEDED = "asNeeded"
    BIANNUALLY = "biannually"
    CONTINUALLY = "continually"
    DAILY = "daily"
    IRREGULAR = "irregular"
    MONTHLY = "monthly"
    NOT_PLANNED = "notPlanned"
    WEEKLY = "weekly"
    UNKNOWN = "unknown"
    UNKOWN = "unkown"
    OTHER_MAINTENANCE_PERIOD = "otherMaintenancePeriod"
