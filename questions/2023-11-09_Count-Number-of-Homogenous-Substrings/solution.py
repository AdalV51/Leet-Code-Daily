class Solution:
    def _getCountOfHomogeneousString(self, homogeneous_string: str) -> int:
        """
        Calculate the count of homogeneous substrings using the Triangular number formula.

        Args:
            homogeneous_string (str): The input homogeneous string.

        Returns:
            int: The count of homogeneous substrings.
        """
        n = len(homogeneous_string)
        return (n * (n + 1)) // 2

    def countHomogenous(self, s: str) -> int:
        """
        Count the total number of homogeneous substrings in the given string.

        Args:
            s (str): The input string.

        Returns:
            int: The count of homogeneous substrings modulo 10^9 + 7.
        """
        current_homogeneous_substring = ""
        total_count = 0

        for character in s:
            if (
                not current_homogeneous_substring
                or current_homogeneous_substring[-1] == character
            ):
                current_homogeneous_substring += character
            else:
                # Count the number of homogeneous substrings in the current substring.
                total_count += self._getCountOfHomogeneousString(
                    current_homogeneous_substring
                )
                current_homogeneous_substring = character

        # Count the number of homogeneous substrings in the last substring.
        total_count += self._getCountOfHomogeneousString(current_homogeneous_substring)

        return total_count % (10**9 + 7)
