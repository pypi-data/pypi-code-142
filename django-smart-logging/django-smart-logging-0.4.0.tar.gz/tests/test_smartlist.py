import pytest
from smart_logging.manager import SmartList


@pytest.fixture()
def smart_list() -> SmartList:
    return type("test", (SmartList,), {"cls": tuple})()


def test_smartlist_setitem(smart_list):
    obj = ()
    smart_list["test"] = obj
    smart_list[obj] = "test"

    assert obj in smart_list
    assert "test" in smart_list


def test_smartlist_type_checking(smart_list):
    obj = ()
    with pytest.raises(ValueError):
        smart_list[2] = obj
    with pytest.raises(ValueError):
        smart_list[[]] = "fail"
    with pytest.raises(ValueError):
        smart_list[3]

    with pytest.raises(ValueError):
        assert 2 in smart_list

    with pytest.raises(ValueError):
        smart_list.get_name(2)

    with pytest.raises(ValueError):
        smart_list.get_instance(2)

    with pytest.raises(ValueError):
        smart_list.register("tuple", 2)

    with pytest.raises(ValueError):
        smart_list.register(2, "--")


def test_smartlist_register(smart_list):
    smart_list.register("tuple", tuple())
