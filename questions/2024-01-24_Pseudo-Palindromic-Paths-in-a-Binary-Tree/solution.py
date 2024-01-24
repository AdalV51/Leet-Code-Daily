from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        """
        Counts the number of pseudo-palindromic paths from the root to leaf nodes.
        A path is pseudo-palindromic if at most one digit has an odd count.
        """
        count = defaultdict(int)
        odd_count_digits = 0  # Count of digits with odd occurrences

        def dfs(node: TreeNode) -> int:
            nonlocal odd_count_digits
            if not node:
                return 0

            # Track the count of the value in this path
            count[node.val] += 1
            # If the count is odd, increment odd_count_digits, otherwise decrement it
            odd_count_change = 1 if count[node.val] % 2 == 1 else -1
            odd_count_digits += odd_count_change

            # If at a leaf node, check if the path is pseudo-palindromic
            if not node.left and not node.right:
                result = 1 if odd_count_digits <= 1 else 0
            else:
                # Continue DFS on children nodes
                result = dfs(node.left) + dfs(node.right)

            # Backtrack: undo the count and odd_count_digits changes
            odd_count_digits -= odd_count_change
            count[node.val] -= 1

            return result

        return dfs(root)
