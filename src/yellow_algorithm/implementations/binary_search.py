from typing import Iterable, Any, Optional


def binary_search(A: Iterable[Any], x: Any) -> Optional[int]:
    """
    Find element x in sorted array A. If element is present,
    return index in array A, otherwise None.

    Recursive implementation
    """

    def binary_search_aux(A: Iterable[Any], x: Any, p: int, q: int) -> Optional[int]:
        """
        p, q - left index, right index
        """
        if p + 1 == q:
            return p if A[p] == x else None
        c = (p + q + 1) // 2
        if A[c] <= x:
            return binary_search_aux(A, x, c, q)
        else:
            return binary_search_aux(A, x, p, c)

    return binary_search_aux(A, x, 0, len(A))
