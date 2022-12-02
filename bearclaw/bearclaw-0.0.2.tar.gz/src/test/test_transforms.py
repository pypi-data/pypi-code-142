from pathlib import Path
from unittest import TestCase

from numpy.linalg import norm
from numpy.testing import assert_almost_equal, assert_array_almost_equal
from pandas import DataFrame, read_csv

from bearclaw.feature_extraction import (
    _get_cosmic_feature_names,
    _POSSIBLE_SBS_SEQUENCING_ARTEFACTS,
    _COSMIC_MUTATIONAL_SIGNATURES,
    CosmicNMF,
)
from bearclaw.preprocessing import VariantDataGenerator
from bearclaw.transforms import mutational_signature, non_synonymous_spectrum, spectrum

TEST_RESOURCES = Path(__file__).parent.resolve() / "resources"
TEST_TSO500 = TEST_RESOURCES / "tso500"
TEST_VCF_GRCH37 = Path(__file__).parent.resolve() / "resources" / "GRCh37"


class TestVariantDataGenerator(TestCase):
    def setUp(self):
        """Initialise data frame with samples."""
        self.dataframe = DataFrame(
            {
                "vcf": [
                    str(TEST_VCF_GRCH37 / "sample1.vcf"),
                    str(TEST_VCF_GRCH37 / "sample2.vcf"),
                ],
                "coverage": [2, 3],
                "class": [1, 0],
            },
            index=["dummy1", "dummy2"],
        )

    def test_sbs_non_synonymous_spectrum(self):
        """Test non-synonymous single base substitution spectrum."""
        dg = VariantDataGenerator(transform=non_synonymous_spectrum)

        X_spectrum, _ = dg.flow_from_dataframe(self.dataframe, x_col="vcf")
        sample_name = "dummy1"

        # Only non-synonymous variants should be present.
        self.assertEqual(X_spectrum.loc[sample_name, "T[T>A]G"], 1)
        self.assertEqual(X_spectrum.loc[sample_name, "A[C>T]G"], 1)
        self.assertEqual(X_spectrum.loc[sample_name, "G[C>T]G"], 1)

        # All other items should be zero.
        sbs_names = _get_cosmic_feature_names(
            representation="single_base_substitutions", signatures=False
        )
        self.assertEqual(X_spectrum.loc[sample_name, sbs_names].sum(), 3)

        # Overall normalisation.
        X_overall_normalised, _ = dg.flow_from_dataframe(
            self.dataframe, coverage_size=2, x_col="vcf"
        )
        self.assertEqual(X_overall_normalised.loc[sample_name, sbs_names].sum(), 3 / 2)

        # Sample wise normalisation.
        X_normalised, _ = dg.flow_from_dataframe(
            self.dataframe, coverage_size="coverage", x_col="vcf"
        )
        self.assertEqual(X_normalised.loc[sample_name, sbs_names].sum(), 3 / 2)
        assert_almost_equal(
            X_normalised.loc["dummy2", sbs_names].sum(), 1 / 3, decimal=2
        )

    def test_sbs_spectrum(self):
        """Test non-synonymous single base substitution spectrum."""
        dg = VariantDataGenerator(transform=spectrum)
        sbs_names = _get_cosmic_feature_names(
            representation="single_base_substitutions", signatures=False
        )

        X_spectrum, _ = dg.flow_from_dataframe(self.dataframe, x_col="vcf")

        # Both synonymous and non-synonymous variants can be present.
        sample1 = "dummy1"
        self.assertEqual(X_spectrum.loc[sample1, "A[C>T]A"], 1)
        self.assertEqual(X_spectrum.loc[sample1, "A[C>T]G"], 1)
        self.assertEqual(X_spectrum.loc[sample1, "C[C>G]C"], 1)
        self.assertEqual(X_spectrum.loc[sample1, "C[T>A]T"], 1)
        self.assertEqual(X_spectrum.loc[sample1, "G[C>T]G"], 1)
        self.assertEqual(X_spectrum.loc[sample1, "T[T>A]G"], 1)

        # All other items should be zero.
        self.assertEqual(X_spectrum.loc[sample1, sbs_names].sum(), 6)

        sample2 = "dummy2"
        self.assertEqual(X_spectrum.loc[sample2, "T[C>A]G"], 7)
        self.assertEqual(X_spectrum.loc[sample2, "C[C>A]G"], 1)
        self.assertEqual(X_spectrum.loc[sample2, "T[C>A]A"], 1)

        self.assertEqual(X_spectrum.loc[sample2, sbs_names].sum(), 9)

    def test_sbs_filter_sequencing_artefacts(self):
        """Verify that all SBS sequencing artefacts are removed."""
        dg = VariantDataGenerator(transform=mutational_signature)
        X, _ = dg.flow_from_dataframe(self.dataframe, keep_columns=False, x_col="vcf")

        self.assertEqual(
            len(X.columns),
            11 + 78 + 18 - len(_POSSIBLE_SBS_SEQUENCING_ARTEFACTS),
        )

    def test_sbs_mutational_signature(self):
        """Test non-synonymous single base substitution mutational signature."""
        dg = VariantDataGenerator(
            transform=lambda x: mutational_signature(
                x, filter_seq_artefact_signatures=False
            ),
        )

        signature_names = _get_cosmic_feature_names(
            representation="single_base_substitutions", signatures=True
        )

        # By inspection of SBS48 we notice the size of the coefficients:
        #
        # T[C>A]G: 7.093881e-01
        # C[C>A]G: 1.370750e-01
        # T[C>A]A: 1.240679e-01
        #
        # In other words: T[C>A]G almost maps one-to-one to SBS48.
        # Incidentally, dummy2 contains the T[C>A]G, C[C>A]G, and T[C>A]A
        # mutation in the approximate ratios. So we expect almost complete
        # SBS48 activation. Lets validate.
        W_reconstr, _ = dg.flow_from_dataframe(
            self.dataframe, decimals=None, x_col="vcf", keep_columns=False
        )

        H = read_csv(
            _COSMIC_MUTATIONAL_SIGNATURES["single_base_substitutions"],
            sep="\t",
            index_col=0,
        ).T

        # Verify that SBS48 is the most activated state.
        sample2 = "dummy2"
        self.assertEqual(W_reconstr.loc[sample2].idxmax(), "SBS48")

        X_true = DataFrame(0, columns=H.columns, index=[sample2])
        X_true.loc[sample2, "T[C>A]G"] = 7
        X_true.loc[sample2, "C[C>A]G"] = 1
        X_true.loc[sample2, "T[C>A]A"] = 1

        # Reconstruction should be less than 10 %.
        X_reconstr = W_reconstr[signature_names] @ H
        error = norm(abs(X_reconstr.loc[sample2] - X_true.loc[sample2]))
        assert_almost_equal(error / norm(X_true.loc[sample2].to_numpy()), 0, decimal=1)

    def test_commutation_normalisation_operation(self):
        """Test that deconvolution<->normalisation commutes."""

        all_sbs_signatures = _get_cosmic_feature_names(
            representation="single_base_substitutions", signatures=True
        )
        sbs_signatures = [
            c for c in all_sbs_signatures if c not in _POSSIBLE_SBS_SEQUENCING_ARTEFACTS
        ]
        sbs_spectrum = _get_cosmic_feature_names(
            representation="single_base_substitutions", signatures=False
        )
        # 1)
        # First deconvolution, then normalisation.
        deconv = VariantDataGenerator(transform=mutational_signature)
        X_normalised, _ = deconv.flow_from_dataframe(
            self.dataframe,
            coverage_size="coverage",
            decimals=None,
            x_col="vcf",
        )

        # 2)
        # First normalisation, then deconvolution.
        spectromer = VariantDataGenerator(transform=spectrum)
        X_spectrum, _ = spectromer.flow_from_dataframe(
            self.dataframe,
            coverage_size="coverage",
            x_col="vcf",
        )

        decomposer = CosmicNMF(cosmic_signature="single_base_substitutions")
        X_sbs96_deconv = decomposer.transform(X_spectrum[sbs_spectrum]).drop(
            columns=_POSSIBLE_SBS_SEQUENCING_ARTEFACTS
        )

        # Compare results.
        assert_array_almost_equal(
            X_sbs96_deconv, X_normalised[sbs_signatures], decimal=5
        )

    def test_indel_spectrum(self):
        """Test non-synonymous indel spectrum."""
        dg = VariantDataGenerator(transform=non_synonymous_spectrum)
        signature_names = _get_cosmic_feature_names(
            representation="indel", signatures=False
        )

        X_spectrum, _ = dg.flow_from_dataframe(self.dataframe, x_col="vcf")
        sample_name = "dummy1"

        # Only non-synonymous variants should be present.
        self.assertEqual(X_spectrum.loc[sample_name, "1:Del:C:2"], 1)
        self.assertEqual(X_spectrum.loc[sample_name, "1:Del:C:1"], 1)
        self.assertEqual(X_spectrum.loc[sample_name, "3:Del:R:4"], 1)

        # All other items should be zero.
        self.assertEqual(X_spectrum.loc[sample_name, signature_names].sum(), 3)
