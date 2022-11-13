"""
Title : Construct Binary Tree from Preorder and Inorder Traversal
Link : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            idx = inorder.index(preorder.pop(0))
            node = TreeNode(inorder[idx])
            node.left = self.buildTree(preorder, inorder[0:idx])
            node.right = self.buildTree(preorder, inorder[idx + 1 :])
            return node


if __name__ == "__main__":
    pass
