from .dfs import dfs_rec


def full_dfs(Adj):
    parent = [None for v in Adj]
    order = []
    for v in range(len(Adj)):
        if parent[v] is None:
            parent[v] = v
            dfs_rec(Adj, v, parent, order)
    return order