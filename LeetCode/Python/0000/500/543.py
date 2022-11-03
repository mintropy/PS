"""
Title : Diameter of Binary Tree
Link : https://leetcode.com/problems/diameter-of-binary-tree/
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.ans = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.search(root, 1)[1]

    def search(self, node, depth):
        if node.left is None and node.right is None:
            return 0, depth
        left_depth = right_depth = depth
        left_max = right_max = 0
        if node.left is not None:
            left_max, left_depth = self.search(node.left, depth + 1)
        if node.right is not None:
            right_max, right_depth = self.search(node.right, depth + 1)
        self.ans = max(self.ans, left_max + right_max)
        return max(left_max, right_max), max(left_depth, right_depth)


if __name__ == "__main__":
    pass
