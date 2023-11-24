from typing import List


class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        def is_arithmetic(arr):
            arr.sort()
            difference = arr[1] - arr[0]
            for i in range(2, len(arr)):
                if arr[i] - arr[i - 1] != difference:
                    return False
            return True

        return [is_arithmetic(nums[left : right + 1]) for left, right in zip(l, r)]
