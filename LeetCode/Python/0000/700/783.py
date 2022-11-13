"""
Title : Minimum Distance Between BST Nodes
Link : https://leetcode.com/problems/minimum-distance-between-bst-nodes/
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
        self.ans = 100_000

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.search(root)
        return self.ans

    def search(self, node):
        if node is None:
            return 200_000
        val = node.val
        left, right = self.search(node.left), self.search(node.right)
        self.ans = min(self.ans, abs(val - left), abs(val - right))
        return val


if __name__ == "__main__":
    pass
