from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """
        Calculate the sum of absolute differences for each element in the array.
        The sum of absolute differences of an array element is the total sum of
        the difference between this element and each other element in the array.

        Args:
        nums (List[int]): A list of integers.

        Returns:
        List[int]: A list containing the sum of absolute differences for each array element.
        """
        nums_length = len(nums)
        total_sum = sum(nums)
        current_left_sum = 0
        absolute_differences = []

        for idx, num in enumerate(nums):
            current_right_sum = total_sum - current_left_sum - num
            left_count = idx
            right_count = nums_length - idx - 1

            # Calculate the total difference on the left side:
            # Multiplies the current number by its index (number of elements on the left)
            # and subtracts the sum of all elements to the left of the current number.
            left_total = left_count * num - current_left_sum

            # Calculate the total difference on the right side:
            # Subtracts the product of the current number and the number of elements on the right
            # from the sum of all elements to the right of the current number.
            right_total = current_right_sum - right_count * num

            absolute_differences.append(left_total + right_total)
            current_left_sum += num

        return absolute_differences
