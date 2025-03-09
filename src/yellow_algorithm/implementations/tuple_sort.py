from typing import Iterable, Tuple


def tuple_sort(A: Iterable[Tuple[int]]): 
    """
    Tuple sort - sort tuples from least important key to most important with counting sort

    Time Complexity: O(k*N), where k - number of keys in tuple, N - input length 
    Space Complexity: 
    requires stable subsorting algorithm
    """
    if len(A) < 2:
        return 
    
    for i in range(len(A[0])-1, -1, -1):
        # apply sort to ith keys starting from right (least significant)
        A.sort(key=lambda x: x[i])