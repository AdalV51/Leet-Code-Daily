from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder_traversal = []

        def helper_function(root):
            if root:
                helper_function(root.left)
                self.inorder_traversal.append(root.val)
                helper_function(root.right)

        helper_function(root)

        return self.inorder_traversal
