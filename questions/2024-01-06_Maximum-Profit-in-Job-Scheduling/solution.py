from bisect import bisect_right
from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        # Combine the three lists into a single list of tuples (end_time, start_time, profit)
        jobs = sorted(zip(endTime, startTime, profit))

        # Initialize a list to store the maximum profit for each job
        dp = [0] * (len(profit) + 1)

        for i, (current_end_time, current_start_time, current_profit) in enumerate(
            jobs
        ):
            # Find the index of the latest job that doesn't conflict with the current job
            index = bisect_right(jobs, current_start_time, hi=i, key=lambda x: x[0])

            # Calculate the maximum profit at this position
            dp[i + 1] = max(dp[i], dp[index] + current_profit)

        return dp[len(profit)]
