from typing import Any
from typing import ItemsView
from typing import Iterator
from typing import KeysView
from typing import List
from typing import Mapping
from typing import Optional
from typing import Union
from typing import ValuesView

from .prometheus_metrics import decider_client_counter
from .rust_decider import Decider as PyDecider
from .rust_decider import DeciderException
from .rust_decider import DeciderFeatureNotFoundException  # noqa: F401
from .rust_decider import DeciderInitException
from .rust_decider import init
from .rust_decider import make_ctx


DEFAULT_DECISIONMAKERS = (
    "darkmode overrides targeting holdout mutex_group fractional_availability value"
)

JsonValue = Union[
    None, int, float, str, bool, List["JsonValue"], Mapping[str, "JsonValue"]
]


class Decision(Mapping[str, Any]):
    def __init__(
        self,
        variant: Optional[str],
        value: Optional[Any],
        feature_id: int,
        feature_name: str,
        feature_version: int,
        events: List[str],
    ):
        self.variant = variant
        self.value = value
        self.feature_id = feature_id
        self.feature_name = feature_name
        self.feature_version = feature_version
        self.events = events

    def keys(self) -> KeysView[str]:
        return self.__dict__.keys()

    def items(self) -> ItemsView[str, Any]:
        return self.__dict__.items()

    def values(self) -> ValuesView[Any]:
        return self.__dict__.values()

    def get(self, key: str, default=None) -> Optional[Any]:
        return self.__dict__.get(key, default)

    def __contains__(self, key: str) -> bool:
        return key in self.__dict__

    def __getitem__(self, key: str) -> Any:
        return self.__dict__[key]

    def __iter__(self) -> Iterator[str]:
        return iter(self.__dict__)

    def __len__(self) -> int:
        return len(self.__dict__)


class Decider:
    """Decider class wraps python bindings for Rust decider crate."""

    def __init__(self, path: str):
        # FIXME
        # remove py_decider in favor of _decider
        # once `get_decider()` can be deprecated in Experiments.py
        py_decider = init(DEFAULT_DECISIONMAKERS, path)
        self._validate_decider(py_decider)
        self.py_decider = py_decider

        try:
            self._decider = PyDecider(path)
        except DeciderInitException as e:
            decider_client_counter.labels(
                operation="init",
                success="false",
                error_type="init_exception",
            ).inc()
            raise e

        decider_client_counter.labels(
            operation="init",
            success="true",
            error_type="",
        ).inc()

    # FIXME
    # Remove me once Experiments.py has no further dependencies on
    # accessing internal `self.py_decider` instance directly
    @staticmethod
    def _validate_decider(decider: Optional[Any]) -> None:
        if decider is None:
            decider_client_counter.labels(
                operation="init",
                success="false",
                error_type="missing_decider",
            ).inc()
            raise DeciderInitException(
                "rust_decider.init() returned `None` and did not initialize."
            )

        decider_err = decider.err()
        if decider_err:
            decider_client_counter.labels(
                operation="init",
                success="false",
                error_type="init_exception",
            ).inc()
            raise DeciderInitException(f"rust_decider.init() has error: {decider_err}")

    # FIXME
    # Remove me once Experiments.py has no further dependencies on
    # accessing internal `self.py_decider` instance directly
    def get_decider(self):
        return self.py_decider

    def choose(
        self,
        feature_name: str,
        context: Mapping[str, JsonValue],
    ) -> Decision:
        """Return a :code:`Decision` for a given :code:`feature_name` and :code:`context`.

        If dict() is called on the Decision instance, the following fields are returned`:

            {
                "variant": Optional[str],
                "value": Optional[Any],
                "feature_id": int,
                "feature_name": str,
                "feature_version": int,
                "events": [str]
            }

        :param feature_name: Name of feature you want a variant or value for.

        :param context: An optional :code:`Mapping[str, JsonValue]` of context fields used for
            feature overrides, targeting, & bucketing.

        :return: A Decision instance.
        """
        if context is None:
            decider_client_counter.labels(
                operation="choose",
                success="false",
                error_type="missing_context",
            ).inc()
            raise DeciderException(
                f"Missing `context` param in choose() for feature_name: {feature_name}"
            )

        ctx = make_ctx(context)
        ctx_err = ctx.err()
        if ctx_err:
            decider_client_counter.labels(
                operation="choose",
                success="false",
                error_type="invalid_context",
            ).inc()
            raise DeciderException(
                f"Encountered error from rust_decider.make_ctx() in choose() for context: {context}; {ctx_err}"
            )

        try:
            decision = self._decider.choose(feature_name, ctx)
        except DeciderFeatureNotFoundException as e:
            decider_client_counter.labels(
                operation="choose",
                success="false",
                error_type="feature_not_found",
            ).inc()
            raise e
        except DeciderException as e:
            decider_client_counter.labels(
                operation="choose",
                success="false",
                error_type="decider_exception",
            ).inc()
            raise e

        decider_client_counter.labels(
            operation="choose",
            success="true",
            error_type="",
        ).inc()

        return Decision(
            variant=decision.variant_name,
            feature_id=decision.feature_id,
            feature_name=decision.feature_name,
            feature_version=decision.feature_version,
            value=decision.value,
            events=decision.event_data,
        )
