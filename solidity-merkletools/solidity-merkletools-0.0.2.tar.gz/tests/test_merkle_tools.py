import json
from typing import List

import pytest
from solidity_merkletools import MerkleTools

ADDRESS_ZERO = "0x0000000000000000000000000000000000000000"


@pytest.fixture
def merkle_trees():
    with open("tests/node_merkle_tree_output.json", "r") as f:
        return json.load(f)


@pytest.fixture
def tree_size_one(merkle_trees) -> List[str]:
    return merkle_trees["1"]["input"]


@pytest.fixture
def tree_size_one_root(merkle_trees) -> str:
    return merkle_trees["1"]["merkleRoot"]


@pytest.fixture
def tree_size_two(merkle_trees) -> List[str]:
    return merkle_trees["2"]["input"]


@pytest.fixture
def tree_size_two_root(merkle_trees) -> str:
    return merkle_trees["2"]["merkleRoot"]


@pytest.fixture
def tree_size_two_proofs(merkle_trees) -> str:
    return merkle_trees["2"]["proofs"]


@pytest.fixture
def tree_size_three(merkle_trees) -> List[str]:
    return merkle_trees["3"]["input"]


@pytest.fixture
def tree_size_three_root(merkle_trees) -> str:
    return merkle_trees["3"]["merkleRoot"]


@pytest.fixture
def tree_size_three_proofs(merkle_trees) -> str:
    return merkle_trees["3"]["proofs"]


@pytest.fixture
def tree_size_four(merkle_trees) -> List[str]:
    return merkle_trees["4"]["input"]


@pytest.fixture
def tree_size_four_root(merkle_trees) -> str:
    return merkle_trees["4"]["merkleRoot"]


@pytest.fixture
def tree_size_four_proofs(merkle_trees) -> str:
    return merkle_trees["4"]["proofs"]


@pytest.fixture
def tree_size_five(merkle_trees) -> List[str]:
    return merkle_trees["5"]["input"]


@pytest.fixture
def tree_size_five_root(merkle_trees) -> str:
    return merkle_trees["5"]["merkleRoot"]


@pytest.fixture
def tree_size_five_proofs(merkle_trees) -> str:
    return merkle_trees["5"]["proofs"]


@pytest.fixture
def tree_size_hundred(merkle_trees) -> List[str]:
    return merkle_trees["100"]["input"]


@pytest.fixture
def tree_size_hundred_root(merkle_trees) -> str:
    return merkle_trees["100"]["merkleRoot"]


@pytest.fixture
def tree_size_hundred_proofs(merkle_trees) -> str:
    return merkle_trees["100"]["proofs"]


def tree_tests(inputs, root, tree_proofs):
    mt = MerkleTools()
    for input in inputs:
        mt.add_leaf(input)

    mt.make_tree()
    assert mt.get_merkle_root() == root

    for address, proofs in tree_proofs.items():
        idx = mt.get_index(address)
        tree_proofs = mt.get_proof(idx, value_only=True)
        assert tree_proofs == proofs

    for input in inputs:
        proof = mt.get_proof_for_value(input)
        assert mt.validate_proof(proof, mt.hash_address(input).hex(), root)

    proof = mt.get_proof_for_value(ADDRESS_ZERO)
    assert not mt.validate_proof(proof, mt.hash_address(ADDRESS_ZERO).hex(), root)


def test_tree_size_one(tree_size_one, tree_size_one_root):
    mt = MerkleTools()
    mt.add_leaf(tree_size_one)

    mt.make_tree()
    assert mt.get_merkle_root() == tree_size_one_root


def test_tree_size_two(tree_size_two, tree_size_two_root, tree_size_two_proofs):
    tree_tests(tree_size_two, tree_size_two_root, tree_size_two_proofs)


def test_tree_size_three(tree_size_three, tree_size_three_root, tree_size_three_proofs):
    tree_tests(tree_size_three, tree_size_three_root, tree_size_three_proofs)


def test_tree_size_four(tree_size_four, tree_size_four_root, tree_size_four_proofs):
    tree_tests(tree_size_four, tree_size_four_root, tree_size_four_proofs)


def test_tree_size_five(tree_size_five, tree_size_five_root, tree_size_five_proofs):
    tree_tests(tree_size_five, tree_size_five_root, tree_size_five_proofs)


def test_tree_size_hundred(
    tree_size_hundred, tree_size_hundred_root, tree_size_hundred_proofs
):
    tree_tests(tree_size_hundred, tree_size_hundred_root, tree_size_hundred_proofs)
