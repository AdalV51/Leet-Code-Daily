from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # Sort the array
        arr.sort()

        # Initialize the first element to 1
        arr[0] = 1

        # Iterate through the array to ensure the absolute difference is at most 1
        for index in range(1, len(arr)):
            if arr[index] - arr[index - 1] > 1:
                arr[index] = arr[index - 1] + 1

        # The maximum element will be the last element in the sorted array
        return arr[-1]
