from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # Count occurrences of each character in s and t
        s_occurrences = Counter(s)
        t_occurrences = Counter(t)

        # Initialize the minimum steps required to zero
        minimum_steps = 0

        # Iterate over the occurrences in t
        for char in t_occurrences:
            # If the character in t is more frequent than in s, add the difference to minimum_steps
            if t_occurrences[char] > s_occurrences[char]:
                minimum_steps += t_occurrences[char] - s_occurrences[char]

        return minimum_steps
