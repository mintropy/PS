"""
Title : Network Delay Time
Link : https://leetcode.com/problems/network-delay-time/
"""

from collections import deque
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = [[] for _ in range(n + 1)]
        for u, v, w in times:
            edges[u].append((v, w))
        max_times = [-1] * (n + 1)
        queue = deque([(k, 0)])
        while queue:
            x, t = queue.popleft()
            if -1 != max_times[x] <= t:
                continue
            max_times[x] = t
            for y, w in edges[x]:
                queue.append((y, t + w))
        if max_times.count(-1) > 1:
            return -1
        return max(max_times)


if __name__ == "__main__":
    times = [[1, 2, 1], [2, 3, 2], [1, 3, 4]]
    n = 3
    k = 1

    solution = Solution()
    print(solution.networkDelayTime(times, n, k))
