from dataclasses import dataclass

from emllib.dataclass.eml220.semantic_annotation import SemanticAnnotation

__NAMESPACE__ = "https://eml.ecoinformatics.org/semantics-2.2.0"


@dataclass
class Annotation(SemanticAnnotation):
    class Meta:
        name = "annotation"
        namespace = "https://eml.ecoinformatics.org/semantics-2.2.0"
