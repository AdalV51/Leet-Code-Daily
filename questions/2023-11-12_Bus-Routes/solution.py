from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0  # If the source and target are the same, no buses are needed.

        # Create a graph where each stop is a key and the value is a list of buses (routes) that stop there.
        stop_to_bus = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_bus[stop].add(i)

        # Use BFS to find the shortest path. Queue items are (stop, buses_taken).
        queue = deque([(source, 0)])
        visited_stops = set([source])
        visited_buses = set()

        while queue:
            current_stop, buses_taken = queue.popleft()

            # Check all the buses that go through the current stop.
            for bus in stop_to_bus[current_stop]:
                if bus in visited_buses:
                    continue  # Skip if we've already used this bus.

                visited_buses.add(bus)  # Mark this bus as used.

                # Check all stops for the current bus.
                for stop in routes[bus]:
                    if stop == target:
                        return (
                            buses_taken + 1
                        )  # Found the target, return the number of buses taken.

                    if stop not in visited_stops:
                        visited_stops.add(stop)  # Mark this stop as visited.
                        queue.append(
                            (stop, buses_taken + 1)
                        )  # Add to queue with an incremented bus count.

        return -1  # If the queue is empty, the target is unreachable.
