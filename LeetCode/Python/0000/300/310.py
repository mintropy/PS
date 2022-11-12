"""
Title : Minimum Height Trees
Link : https://leetcode.com/problems/minimum-height-trees/
"""

from typing import List
from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return 1
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        node = self.find_node(n, 0, graph)[0]
        nodes = self.find_node(n, node, graph)
        nodes.append(node)
        return nodes

    def find_node(self, n, st, graph):
        queue = [st]
        ans = []
        visited = [False] * n
        while queue:
            ans = queue[::]
            next_queue = set()
            for x in queue:
                for y in graph[x]:
                    if not visited[y]:
                        next_queue.add(y)
            next_queue = list(next_queue)
            queue = next_queue[::]
        return ans


if __name__ == "__main__":
    pass
