from datetime import datetime
from pathlib import Path

from pandas import notna, read_csv
import vcfpy
from vcfpy import DEL, INS, SNV, MNV, Header, HeaderLine, SamplesInfos, Substitution

import bearclaw


def _build_header() -> Header:
    """Construct VCF header with meta data."""
    header = Header(samples=SamplesInfos(sample_names=[]))
    header.add_line(
        HeaderLine(key="fileformat", value="VCFv4.3"),
    )
    header.add_line(
        HeaderLine(key="fileDate", value=datetime.now().strftime(r"%Y%m%d")),
    )
    header.add_line(
        HeaderLine(key="source", value=f"Bearclaw {bearclaw.__version__}"),
    )
    header.add_line(HeaderLine(key="reference", value="GRCh37"))
    header.add_line(HeaderLine(key="platform", value="Derived from TSO500"))

    header.add_filter_line({"ID": "PASS", "Description": "All filters passed"})
    # Write info lines.
    header.add_info_line(
        {
            "ID": "AF",
            "Number": "A",  # One per alternate allele.
            "Type": "Float",
            "Description": "Allele Frequency",
        }
    )

    header.add_info_line(
        {
            "ID": "DP",
            "Number": 1,
            "Type": "Integer",
            "Description": "Total Depth",
        }
    )

    return header


def tmb_trace_to_vcf(input_tsv: Path, output_vcf: Path):
    """Convert *_TMB_Trace.tsv from TSO500 run to VCF format.

    Keeps only the variants that are marked as `IncludedInTMBNumerator`.
    """
    variant_dataframe = read_csv(input_tsv, sep=r"\t")
    tmb_variants = variant_dataframe[variant_dataframe.IncludedInTMBNumerator]
    header = _build_header()
    with vcfpy.Writer.from_path(output_vcf, header) as writer:
        for _, row in tmb_variants.iterrows():
            info = {"DP": row["Depth"], "AF": [row["VAF"]]}
            variant_type = (
                row[["VariantType"]]
                .map({"SNV": SNV, "MNV": MNV, "insertion": INS, "deletion": DEL})
                .squeeze()
            )
            variant_id = "."
            if notna(row["CosmicIDs"]):
                variant_id = row["CosmicIDs"]

            alternate = Substitution(type_=variant_type, value=row["AltCall"])
            record = vcfpy.Record(
                CHROM=row["Chromosome"],
                POS=row["Position"],
                ID=[variant_id],
                REF=row["RefCall"],
                ALT=[alternate],
                INFO=info,
                FILTER=["PASS"],
                QUAL=".",
            )
            writer.write_record(record)
