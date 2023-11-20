from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        chars = ["M", "P", "G"]

        # Initialize a dictionary to store the highest index for each character
        highest_indices = {char: None for char in chars}
        total_time = 0

        # Keep track of total trash recolected
        trash_recolected = sum([len(x) for x in garbage])

        # Iterate in reverse order
        for i in range(len(garbage) - 1, -1, -1):
            for char in chars:
                if char in garbage[i] and highest_indices[char] is None:
                    highest_indices[char] = i
                    total_time += sum(travel[:i])

            # Check if all characters have been found
            if all(highest_indices[char] is not None for char in chars):
                break

        return trash_recolected + total_time
