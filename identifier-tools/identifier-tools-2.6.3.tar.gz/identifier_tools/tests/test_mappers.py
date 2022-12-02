from identifier_tools.mappers import territory_to_parent_mapper, get_verification_register


def test_territory_to_parent_mapper():
    assert territory_to_parent_mapper("CZ") == "CZ"  # case if country is not in territory list
    assert territory_to_parent_mapper("AX") == "FI"
    assert territory_to_parent_mapper("BL") == "FR"
    assert territory_to_parent_mapper("GF") == "FR"
    assert territory_to_parent_mapper("GP") == "FR"
    assert territory_to_parent_mapper("MC") == "FR"
    assert territory_to_parent_mapper("MF") == "FR"
    assert territory_to_parent_mapper("MQ") == "FR"
    assert territory_to_parent_mapper("PM") == "FR"
    assert territory_to_parent_mapper("RE") == "FR"
    assert territory_to_parent_mapper("YT") == "FR"
    assert territory_to_parent_mapper("EH") == "MA"
    assert territory_to_parent_mapper("SJ") == "NO"
    assert territory_to_parent_mapper("PR") == "US"


def test_get_verification_register():
    assert get_verification_register("DK_CVR_CD") == "http://www.cvr.dk"
    assert get_verification_register("US_EIN_CD") == (
        "https://www.irs.gov/businesses/small-businesses-self-employed/employer-id-numbers-eins",
        "https://eintaxid.com/",
    )
