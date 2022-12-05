"""
source_batch = <tf.Tensor 'source_batch:0' shape=(None,) dtype=string>
sim = <tf.Tensor 'while/StatefulPartitionedCall:0' shape=<unknown> dtype=float32>
source_batch[i] = <tf.Tensor 'while/strided_slice_3:0' shape=() dtype=string>

"""

import unicodedata

import numpy as np


COST = {
    "DELETE": 1,
    "INSERT": 1,
    "SUBSTITUTE": 2,
}

def lev(source:str, target:str, cost:dict=COST) -> float:
    """
    Levenshtein distance
    """
    m = len(source)
    n = len(target)
    # Think of distance_matrix as a (m+1, n+1)-matrix
    distance_matrix = dict()

    distance_matrix[0,0] = 0
    for i in range(1,m+1):
        distance_matrix[i,0] = distance_matrix[i-1,0] + cost["DELETE"]
    for j in range(1,n+1):
        distance_matrix[0,j] = distance_matrix[0,j-1] + cost["INSERT"]

    for i in range(1,m+1):
        for j in range(1,n+1):
            candidates = (
                distance_matrix[i-1, j-1] + (0 if source[i-1] == target[j-1] else cost["SUBSTITUTE"]),
                distance_matrix[i-1, j] + cost["DELETE"],
                distance_matrix[i, j-1] + cost["INSERT"],
            )
            distance_matrix[i,j] = min(candidates)

    return distance_matrix[m, n]


def norm_lev(
        source:str,
        target:str,
        form:str="NFD",
        cost:dict=COST,
    ):
    source = unicodedata.normalize(form, source)
    target = unicodedata.normalize(form, target)
    return lev(source, target, cost)


def batch_lev(
        source_batch,
        target_batch,
        form:str="NFD",
        cost:dict=COST,
    ):
    somme = 0
    for source, target in zip(source_batch, target_batch):
        somme += norm_lev(source, target, form, cost)
    avg = somme / len(source_batch)
    return avg


def sim(
        source:str,
        target:str,
        alpha:float=1/3,
        soft:bool=True,
        proportional:bool=True,
    ) -> float:
    """
    The idea is that we need this function to return an
    accuracy-like score, in the range of [0, 1],
    to measure the similarity between two strings.

    We have provided two distinct definition for soft similarity,
    controlled by the boolean `proportional`
    """
    if soft:
        dist = lev(source, target)
        if proportional:
            proportion = dist / (COST["SUBSTITUTE"]*max(len(target), 1))
            similarity = 1 - min(1, proportion)
        else:
            if dist > len(target)*COST["SUBSTITUTE"]:
                # That is, when they are completely different strings
                similarity = 0
            else:
                similarity = 1 / (alpha*dist + 1)
    else:
        # hard similarity is binary: same string or not
        similarity = float(source == target)
    return similarity


def norm_sim(
        source:str,
        target:str,
        alpha:float=1/3,
        soft:bool=True,
        proportional:bool=True,
        form:str="NFD",
    ) -> float:
    source = unicodedata.normalize(form, source)
    target = unicodedata.normalize(form, target)
    return sim(source, target, alpha, soft, proportional)


def batch_sim(
        source_batch,
        target_batch,
        alpha:float=1/3,
        soft:bool=True,
        proportional:bool=True,
        form:str="NFD",
    ) -> float:
    somme = 0
    for source, target in zip(source_batch, target_batch):
        somme += norm_sim(source, target, alpha, soft, proportional, form)
    avg = somme / len(source_batch)
    return avg


if __name__ == "__main__":
    #source = "Tôi ở Sài Gòn được 6 năm rồi."
    ##target = "Tôi ở Sài Gòn được 7 năm."
    #target = "Tôi ở đây chưa lâu."
    #print(f"{source = }")
    #print(f"{target = }")
    #d = norm_lev(source, target, form="NFKD")
    #print(f"(Python land) {d = }")
    #source = tf.constant(source)
    #target = tf.constant(target)
    #d = tf_byte_lev(source, target)
    #print(f"(TF land)     {d = }")
    #print()
    #proportional_similarity = tf_byte_sim(source, target)
    #print(f"(TF land)     {proportional_similarity = }")
    #unproportional_similarity = tf_byte_sim(source, target, proportional=tf.constant(False))
    #print(f"(TF land)     {unproportional_similarity = }")
    pass
