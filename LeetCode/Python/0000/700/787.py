"""
Title : Cheapest Flights Within K Stops
Link : https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""

from collections import deque
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = [[] for _ in range(n)]
        for st, to, p in flights:
            graph[st].append((to, p))
        for i, line in enumerate(graph):
            graph[i] = sorted(line, key=lambda x: x[1])
        visited = [[1_000_000] * (k + 2) for _ in range(n)]
        queue = deque([(src, 0, 0)])
        while queue:
            x, time, stop = queue.popleft()
            if visited[x][stop] <= time:
                continue
            visited[x][stop] = time
            if x == dst or stop == k + 1:
                continue
            for y, p in graph[x]:
                queue.append((y, time + p, stop + 1))
        ans = min(visited[dst])
        return ans if ans != 1_000_000 else -1


if __name__ == "__main__":
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1

    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src = 0
    dst = 3
    k = 1

    solution = Solution()
    print(solution.findCheapestPrice(n, flights, src, dst, k))
