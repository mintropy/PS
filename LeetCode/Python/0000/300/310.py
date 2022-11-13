"""
Title : Minimum Height Trees
Link : https://leetcode.com/problems/minimum-height-trees/
"""

from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        node_count = n
        nodes = {i for i in range(n)}
        graph = [set() for _ in range(n)]
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
        leaf = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaf.append(i)
        while node_count > 2:
            next_leaf = []
            for x in leaf:
                y = graph[x].pop()
                graph[y].remove(x)
                if len(graph[y]) == 1:
                    next_leaf.append(y)
                node_count -= 1
                nodes.remove(x)
            leaf = next_leaf[::]
        return list(nodes)


if __name__ == "__main__":
    n = 6
    edges = [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]

    solution = Solution()
    print(solution.findMinHeightTrees(n, edges))
