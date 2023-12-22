class Solution:
    def countOcurrences(self, word: str, letter: str) -> int:
        return word.count(letter)

    def maxScore(self, s: str) -> int:
        max_score = 0

        for index in range(1, len(s)):
            current_score = self.countOcurrences(s[:index], "0") + self.countOcurrences(
                s[index:], "1"
            )
            max_score = max(max_score, current_score)

        return max_score
