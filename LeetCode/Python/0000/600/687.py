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
        _, ans, _ = self.search(root)
        return ans

    def search(self, node: Optional[TreeNode]):
        if node is None:
            return 2000, 0, 0
        left_val, left_max, left_count = self.search(node.left)
        right_val, right_max, right_count = self.search(node.right)
        mid_val, mid_max, mid_count = node.val, 0, 0
        tmp = 1
        if mid_val == left_val:
            tmp += left_count
            mid_count = left_count + 1
        if mid_val == right_val:
            tmp += right_count
            mid_count = max(mid_count, right_count)
        mid_max = max(left_max, right_max, tmp)
        return mid_val, mid_max, mid_count


if __name__ == "__main__":
    pass
