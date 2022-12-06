from typing import TYPE_CHECKING, Any, Union, Dict

from pandas import DataFrame

from .._tools import (
    ADC_FUNC_PATTERN_IN_FIELDS,
    ADC_TR_PATTERN,
    fields_arg_parser,
    cached_property,
    iterator_str_arg_parser,
)

if TYPE_CHECKING:
    from .._types import OptStrStrs, StrStrings


class Container:
    def __init__(self, raw: Any = None) -> None:
        self._raw = raw

    @property
    def raw(self) -> Any:
        return self._raw

    def __bool__(self) -> bool:
        return bool(self._raw)

    def __iter__(self):
        return iter(self._raw)


class UniverseContainer(Container):
    def __init__(self, raw: "OptStrStrs" = None) -> None:
        super().__init__(raw)
        self._hp = []

    @cached_property
    def _universe(self) -> "StrStrings":
        return iterator_str_arg_parser.get_list(self._raw)

    @cached_property
    def hp_and_cust_inst(self):
        return self.hp + self.cust_inst

    @cached_property
    def adc(self) -> "StrStrings":
        return [inst for inst in self._universe if not inst.startswith("S)")]

    @cached_property
    def cust_inst(self) -> "StrStrings":
        return [inst for inst in self._universe if inst.startswith("S)")]

    @property
    def hp(self) -> "StrStrings":
        return self._hp

    @cached_property
    def is_universe_expander(self):
        from ..discovery._universe_expanders._universe_expander import UniverseExpander

        return isinstance(self._raw, UniverseExpander)

    def calc_hp(self, adc_raw: Union[Dict, None]) -> None:
        if adc_raw is not None:
            adc_rics = [item[0] for item in adc_raw.get("data", {})]
        else:
            adc_rics = None
        self._hp = adc_rics or self.adc

    def __iter__(self):
        return iter(self._universe)

    def __len__(self):
        return len(self._universe)


class FieldsContainer(Container):
    def __init__(self, raw: "OptStrStrs" = None) -> None:
        super().__init__(raw)
        self._adc_fields: "OptStrStrs" = None
        self._hp_fields: "OptStrStrs" = None

    def _parse(self) -> None:
        self._adc_fields = []
        self._hp_fields = []

        for field in self._fields:
            if ADC_TR_PATTERN.match(field) or ADC_FUNC_PATTERN_IN_FIELDS.match(field):
                self._adc_fields.append(field)
            else:
                self._hp_fields.append(field)

        if not self._adc_fields:
            self._adc_fields = ["TR.RIC"]

    @cached_property
    def _fields(self) -> "StrStrings":
        return fields_arg_parser.get_list(self._raw or [])

    @property
    def adc(self) -> "StrStrings":
        if self._adc_fields is None:
            self._parse()
        return self._adc_fields

    @property
    def hp(self) -> "StrStrings":
        if self._hp_fields is None:
            self._parse()
        return self._hp_fields

    @property
    def is_no_hp(self) -> bool:
        return not self.hp

    @cached_property
    def is_disjoint_adc(self) -> bool:
        return set(self.adc).isdisjoint(set(self._fields))

    @cached_property
    def is_one_adc_no_hp(self) -> bool:
        return len(self.adc) == 1 and not self.hp

    def __getattr__(self, attr: str) -> Any:
        try:
            return getattr(self._fields, attr)
        except KeyError:
            raise AttributeError(attr)

    def __iter__(self):
        return iter(self._fields)


class DataContainer(Container):
    def __init__(
        self, raw: Union[dict, list, None], df: Union[DataFrame, None]
    ) -> None:
        super().__init__(raw)
        self._df = df

    @property
    def df(self) -> DataFrame:
        return self._df


class ADCDataContainer(DataContainer):
    def __init__(
        self,
        raw: Union[dict, list, None],
        df: Union[DataFrame, None],
        fields: "FieldsContainer",
    ):
        super().__init__(raw, df)
        self._fields = fields

    def __bool__(self):
        is_none = self._raw in [{}, None] or (
            self._raw and self._fields.is_disjoint_adc
        )
        return not is_none


class HPDataContainer(DataContainer):
    pass


class CustInstDataContainer(DataContainer):
    pass


class HPAndCustInstDataContainer(HPDataContainer):
    def __init__(
        self,
        columns: Union[list, None],
        raw: Union[dict, list, None],
        df: Union[DataFrame, None],
    ):
        super().__init__(raw, df)
        self._columns = columns

    @property
    def columns(self):
        return self._columns
