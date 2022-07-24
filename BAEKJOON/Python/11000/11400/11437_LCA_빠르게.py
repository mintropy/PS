import sys
from collections import defaultdict
from functools import cache

input = lambda : sys.stdin.readline()
sys.setrecursionlimit(int(1e6))

graph = defaultdict(list)
n = int(input().strip())

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 점의 깊이
depth = [0 for _ in range(n + 1)]
depth[1] = 1

# 각 점의 부모
parent = [0 for _ in range(n + 1)]
parent[1] = 1

def dfs(node, dpt):
    for next in graph[node]:
        if depth[next] == 0:
            depth[next] = dpt + 1
            parent[next] = node
            dfs(next, dpt + 1)

@ cache
def lca(a, b):
    global depth, parent
    if depth[a] > depth[b]:
        a, b = b, a
    # 높이 맞춰주기
    while depth[b] != depth[a]:
        b = parent[b]
    # 조상 찾기
    while a != b:
        a, b = parent[a], parent[b]

    return a
    
# dfs
dfs(1, 1)

m = int(input().strip())

for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))