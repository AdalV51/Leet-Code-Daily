from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        left = 0
        right = 1
        current_time_sum = 0

        while right < len(colors):
            # Grouping same colored balloons
            while right < len(colors) and colors[left] == colors[right]:
                right += 1

            # Calculating cost for groups with more than one balloon
            if (right - left) > 1:
                slice_of_time = neededTime[left:right]
                current_time_sum += sum(slice_of_time) - max(slice_of_time)

            # Move to the next group
            left = right
            right = left + 1

        return current_time_sum
