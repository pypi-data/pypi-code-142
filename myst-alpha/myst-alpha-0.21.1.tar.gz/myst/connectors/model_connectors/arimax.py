import enum
from typing import Optional, Sequence, Union
from uuid import UUID

from myst.connectors.model_connector import ModelConnector
from myst.core.time.time_delta import TimeDelta


@enum.unique
class GroupName(str, enum.Enum):
    FEATURES = "features"
    TARGETS = "targets"


@enum.unique
class LabelIndexer(str, enum.Enum):
    LOC = "loc"
    SCALE = "scale"


class ARIMAX(ModelConnector):
    def __init__(
        self,
        run_inputs_time_delta: Optional[TimeDelta] = None,
        auto_regressive_orders: Optional[Union[int, Sequence[int]]] = None,
        integration_order: Optional[int] = None,
        moving_average_orders: Optional[Union[int, Sequence[int]]] = None,
        trend_polynomial_terms: Optional[Sequence[bool]] = None,
        measurement_error: Optional[bool] = None,
        time_varying_regression: Optional[bool] = None,
        mle_regression: Optional[bool] = None,
        enforce_stationarity: Optional[bool] = None,
        enforce_invertibility: Optional[bool] = None,
        hamilton_representation: Optional[bool] = None,
    ):
        super().__init__(
            uuid=UUID("a921bb8c-2699-4dd4-ad8e-a5f32d02555a"),
            parameters=dict(
                run_inputs_time_delta=run_inputs_time_delta,
                auto_regressive_orders=auto_regressive_orders,
                integration_order=integration_order,
                moving_average_orders=moving_average_orders,
                trend_polynomial_terms=trend_polynomial_terms,
                measurement_error=measurement_error,
                time_varying_regression=time_varying_regression,
                mle_regression=mle_regression,
                enforce_stationarity=enforce_stationarity,
                enforce_invertibility=enforce_invertibility,
                hamilton_representation=hamilton_representation,
            ),
        )
