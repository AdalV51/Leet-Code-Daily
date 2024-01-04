from collections import Counter
from math import ceil
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        frequency_counter = Counter(nums)
        total_operations = 0

        for count in frequency_counter.values():
            # If any number appears only once, it's impossible to make all elements equal
            if count == 1:
                return -1

            # Add the ceiling of the count divided by 3 to the total operations
            total_operations += ceil(count / 3)

        return total_operations
