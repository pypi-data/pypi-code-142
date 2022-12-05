from pathlib import Path

from genomic_references.base_dir import BaseDir
from genomic_references.helpers import depends, existing_file


class Annotation(BaseDir):
    @property
    @depends("gencode_version")
    def gtf_file(self) -> Path:
        return existing_file(self.path / "gtf" / f"gencode_v{self.reference.gencode_version}" / "annotation.gtf")

    @property
    @depends("gencode_version")
    def collapsed_gtf_file(self) -> Path:
        return existing_file(
            self.path / "gtf" / f"gencode_v{self.reference.gencode_version}" / "annotation.collapsed.gtf"
        )

    @property
    @depends("refseq_version")
    def refseq_bed(self) -> Path:
        return existing_file(self.path / "refseq" / f"refseq_v{self.reference.refseq_version}" / "refseq.bed")
