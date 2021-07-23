import sys
sys.setrecursionlimit(int(1e6))
input = lambda : sys.stdin.readline()


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 깊이
depth = [0] * (n + 1)
depth[1] = 1

# 2^i 번째 부모
log = 18
parent = [[0] * log for _ in range(n + 1)]

# 부모 찾기
def dfs(node, dpt):
    global graph, depth, parent
    for next in graph[node]:
        if depth[next] == 0:
            depth[next] = dpt + 1
            parent[next][0] = node
            dfs(next, dpt + 1)

dfs(1, 1)

for i in range(log - 1):
    for j in range(1, n + 1):
        if parent[j][i] > 0:
            parent[j][i + 1] = parent[parent[j][i]][i]


# lca
def lca(a, b):
    global depth, parent
    if depth[a] < depth[b]:
        a, b = b, a
    x = depth[a] - depth[b]
    for i in range(log - 1, -1, -1):
        if x & (1 << i):
            a = parent[a][i]

    if a == b:
        return a

    for k in range(log - 1, -1, -1):
        if parent[a][k] != parent[b][k]:
            a, b = parent[a][k], parent[b][k]
    return parent[a][0]


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lca(a, b))