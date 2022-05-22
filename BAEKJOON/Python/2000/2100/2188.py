import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def dfs(cow):
    global cows, rooms, visited
    if visited[cow]:
        return False
    visited[cow] = True
    for room in cows[cow]:
        if not rooms[room] or dfs(rooms[room]):
            rooms[room] = cow
            return True
    return False


if __name__ == "__main__":
    N, M = MIIS()
    cows = [[]]
    for _ in range(N):
        _, *rooms = MIIS()
        cows.append(rooms)
    rooms = [0] * (M + 1)
    for cow in range(1, N + 1):
        visited = [False] * (N + 1)
        dfs(cow)
    print(M + 1 - rooms.count(0))

'''
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
'''

'''
50 40
2 24 21
2 39 39
4 30 31 15 18
2 21 3
4 21 40 39 30
1 20
5 20 30 4 29 25
3 39 9 33
1 32
5 27 22 36 2 11
1 9
5 35 29 14 38 1
3 28 22 1
4 18 20 29 22
3 5 11 38
3 36 30 36
5 9 17 35 10 19
3 18 31 7
3 4 36 30
4 24 12 9 14
4 28 2 2 27
3 13 16 2
3 6 37 39
4 5 26 15 16
3 25 6 36
2 9 31
4 17 6 7 17
5 27 4 13 29 30
1 1
1 12
5 3 1 38 8 5
3 14 12 12
3 17 39 12
3 30 15 26
2 21 3
3 7 6 11
2 28 13
2 25 16
3 19 16 16
1 13
5 39 24 34 29 33
2 40 10
3 6 35 40
1 37
2 24 35
4 11 22 3 29
3 19 7 16
1 14
1 38
5 31 14 28 19 6
ans 39
out 49 (38도 나온다고 함)
'''