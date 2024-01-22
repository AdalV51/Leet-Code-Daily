from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        maxLootAtPrevious, maxLootAtCurrent = 0, 0

        for currentHouseValue in nums:
            maxLoot = max(currentHouseValue + maxLootAtPrevious, maxLootAtCurrent)
            maxLootAtPrevious = maxLootAtCurrent
            maxLootAtCurrent = maxLoot

        return maxLootAtCurrent
