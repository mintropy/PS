"""
Title : 특정 거리의 도시 찾기
Link : https://www.acmicpc.net/problem/18352
"""

import sys, collections
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

queue = collections.deque([(x, 0)])
visited = [False] * (n + 1)
visited[x] = True
dist_k = []
while queue:
    y, d = queue.popleft()
    if d > k:
        break
    if d == k:
        dist_k.append(y)
        continue
    for z in graph[y]:
        if not visited[z]:
            visited[z] = True
            queue.append((z, d + 1))

if dist_k:
    for x in sorted(dist_k):
        print(x)
else:
    print(-1)