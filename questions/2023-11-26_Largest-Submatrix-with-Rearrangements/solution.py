from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        """
        Calculate the largest submatrix with all ones after rearranging rows.

        Args:
        matrix (List[List[int]]): A binary matrix.

        Returns:
        int: The area of the largest submatrix that can be formed with all ones.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        max_area = 0

        for row in range(rows):
            for col in range(cols):
                # Increment the cell value if the cell above is non-zero
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]

            # Sort the current row in descending order
            sorted_row = sorted(matrix[row], reverse=True)

            # Calculate the maximum area considering each column as the height
            for i, height in enumerate(sorted_row):
                max_area = max(max_area, height * (i + 1))

        return max_area
