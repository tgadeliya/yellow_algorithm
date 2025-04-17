from typing import Iterable, Any


def selection_sort(A: Iterable[Any]):
    "In-Place stable? non-recursive Selection sort"
    for i in range(len(A) - 1):
        min_el_idx = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_el_idx]:
                min_el_idx = j
        A[i], A[min_el_idx] = A[min_el_idx], A[i]
