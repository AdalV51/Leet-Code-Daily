from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        columns = len(img[0])
        new_img = [[0 for _ in range(columns)] for _ in range(rows)]
        movements = [
            # No movement
            (0, 0),
            # Horizontal
            (-1, 0),
            (1, 0),
            # Vertical
            (0, -1),
            (0, 1),
            # Diagonal
            (-1, -1),
            (1, -1),
            (1, 1),
            (-1, 1),
        ]

        for row in range(rows):
            for column in range(columns):
                number_of_elements = 0
                current_sum = 0

                for movement_row, movement_col in movements:
                    if (
                        0 <= (row + movement_row) < rows
                        and 0 <= (column + movement_col) < columns
                    ):
                        number_of_elements += 1
                        current_sum += img[row + movement_row][column + movement_col]

                new_img[row][column] = current_sum // number_of_elements

        return new_img
