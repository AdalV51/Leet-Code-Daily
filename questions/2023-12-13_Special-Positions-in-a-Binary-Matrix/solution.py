from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows_number = len(mat)
        columns_number = len(mat[0])

        row_count = [0] * rows_number
        col_count = [0] * columns_number
        one_positions = []  # List to store the positions of 1s

        # First pass: count the number of 1s in each row and column
        # and store the positions of 1s
        for row in range(rows_number):
            for col in range(columns_number):
                if mat[row][col] == 1:
                    row_count[row] += 1
                    col_count[col] += 1
                    one_positions.append((row, col))

        nums_special = 0
        # Second pass: Check only the positions of 1s
        for row, col in one_positions:
            if row_count[row] == 1 and col_count[col] == 1:
                nums_special += 1

        return nums_special
