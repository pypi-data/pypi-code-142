from typing import TYPE_CHECKING

from .._content_provider_layer import ContentUsageLoggerMixin
from ..._content_type import ContentType
from ..._tools import create_repr, validate_bool_value, try_copy_to_list
from ...delivery._data._data_provider import (
    DataProviderLayer,
    BaseResponse,
    UniverseData,
)

if TYPE_CHECKING:
    from ..._types import StrStrings


class Definition(
    ContentUsageLoggerMixin[BaseResponse[UniverseData]],
    DataProviderLayer[BaseResponse[UniverseData]],
):
    """
    This class describe parameters to retrieve ESG basic data.

    Parameters
    ----------
    universe : str, list of str
        The Universe parameter allows the user to define the company they
        want content returned for, ESG content is delivered at the Company Level.

    use_field_names_in_headers: bool, optional
        Return field name as column headers for data instead of title

    Examples
    --------
    >>> from refinitiv.data.content import esg
    >>> definition = esg.basic_overview.Definition("IBM.N")
    >>> response = definition.get_data()

    >>> response = await definition.get_data_async()
    """

    _USAGE_CLS_NAME = "ESG.BasicOverviewDefinition"

    def __init__(
        self,
        universe: "StrStrings",
        use_field_names_in_headers: bool = False,
    ):
        validate_bool_value(use_field_names_in_headers)
        universe = try_copy_to_list(universe)

        super().__init__(
            ContentType.ESG_BASIC_OVERVIEW,
            universe=universe,
            use_field_names_in_headers=use_field_names_in_headers,
        )

    def __repr__(self):
        return create_repr(
            self,
            middle_path="basic_overview",
            content=f"{{universe='{self._kwargs.get('universe')}'}}",
        )
