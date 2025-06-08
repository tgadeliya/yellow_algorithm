from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        visited = set()
        new_node = Node(node.val, neighbors=node.neighbors)
        visited.add(new_node)
        level = [[new_node]]
        while len(level[-1]) > 0:
            level.append([])
            for u in level[-2]:
                u_new_neigh = [] 
                for v in u.neighbors:
                    new_v = Node(v.val, v.neighbors)
                    u_new_neigh.append(new_v)
                    if new_v not in visited:
                        visited.add(new_v)
                        level[-1].append(new_v)
                u.neighbors = u_new_neigh
        return new_node