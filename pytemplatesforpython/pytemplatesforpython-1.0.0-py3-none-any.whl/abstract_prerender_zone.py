from abc import abstractclassmethod, abstractmethod, abstractstaticmethod
from dataclasses import dataclass
from typing import Iterable, Type
from .pointer_string import PointerString

class InnerPrerendererError(Exception):
    def __init__(self):
        super().__init__("inner prerenderer error")

@dataclass
class PrerenderZonesParametersBase: 
    pointer_original: PointerString


class AbstractPrerenderZone:
    @abstractclassmethod
    def entry_condition(cls, parameters: PrerenderZonesParametersBase) -> bool:
        """If the parameters.pointer_original.get_symb(0) should be the first symbol of the zone, returns True, else returns False.
        Doesn't move the pointer in the parameters.pointer_original PointerString"""
        raise NotImplementedError()
    
    @abstractmethod
    def process(self, parameters: PrerenderZonesParametersBase) -> str:
        """Returns the result of the parsing of the zone that starts from parameters.pointer_original.get_symb(0) and moves the pointer to the last symbol of the zone"""
        raise NotImplementedError()



class AbstractPrerenderZoneWithSubzones(AbstractPrerenderZone):
    _possible_subzone_types: Iterable[Type[AbstractPrerenderZone]]
    
    @abstractclassmethod
    def _entry_condition(cls, parameters: PrerenderZonesParametersBase) -> bool:
        """If the parameters.pointer_original.get_symb(0) should be the first symbol of the zone, returns True, else returns False.
        Doesn't move the pointer in the parameters.pointer_original PointerString"""
        raise NotImplementedError()

    @abstractmethod
    def _entry(self, parameters: PrerenderZonesParametersBase) -> str:
        """Returns the result of the parsing of the start of the zone whose first symbol is parameters.pointer_string.get_symb(0)."""
        raise NotImplementedError()
    
    @abstractmethod
    def _process_symbol(self, parameters: PrerenderZonesParametersBase) -> str:
        """Returns the result of the parsing of the symbol parameters.pointer_string.get_symb(0) that's inside of the zone."""
        raise NotImplementedError()

    @abstractmethod
    def _exit_condition(self, parameters: PrerenderZonesParametersBase) -> bool:
        "Returns True if zone's last symbol is parameters.pointer_original.get_symb(0), else returns False"
        raise NotImplementedError()
    
    @abstractmethod
    def _exit(self, parameters: PrerenderZonesParametersBase) -> str:
        """Returns the result of the parsing of the end of the zone whose last symbol is parameters.pointer_string.get_symb(0)."""
        raise NotImplementedError()

    @abstractmethod
    def _subzone_absence_entry(self, parameters: PrerenderZonesParametersBase) -> str:
        """Returns the result of the parsing of the start of the subzone absence whose first symbol is parameters.pointer_string.get_symb(0)."""
        raise NotImplementedError()

    @abstractmethod
    def _subzone_absence_exit(self, parameters: PrerenderZonesParametersBase) -> str:
        """Returns the result of the parsing of the end of the subzone absence whose last symbol is parameters.pointer_string.get_symb(0)."""
        raise NotImplementedError()

    @abstractmethod
    def _process_index_error(self, e: IndexError, parameters: PrerenderZonesParametersBase) -> None:
        raise NotImplementedError()

    @classmethod
    def entry_condition(cls, parameters: PrerenderZonesParametersBase) -> bool:
        return cls._entry_condition(parameters)
    
    def process(self, parameters: PrerenderZonesParametersBase) -> str:
        result: str = ""
        result += self._entry(parameters)
        original: PointerString = parameters.pointer_original
        is_zone_absence_entry: bool = True
        while 1:
            Subzone: Type[AbstractPrerenderZone]
            for Subzone in self._possible_subzone_types:
                if Subzone.entry_condition(parameters):
                    if not is_zone_absence_entry:
                        result += self._subzone_absence_exit(parameters)
                    subzone = Subzone()
                    result += subzone.process(parameters)
                    is_zone_absence_entry = True
                    break
            else:
                if is_zone_absence_entry:
                    result += self._subzone_absence_entry(parameters)
                result += self._process_symbol(parameters)
                is_zone_absence_entry = False
            try:
                original.move(1)
            except IndexError as e:
                self._process_index_error(e, parameters)
                raise InnerPrerendererError()
            if self._exit_condition(parameters):
                result += self._process_symbol(parameters)
                if not is_zone_absence_entry:
                    result += self._subzone_absence_exit(parameters)
                result += self._exit(parameters)
                break #TODO: move exit condition checking to the start of the while loop to fix the bag of one symbol template
        return result