"""
This module defines the Building class, which represents buildings containing different units and their data
"""
import re
from typing import Any, Optional, Union

import pandas as pd

from . import unit_graph
from .api import AccessDeniedError, api_get
from .backwards_compatibility import load_parameter_old_naming
from .building_unit import (
    BaseBuildingUnit,
    exclude_shared_units_from_list,
    populate_units,
)
from .data import load_model_data
from .device import Device
from .helpers import (
    check_no_remaining_fields,
    convenience_result_list_shortener,
    sanitise_datetime_input,
)
from .price import SupplyPoint
from .types import TYPE_DATETIME_INPUT
from .weather import Weather
from .zone import Zone, populate_zones, zone_matches


class Building(object):
    """Building defines a building in the PreHEAT sense"""

    def __init__(self, location_id: int):
        self.location_id = location_id

        # dict containing the details of the location
        self.location: dict[str, Any] = {}
        # list of zones within the building (of class PreHEAT_API.Zone)
        self.zones: list[Zone] = []
        # dict w.units within the building (of class PreHEAT_API.Unit)
        self.units = {}
        # dict w. weather information for the location (PreHEAT_API.Weather)
        self.weather = None  # type: Weather
        # Area of the building
        self.area = None
        # All characteristics get summarised in this dictionary
        # (duplicate with some attributes do to backwards-compatibility requirement)
        self.characteristics = {}

        # Supply points (for pricing)
        self.__supply_points = []

        # Load from API
        self.__populate()

        # Construct graph
        self.G = unit_graph.generate_unit_graph(self)

        # Traverse and map sub-unit references
        for node, data in self.G.nodes.data():
            # Add sub-units as new nodes
            if hasattr(data["unit"], "_related_sub_units_refs"):
                for ref in data["unit"]._related_sub_units_refs:
                    data["unit"].add_sub_unit(self.G.nodes[ref]["unit"])
            if hasattr(data["unit"], "_related_meters_refs"):
                for ref in data["unit"]._related_meters_refs:
                    data["unit"]._meters.append(self.G.nodes[ref]["unit"])

        # Devices
        self.__devices: Optional[list[Device]] = None

    def get_unit_graph(self):
        """

        :return:
        :rtype:
        """
        return self.G

    def load_data(
        self,
        start: TYPE_DATETIME_INPUT,
        end: TYPE_DATETIME_INPUT,
        resolution: str = "hour",
        components: Optional[dict[str, str]] = None,
        **kwargs,
    ) -> None:
        """

        :param start:
        :type start:
        :param end:
        :type end:
        :param resolution:
        :type resolution:
        :param components:
        :type components:
        :return:
        :rtype:
        """

        if components is None:
            components = {}

        start, end, resolution = load_parameter_old_naming(
            start, end, resolution, **kwargs
        )

        start = sanitise_datetime_input(start)
        end = sanitise_datetime_input(end)
        if components is None:
            components = {}

        if len(components) == 0:
            # Load all data on building, if nothing is specified
            self.weather.load_data(start, end, resolution, components.get("weather"))
            for node, data in self.G.nodes.data():
                u_i = data["unit"]
                c_i = components.get(u_i.unit_type)
                u_i.load_data(start, end, resolution, components=c_i)

        else:
            # Otherwise, just load specific components
            for i in components.keys():
                c_i = components.get(i)
                if i == "weather":
                    self.weather.load_data(start, end, resolution, components=c_i)
                else:
                    for u_i in self.query_units(unit_type=i):
                        u_i.load_data(start, end, resolution, components=c_i)

    def load_dataset(
        self,
        component_map,
        start: TYPE_DATETIME_INPUT,
        end: TYPE_DATETIME_INPUT,
        resolution: str = "hour",
        load_weather: bool = True,
    ) -> pd.DataFrame:
        """

        :param component_map:
        :type component_map:
        :param start:
        :type start:
        :param end:
        :type end:
        :param resolution:
        :type resolution:
        :param load_weather:
        :type load_weather:
        :return:
        :rtype:
        """

        df = load_model_data(component_map, start, end, resolution)

        if load_weather is True:
            self.weather.load_data(start, end, resolution)
            df_weather = self.weather.data
            df_weather.columns = "weather." + df_weather.columns
            df = pd.concat((df_weather, df), axis=1)

        return df

    def clear_data(self) -> None:
        """

        :return:
        :rtype:
        """
        self.weather.clear_data()

        for node, data in self.G.nodes.data():
            data["unit"].clear_data()

    def get_all_component_ids(self):
        """

        :return:
        :rtype:
        """
        return {
            k: v
            for node, data in self.G.nodes.data()
            for k, v in data["unit"].get_all_component_ids(True).items()
        }

    def get_all_component_details(self):
        """

        :return:
        :rtype:
        """
        all_comps = []
        for node, data in self.G.nodes.data():
            all_comps += data["unit"].get_all_component_details(prefix=True)

        return all_comps

    def query_units(
        self,
        unit_type: str = None,
        name: str = None,
        unit_id: int = None,
        exclude_shared: bool = False,
    ) -> list[BaseBuildingUnit]:
        """

        :param unit_type:
        :type unit_type:
        :param name:
        :type name:
        :param unit_id:
        :type unit_id:
        :param exclude_shared: if True, excludes shared units
        :type exclude_shared:
        :return:
        :rtype:
        """
        # If we pass a unit ID, find specific unit
        if unit_id:
            if unit_id in self.G.nodes.keys():
                out = [self.G.nodes[unit_id]["unit"]]
            else:
                out = []

        else:
            # If we pass a unit_type, check if we do regex search or strict search
            if unit_type:
                if unit_type[0] == "?":
                    r_type = re.compile(unit_type[1:])
                    type_match = lambda t: r_type.search(t)
                else:
                    type_match = lambda t: t == unit_type

            # If we pass name, check if we do regex search or strict search
            if name:
                # Check if we do strict search or search by regex:
                if name[0] == "?":
                    r_name = re.compile(name[1:])
                    name_match = lambda n: r_name.search(n)
                else:
                    name_match = lambda n: n == name

            try:
                # If we pass unit_type and name
                if unit_type and name:
                    result = [
                        data["unit"]
                        for node, data in self.G.nodes.data()
                        if name_match(data["unit"].name)
                        and type_match(data["unit"].unit_type)
                    ]

                elif name:
                    result = [
                        data["unit"]
                        for node, data in self.G.nodes.data()
                        if name_match(data["unit"].name)
                    ]

                elif unit_type:
                    result = [
                        data["unit"]
                        for node, data in self.G.nodes.data()
                        if type_match(data["unit"].unit_type)
                    ]

                out = result

            except:
                out = []

        if exclude_shared:
            out = exclude_shared_units_from_list(out)

        return out

    def qu(self, *args, **kwargs) -> Union[BaseBuildingUnit, list[BaseBuildingUnit]]:
        """

        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        result = self.query_units(*args, **kwargs)
        return convenience_result_list_shortener(result)

    def __populate(self) -> None:
        # Request PreHEAT API for location
        resp = api_get(f"locations/{self.location_id}", out="json")

        # Check if we have building data and if we do, extract and populate
        if "building" in resp:
            data = resp["building"]

            self.location = data.pop("location")
            self.area = data.pop("buildingArea")
            self.type = data.pop("buildingType")
            self.characteristics = {
                "area": self.area,
                "type": self.type,
                "apartments": data.pop("apartments"),
            }

            self.weather = Weather(self.location_id, data.pop("weatherForecast"))
            self.zones = populate_zones(data.pop("zones"))

            # Order is important for dependency
            unit_types = [
                "main",
                "coldWater",
                "heating",
                "hotWater",
                "cooling",
                "electricity",
                "ventilation",
                "heatPumps",
                "indoorClimate",
                "custom",
                "localWeatherStations",
                "pvs",
                "carChargers",
            ]

            for unit_type in unit_types:
                self.units[unit_type] = populate_units(
                    unit_type, data.pop(unit_type), self
                )

            for sp_i in data.pop("supplyPoints"):
                self.__supply_points.append(SupplyPoint(sp_i))

        else:
            raise AccessDeniedError("Access denied for given building")

        # For development validation, validate that no fields are left
        check_no_remaining_fields(data, debug_helper="building_data[building]")

    def get_supply_points(self):
        """

        :return:
        :rtype:
        """
        return self.__supply_points

    def __repr__(self):
        return f"""{type(self).__name__}({self.location_id}): {self.location["address"]} - {self.type}"""

    def get_zones(self, zone_ids) -> list[Zone]:
        """

        :param zone_ids:
        :type zone_ids:
        :return:
        :rtype:
        """
        res = []
        for z_i in self.zones:
            if z_i.id in zone_ids:
                res.append(z_i)
            res += z_i.get_sub_zones(zone_ids=zone_ids)
        return res

    def get_zone(self, id: int) -> Zone:
        """

        :param id:
        :type id:
        :return:
        :rtype:
        """
        zs = self.get_zones([id])
        n_zs = len(zs)
        if n_zs < 1:
            raise Exception(f"Zone not found (id={id})")
        elif n_zs > 1:
            raise Exception(f"Too many zones found for id (id={id} / {n_zs} found)")
        return zs[0]

    def describe(self, display: bool = True) -> str:
        apartments = self.characteristics.get("apartments")
        out = """ID: {id}
Address: {address}
City: {city}
Country: {country}

Type: {building_type}
Heated area: {area}
{apartments}

Units:
==============================\n""".format(
            id=self.location_id,
            address=self.location.get("address"),
            city=self.location.get("city"),
            country=self.location.get("country"),
            building_type=self.characteristics.get("type"),
            area=self.characteristics.get("area"),
            apartments=(
                "Apartments: {}".format(apartments) if apartments is not None else ""
            ),
        )

        main_was_found = False

        for i in [
            "main",
            "heating",
            "hotWater",
            "indoorClimate",
            "electricity",
            "cooling",
            "custom",
            "heatPumps",
            "weatherStations",
        ]:
            units_i = self.query_units(i)
            if len(units_i) == 0:
                continue
            elif i == "main":
                main_was_found = True
            elif main_was_found and i in ["heating", "hotWater"]:
                continue  # Skip heating and hot water, as they are already listed under the main

            out += "    [{}] \n".format(i.upper())
            for u in units_i:
                out += u.describe(display=False, prefix="\t -", children=True) + "\n"
            out += "\n"

        out += """
Zones:
==========================\n"""
        zones = self.zones
        if len(zones) == 0:
            out += "(None)\n"
        else:
            for z in zones:
                out += z.describe(prefix="- ", children=True, display=False) + "\n"

        if display:
            print(out)
        return out

    # Managing devices
    def load_devices(self):
        resp = api_get("locations/{}/devices".format(self.location_id), out="json")
        devices = resp["devices"]
        self.__devices = []
        for d in devices:
            d_type = d["typeName"]
            device_d = Device(d_type, d, self)
            self.__devices.append(device_d)

    def load_device_data(
        self,
        start: TYPE_DATETIME_INPUT,
        end: TYPE_DATETIME_INPUT,
        resolution: str = "hour",
    ):
        for d in self.devices:
            d.load_data(start, end, resolution)

    def clear_device_data(
        self,
    ):
        for d in self.devices:
            d.clear_data()

    @property
    def devices(self) -> list[Device]:
        if self.__devices is None:
            self.load_devices()
        return self.__devices

    def describe_devices(self, display: bool = True) -> str:
        apartments = self.characteristics.get("apartments")
        out = """ID: {id}
Address: {address}
City: {city}
Country: {country}

Type: {building_type}
Heated area: {area}
{apartments}

Devices:
==============================\n""".format(
            id=self.location_id,
            address=self.location.get("address"),
            city=self.location.get("city"),
            country=self.location.get("country"),
            building_type=self.characteristics.get("type"),
            area=self.characteristics.get("area"),
            apartments=(
                "Apartments: {}".format(apartments) if apartments is not None else ""
            ),
        )

        for d in self.devices:
            out += d.describe(display=False, prefix="\t -", children=False) + "\n"
        out += "\n"

        if display:
            print(out)
        return out

    def query_devices(
        self,
        name: Optional[str] = None,
        id: Optional[int] = None,
        device_type: Optional[str] = None,
    ) -> list[Device]:
        out = []
        for i in self.devices:
            add_i = None
            if name is not None:
                add_i = i.name == name
            if id is not None:
                if add_i is None:
                    add_i = True
                add_i = add_i and (i.id == id)
            if device_type is not None:
                if add_i is None:
                    add_i = True
                add_i = add_i and (i.unit_type == device_type)
            if add_i:
                out.append(i)
        return out

    def query_zones(
        self, zone_id: Optional[int] = None, zone_type: Optional[str] = None
    ) -> list[Zone]:
        out = []
        for z in self.zones:
            if zone_matches(z, zone_id=zone_id, zone_type=zone_type):
                out += [z]
            out += z.query_zones(zone_id=zone_id, zone_type=zone_type)
        return out


def available_buildings() -> pd.DataFrame:
    """
    lists available buildings

    :return: dataframe of buildings available
    :rtype:
    """
    out = api_get("locations")
    return pd.DataFrame(out["locations"])
