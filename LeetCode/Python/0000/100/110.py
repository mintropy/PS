"""
Title : Balanced Binary Tree
Link : https://leetcode.com/problems/balanced-binary-tree/
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.search(root, 1)[0]

    def search(self, node: Optional[TreeNode], depth):
        if node is None:
            return True, depth - 1
        left_condition, left_depth = self.search(node.left, depth + 1)
        right_condition, right_depth = self.search(node.right, depth + 1)
        if not left_condition or not right_condition:
            return False, 0
        if abs(left_depth - right_depth) <= 1:
            return True, max(left_depth, right_depth)
        return False, 0


if __name__ == "__main__":
    pass
