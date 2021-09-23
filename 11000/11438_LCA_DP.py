"""
Title : LCA 2
Link : https://www.acmicpc.net/problem/11438
"""

import sys
import collections
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 깊이
depth = [0] * (n + 1)

# 2^i 번째 부모
LOG = 21
parent = [[0] * LOG for _ in range(n + 1)]

# 각 점에서 부모 찾기 & 2^i 번째 부모 찾기
queue = collections.deque([(1, 1)])
while queue:
    p, d = queue.popleft()
    if depth[p]:
        continue
    depth[p] = d
    for q in graph[p]:
        if not depth[q]:
            parent[q][0] = p
            queue.append((q, d + 1))
# 추가적 부모 관계
for i in range(1, LOG):
    for j in range(1, n + 1):
        parent[j][i] = parent[parent[j][i - 1]][i - 1]

for _ in range(int(input())):
    a, b = map(int, input().split())
    # b 깊이가 더 깊거나 같도록
    if depth[a] > depth[b]:
        a, b = b, a
    # 높이 맞춰주기
    for i in range(LOG - 1, -1, -1):
        if depth[b] - depth[a] >= 1 << i:
            b = parent[b][i]
    if a == b:
        print(a)
        continue
    # 공통 조상 찾아가기
    for i in range(LOG - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a, b = parent[a][i], parent[b][i]
    print(parent[a][0])
