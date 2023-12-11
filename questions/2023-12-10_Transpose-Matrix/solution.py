from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        num_columns = len(matrix[0])

        transposed_matrix = [[] for _ in range(num_columns)]

        for row in matrix:
            for index, column in enumerate(row):
                transposed_matrix[index].append(column)

        return transposed_matrix
