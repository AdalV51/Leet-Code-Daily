from collections import defaultdict, deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.node_connections = defaultdict(list)

    def createNodeConnections(self, node: Optional[TreeNode]):
        """
        Creates a bidirectional connection map of the tree nodes.
        """
        if node:
            if node.left:
                self.node_connections[node.val].append(node.left.val)
                self.node_connections[node.left.val].append(node.val)
                self.createNodeConnections(node.left)
            if node.right:
                self.node_connections[node.val].append(node.right.val)
                self.node_connections[node.right.val].append(node.val)
                self.createNodeConnections(node.right)

    def bfs_to_find_maximum_distance(self, start: int) -> int:
        """
        Performs BFS to find the maximum distance from the start node.
        """
        nodes_to_visit = deque([(start, 0)])
        visited = {start}
        distance = 0

        while nodes_to_visit:
            current_node, distance = nodes_to_visit.popleft()

            for node in self.node_connections[current_node]:
                if node not in visited:
                    nodes_to_visit.append((node, distance + 1))
                    visited.add(node)

        return distance

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        """
        Calculates the amount of time (maximum distance) from the start node.
        """
        if root is None:
            return 0

        self.createNodeConnections(root)
        return self.bfs_to_find_maximum_distance(start)
