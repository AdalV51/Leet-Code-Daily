from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_1, min_2 = float("inf"), float("inf")

        for price in prices:
            if price < min_1:
                min_2 = min_1
                min_1 = price
            elif price < min_2:
                min_2 = price

        if (money - (min_1 + min_2)) >= 0:
            return money - (min_1 + min_2)
        else:
            return money
