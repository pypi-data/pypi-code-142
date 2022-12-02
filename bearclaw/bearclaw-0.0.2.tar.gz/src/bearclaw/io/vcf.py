from functools import wraps
from pathlib import Path
import re
from tempfile import TemporaryDirectory
import warnings

import vcfpy
from vcfpy.exceptions import FieldInfoNotFound, VCFPyException


def non_synonymous(method):
    """Decorator that pre-filters synonymous variants from the VCF file."""

    @wraps(method)
    def decorated_transform(input_vcf: Path, *args, **kwargs):
        with TemporaryDirectory() as tmp_dir:
            target_vcf = Path(tmp_dir) / input_vcf.name.replace(".gz", "")
            filter_synonymous_variants(input_vcf, target_vcf, soft=False)
            x_transformed = method(target_vcf, *args, **kwargs)
        return x_transformed

    return decorated_transform


def _is_non_synonymous(annotation: dict) -> bool:
    """Test if an annotated variant is non-synonymous.

    Args:
        annotation: dict where keys and values are according to ANN standard.
    """
    field_names = tuple(annotation.keys())

    # The standard for the annotation field can be found here:
    # https://pcingola.github.io/SnpEff/adds/VCFannotationformat_v1.0.pdf
    annotation_field = field_names[1]
    hgsvp_field = field_names[10]
    # Only variants affecting protein.
    if annotation[hgsvp_field] != "":
        # Only variants that change amino-acid sequence.
        var_annot_values = annotation[annotation_field].split("&")
        synonymous_type = (
            "synonymous_variant",
            "stop_retained_variant",
            "start_retained_variant",
        )
        is_non_synonymous = all(
            v.strip() not in synonymous_type for v in var_annot_values
        )
        if is_non_synonymous:
            return True
    return False


def _check_vcf_ann_header(reader: vcfpy.Reader):
    """Validate header to see if INFO column has variant annotation `ANN` fields.

    Raises:
        VCFPyException: When header specifies no ANN field  or incorrect ANN keys.
    """
    with warnings.catch_warnings():
        warnings.filterwarnings("error")
        try:
            annotation = reader.header.get_info_field_info("ANN")
        except FieldInfoNotFound:
            raise VCFPyException("Missing ANN field in VCF.")

    return annotation


def _get_annotations_keys(reader: vcfpy.Reader) -> list:
    """Extract the annotation's data fields (=keys) from the VCF header.

    This corresponds to the data fields in the value corresponding to the
    `ANN` key in the `INFO`field.

    Returns:
        Keys corresponding to record ANN array.
    """
    annotation = _check_vcf_ann_header(reader)
    ann_format = annotation.description
    mo = re.search("'(.+)'", ann_format)
    ann_keys = [key.strip() for key in mo.group(1).split("|")]

    # According to standard, there are 16 annotations data fields.
    assert len(ann_keys) == 16, "Variant annotations not compatible with standard."

    return ann_keys


def _get_annotations(record: vcfpy.Record, reader: vcfpy.Reader) -> list[dict]:
    """Turn annotations data field into dictionary.

    Args:
        record: Single record in the VCF file.
        reader: VCFpy `Reader` istance with header information.

    Returns:
        Annotation dictionary per allele.
    """

    ann_keys = _get_annotations_keys(reader)
    return [
        dict(zip(ann_keys, ann_values.split("|"))) for ann_values in record.INFO["ANN"]
    ]


def filter_synonymous_variants(input_vcf: Path, filtered_vcf: Path, soft: bool = False):
    """Filter synonymous (non-amino acid sequencing changing) variants.

    Args:
        input_vcf: Variant file (possbily gzipped) to filter.
        filtered_vcf: Store filtered VCF to this (possbily gzipped) file.
        soft: When `True`, apply a soft filter that only changes the FILTER
            column (but keeps the record). When `False`, remove filtered
            records.

    Raises:
        VCFPyException: When header specifies no `ANN` field  or incorrect `ANN`
            keys.
    """
    with vcfpy.Reader.from_path(str(input_vcf)) as reader:
        # Soft filter adds the following variant FILTER.
        if soft:
            reader.header.add_filter_line(
                vcfpy.OrderedDict(
                    [
                        ("ID", "IS_SYNON"),
                        (
                            "Description",
                            "The variant is not amino-acid sequence changing.",
                        ),
                    ]
                )
            )

        with vcfpy.Writer.from_path(filtered_vcf, reader.header) as writer:
            for record in reader:
                try:
                    annotations = _get_annotations(record, reader)
                except KeyError:
                    # Filter variants without annotation.
                    if not soft:
                        continue
                    record.add_filter("IS_SYNON")
                else:
                    # Filter variants that are not non-synonymous.
                    if not any(map(_is_non_synonymous, annotations)):
                        if not soft:
                            continue
                        record.add_filter("IS_SYNON")

                writer.write_record(record)
