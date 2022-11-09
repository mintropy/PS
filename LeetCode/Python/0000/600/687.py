"""
Title : Longest Univalue Path
Link : https://leetcode.com/problems/longest-univalue-path/
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        return self.search(root, 1)[1]

    def search(self, node: Optional[TreeNode], depth):
        if node is None:
            return -1, 0, depth - 1
        left_val, left_ans, left_max = self.search(node.left, depth + 1)
        right_val, right_ans, right_max = self.search(node.right, depth + 1)
        mid_ans , mid_max = 0, depth
        if node.val == left_val:
            mid_ans += left_max - depth
            mid_max = max(mid_max, left_max)
        if node.val == right_val:
            mid_ans += right_max - depth
            mid_max = max(mid_max, right_max)
        return node.val, max(left_ans, right_ans, mid_ans), mid_max


if __name__ == "__main__":
    pass
