from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """
        Hint 1: Notice that numbers with equal sums of row and column indexes belong to the same diagonal.

        Hint 2: Store them in tuples (sum, row, val), sort them, and then regroup the answer.
        """

        diagonals = defaultdict(list)

        for row_index, row in enumerate(nums):
            for column_index, value in enumerate(row):
                # The sum of indices determines the diagonal; append to the end of the list
                diagonals[row_index + column_index].append(value)

        # Flatten the list of diagonals into a single list
        return [val for diagonal in diagonals.values() for val in reversed(diagonal)]
