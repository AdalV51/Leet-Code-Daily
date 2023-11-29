class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += (
                n & 1
            )  # If the least significant bit is 1, then (n & 1) will result in 1.
            n >>= 1  # Right shift to discard the least significant bit.
        return count
