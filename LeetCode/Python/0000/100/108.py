"""
Title : Convert Sorted Array to Binary Search Tree
Link : https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""

from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        length = len(nums)
        root = TreeNode(nums[(length - 1) // 2])
        queue = deque([(root, 0, length - 1)])
        while queue:
            node, left, right = queue.popleft()
            if left == right:
                continue
            mid = (left + right) // 2
            if mid > left:
                node.left = TreeNode(nums[(mid - 1 + left) // 2])
                queue.append((node.left, left, mid - 1))
            if mid < right:
                node.right = TreeNode(nums[(right + mid + 1) // 2])
                queue.append((node.right, mid + 1, right))
        return root


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]

    solution = Solution()
    print(solution.sortedArrayToBST(nums))
