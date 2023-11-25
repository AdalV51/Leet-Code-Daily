from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        my_coins = 0

        left, right = 0, len(piles) - 2

        while left < right:
            my_coins += piles[right]

            left += 1
            right -= 2

        return my_coins
