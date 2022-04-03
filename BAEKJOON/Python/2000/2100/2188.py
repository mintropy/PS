import sys
from collections import deque

input = lambda : sys.stdin.readline()

# 소, 축사의 수
n, m = map(int, input().split())
# 탐색을 위해 추가한 s, t점
# s에서 시작, 모든 소와 연결
# t는 모든 축사와 연결
s, t = 0, n + m + 1
# 소의 번호는 1 ~ n, 축사의 번호는 n + 1 ~ m
adj = [[] for _ in range(n + m + 2)]
# s번 점과 t번 점을 각각 소와 축사와 인접하다고 표시
adj[0] = [i + 1 for i in range(n)]
for i in range(n + 1, n + m + 2):
    adj[i].append(t)

capacity = [[0] * (n + m + 2) for _ in range(n + m + 2)]
flow = [[0] * (n + m + 2) for _ in range(n + m + 2)]
for i in range(1, n + 1):
    capacity[0][i] = 1
for i in range(n + 1, n + m + 1):
    capacity[i][-1] = 1


for i in range(1, m + 1):
    tmp = list(map(int, input().split()))
    for j in tmp[1:]:
        adj[j].append(n + i)
        capacity[j][n + i] = 1


def make_flow(s, t, path):
    global capacity, flow
    c = 1
    cur = t
    while cur != s:
        flow[path[cur]][cur] += c
        flow[cur][path[cur]] -= c
        cur = path[cur]
    return c


def bfs(s, t):
    global capacity, flow
    path = [-1] * (n + m + 2)
    queue = deque([s])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if capacity[u][v] - flow[u][v] > 0 and path[v] < 0:
                queue.append(v)
                path[v] = u
                if v == t:
                    return make_flow(s, t, path)
    return 0


def edmods_karp(s, t):
    max_flow = 0
    while True:
        c = bfs(s, t)
        if c > 0:
            max_flow += c
        else:
            break
    return max_flow


print(edmods_karp(s, t))