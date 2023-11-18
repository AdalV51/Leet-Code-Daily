from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Calculate the maximum number as 2^n - 1, where n is the length of nums
        max_number = 2 ** len(nums) - 1

        # Convert nums into a set of integers for faster membership checking
        set_nums = {int(num, 2) for num in nums}

        # Iterate through numbers from 0 to max_number
        for number in range(max_number + 1):
            # Check if the integer representation of number is not in set_nums
            if number not in set_nums:
                # Return number as a binary string with a fixed length
                return format(number, "0{width}b".format(width=len(nums)))
