from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Initialize a deque to store tree nodes for traversal
        binary_tree_elements = deque([root])
        range_sum = 0

        while binary_tree_elements:
            current_element = binary_tree_elements.pop()

            # Check if the current node's value is within the specified range
            if low <= current_element.val <= high:
                range_sum += current_element.val

            # Add left and right children to the deque if they exist
            if current_element.left:
                binary_tree_elements.append(current_element.left)
            if current_element.right:
                binary_tree_elements.append(current_element.right)

        return range_sum
