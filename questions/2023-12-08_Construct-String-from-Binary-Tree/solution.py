# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if not root:
            return ""

        # Convert the value of the node to string
        result = str(root.val)

        # If left child exists, process left subtree
        if root.left:
            result += "(" + self.tree2str(root.left) + ")"

        # If right child exists, process right subtree
        # Note: We need to include parenthesis for the right child even if the left child is absent
        if root.right:
            if not root.left:
                result += "()"
            result += "(" + self.tree2str(root.right) + ")"

        return result
