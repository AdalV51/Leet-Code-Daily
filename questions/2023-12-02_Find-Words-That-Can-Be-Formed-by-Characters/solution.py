from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter_chars = Counter(chars)
        sum_of_lengths = 0

        for word in words:
            if Counter(word) <= counter_chars:
                sum_of_lengths += len(word)

        return sum_of_lengths
