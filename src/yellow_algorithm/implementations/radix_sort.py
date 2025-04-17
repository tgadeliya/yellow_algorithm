from typing import Iterable


def counting_sort(A: Iterable[int]):
    """
    Counting sort

    """
    if len(A) == 0:
        return
    max_el = max([a.key for a in A])
    S = [[] for i in range(max_el + 1)]
    for a in A:
        S[a.key].append(a)
    i = 0
    for chain in S:
        for c in chain:
            A[i] = c
            i += 1


def radix_sort(A: Iterable[int]):
    n = len(A)
    u = 1 + max([a for a in A])
    c = 1 + (u.bit_length() // n.bit_length())

    class Obj:
        pass

    D = [Obj() for a in A]
    for i in range(n):
        D[i].digits = []
        D[i].item = A[i]
        high = A[i]
        for j in range(c):
            high, low = divmod(high, n)
            D[i].digits.append(low)

    for i in range(c):
        for j in range(n):
            D[j].key = D[j].digits[i]
        counting_sort(D)

    for i in range(n):
        A[i] = D[i].item
