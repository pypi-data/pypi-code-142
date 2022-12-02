from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from bearclaw.io.vcf import filter_synonymous_variants, _is_non_synonymous


TEST_RESOURCES = Path(__file__).parent.resolve() / "resources"
TEST_VCF_GRCH37 = TEST_RESOURCES / "GRCh37"


def _count_lines(filename: Path, ignore_prefix="#") -> int:
    with open(str(filename)) as fo:
        lines = fo.readlines()
        if ignore_prefix is not None:
            return len([l for l in lines if not l.startswith(ignore_prefix)])
        return len(lines)


class TestVariantFilter(TestCase):
    synonymous_annotation = {
        "Allele": "A",
        "Annotation": "splice_region_variant&synonymous_variant",
        "Annotation_Impact": "LOW",
        "Gene_Name": "DLEU1",
        "Gene_ID": "ENSG00000176124",
        "Feature_Type": "transcript",
        "Feature_ID": "ENST00000378180",
        "Transcript_BioType": "protein_coding",
        "Rank": "2/2",
        "HGVS.c": "c.123G>A",
        "HGVS.p": "p.Val41Val",
        "cDNA.pos / cDNA.length": "389/981",
        "CDS.pos / CDS.length": "123/237",
        "AA.pos / AA.length": "41/78",
        "Distance": "",
        "ERRORS / WARNINGS / INFO": "",
    }
    empty_annotation = {
        "Allele": "",
        "Annotation": "",
        "Annotation_Impact": "",
        "Gene_Name": "",
        "Gene_ID": "",
        "Feature_Type": "",
        "Feature_ID": "",
        "Transcript_BioType": "",
        "Rank": "",
        "HGVS.c": "",
        "HGVS.p": "",
        "cDNA.pos / cDNA.length": "",
        "CDS.pos / CDS.length": "",
        "AA.pos / AA.length": "",
        "Distance": "",
        "ERRORS / WARNINGS / INFO": "",
    }

    def test_is_non_synonymous(self):
        """Test identification of non-synonymous variants by annotation."""

        self.assertFalse(_is_non_synonymous(self.synonymous_annotation))

    def test_soft_filter(self):
        """Test that correct variants are filtered but not removed."""
        sample1_vcf = TEST_VCF_GRCH37 / "sample1.vcf"
        with TemporaryDirectory() as tmp_dir:
            tmp_file = Path(tmp_dir) / "sample1.filtered.vcf"
            filter_synonymous_variants(
                input_vcf=sample1_vcf,
                filtered_vcf=tmp_file,
                soft=True,
            )

            self.assertEqual(_count_lines(sample1_vcf), _count_lines(tmp_file))

            with open(tmp_file) as fo:
                variants = [line for line in fo.readlines() if not line.startswith("#")]
                # Select filtered variants.
                filtered_variants = filter(lambda x: "IS_SYNON" in x, variants)

                # Combine chromosome and position, for easy comparison.
                positions = {":".join(var.split("\t")[:2]) for var in filtered_variants}

                # The following variants are synonymous.
                self.assertEqual(
                    set(positions),
                    {
                        "chr1:11181327",
                        "chr4:1803556",
                        "chrX:149083064",
                        "chrX:149162806",
                    },
                )

    def test_hard_filter(self):
        """Test that correct variants are filtered and removed."""
        sample1_vcf = TEST_VCF_GRCH37 / "sample1.vcf"
        with TemporaryDirectory() as tmp_dir:
            tmp_file = Path(tmp_dir) / "sample1.filtered.vcf"
            filter_synonymous_variants(
                input_vcf=sample1_vcf,
                filtered_vcf=tmp_file,
                soft=True,
            )

            self.assertEqual(_count_lines(sample1_vcf), _count_lines(tmp_file))

            with open(tmp_file) as fo:
                variants = [line for line in fo.readlines() if not line.startswith("#")]
                # only select unfiltered variants.
                unfiltered_variants = filter(lambda x: "IS_SYNON" not in x, variants)

                # Combine chromosome and position, for easy comparison.
                positions = {
                    ":".join(var.split("\t")[:2]) for var in unfiltered_variants
                }

                # The following variants are non-synonymous.
                self.assertEqual(
                    set(positions),
                    {
                        "chr1:115256529",
                        "chr5:112128191",
                        "chr4:1807803",
                        "chr1:149785104",
                        "chr11:209584",
                        "chr9:133759489",
                    },
                )
