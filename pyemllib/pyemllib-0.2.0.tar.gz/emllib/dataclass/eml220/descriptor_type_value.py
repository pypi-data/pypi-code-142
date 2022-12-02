from enum import Enum

__NAMESPACE__ = "https://eml.ecoinformatics.org/project-2.2.0"


class DescriptorTypeValue(Enum):
    CLIMATE = "climate"
    HYDROLOGY = "hydrology"
    SOILS = "soils"
    GEOLOGY = "geology"
    DISTURBANCE = "disturbance"
    BAILEY = "bailey"
    BIOME = "biome"
