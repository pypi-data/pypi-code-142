from dataclasses import dataclass

from emllib.dataclass.eml220.research_project_type import ResearchProjectType

__NAMESPACE__ = "https://eml.ecoinformatics.org/project-2.2.0"


@dataclass
class ResearchProject(ResearchProjectType):
    class Meta:
        name = "researchProject"
        namespace = "https://eml.ecoinformatics.org/project-2.2.0"
