import sys
from collections import defaultdict

input = lambda : sys.stdin.readline()
sys.setrecursionlimit(int(1e6))

# 임의의 값으로 지정
log = 20

n = int(input().strip())
# 부모 확인하는 dp 배열
parent = [[0] * log for _ in range(n + 1)]
depth = [0 for _ in range(n + 1)]
depth[1] = 1

graph = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node, dpt):
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


for _ in range(int(input().strip())):
    a, b = map(int, input().split())
    if depth[a] < depth[b]:
        a, b = b, a
    x = depth[a] - depth[b]
    idx = 0
    while x != 0:
        if x % 2:
            a = parent[a][idx]
        x //= 2
        idx += 1

    if a != b:
        for k in range(log)[::-1]:
            if parent[a][k] != parent[b][k]:
                a, b = parent[a][k], parent[b][k]
        a = parent[a][0]
    print(a)