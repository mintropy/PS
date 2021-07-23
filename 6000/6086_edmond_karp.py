import sys
from collections import deque

input = lambda : sys.stdin.readline()
# 알파벳을 숫자로 대응
# 대문자 알파벳을 0 ~ 25, 소문자를 26 ~ 51
alp_to_num = lambda x: ord(x) - ord('A') if x <= 'Z' else ord(x) - ord('a') + 26


def make_flow(s, t, path):
    global capacity, flow
    c = 10 ** 9
    cur = t
    while cur != s:
        c = min(c, capacity[path[cur]][cur] - flow[path[cur]][cur])
        cur = path[cur]
    cur = t
    while cur != s:
        flow[path[cur]][cur] += c
        flow[cur][path[cur]] -= c
        cur = path[cur]
    return c


def bfs(s, t):
    global capacity, flow
    path = [-1] * 52
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


def edmonds_karp(s, t):
    max_flow = 0
    while True:
        c = bfs(s, t)
        if c > 0:
            max_flow += c
        else:
            break
    return max_flow


capacity = [[0] * 52 for _ in range(52)]
flow = [[0] * 52 for _ in range(52)]
adj = [[] for _ in range(52)]
n = int(input())
for _ in range(n):
    u, v, c = map(str, input().split())
    u, v, c = alp_to_num(u), alp_to_num(v), int(c)
    capacity[u][v] += c
    capacity[v][u] += c
    adj[u].append(v)
    adj[v].append(u)
# 시작, 종료 지점
s, t = alp_to_num('A'), alp_to_num('Z')
max_flow = edmonds_karp(s, t)
print(max_flow)