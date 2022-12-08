import logging
import os
from dataclasses import InitVar, dataclass
from pathlib import Path
from typing import Dict, List, Optional

import yaml
from dataclass_type_validator import dataclass_validate

from genomic_references.annotation import Annotation
from genomic_references.base_dir import BaseDir
from genomic_references.helpers import depends, existing_dir, uniq_file

METADATA_FILE = "meta_data.yaml"


@dataclass_validate
@dataclass
class GenomicReference:
    reference_dir: Path
    genome_version: str
    gencode_version: Optional[int] = None
    refseq_version: Optional[int] = None
    ensembl_release: Optional[int] = None
    init_venv: InitVar[bool] = True  # To handle OncoIT, It should be removed asap

    def __post_init__(self, init_venv):
        with open(self.reference_dir / METADATA_FILE, "r") as meta_data_file:
            data = yaml.safe_load(meta_data_file)
            self.species = data[self.genome_version]["species"]
            self.version = data[self.genome_version]["version"]
        if init_venv:
            os.environ["FASTA"] = str(self.fasta)
            os.environ["GENOME"] = self.version

    @property
    def path(self) -> Path:
        path = self.reference_dir / self.species / self.version
        if not path.is_dir():
            raise FileNotFoundError(
                f"There is no reference directory for this {self.genome_version}." " Consider update the metadata_file"
            )
        return path

    @property
    def fasta(self) -> Path:  # genome_fasta_file
        return uniq_file(
            [path for path in self.path.iterdir() if path.suffix in [".fa", ".fasta"] and "genome" in path.name]
        )

    @property
    @depends("gencode_version")
    def uhrr_bams(self) -> List[Path]:
        bam_files = [
            path
            for path in existing_dir(self.path / "uhrr" / f"gencode_v{self.gencode_version}").iterdir()
            if path.suffix in [".bam"]
        ]
        if len(bam_files) == 0:
            raise FileNotFoundError(
                "0 bam found in reference directory ({})".format(
                    Path(self.path, "uhrr", f"gencode_v{self.gencode_version}")
                )
            )
        return bam_files

    @property
    def annotation(self) -> Annotation:
        return Annotation(self, self.path / "annotation")

    @property
    def tools(self) -> BaseDir:
        return BaseDir(self, self.path / "tool")

    @property
    def databases(self) -> BaseDir:
        return BaseDir(self, self.path / "databases")

    @property
    def commons(self) -> BaseDir:
        return BaseDir(self, self.reference_dir / self.species / "commons")

    @staticmethod
    def get_available_genomes(ref_dir_path: Path, logger: logging = logging) -> Dict[str, Path]:
        available_genomes = {}
        with open(ref_dir_path / METADATA_FILE, "r") as meta_data_file:
            data = yaml.safe_load(meta_data_file)
        for key in data.keys():
            path = ref_dir_path / data[key]["species"] / data[key]["version"]
            if not path.is_dir():
                logger.warning(f"{key} is defined in metadata file but no directory is corresponding to {path}")
                available_genomes[key] = None
            else:
                available_genomes[key] = path
        return available_genomes
