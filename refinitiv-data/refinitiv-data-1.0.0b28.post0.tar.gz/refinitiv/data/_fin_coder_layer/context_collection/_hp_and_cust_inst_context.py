from typing import Union, List

from ._hp_context import HPContext


class HPAndCustInstContext(HPContext):
    @property
    def dfbuilder(self) -> "DFBuilder":
        pass

    @property
    def date_name(self) -> str:
        pass

    def prepare_headers(self, raw: Union[list, dict], *args) -> List[List[str]]:
        pass

    @property
    def can_get_data(self):
        return super().can_get_data or self.universe.cust_inst
