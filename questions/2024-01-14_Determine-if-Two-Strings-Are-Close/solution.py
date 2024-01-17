from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Count the occurrences of each character in both words
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        # Check if both strings have the same unique set of characters
        if set(counter1.keys()) != set(counter2.keys()):
            return False

        # Check if both strings have the same frequency of characters
        if sorted(counter1.values()) != sorted(counter2.values()):
            return False

        return True
