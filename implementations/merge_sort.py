import typing as T

# List with comparable objects
ListAny = T.List[T.Any]

def mergesort(x: ListAny) -> ListAny:
    def merge(a: ListAny, b: ListAny) -> ListAny:
        c = [None] * (len(a) + len(b)) 
        i, j = 0,0
        while i < len(a) or j < len(b):
            if j == len(b) or (i < len(a) and a[i] < b[j]):
                c[i+j] = a[i]; i += 1
            else:
                c[i+j] = b[j]; j += 1
        return c

    n = len(x)
    if n <= 1:
        return x
    l = mergesort(x[:n//2])
    r = mergesort(x[n//2:])
    return  merge(l,r)
