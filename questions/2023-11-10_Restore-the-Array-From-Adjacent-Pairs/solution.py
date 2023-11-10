from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # Check for empty or malformed input
        if not adjacentPairs:
            return []

        mapper = defaultdict(list)

        # Building the graph representation from pairs
        for a, b in adjacentPairs:
            mapper[a].append(b)
            mapper[b].append(a)

        # Finding the starting element (which is at an edge)
        start_element = [key for key, value in mapper.items() if len(value) == 1][0]

        # Initializing queue and visited set with the start element
        queue = [start_element]
        visited = {start_element}

        # Loop until the queue's length is equal to the number of elements in the original array
        while len(queue) < len(adjacentPairs) + 1:
            current_element = queue[-1]
            possible_options = mapper[current_element]

            for option in possible_options:
                if option not in visited:
                    visited.add(option)
                    queue.append(option)
                    break  # Break after adding one unvisited option

        return queue
