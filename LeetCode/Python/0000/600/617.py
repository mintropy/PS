"""
Title : Merge Two Binary Trees
Link : https://leetcode.com/problems/merge-two-binary-trees/
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        return self.search(root1, root2)

    def search(
        self,
        tree1: Optional[TreeNode],
        tree2: Optional[TreeNode],
    ):
        if tree1.val is None and tree2.val is None:
            return None
        elif tree1 is None:
            return tree2
        elif tree2 is None:
            return tree1
        else:
            new_node = TreeNode(val=tree1.val + tree2.val)
            new_node.left = self.search(tree1.left, tree2.left)
            new_node.right = self.search(tree1.right, tree2.right)
            return new_node


if __name__ == "__main__":
    pass
