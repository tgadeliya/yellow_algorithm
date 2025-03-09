from typing import Iterable


def counting_sort(A: Iterable[int]):
    """
    Counting sort

    """
    if len(A) == 0:
        return
    max_el = max(A)
    S = [0] * (max_el + 1)
    for a in A:
        S[a] += 1

    i = 0
    for idx in range(max_el + 1):
        if idx > 0:
            while S[idx] > 0:
                A[i] = idx
                i += 1
                S[idx] -= 1
