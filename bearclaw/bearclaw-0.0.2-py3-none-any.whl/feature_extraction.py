from pathlib import Path
from typing import Literal

from pandas import DataFrame, read_csv
from sklearn.decomposition import NMF


RESOURCE_DIR = Path(__file__).parent.resolve() / "resources"

_COSMIC_MUTATIONAL_SIGNATURES = {
    "single_base_substitutions": RESOURCE_DIR / "COSMIC_v3.3_SBS_GRCh37.txt",
    "doublet_base_substitutions": RESOURCE_DIR / "COSMIC_v3.3_DBS_GRCh37.txt",
    "indel": RESOURCE_DIR / "COSMIC_v3.3_ID_GRCh37.txt",
    "cnv": RESOURCE_DIR / "COSMIC_v3.3_CN_GRCh37.txt",
}

_POSSIBLE_SBS_SEQUENCING_ARTEFACTS = [
    # Extracted from https://cancer.sanger.ac.uk/signatures/sbs/.
    "SBS27",
    "SBS43",
    "SBS45",
    "SBS46",
    "SBS47",
    "SBS48",
    "SBS49",
    "SBS50",
    "SBS51",
    "SBS52",
    "SBS53",
    "SBS54",
    "SBS55",
    "SBS56",
    "SBS57",
    "SBS58",
    "SBS59",
    "SBS60",
]

_POSSIBLE_CN_SEQUENCING_ARTEFACTS = ["CN22", "CN23", "CN24"]


def _get_cosmic_feature_names(
    representation: Literal[
        "single_base_substitutions",
        "doublet_base_substitutions",
        "indel",
        "cnv",
    ],
    signatures: bool = True,
) -> list:
    """Fetch feature/signature names of a given spectrum.

    Args:
        signatures: If True, return COSMIC signature names, otherwise the
            transition names.
    """
    # Extract from mutational signature file.
    dataframe = read_csv(
        _COSMIC_MUTATIONAL_SIGNATURES[representation], sep="\t", index_col=0
    )
    if signatures:
        return dataframe.columns.to_list()
    return dataframe.index.to_list()


class CosmicNMF(NMF):
    """Load NMF model fit with COSMIC GRCh37 signatures.

    Given the mutational signature H, the `transform` method computes `W` so that
    X = WH
    where X is the mutation spectrum.
    """

    def __init__(
        self,
        cosmic_signature: Literal[
            "single_base_substitutions", "doublet_base_substitutions", "indel", "cnv"
        ],
        tol: float = 1e-6,
        max_iter: int = 10000,
    ):
        """
        Load NMF COSMIC GRCh37 mutational signature checkpoint.

        Args:
            cosmic_signature: Input features correspond to 96 single base
                substution (SBS), 78 double base substitutions (DBS), 83
                indels mutational spectrum, or 48 copy number variant classes.
        """
        self.cosmic_signature = cosmic_signature
        H = read_csv(
            _COSMIC_MUTATIONAL_SIGNATURES[cosmic_signature], sep="\t", index_col=0
        ).T
        self.n_components_, self.n_features_in_ = H.shape

        super().__init__(
            n_components=self.n_components_,
            max_iter=max_iter,
            solver="cd",
            init="nndsvda",
            tol=tol,
        )
        self.components_ = H.to_numpy()
        self.feature_names_in_ = H.columns
        self.feature_names_out_ = H.index

    def transform(self, X):
        """Transform back to pandas dataframe."""
        X_numpy = super().transform(X)
        return DataFrame(X_numpy, index=X.index, columns=self.feature_names_out_)
