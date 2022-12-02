from pathlib import Path
from unittest import TestCase

from pandas import DataFrame

from bearclaw.feature_extraction import _get_cosmic_feature_names
from bearclaw.io import extract_mutation_spectra
from bearclaw.preprocessing import VariantDataGenerator
from bearclaw.transforms import mutational_signature_from_trace, spectrum_from_trace

TEST_RESOURCES = Path(__file__).parent.resolve() / "resources"
TEST_VCF_GRCH37 = TEST_RESOURCES / "GRCh37"
TEST_TSO500 = TEST_RESOURCES / "tso500"


class TestSpectra(TestCase):
    def test_whole_genome_sbs96_spectra(self):
        """Test whole genome single base substitution spectrum computation."""
        spectra = extract_mutation_spectra(TEST_VCF_GRCH37 / "sample1.vcf", exome=False)
        sbs_matrix = spectra["single_base_substitutions"].squeeze()

        # This is a synonymous variant: chr1:11181327 C>T
        # ACA => ATA; A[C>T]A
        self.assertEqual(sbs_matrix.loc["A[C>T]A"], 1)

        # This is a non-synonymous variant: chr1:115256529 T>A
        # TTG => TAG;  T[T>A]G
        # chr1:115256529
        self.assertEqual(sbs_matrix.loc["T[T>A]G"], 1)

        # This is a synonymous variant: chr4:1803556 C>G
        # CCC => CGC; C[C>G]C.
        self.assertEqual(sbs_matrix.loc["C[C>G]C"], 1)

        # This is a non-synonymous variant: chr5:112128191 C>T
        # ACG => ATG; A[C>T]G;
        #
        self.assertEqual(sbs_matrix.loc["A[C>T]G"], 1)

        # This is a non-synonymous variant: chr4:1807803 G>A
        # In pyrimidine (T, C) first notation: GCG => GTG (original, CGC > CAC);
        # G[C>T]G.
        self.assertEqual(sbs_matrix.loc["G[C>T]G"], 1)

        # This is a snonymous variant: ChrX:149162806
        # CTT => CAT; C[T>A]T;
        self.assertEqual(sbs_matrix.loc["C[T>A]T"], 1)

        # Verify that the remainder is zero.
        self.assertEqual(sbs_matrix.sum(), 6)

    def test_compressed_wgs_sbs96_spectra(self):
        """Test that a spectrum can be generated from a gzipped VCF file."""
        spectra = extract_mutation_spectra(
            TEST_VCF_GRCH37 / "sample1.vcf.gz", exome=False
        )
        sbs_matrix = spectra["single_base_substitutions"].squeeze()

        # Verify that the remainder is zero.
        self.assertEqual(sbs_matrix.sum(), 6)

    def test_whole_genome_indel_spectra(self):
        """Test whole genome indel spectrum computation."""
        spectra = extract_mutation_spectra(TEST_VCF_GRCH37 / "sample1.vcf", exome=False)
        indel_matrix = spectra["indel"].squeeze()

        # This is a synonymous indel: chrx:149914846.
        self.assertEqual(indel_matrix.loc["1:Del:T:2"], 1)

        # This is a non-synonymous indel (frameshift) chr11:209584.
        self.assertEqual(indel_matrix.loc["1:Del:C:1"], 1)

        # This is a non-synonymous indel (frameshift): chr1:149785104.
        self.assertEqual(indel_matrix.loc["1:Del:C:2"], 1)

        # This is a non-synonymous indel: chr9:133759489.
        self.assertEqual(indel_matrix.loc["3:Del:R:4"], 1)

        self.assertEqual(indel_matrix.sum(), 4)

    def test_exome_sbs96_spectra(self):
        """Test exome single base substitution spectrum computation."""
        spectra = extract_mutation_spectra(TEST_VCF_GRCH37 / "sample1.vcf", exome=True)
        sbs_matrix = spectra["single_base_substitutions"].squeeze()

        # This is a synonymous variant: chr1:11181327 C>T
        # ACA => ATA; A[C>T]A
        self.assertEqual(sbs_matrix.loc["A[C>T]A"], 1)

        # This is a non-synonymous variant: chr1:115256529 T>A
        # TTG => TAG;  T[T>A]G
        # chr1:115256529
        self.assertEqual(sbs_matrix.loc["T[T>A]G"], 1)

        # This is a synonymous variant: chr4:1803556 C>G
        # CCC => CGC; C[C>G]C.
        self.assertEqual(sbs_matrix.loc["C[C>G]C"], 1)

        # This is a non-synonymous variant: chr5:112128191 C>T
        # ACG => ATG; A[C>T]G;
        #
        self.assertEqual(sbs_matrix.loc["A[C>T]G"], 1)

        # This is a non-synonymous variant: chr4:1807803 G>A
        # In pyrimidine (T, C) first notation: GCG => GTG (original, CGC > CAC);
        # G[C>T]G.
        self.assertEqual(sbs_matrix.loc["G[C>T]G"], 1)

        # This is a snonymous variant: ChrX:149162806
        # CTT => CAT; C[T>A]T;
        # N.B. This is an intronic variant not in the exome.
        self.assertEqual(sbs_matrix.loc["C[T>A]T"], 0)

        # Verify that the remainder is zero.
        self.assertEqual(sbs_matrix.sum(), 5)

    def test_exome_indel_spectra(self):
        """Test exome spectrum computation."""
        spectra = extract_mutation_spectra(TEST_VCF_GRCH37 / "sample1.vcf", exome=True)
        indel_matrix = spectra["indel"].squeeze()

        # This is a synonymous indel: chrx:149914846.
        self.assertEqual(indel_matrix.loc["1:Del:T:2"], 0)

        # This is a non-synonymous indel (frameshift): chr1:149785104.
        self.assertEqual(indel_matrix.loc["1:Del:C:2"], 1)

        # This is a non-synonymous indel (frameshift) chr11:209584.
        self.assertEqual(indel_matrix.loc["1:Del:C:1"], 1)

        # This is a non-synonymous indel: chr9:133759489.
        self.assertEqual(indel_matrix.loc["3:Del:R:4"], 1)

        self.assertEqual(indel_matrix.sum(), 3)


class TestTSO500Trace(TestCase):
    def setUp(self):
        """Initialise dataframe with TSO500 trace samples."""
        self.dataframe = DataFrame(
            {
                "trace": [str(TEST_TSO500 / "example_TMB_Trace.tsv")],
                "coverage": [3],
                "class": [0],
            },
            index=["dummy1"],
        )

    def test_spectrum(self):
        """Test correct transitions are extracted from TSO500 TMB trace file."""
        dg = VariantDataGenerator(transform=spectrum_from_trace)
        X = dg.flow_from_dataframe(self.dataframe, x_col="trace", class_mode=None)
        # At location chr6:32163456 C[G>A]A <==> T[C>T]G.
        self.assertEqual(X.loc["dummy1", "T[C>T]G"], 1)
        # chr3:134825333 G[C>T]T
        self.assertEqual(X.loc["dummy1", "G[C>T]T"], 1)
        # chr1:17350501	TC>T (deletion of a C).
        self.assertEqual(X.loc["dummy1", "1:Del:C:1"], 1)

    def test_signature(self):
        """Test that signatures are generated from example TMB_Trace.tsv file."""
        dg = VariantDataGenerator(
            transform=lambda x: mutational_signature_from_trace(
                x, filter_seq_artefact_signatures=False
            )
        )
        signature_names = _get_cosmic_feature_names(
            representation="single_base_substitutions", signatures=True
        )
        X = dg.flow_from_dataframe(self.dataframe, x_col="trace", class_mode=None)
        x_dummy1 = X.loc["dummy1"]
        self.assertGreater(x_dummy1[signature_names].sum(), 0)
