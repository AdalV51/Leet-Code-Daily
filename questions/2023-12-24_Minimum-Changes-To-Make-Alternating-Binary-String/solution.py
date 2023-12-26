class Solution:
    def minOperations(self, s: str) -> int:
        # Counters for the number of changes needed to match each pattern
        start_with_0 = 0  # Pattern "01"
        start_with_1 = 0  # Pattern "10"

        for index, char in enumerate(s):
            # Increment counters based on mismatches with each pattern
            if char != "01"[index % 2]:
                start_with_0 += 1
            if char != "10"[index % 2]:
                start_with_1 += 1

        # Return the minimum number of changes required
        return min(start_with_0, start_with_1)
