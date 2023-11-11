import heapq
from collections import defaultdict
from typing import List


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        # Initialize a graph with a default dictionary to store adjacency lists
        self.graph = defaultdict(list)
        # For each edge, add it to the graph
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: List[int]) -> None:
        # Extract nodes and cost from the edge, then add the edge to the graph
        from_node, to_node, cost = edge
        self.graph[from_node].append((to_node, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        # Initialize a heap with the starting node and a cost of 0
        heap = [(0, node1)]
        # Set to keep track of visited nodes
        visited = set()

        while heap:
            # Pop the node with the smallest cost from the heap
            cost, node = heapq.heappop(heap)
            visited.add(node)

            if node == node2:  # Check if the target node is reached
                return cost  # Return the cost for the shortest path

            # Iterate through the neighbors of the current node
            for neighbor, neighbor_cost in self.graph[node]:
                # Add the neighbor to the heap if it's not visited
                if neighbor not in visited:
                    heapq.heappush(heap, (neighbor_cost + cost, neighbor))

        return -1  # Return -1 if there's no path between node1 and node2


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
