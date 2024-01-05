from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Calculates the length of the longest increasing subsequence in the array.
        """
        n = len(nums)
        if n == 0:
            return 0

        longest_subseq = [1] * n
        for current in range(1, n):
            for previous in range(current):
                if nums[current] > nums[previous]:
                    longest_subseq[current] = max(
                        longest_subseq[current], longest_subseq[previous] + 1
                    )

        return max(longest_subseq)
