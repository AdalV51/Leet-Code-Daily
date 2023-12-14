from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows_number, columns_number = len(grid), len(grid[0])

        ones_row, zeros_row = [0] * rows_number, [0] * rows_number
        ones_col, zeros_col = [0] * columns_number, [0] * columns_number

        # Combined loop for counting ones and zeros
        for row in range(rows_number):
            for col in range(columns_number):
                if grid[row][col] == 1:
                    ones_row[row] += 1
                    ones_col[col] += 1
                else:
                    zeros_row[row] += 1
                    zeros_col[col] += 1

        # Using list comprehension for constructing the diff_matrix
        return [
            [
                ones_row[row] + ones_col[col] - zeros_row[row] - zeros_col[col]
                for col in range(columns_number)
            ]
            for row in range(rows_number)
        ]
