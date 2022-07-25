# 일반적인 풀이법
# pypy로만 통과

from sys import stdin
from collections import deque

n = int(stdin.readline().strip())
node_level = [10000 for _ in range(n + 1)]
node_level[1] = 1
parent = [0 for _ in range(n + 1)]
parent[1] = 1
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 점의 레벨과 부모 확인
queue = deque([1])
while queue:
    x = queue.popleft()
    xn = node_level[x]
    for y in graph[x]:
        if parent[y] != 0:
            continue
        queue.append(y)
        parent[y] = x
        node_level[y] = xn + 1

m = int(stdin.readline().strip())
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    l1, l2 = node_level[a], node_level[b]
    p1, p2 = a, b
    while True:
        if l1 == l2 and p1 == p2:
            print(p1)
            break
        elif l1 == l2:
            p1, p2 = parent[p1], parent[p2]
            l1 -= 1
            l2 -= 1
        elif l1 > l2:
            p1 = parent[p1]
            l1 -= 1
        elif l2 > l1:
            p2 = parent[p2]
            l2 -= 1