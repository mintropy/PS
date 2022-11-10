"""
Title : Serialize and Deserialize Binary Tree
Link : https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""

from collections import deque

# Definition for a binary tree node.
# Defining a class called TreeNode.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        tree = ["#"]
        while queue:
            node = queue.popleft()
            if node is None:
                tree.append("#")
            else:
                queue.append(node.left)
                queue.append(node.right)
                tree.append(f"{node.val}")
        return " ".join(tree)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split()
        if nodes[1] == "#":
            return None
        root = TreeNode(int(nodes[1]))
        queue = deque([root])
        idx = 2
        while queue:
            node = queue.popleft()
            if nodes[idx] != "#":
                node.left = TreeNode(int(nodes[idx]))
                queue.append(node.left)
            idx += 1
            if nodes[idx] != "#":
                node.right = TreeNode(int(nodes[idx]))
                queue.append(node.right)
            idx += 1
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
