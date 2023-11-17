from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        # Sort nums
        nums.sort()

        # Define pointers
        i, j = 0, len(nums)-1

        # Array that will sotre the results
        max_pair_sum = -float("inf")

        while i < j:
            # Update max_pair_sum directly as sum will be maximum at middle
            max_pair_sum = max(max_pair_sum, nums[i] + nums[j])
            i += 1
            j -= 1

        return max_pair_sum
