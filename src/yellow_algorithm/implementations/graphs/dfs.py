


def dfs_rec(Adj ,s, parent=None, order=None):
        """
        recursive DFS implementation.
        """
        if parent is None:
            parent = [None for v in Adj]
            parent[s] = s
            order = []
        for u in Adj[s]:
            if parent[u] is None:
                parent[u] = s
                dfs_rec(Adj, u, parent=parent,order=order)
        order.append(s)
        return parent, order


def dfs(Adj, s):
    """
    Perform a depth-first search (DFS) on a graph.
    Simplification of interface for dfs_aux
    """
    parent, order = dfs_rec(Adj,s, parent=None, order=None)
    return parent, order