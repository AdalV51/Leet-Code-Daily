from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        num_rows = len(matrix)

        # Iterate through each row, starting from the second row
        for row in range(1, num_rows):
            for col in range(num_rows):
                # The value directly above the current cell
                above = matrix[row - 1][col]

                # The value above and to the left of the current cell,
                # or infinity if we are at the left edge
                above_left = matrix[row - 1][col - 1] if col > 0 else float("inf")

                # The value above and to the right of the current cell,
                # or infinity if we are at the right edge
                above_right = (
                    matrix[row - 1][col + 1] if col < num_rows - 1 else float("inf")
                )

                # Update the current cell with the minimum sum of the path reaching it
                matrix[row][col] += min(above, above_left, above_right)

        # Return the minimum value in the last row, which represents
        # the minimum sum of all possible falling paths
        return min(matrix[-1])
