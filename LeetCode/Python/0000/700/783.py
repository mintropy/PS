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
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = -200_000
        ans = 200_000
        node = root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            ans = min(ans, node.val - prev)
            prev = node.val
            node = node.right
        return ans


if __name__ == "__main__":
    pass
