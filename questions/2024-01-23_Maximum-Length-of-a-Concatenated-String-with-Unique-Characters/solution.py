from collections import Counter
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # A set to store the unique characters of concatenated strings.
        unique_chars = set()

        def has_overlap(existing_chars, new_str):
            """Check if adding new_str to existing_chars causes any character overlap."""
            combined_count = Counter(existing_chars) + Counter(new_str)
            return max(combined_count.values()) > 1

        def find_max_length(index):
            """Backtrack function to find the maximum length of a unique character string."""
            if index == len(arr):
                return len(unique_chars)

            max_length = 0
            if not has_overlap(unique_chars, arr[index]):
                # Add characters of the current string to the set and recurse
                unique_chars.update(arr[index])
                max_length = find_max_length(index + 1)
                # Remove the characters after exploring this path
                unique_chars.difference_update(arr[index])

            # Explore the path where current string is not included
            return max(max_length, find_max_length(index + 1))

        return find_max_length(0)
