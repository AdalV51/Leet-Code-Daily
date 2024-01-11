from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node, min_val, max_val):
            if not node:
                return 0
            return max(
                abs(node.val - min_val),
                abs(node.val - max_val),
                helper(node.left, min(node.val, min_val), max(node.val, max_val)),
                helper(node.right, min(node.val, min_val), max(node.val, max_val)),
            )

        return helper(root, root.val, root.val)
