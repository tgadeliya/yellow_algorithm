from typing import Iterable, Any


def merge_sort(A: Iterable[Any]):
    """
    In-place non-stable recursive ? Merge sort
    """

    def merge_aux(
        A: Iterable[Any],
        L: Iterable[Any],
        R: Iterable[Any],
        i: int,
        j: int,
        a: int,
        b: int,
    ):
        if a < b:
            if (j <= 0) or (i > 0 and L[i - 1] > R[j - 1]):
                A[b - 1] = L[i - 1]
                i -= 1
            else:
                A[b - 1] = R[j - 1]
                j -= 1
            merge_aux(A, L, R, i, j, a, b - 1)

    def sort_aux(A, a, b=None):
        if b is None:
            b = len(A)
        if a + 1 < b:
            c = (a + b + 1) // 2
            sort_aux(A, a, c)
            sort_aux(A, c, b)
            L, R = A[a:c], A[c:b]
            merge_aux(A, L, R, len(L), len(R), a, b)

    sort_aux(A, 0, b=None)
