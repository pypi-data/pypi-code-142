from preheat_open import test


class TestBuilding(test.PreheatTest):
    def test_zone_type(self, building_with_data):
        apt_zone = building_with_data.get_zones(zone_ids=[4832])[0]
        wet_zone = building_with_data.get_zones(zone_ids=[4833])[0]
        dry_zone = building_with_data.get_zones(zone_ids=[4835])[0]

        type_1, wet_or_dry_1 = apt_zone.get_type()
        assert type_1 == "apartment"
        assert wet_or_dry_1 == "?"

        type_a, wet_or_dry_a = wet_zone.get_type()
        assert type_a == "bathroom"
        assert wet_or_dry_a == "wet"

        type_b, wet_or_dry_b = dry_zone.get_type()
        assert type_b == "corridor"
        assert wet_or_dry_b == "dry"

    def query_zones(self, building_with_data):
        z = building_with_data.query_zones(zone_id=4832, zone_type="apartment")[0]
        assert len(z.query_zones(zone_id=4833)) == 1
        assert len(z.query_zones(zone_type="bathroom")) == 1
        assert len(z.query_zones(zone_id=4833, zone_type="bathroom")) == 1

        assert len(z.query_zones(zone_id=4833, zone_type="apartment")) == 0
        assert len(z.query_zones(zone_type="doesnt exist")) == 0
        assert len(z.query_zones(zone_id=0)) == 0

    def test_get_units(self, building_with_data):
        # Zone A1 -- connected to unit named 'indoor_climate_1'
        zone_A1 = building_with_data.get_zones(zone_ids=[4830])[0]
        units_A1 = zone_A1.get_units("indoorClimate")
        assert units_A1[0] == building_with_data.qu(name="indoor_climate_1")
        zone_A1b = building_with_data.get_zone(id=4830)
        assert zone_A1 == zone_A1b

        # Zone A2 -- not connected to any units
        zone_A2 = building_with_data.get_zones(zone_ids=[4831])[0]
        units_A2 = zone_A2.get_units("indoorClimate")
        assert not units_A2

        zone_A = zone_A1b.get_parent_zone()
        assert zone_A.get_parent_zone() is None
        assert len(zone_A.get_units("indoorClimate")) > 0

    def test_get_unit_types(self, building_with_data):
        # Zone A1 -- connected to unit named 'indoor_climate_1'
        zone_A1 = building_with_data.get_zones(zone_ids=[4830])[0]
        types_A1 = zone_A1.get_unit_types()
        assert isinstance(types_A1, list)
        for t in types_A1:
            assert isinstance(t, str)

        # Zone A2 -- not connected to any units
        zone_A2 = building_with_data.get_zones(zone_ids=[4831])[0]
        types_A2 = zone_A2.get_unit_types()
        assert isinstance(types_A2, list)
        assert not types_A2
