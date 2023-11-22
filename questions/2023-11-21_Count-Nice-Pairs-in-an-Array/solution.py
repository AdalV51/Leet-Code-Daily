from collections import Counter
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        counter = Counter([x - int(str(x)[::-1]) for x in nums])

        sumatory = 0

        for value in counter.values():
            sumatory += (value * (value - 1)) // 2

        return sumatory % (10**9 + 7)
