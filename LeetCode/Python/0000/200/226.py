"""
Title : Invert Binary Tree
Link : https://leetcode.com/problems/invert-binary-tree/
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.search(root)

    def search(self, node: Optional[TreeNode]):
        if node is None:
            return
        node.left, node.right = node.right, node.left
        self.search(node.left)
        self.search(node.right)
        return node


if __name__ == "__main__":
    pass
