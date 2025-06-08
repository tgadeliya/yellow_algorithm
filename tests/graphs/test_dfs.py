
import pytest
from yellow_algorithm.implementations.graphs import dfs


class TestDFS:
    
    def test_single_node_graph(self):
        """Test DFS on a graph with a single node."""
        Adj = [[]]  # Node 0 has no neighbors
        parent, order = dfs(Adj, 0)
        assert parent == [0]
        assert order == [0]
    
    def test_two_node_connected_graph(self):
        """Test DFS on a simple two-node connected graph."""
        Adj = [[1], [0]]  # 0 -> 1, 1 -> 0
        parent, order = dfs(Adj, 0)
        assert parent == [0, 0]
        assert order == [1, 0]
    
    def test_linear_graph(self):
        """Test DFS on a linear graph: 0 -> 1 -> 2 -> 3."""
        Adj = [[1], [2], [3], []]
        parent, order = dfs(Adj, 0)
        assert parent == [0, 0, 1, 2]
        assert order == [3, 2, 1, 0]
    
    def test_tree_structure(self):
        """Test DFS on a tree structure."""
        # Tree: 0 has children 1, 2; 1 has child 3; 2 has child 4
        Adj = [[1, 2], [3], [4], [], []]
        parent, order = dfs(Adj, 0)
        assert parent[0] == 0  # Root
        assert parent[1] == 0  # Child of 0
        assert parent[2] == 0  # Child of 0
        assert parent[3] == 1  # Child of 1
        assert parent[4] == 2  # Child of 2
        # Order should be post-order traversal
        assert order[-1] == 0  # Root should be last
    
    def test_graph_with_cycle(self):
        """Test DFS on a graph with cycles."""
        # Graph: 0 -> 1 -> 2 -> 0 (cycle)
        Adj = [[1], [2], [0]]
        parent, order = dfs(Adj, 0)
        assert parent == [0, 0, 1]
        assert len(order) == 3
        assert 0 in order and 1 in order and 2 in order
    
    def test_disconnected_components_from_connected_node(self):
        """Test DFS starting from a node that can't reach all nodes."""
        # Graph: 0 -> 1, 2 -> 3 (disconnected components)
        Adj = [[1], [], [3], []]
        parent, order = dfs(Adj, 0)
        assert parent == [0, 0, None, None]  # Nodes 2,3 unreachable from 0
        assert order == [1, 0]
    
    def test_complex_connected_graph(self):
        """Test DFS on a more complex connected graph."""
        # Graph with multiple paths
        Adj = [
            [1, 2],    # 0 -> 1, 2
            [0, 3],    # 1 -> 0, 3  
            [0, 3, 4], # 2 -> 0, 3, 4
            [1, 2],    # 3 -> 1, 2
            [2]        # 4 -> 2
        ]
        parent, order = dfs(Adj, 0)
        
        # Check that all nodes are visited
        assert len(order) == 5
        assert set(order) == {0, 1, 2, 3, 4}
        
        # Check parent relationships are valid
        assert parent[0] == 0  # Root
        for i in range(1, 5):
            if parent[i] is not None:
                assert i in Adj[parent[i]]  # Parent should have child in adjacency list
    
    def test_start_from_different_nodes(self):
        """Test DFS starting from different nodes in the same graph."""
        Adj = [[1], [2], [0]]  # Cycle: 0 -> 1 -> 2 -> 0
        
        # Start from node 0
        parent0, order0 = dfs(Adj, 0)
        assert parent0[0] == 0
        
        # Start from node 1  
        parent1, order1 = dfs(Adj, 1)
        assert parent1[1] == 1
        
        # Start from node 2
        parent2, order2 = dfs(Adj, 2)
        assert parent2[2] == 2
    
    def test_empty_adjacency_for_some_nodes(self):
        """Test DFS where some nodes have no outgoing edges."""
        Adj = [[1, 2], [], []]  # Only node 0 has outgoing edges
        parent, order = dfs(Adj, 0)
        assert parent == [0, 0, 0]
        assert len(order) == 3
        assert order[-1] == 0  # Root should be processed last
    
    def test_self_loop(self):
        """Test DFS on a graph with self-loops."""
        Adj = [[0, 1], []]  # Node 0 has self-loop and edge to 1
        parent, order = dfs(Adj, 0)
        assert parent == [0, 0]
        assert order == [1, 0]
    
    def test_larger_disconnected_graph(self):
        """Test DFS on a larger graph with disconnected components."""
        # Two separate triangles: 0-1-2-0 and 3-4-5-3
        Adj = [
            [1, 2],    # 0 -> 1, 2
            [0, 2],    # 1 -> 0, 2
            [0, 1],    # 2 -> 0, 1
            [4, 5],    # 3 -> 4, 5
            [3, 5],    # 4 -> 3, 5
            [3, 4]     # 5 -> 3, 4
        ]
        
        # Start from first component
        parent, order = dfs(Adj, 0)
        visited_nodes = set(order)
        assert visited_nodes.issubset({0, 1, 2})
        assert len(visited_nodes) == 3
        
        # Nodes 3, 4, 5 should not be reachable
        assert parent[3] is None
        assert parent[4] is None  
        assert parent[5] is None
    
    def test_edge_case_large_node_indices(self):
        """Test that the function works with larger node indices."""
        # Simple graph but with gaps in node numbering
        Adj = [[], [2], []]  # Node 1 -> Node 2
        parent, order = dfs(Adj, 1)
        assert parent == [None, 1, 1]
        assert order == [2, 1]