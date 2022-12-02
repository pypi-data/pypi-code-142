from pyclue.features.cohort import CohortFeatures
from pyclue.features.comparison import CohortComparisonFeatures
from pyclue.features.incidence_rate import IncidenceRateFeatures


class FeatureAdapter(
    CohortFeatures,
    CohortComparisonFeatures,
    IncidenceRateFeatures
):
  pass
