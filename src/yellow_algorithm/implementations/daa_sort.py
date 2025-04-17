from typing import Iterable


def direct_access_aray_sort(A: Iterable[int]):
    """
    Direct Access array sort

    Property: unique values
    """
    if len(A) == 0:
        return
    max_el = max(A)
    S = [None] * (max_el + 1)

    for a in A:
        S[a] = a

    i = 0
    for j in range(max_el + 1):
        if S[j] is not None:
            A[i] = S[j]
            i += 1
