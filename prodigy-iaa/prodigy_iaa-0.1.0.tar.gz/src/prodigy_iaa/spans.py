from collections import defaultdict
from typing import Any, Dict, List, Tuple
from itertools import product, groupby
from enum import IntEnum


a1 = {
    "text": "I like baby cats because they're cute",
    "spans": [
        {"start": 7, "end": 16, "token_start": 2, "token_end": 3, "label": "REF"},
        {"start": 25, "end": 37, "token_start": 5, "token_end": 7, "label": "REASON"},
    ],
}

a2 = {
    "text": "I like baby cats because they're cute",
    "spans": [
        {"start": 7, "end": 16, "token_start": 2, "token_end": 3, "label": "REF"},
        {"start": 25, "end": 37, "token_start": 5, "token_end": 6, "label": "REASON"},
    ],
}


def calculate_span_overlaps(
    spans1: List[Tuple[int, int]], spans2: List[Tuple[int, int]]
):
    """Calculate spans that are overlapping and unique to each list of input span
    beginning and end tokens."""
    spans1 = set(spans1)
    spans2 = set(spans2)
    overlaps = spans1.intersection(spans2)
    unique1 = spans1.difference(overlaps)
    unique2 = spans2.difference(overlaps)
    return unique1, overlaps, unique2


def calculate_partial_overlaps(
    spans1: List[Tuple[int, int]], spans2: List[Tuple[int, int]]
):
    """Identify spans that are partially overlapping and unique to each list of input span
    beginning and end tokens. A partial overlap is when the range of an interval in the first list of spans
    interval touches the range of an interval in the second list of spans."""


def SpanMatchNone():
    return SpanMatch.none


results = defaultdict(SpanMatchNone)
for (i, s1), s2 in product(enumerate(a1["spans"]), a2["spans"]):
    results[i] = max(results[i], overlapping_spans(s1, s2))

exact = defaultdict(int)
partial = defaultdict(int)
for i, result in results.items():
    if result == SpanMatch.exact:
        exact["true_pos"] += 1
        partial["true_pos"] += 1
    elif result == SpanMatch.partial:
        exact["false_pos"] += 1
        partial["true_pos"] += 1
    else:
        exact["false_pos"] += 1
        partial["false_pos"] += 1


@classmethod
def _calculate_p_r_f1(
    cls, true_pos: int, false_pos: int, false_neg: int
) -> Tuple[float, float, float]:
    """Calculate precision, recall and F1, expressed as %, from
    true positive, false positive and false negative counts.
    """
    if true_pos + false_pos > 0.0:
        p = 100 * true_pos / (true_pos + false_pos)
    else:
        p = 0.0
    if true_pos + false_neg > 0.0:
        r = 100 * true_pos / (true_pos + false_neg)
    else:
        r = 0.0
    if p + r > 0.0:
        f1 = (2 * p * r) / (p + r)
    else:
        f1 = 0.0
    return p, r, f1
