from collections import Counter
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        array_counter = Counter(arr)

        return max(array_counter, key=array_counter.get)
