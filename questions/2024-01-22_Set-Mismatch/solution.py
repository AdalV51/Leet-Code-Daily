from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]):
        number_frequency = {i: 1 for i in range(1, len(nums) + 1)}

        for number in nums:
            number_frequency[number] -= 1

        duplicate_number, missing_number = 0, 0

        for key, value in number_frequency.items():
            if value == -1:
                duplicate_number = key
            elif value == 1:
                missing_number = key

        return [duplicate_number, missing_number]
