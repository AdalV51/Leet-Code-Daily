from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  # Sort the greed factor of children
        s.sort()  # Sort the size of cookies

        child_index = 0  # Initialize child index
        cookie_index = 0  # Initialize cookie index

        # Loop through children and cookies
        while child_index < len(g) and cookie_index < len(s):
            if s[cookie_index] >= g[child_index]:
                # If the cookie can satisfy the child, move to next child
                child_index += 1

            # Move to next cookie
            cookie_index += 1

        return child_index  # The count of content children
