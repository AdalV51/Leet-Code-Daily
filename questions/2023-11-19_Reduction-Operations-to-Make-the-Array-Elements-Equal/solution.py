from collections import Counter
from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()  # Sort the numbers to ensure ascending order.

        # Count the occurrences of each number in the list.
        counter = Counter(nums)

        operations = 0
        multiplier = 0

        # Iterate through each number and its frequency.
        for _, value in counter.items():
            # Increment operations based on frequency and a growing multiplier.
            operations += value * multiplier
            multiplier += 1  # Increment multiplier for next unique number.

        return operations
