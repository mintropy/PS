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
        return self.search(root, 1)[0]

    def search(self, node: Optional[TreeNode], depth):
        if node is None:
            return 0, depth - 1
        left_ans, left_max = self.search(node.left, depth + 1)
        right_ans, right_max = self.search(node.right, depth + 1)
        tmp = left_max + right_max - depth * 2
        return max(left_ans, right_ans, tmp), max(left_max, right_max)


if __name__ == "__main__":
    pass
