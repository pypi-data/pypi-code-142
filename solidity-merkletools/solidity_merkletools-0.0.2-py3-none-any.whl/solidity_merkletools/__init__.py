from web3 import Web3


# This is a fork of https://github.com/Tierion/pymerkletools/blob/master/merkletools/__init__.py
# It didn't support using Web3's SolidityKeccak so we modify the merkle implementation here to support it.
# Matches the implementation in merkletreejs with arguments: this.tree = new MerkleTree(addresses, ethers.utils.keccak256, { sortPairs: true });
class MerkleTools(object):
    def __init__(self):
        self.reset_tree()

    # Changed the hash function to use solidityKeccak
    def hash_address(self, value) -> str:
        return Web3.solidityKeccak(["address"], [value])

    def hash_bytes(self, value) -> str:
        return Web3.solidityKeccak(["bytes32"], [value])

    # Corresponds to merklejs sortPairs=True. Hash the pairs in sorted order.
    def hash_pair(self, v1, v2) -> str:
        if v1 < v2:
            val = Web3.solidityKeccak(["bytes32", "bytes32"], [v1, v2])
        else:
            val = Web3.solidityKeccak(["bytes32", "bytes32"], [v2, v1])
        return val

    def _to_hex(self, x):
        return x.hex()

    def reset_tree(self):
        self.leaves = list()
        self.levels = None
        self.is_ready = False

    # Since we don't sort the leaves. The order in which you add the leaves
    # matters in how the root is generated.
    def add_leaf(self, values):
        self.is_ready = False
        # check if single leaf
        if not isinstance(values, tuple) and not isinstance(values, list):
            values = [values]
        for v in values:
            # Hash the leaves before adding to the tree
            v = self.hash_address(v)
            self.leaves.append(v)

    def get_index(self, value):
        hsh = self.hash_address(value)
        for idx, val in enumerate(self.leaves):
            if val == hsh:
                return idx
        return None

    def get_leaf(self, index):
        return self._to_hex(self.leaves[index])

    def get_leaf_count(self):
        return len(self.leaves)

    def get_tree_ready_state(self):
        return self.is_ready

    def _calculate_next_level(self):
        solo_leave = None
        N = len(self.levels[0])  # number of leaves on the level
        if N % 2 == 1:  # if odd number of leaves on the level
            solo_leave = self.levels[0][-1]
            N -= 1

        new_level = []
        for l, r in zip(self.levels[0][0:N:2], self.levels[0][1:N:2]):
            hsh = self.hash_pair(l, r)
            new_level.append(hsh)
        if solo_leave is not None:
            new_level.append(solo_leave)
        self.levels = [
            new_level,
        ] + self.levels  # prepend new level

    def make_tree(self):
        self.is_ready = False
        if self.get_leaf_count() > 0:
            self.levels = [
                self.leaves,
            ]
            while len(self.levels[0]) > 1:
                self._calculate_next_level()
        self.is_ready = True

    def get_merkle_root(self):
        if self.is_ready:
            if self.levels is not None:
                return self._to_hex(self.levels[0][0])
            else:
                return None
        else:
            return None

    def get_proof_for_value(self, value, value_only=False):
        idx = self.get_index(value)
        if idx is None:
            return []

        return self.get_proof(idx, value_only)

    def get_proof(self, index, value_only=False):
        if self.levels is None:
            return None
        elif not self.is_ready or index > len(self.leaves) - 1 or index < 0:
            return None
        else:
            proof = []
            for x in range(len(self.levels) - 1, 0, -1):
                level_len = len(self.levels[x])
                if (index == level_len - 1) and (
                    level_len % 2 == 1
                ):  # skip if this is an odd end node
                    index = int(index / 2.0)
                    continue
                is_right_node = index % 2
                sibling_index = index - 1 if is_right_node else index + 1
                sibling_pos = "left" if is_right_node else "right"
                sibling_value = self._to_hex(self.levels[x][sibling_index])
                if value_only:
                    proof.append(sibling_value)
                else:
                    proof.append({sibling_pos: sibling_value})
                index = int(index / 2.0)
            return proof

    def validate_proof(self, proof, target_hash, merkle_root):
        if len(proof) == 0:
            return target_hash == merkle_root
        else:
            proof_hash = target_hash
            for p in proof:
                try:
                    # the sibling is a left node
                    sibling = p["left"]
                    proof_hash = self.hash_pair(sibling, proof_hash).hex()
                except:
                    # the sibling is a right node
                    sibling = p["right"]
                    proof_hash = self.hash_pair(proof_hash, sibling).hex()

            return proof_hash == merkle_root

    # Add convenience function to print the tree
    def __str__(self) -> str:
        if not self.is_ready:
            return ""

        s = self.get_merkle_root() + "\n"
        for idx, level in enumerate(self.levels):
            s += f"Level: {idx} "
            for node in level:
                s += f" {self._to_hex(node)} "
            s += "\n"
        return s
