from collections import Counter
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # Check if total length of all words is divisible by the number of words
        total_length = sum(len(word) for word in words)
        if total_length % len(words) != 0:
            return False

        # Count the occurrences of each character
        word_counter = Counter()
        for word in words:
            word_counter += Counter(word)

        # Check if each character's count is divisible by the number of words
        return all(value % len(words) == 0 for value in word_counter.values())
