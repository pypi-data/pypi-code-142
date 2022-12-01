"""Tests for `sqltrie` package."""
import pytest

from sqltrie import ShortKeyError, SQLiteTrie


def test_trie():
    trie = SQLiteTrie()

    trie[("foo",)] = "foo-value"
    trie[("foo", "bar", "baz")] = "baz-value"

    assert len(trie) == 2
    assert trie[("foo",)] == "foo-value"
    assert trie[("foo", "bar")] == None
    assert trie[("foo", "bar", "baz")] == "baz-value"

    del trie[("foo",)]
    assert len(trie) == 1
    # FIXME the next two should raise ShortKeyError
    assert trie[("foo",)] == None
    assert trie[("foo", "bar")] == None
    assert trie[("foo", "bar", "baz")] == "baz-value"

    with pytest.raises(KeyError):
        trie[("non-existent",)]

    with pytest.raises(KeyError):
        trie[("foo", "non-existent")]

    assert trie.longest_prefix(("non-existent",)) == tuple()
    assert trie.longest_prefix(("foo",)) == ("foo",)
    assert trie.longest_prefix(("foo", "non-existent")) == ("foo",)
    assert trie.longest_prefix(("foo", "bar", "baz", "qux")) == ("foo", "bar", "baz")


    assert set(trie.iteritems()) == {
        (("foo",), None),
        (("foo", "bar"), None),
        (("foo", "bar", "baz"), "baz-value"),
    }

    assert list(trie.diff(("foo",), ("foo",))) == []

