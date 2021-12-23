"""
Title : 택배 배송
Link : https://www.acmicpc.net/problem/5972
"""

import heapq
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M = MIIS()
roads = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = MIIS()
    roads[a].append((b, c))
    roads[b].append((a, c))

heap = [(0, 1)]
visited = [False] * (N + 1)

while heap:
    d, cow = heapq.heappop(heap)
    if cow == N:
        print(d)
        break
    if visited[cow]:
        continue
    visited[cow] = True
    for b, c in roads[cow]:
        if not visited[b]:
            heapq.heappush(heap, (d + c, b))
