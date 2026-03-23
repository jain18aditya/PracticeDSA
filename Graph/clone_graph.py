"""
LeetCode 133 - Clone Graph

Problem:

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

Each node in the graph contains:
- An integer value (val)
- A list of its neighbors (neighbors)

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

Input:
- A node from the graph
- The graph is undirected and connected
- The graph may contain cycles

Output:
- Return a deep copy of the graph

Deep Copy Definition:
- All nodes in the new graph must be newly created
- The structure (connections between nodes) must be identical
- No reference from the original graph should be reused

Example:

Input (Adjacency List):
[[2,4],[1,3],[2,4],[1,3]]

Explanation:
Node 1 is connected to nodes 2 and 4
Node 2 is connected to nodes 1 and 3
Node 3 is connected to nodes 2 and 4
Node 4 is connected to nodes 1 and 3

Output:
[[2,4],[1,3],[2,4],[1,3]]

Constraints:
- 0 <= number of nodes <= 100
- 1 <= Node.val <= 100
- Each node’s value is unique
- No duplicate edges
- The graph is connected

Goal:
Create a deep copy of the graph using DFS or BFS while handling cycles.
"""
from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        start = node
        o_to_n = {}
        stack = [start]
        visited = set()
        visited.add(start)
        while stack:
            node = stack.pop()
            #Create node
            o_to_n[node] = Node(node.val)

            #Traverse neighbors
            for nei in node.neighbors:
                if nei not in visited:
                    stack.append(nei)
                    visited.add(nei)

        #Second pass → connect neighbors
        for old_node, new_node in o_to_n.items():
            for nei in old_node.neighbors:
                new_nei = o_to_n[nei]
                new_node.neighbors.append(new_nei)

        return o_to_n[start]


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.neighbors = [node2]
node2.neighbors = [node3]
node3.neighbors = [node1]  # cycle

clone = Solution().cloneGraph(node1)

print(clone.val)
print(clone.neighbors[0].neighbors[0].neighbors[0].val)

print([n.val for n in clone.neighbors])