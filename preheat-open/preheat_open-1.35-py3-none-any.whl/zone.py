from __future__ import annotations

from typing import List, Optional, Tuple

from .building_unit import BaseBuildingUnit
from .helpers import check_no_remaining_fields


def populate_zones(zones_data, parent_zone=None):
    zones = []
    # Loop over zones; create and populate Zone instances
    for zone_i in zones_data:
        zones.append(Zone(zone_i, parent_zone=parent_zone))

    return zones


class Zone(object):
    """Defines a building zone in the PreHEAT sense"""

    def __init__(self, zone_data, parent_zone=None):
        # Identifier of the zone
        self.id = zone_data.pop("id")
        # Name of the zone
        self.name = zone_data.pop("name", str(self.id))
        # Floor area of the zone
        self.area = zone_data.pop("zoneArea", None)
        # Whether zone has an external wall (boolean)
        self.has_external_wall = zone_data.pop("hasExternalWall", None)
        # Sub-zones of the zone (list of PreHEAT_API.Zones)
        self.sub_zones = populate_zones(zone_data.pop("subZones", []), parent_zone=self)
        # Adjacency
        self.adjacent_zones = [
            z["zoneId"] for z in zone_data.pop("adjacentZones", None)
        ]
        # Type of the zone
        self._type = zone_data.pop("type")

        # Parent zone
        self.__parent = parent_zone

        # Adding coupled units
        self.__coupled_units = dict()

        check_no_remaining_fields(zone_data, debug_helper="zone_data")

    def get_sub_zones(self, zone_ids=None) -> List[Zone]:
        if zone_ids is None:
            res = self.sub_zones
        else:
            res = []
            for z_i in self.sub_zones:
                if z_i.id in zone_ids:
                    res.append(z_i)
                res += z_i.get_sub_zones(zone_ids=zone_ids)
        return res

    def get_parent_zone(self) -> Zone:
        return self.__parent

    def get_type(self) -> Tuple[Optional[str], str]:
        """
        Returns the type of the zone ('room', 'stairway', 'corridor', 'bathroom', 'kitchen')
        and its 'dryness' ('dry', 'wet', '?')

        :return: zone_type, wet_or_dry
        """
        if self._type is None:
            return None, "?"
        zone_type = self._type.lower()
        if zone_type in ["room", "stairway", "corridor"]:
            wet_or_dry = "dry"
        elif zone_type in ["bathroom", "kitchen"]:
            wet_or_dry = "wet"
        else:
            wet_or_dry = "?"
        return zone_type, wet_or_dry

    def __repr__(self):
        return "{0}({1})".format(type(self).__name__, self.name)

    def add_coupled_unit(self, unit) -> None:
        unit_type = unit.unit_type
        if unit_type in self.__coupled_units.keys():
            if unit.id in [u_i.id for u_i in self.__coupled_units[unit_type]]:
                pass  # Skip addition of already existing units
            else:
                self.__coupled_units[unit_type].append(unit)
        else:
            self.__coupled_units[unit_type] = [unit]

    def get_units(self, unit_type, sub_zones=True) -> List[BaseBuildingUnit]:
        """
        Returns the coupled units of a given type

        :param unit_type: str
        :param sub_zones: bool (True)
        :return: list(BuildingUnit) or None
        """
        us = self.__coupled_units.get(unit_type)
        if us is None:
            us = []
        if sub_zones is True:
            for z_i in self.sub_zones:
                us_i = z_i.get_units(unit_type, sub_zones=True)
                if len(us_i) > 0:
                    us += us_i
        return us

    def get_unit_types(self, sub_zones=True) -> list[str]:
        """
        Return as list of the coupled unit types
        """
        us = list(self.__coupled_units.keys())
        if sub_zones is True:
            for z_i in self.sub_zones:
                us_i = z_i.get_unit_types(sub_zones=True)
                if us_i is not None:
                    if us is None:
                        us = us_i
                    else:
                        us += us_i
        out = []
        [out.append(k) for k in us if k not in out]
        return out

    def describe(
        self, children: bool = True, prefix: str = "", display: bool = True
    ) -> str:
        z_type, __ = self.get_type()
        type_prefix = "[{}] ".format(z_type) if z_type is not None else ""
        out = prefix + type_prefix + self.name + " [id={}]".format(self.id)
        if children:
            for z in self.sub_zones:
                out += "\n" + z.describe(
                    prefix=prefix.replace("-", "") + "\t- ", display=False
                )
        if display:
            print(out)
        return out

    def query_zones(
        self, zone_id: Optional[int] = None, zone_type: Optional[str] = None
    ) -> List[Zone]:
        out = []
        for z in self.sub_zones:
            if zone_matches(z, zone_id=zone_id, zone_type=zone_type):
                out += [z]
            out += z.query_zones(zone_id=zone_id, zone_type=zone_type)
        return out


def zone_matches(
    z: Zone, zone_id: Optional[int] = None, zone_type: Optional[str] = None
) -> bool:

    by_zone_id = zone_id is not None
    by_zone_type = zone_type is not None
    z_zone_type, __ = z.get_type()

    if by_zone_id and by_zone_type:
        out = (zone_id == z.id) and (zone_type == z_zone_type)
    elif by_zone_id:
        out = zone_id == z.id
    elif by_zone_type:
        out = zone_type == z_zone_type
    else:
        out = False
    return out
