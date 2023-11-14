class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        For a palindrome of length 3, such as "aba", "bcb", "cac", etc., the
        first and the last characters must be the same, and the middle character
        can be any character. Therefore, for each unique character in the string,
        you can find the first and last occurrence of that character and count the
        number of distinct characters that appear between them.
        """

        result = 0
        for char in set(s):  # Iterate over each unique character
            first = s.index(char)  # Find first occurrence
            last = s.rindex(char)  # Find last occurrence
            if last - first > 1:
                result += len(
                    set(s[first + 1 : last])
                )  # Count unique characters in between
        return result
