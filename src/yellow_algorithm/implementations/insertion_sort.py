from typing import Iterable, Any


def insertion_sort(A: Iterable[Any]):
    "In-Place stable? non-recursive Insertion sort"
    for i in range(1, len(A)):
        j = i
        while (j > 0) and (A[j] < A[j - 1]):
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1
