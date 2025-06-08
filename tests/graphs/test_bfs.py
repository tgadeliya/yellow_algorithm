from yellow_algorithm.implementations.graphs import bfs


class TestBFS:
    
    def test_single_node_graph(self):
        """Test BFS on a graph with a single node."""
        Adj = [[]]  # Node 0 has no neighbors
        parent = bfs(Adj, 0)
        assert parent == [0]
    
    def test_two_node_connected_graph(self):
        """Test BFS on a simple two-node connected graph."""
        Adj = [[1], [0]]  # 0 -> 1, 1 -> 0
        parent = bfs(Adj, 0)
        assert parent == [0, 0]
    
    def test_linear_graph(self):
        """Test BFS on a linear graph: 0 -> 1 -> 2 -> 3."""
        Adj = [[1], [2], [3], []]
        parent = bfs(Adj, 0)
        assert parent == [0, 0, 1, 2]
    
    def test_star_graph(self):
        """Test BFS on a star graph with center node 0."""
        # Graph: 0 connected to 1, 2, 3, 4
        Adj = [[1, 2, 3, 4], [], [], [], []]
        parent = bfs(Adj, 0)
        assert parent == [0, 0, 0, 0, 0]
    
    def test_tree_structure(self):
        """Test BFS on a tree structure."""
        # Tree: 0 has children 1, 2; 1 has children 3, 4; 2 has child 5
        Adj = [[1, 2], [3, 4], [5], [], [], []]
        parent = bfs(Adj, 0)
        assert parent[0] == 0  # Root
        assert parent[1] == 0  # Child of 0
        assert parent[2] == 0  # Child of 0
        assert parent[3] == 1  # Child of 1
        assert parent[4] == 1  # Child of 1
        assert parent[5] == 2  # Child of 2
    
    def test_graph_with_cycle(self):
        """Test BFS on a graph with cycles."""
        # Graph: 0 -> 1 -> 2 -> 0 (cycle)
        Adj = [[1], [2], [0]]
        parent = bfs(Adj, 0)
        assert parent == [0, 0, 1]
    
    def test_disconnected_components_from_connected_node(self):
        """Test BFS starting from a node that can't reach all nodes."""
        # Graph: 0 -> 1, 2 -> 3 (disconnected components)
        Adj = [[1], [], [3], []]
        parent = bfs(Adj, 0)
        assert parent == [0, 0, None, None]  # Nodes 2,3 unreachable from 0
    
    def test_complex_connected_graph(self):
        """Test BFS on a more complex connected graph."""
        # Graph with multiple paths and proper BFS level structure
        Adj = [
            [1, 2],    # 0 -> 1, 2
            [0, 3],    # 1 -> 0, 3  
            [0, 4],    # 2 -> 0, 4
            [1],       # 3 -> 1
            [2]        # 4 -> 2
        ]
        parent = bfs(Adj, 0)
        
        # Check parent relationships
        assert parent[0] == 0  # Root
        assert parent[1] == 0  # Level 1 from 0
        assert parent[2] == 0  # Level 1 from 0
        assert parent[3] == 1  # Level 2 from 1
        assert parent[4] == 2  # Level 2 from 2
    
    def test_start_from_different_nodes(self):
        """Test BFS starting from different nodes in the same graph."""
        Adj = [[1], [2], [0]]  # Cycle: 0 -> 1 -> 2 -> 0
        
        # Start from node 0
        parent0 = bfs(Adj, 0)
        assert parent0[0] == 0
        
        # Start from node 1  
        parent1 = bfs(Adj, 1)
        assert parent1[1] == 1
        
        # Start from node 2
        parent2 = bfs(Adj, 2)
        assert parent2[2] == 2
    
    def test_breadth_first_order(self):
        """Test that BFS visits nodes in correct breadth-first order."""
        # Binary tree structure to verify level-by-level traversal
        #     0
        #    / \
        #   1   2
        #  / \   \
        # 3   4   5
        Adj = [[1, 2], [3, 4], [5], [], [], []]
        parent = bfs(Adj, 0)
        
        # Level 0: [0]
        # Level 1: [1, 2] (children of 0)
        # Level 2: [3, 4, 5] (children of 1 and 2)
        assert parent[0] == 0
        assert parent[1] == 0 and parent[2] == 0  # Level 1
        assert parent[3] == 1 and parent[4] == 1 and parent[5] == 2  # Level 2
    
    def test_empty_adjacency_for_some_nodes(self):
        """Test BFS where some nodes have no outgoing edges."""
        Adj = [[1, 2], [], []]  # Only node 0 has outgoing edges
        parent = bfs(Adj, 0)
        assert parent == [0, 0, 0]
    
    def test_self_loop(self):
        """Test BFS on a graph with self-loops."""
        Adj = [[0, 1], []]  # Node 0 has self-loop and edge to 1
        parent = bfs(Adj, 0)
        assert parent == [0, 0]  # Self-loop shouldn't affect result
    
    def test_larger_disconnected_graph(self):
        """Test BFS on a larger graph with disconnected components."""
        # Two separate triangles: 0-1-2 and 3-4-5
        Adj = [
            [1, 2],    # 0 -> 1, 2
            [0, 2],    # 1 -> 0, 2
            [0, 1],    # 2 -> 0, 1
            [4, 5],    # 3 -> 4, 5
            [3, 5],    # 4 -> 3, 5
            [3, 4]     # 5 -> 3, 4
        ]
        
        # Start from first component
        parent = bfs(Adj, 0)
        
        # First component should be reachable
        assert parent[0] == 0
        assert parent[1] == 0
        assert parent[2] == 0
        
        # Second component should not be reachable
        assert parent[3] is None
        assert parent[4] is None  
        assert parent[5] is None
    
    def test_complete_graph(self):
        """Test BFS on a complete graph where every node connects to every other."""
        # Complete graph with 4 nodes
        Adj = [
            [1, 2, 3],  # 0 -> 1, 2, 3
            [0, 2, 3],  # 1 -> 0, 2, 3
            [0, 1, 3],  # 2 -> 0, 1, 3
            [0, 1, 2]   # 3 -> 0, 1, 2
        ]
        parent = bfs(Adj, 0)
        
        assert parent[0] == 0  # Root
        # All other nodes should be direct children of 0 (level 1)
        assert parent[1] == 0
        assert parent[2] == 0
        assert parent[3] == 0
    
    def test_long_path_graph(self):
        """Test BFS on a long path to verify distance/level correctness."""
        # Path: 0 -> 1 -> 2 -> 3 -> 4 -> 5
        Adj = [[1], [2], [3], [4], [5], []]
        parent = bfs(Adj, 0)
        
        # Each node should have the previous node as parent
        expected_parent = [0, 0, 1, 2, 3, 4]
        assert parent == expected_parent
    
    def test_bidirectional_edges(self):
        """Test BFS on a graph with bidirectional edges."""
        # Undirected graph represented as bidirectional edges
        Adj = [
            [1, 3],    # 0 <-> 1, 0 <-> 3
            [0, 2],    # 1 <-> 0, 1 <-> 2  
            [1, 3],    # 2 <-> 1, 2 <-> 3
            [0, 2]     # 3 <-> 0, 3 <-> 2
        ]
        parent = bfs(Adj, 0)
        
        assert parent[0] == 0
        # Nodes 1 and 3 should be children of 0 (level 1)
        assert parent[1] == 0
        assert parent[3] == 0
        # Node 2 should be child of either 1 or 3 (level 2)
        assert parent[2] in [1, 3]
    
    def test_single_edge_cases(self):
        """Test edge cases with minimal graph structures."""
        # Graph with one edge: 0 -> 1
        Adj = [[1], []]
        parent = bfs(Adj, 0)
        assert parent == [0, 0]
        
        # Reverse direction: start from node 1
        parent = bfs(Adj, 1)
        assert parent == [None, 1]  # Node 0 unreachable from 1