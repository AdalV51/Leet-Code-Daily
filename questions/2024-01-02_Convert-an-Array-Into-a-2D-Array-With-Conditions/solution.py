from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # Counter for frequency of each element
        counter_dict = Counter(nums)

        # Find the maximum frequency
        max_frequency = max(counter_dict.values())

        # Preallocate bidimensional array
        bidimensional_array = [[] for _ in range(max_frequency)]

        # Populate the bidimensional array
        for num, freq in counter_dict.items():
            for i in range(freq):
                bidimensional_array[i].append(num)

        return bidimensional_array
