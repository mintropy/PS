"""
Title : 파티
Link : https://www.acmicpc.net/problem/1238
"""

import sys
import collections
input = sys.stdin.readline

n, m, x = map(int, input().split())
# 주어진 도로
roads = [[] for _ in range(n + 1)]
# 주어진 도로 역방향
roads_reverse = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    roads[a].append((b, c))
    roads_reverse[b].append((a, c))

# x에서 각 도시, 각 도시에서 x로의 비용
dist = [10 ** 6] * (n + 1)
dist[x] = 0
dist_reverse = [10 ** 6] * (n + 1)
dist_reverse[x] = 0

queue = collections.deque([(x, 0)])
queue_reverse = collections.deque([(x, 0)])
while queue:
    p, cost = queue.popleft()
    if cost > dist[p]:
        continue
    for q, c in roads[p]:
        if dist[q] > cost + c:
            dist[q] = cost + c
            queue.append((q, cost + c))
while queue_reverse:
    p, cost = queue_reverse.popleft()
    if cost > dist_reverse[p]:
        continue
    for q, c in roads_reverse[p]:
        if dist_reverse[q] > cost + c:
            dist_reverse[q] = cost + c
            queue_reverse.append((q, cost + c))

max_dist = 0
for i in range(1, n + 1):
    if i == x:
        continue
    if dist[i] + dist_reverse[i] > max_dist:
        max_dist = dist[i] + dist_reverse[i]

print(max_dist)
