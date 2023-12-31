class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_occurrence = {}
        max_difference = -1

        for index, character in enumerate(s):
            if character in first_occurrence:
                # Calculate the difference for characters seen more than once
                max_difference = max(
                    max_difference, index - first_occurrence[character] - 1
                )
            else:
                # Store the first occurrence of the character
                first_occurrence[character] = index

        return max_difference
