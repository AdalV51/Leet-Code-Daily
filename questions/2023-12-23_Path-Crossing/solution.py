class Solution:
    def isPathCrossing(self, path: str) -> bool:
        movements = {"N": (0, 1), "S": (0, -1), "W": (-1, 0), "E": (1, 0)}
        visited = set([(0, 0)])
        current_x, current_y = 0, 0

        for step in path:
            dx, dy = movements[step]
            current_x += dx
            current_y += dy

            if (current_x, current_y) in visited:
                return True

            visited.add((current_x, current_y))

        return False
