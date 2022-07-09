"""
Title : 간선 이어가기 2
Link : https://www.acmicpc.net/problem/14284
"""

import sys, collections
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

st, end = map(int, input().split())

INF = 10 ** 7
dist = [INF] * (n + 1)

queue = collections.deque([st])
dist[st] = 0

while queue:
    p = queue.popleft()
    d0 = dist[p]
    for q, d in edges[p]:
        if d0 + d < dist[q]:
            dist[q] = d0 + d
            queue.append(q)

print(dist[end])
