from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ocurrences = Counter(arr)

        return len(ocurrences.keys()) == len(set(ocurrences.values()))
