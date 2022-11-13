"""
Title : Binary Search Tree To Grater Sum Tree
Link : https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root.left is None and root.right is None:
            return root
        self.search(root, 0)
        return root

    def search(self, node, val):
        if node.right is not None:
            val = self.search(node.right, val)
        val += node.val
        node.val = val
        if node.left is not None:
            val = self.search(node.left, val)
        return val


if __name__ == "__main__":
    pass
