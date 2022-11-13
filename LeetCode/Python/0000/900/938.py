"""
Title : Range Sum of BST
Link : https://leetcode.com/problems/range-sum-of-bst/
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.search(root, low, high)

    def search(self, node, low, high):
        val = node.val
        if low <= node.val <= high:
            val = node.val
        else:
            val = 0
        if node.right is not None:
            val += self.search(node.right, low, high)
        if node.left is not None:
            val += self.search(node.left, low, high)
        return val


if __name__ == "__main__":
    pass
