from functools import wraps
from pathlib import Path
from shutil import copyfileobj, copyfile
from tempfile import TemporaryDirectory
import gzip

from SigProfilerMatrixGenerator.scripts import SigProfilerMatrixGeneratorFunc as matGen
from pandas import DataFrame, Series

from bearclaw.io import tso, vcf
from bearclaw.feature_extraction import _get_cosmic_feature_names


def from_tso500_trace(method):
    """Decorate method with a TSO500 TMB trace to VCF conversion preprocessing step."""

    @wraps(method)
    def decorated_transform(input_trace_tsv: Path, *args, **kwargs):
        with TemporaryDirectory() as tmp_dir:
            output_vcf = Path(tmp_dir) / input_trace_tsv.name.replace("tsv", "vcf")
            tso.tmb_trace_to_vcf(input_trace_tsv, output_vcf)
            x_transformed = method(output_vcf, *args, **kwargs)
        return x_transformed

    return decorated_transform


def extract_mutation_spectra(input_vcf: Path, exome: bool = True) -> dict[str, Series]:
    """Classify variants according to mutation type and pool per sample and type.

    Uses SigProfilerMatrixGenerator [1] with GRCh37 to extract the following
    classes:
    - 96 single base substitutions,
    - 78 doublet base substitutions,
    - 83 indels.

    Args:
        input_vcf: A VCF file with variants used to construct spectrum.

    Returns: Dictionary of series with number of mutations per mutation type,
        where the keys are the classes: `single_base_substitutions`,
        `doublet_base_substitutions`, and `indel`.

    [1]: Bergstrom EN, Huang MN, Mahto U, Barnes M, Stratton MR, Rozen SG, and
        Alexandrov LB (2019) SigProfilerMatrixGenerator: a tool for visualizing
        and exploring patterns of small mutational events. BMC Genomics 20,
        Article number: 685.
    """
    # Provision temporary folder to run SigProfilerMatrixGenerator.
    with TemporaryDirectory() as tmp_dir:
        # Decompress VCF file for SigProfilerMatrixGenerator.
        if input_vcf.name.endswith("gz"):
            target_vcf = Path(tmp_dir) / input_vcf.name.removesuffix(".gz")
            with gzip.open(input_vcf, "rb") as fo_gz:
                with open(target_vcf, "wb") as fo_out:
                    copyfileobj(fo_gz, fo_out)
        else:
            target_vcf = Path(tmp_dir) / input_vcf.name
            copyfile(str(input_vcf), str(target_vcf))

        # Unique project name.
        name = "mutation-class"
        matrices = matGen.SigProfilerMatrixGeneratorFunc(
            project=name,
            genome="GRCh37",
            vcfFiles=tmp_dir,
            plot=False,
            exome=exome,
            seqInfo=False,
        )

    index = input_vcf.name.split(".")[0]

    sbs96_columns = _get_cosmic_feature_names(
        "single_base_substitutions", signatures=False
    )
    db78_columns = _get_cosmic_feature_names(
        "doublet_base_substitutions", signatures=False
    )
    indel_columns = _get_cosmic_feature_names("indel", signatures=False)
    X_SBS96 = DataFrame(0, columns=sbs96_columns, index=[index])
    X_DB78 = DataFrame(0, columns=db78_columns, index=[index])
    X_ID83 = DataFrame(0, columns=indel_columns, index=[index])

    if "96" in matrices:
        if matrices["96"] is not None:
            X_SBS96 = matrices["96"].transpose()
    if "DINUC" in matrices:
        if matrices["DINUC"] is not None:
            X_DB78 = matrices["DINUC"].transpose()
    if "ID" in matrices:
        if matrices["ID"] is not None:
            X_ID83 = matrices["ID"].transpose()

    return {
        "single_base_substitutions": X_SBS96,
        "doublet_base_substitutions": X_DB78,
        "indel": X_ID83,
    }
