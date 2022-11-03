"""
Title : Maximu Depth of Binary Tree
Link : https://leetcode.com/problems/maximum-depth-of-binary-tree/
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
        self.depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is not None:
            self.search(root, 1)
        return self.depth

    def search(self, node: TreeNode, depth: int) -> None:
        if node.left is None and node.right is None:
            self.depth = max(self.depth, depth)
            return
        if node.left is not None:
            self.search(node.left, depth + 1)
        if node.right is not None:
            self.search(node.right, depth + 1)


if __name__ == "__main__":
    pass
