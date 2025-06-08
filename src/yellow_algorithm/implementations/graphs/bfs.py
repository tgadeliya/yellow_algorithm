


def bfs(Adj, s):
    parent = [None for v in Adj]
    parent[s] = s
    level = [[s]]
    while len(level[-1]) > 0:
        level.append([])
        for v in level[-2]:
            for u in Adj[v]:
                if parent[u] is None:
                    parent[u] = v
                    level[-1].append(u)
    return parent
