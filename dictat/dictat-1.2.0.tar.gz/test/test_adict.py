"""`pytest` unit tests for module `dictat` and it's classes."""

# pylint: disable=redefined-outer-name
# pylint: disable=missing-function-docstring

from typing import Any, Dict
import json

import pytest

from dictat import Adict, JsonEncoder


@pytest.fixture
def adict() -> Adict:
    return Adict()


@pytest.fixture
def subdict() -> Dict[Any, Any]:
    return {
        'key1': 'val1',
        'key2': 'val2',
        'subsub': {
            'subkey1': 'subval1',
            'subkey2': 'subval2',
        }
    }


def test_access_non_existing(adict: Adict) -> None:

    assert 'key' not in adict
    assert ('key' in adict) is False

    # default dict behaviour
    with pytest.raises(KeyError):
        adict['key']  # pylint: disable=pointless-statement

    # safe access with attribute notation
    assert adict.key is None


def test_bool(adict: Adict) -> None:

    assert not adict
    assert bool(adict) is False

    adict.key = 'value'
    assert adict
    assert bool(adict) is True

    adict = Adict()
    adict['key'] = 'value'
    assert adict
    assert bool(adict) is True


def test_len(adict: Adict) -> None:

    assert len(adict) == 0
    adict.key = 'value'
    assert len(adict) == 1
    adict.key2 = 'value2'
    assert len(adict) == 2
    adict.sub = {}
    assert isinstance(adict.sub, Adict)  # check needed to convince type checker
    adict.sub.key = 'subval'
    assert len(adict) == 3


def test_iterator(adict: Adict) -> None:
    count = 0
    for _ in adict:
        count += 1
    assert count == 0

    adict.a = 1
    adict.b = 2
    adict.c = 3

    keys = []
    sum_ = 0
    for key in adict:
        keys.append(key)
        sum_ += adict[key]
    assert keys == ['a', 'b', 'c']
    assert sum_ == 6


def test_get_set(adict: Adict) -> None:

    adict.key = 'value'
    assert adict.key == 'value'
    assert adict['key'] == 'value'

    adict.sub = {}
    # technical detail: dicts are returned wrapped in an 'Adict'
    assert isinstance(adict.sub, Adict)
    assert type(adict.sub) is Adict  # pylint: disable=unidiomatic-typecheck
    assert type(adict['sub']) is Adict  # pylint: disable=unidiomatic-typecheck

    assert adict.sub.key is None
    # default dict behaviour
    with pytest.raises(KeyError):
        adict.sub['key']  # pylint: disable=pointless-statement


def test_sub_dict(adict: Adict, subdict: Dict[Any, Any]) -> None:
    adict.sub = subdict
    assert isinstance(adict.sub, Adict)  # check needed to convince type checker
    assert adict.sub.key1 == 'val1'
    assert adict.sub.key2 == 'val2'
    assert adict.sub.subsub.subkey1 == 'subval1'
    assert adict.sub.subsub.subkey2 == 'subval2'


def test_paren_syntax(adict: Adict, subdict: Dict[Any, Any]) -> None:
    """Test safe access to non-existing keys using the paranthesis syntax.

    The only thing that can raise from here, is if we've traversed down to a leaf value, which
    then cannot accessed using () syntax."""
    adict.sub = subdict

    assert adict('sub')('key1') == 'val1'
    assert adict('sub')('key2') == 'val2'
    assert adict('sub')('subsub')('subkey1') == 'subval1'
    assert adict('sub')('subsub')('subkey2') == 'subval2'

    assert not adict('a')('b')('c')
    assert adict('a')('b')('c') == {}
    assert not adict('sub')('key3')
    assert adict('sub')('key3') == {}

    # with default value, e.g. when we know the last level is a leaf level
    assert adict('a')('b')('c', default=None) is None
    assert adict('sub')('key3', default=None) is None
    assert adict('a')('b')('c', 'd') == 'd'
    # test that the default=__NONE__=object() semantic is correct
    assert adict('a')('b')('c', default=object()) is not None
    assert adict('a')('b')('c', default=object()) != {}

    # equivalence of `dict.get('key', {})`, but converting `{}` to `Adict({})``
    assert adict('a', default={}) == {}
    assert isinstance(adict('a', default={}), Adict)
    assert adict('a', default={'b': 'c'})('b') == 'c'

    # the only chance to raise is when we ()-access a leaf value
    with pytest.raises(TypeError) as info:
        adict('sub')('subsub')('subkey2')('nomore')
    assert "'str' object is not callable" in str(info)


def test_delete(adict: Adict) -> None:

    # non-existing
    with pytest.raises(KeyError):
        del adict['key']

    # non-existing, attribute notation: safe to use
    del adict.key

    adict.key = 'value'
    assert adict.key == 'value'
    del adict.key
    assert 'key' not in adict
    assert adict.key is None


def test_mutable(adict: Adict) -> None:

    sub: Dict[Any, Any] = {}
    adict.sub = sub
    assert isinstance(adict.sub, Adict)  # check needed to convince type checker
    sub['key'] = 'value'
    assert adict.sub.key == 'value'

    adict.sub['new'] = 'newval'
    assert sub['new'] == 'newval'

    sub['key'] = 'changed'
    assert adict.sub.key == 'changed'


def test_initial_dict(subdict: Dict[Any, Any]) -> None:
    adict = Adict(subdict)
    assert adict.key1 == 'val1'
    assert adict.key2 == 'val2'
    assert adict.subsub.subkey1 == 'subval1'
    assert adict.subsub.subkey2 == 'subval2'

    assert adict.__dict__ == subdict
    assert adict.__dict__ is subdict


def test_initial_kwargs() -> None:
    adict = Adict(key3='val3', key4='val4')
    assert adict.key3 == 'val3'
    assert adict.key4 == 'val4'


def test_initial_dict_and_kwargs(subdict: Dict[Any, Any]) -> None:
    adict = Adict(subdict, key3='val3', key4='val4')
    assert adict.key1 == 'val1'
    assert adict.key2 == 'val2'
    assert adict.subsub.subkey1 == 'subval1'
    assert adict.subsub.subkey2 == 'subval2'
    assert adict.key3 == 'val3'
    assert adict.key4 == 'val4'


def test_str(adict: Adict, subdict: Dict[Any, Any]) -> None:

    assert str(adict) == '{}'

    adict.key = 'value'
    assert str(adict) == str({'key': 'value'})

    adict.sub = subdict
    assert str(adict) == str({'key': 'value', 'sub': subdict})


def test_dict(adict: Adict, subdict: Dict[Any, Any]) -> None:

    assert adict.__dict__ == {}

    adict.key = 'value'
    assert adict.__dict__ == {'key': 'value'}

    adict.sub = subdict
    assert adict.__dict__ == {'key': 'value', 'sub': subdict}


def test_json(adict: Adict, subdict: Dict[Any, Any]) -> None:

    import pathlib  # pylint: disable=import-outside-toplevel

    adict.sub = subdict
    adict.path = pathlib.Path('somepath')  # normally not JSON serializable

    # equivalent standad dict
    standard = {
        'sub': subdict,
        'path': str(pathlib.Path('somepath'))
    }

    dump_adict = json.dumps(adict, cls=JsonEncoder)
    dump_standard = json.dumps(standard)
    assert dump_adict == dump_standard

    # the encoder can also be used for standard dicts
    dump_standard2 = json.dumps(standard, cls=JsonEncoder)
    assert dump_standard2 == dump_standard
    assert dump_standard2 == dump_adict
