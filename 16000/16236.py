# 상어는 가장 가까운 물고기를 먹는다
# 그런 물고기가 여러 마리일 경우 가장 위, 왼쪽 물고기를 먹는다
# 가장 가까운 물고기를 찾고, 가장 위, 왼쪽 물고기를 찾는 방식 필요

from sys import stdin
from collections import deque

# 공간의 크기
n = int(stdin.readline().strip())

# 공간의 상태
graph = []
for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))
    
# 상어 위치
baby_shark = ()
# 마리수
fish_count = 0
# 물고기 크기별 위치
fish = [[] for _ in range(7)]
for i in range(n):
    for j in range(n):
        num = graph[i][j]
        if num == 9:
            baby_shark = (i, j)
        elif num != 0:
            fish_count += 1
            fish[num].append((i, j))


def bfs(baby_shark, i, j):
    global graph
    queue = deque([(baby_shark[0], baby_shark[1], 0)])
    visited = [[False] * n for _ in range(n)]
    visited[baby_shark[0]][baby_shark[1]] = True
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        a, b, c = queue.popleft()
        for i in range(4):
            na, nb = a + dx[i], b + dy[i]
            if na == i and nb == j:
                graph[na][nb] = 0
                return c + 1
            if na < 0 or na >= n:
                continue
            if nb < 0 or nb >= n:
                continue
            if visited[na][nb]:
                continue
            if graph[na][nb] > baby_shark_size:
                continue
            queue.append((na, nb, c + 1))
            visited[na][nb] = True
    return 0


# 움직인 거리
answer = 0
# 상어 크기
baby_shark_size = 2
# 상어가 해당 크기에서 먹은 물고기 수
fish_eaten = 0
# 먹을 수 있는 물고기
able = []
able.extend(fish[1])
while True:
    # 먹을 수 있는 물고기가 없으면 종료
    if able == []:
        print(answer)
        break
    # 가장 가까운 물고기까지 거리 찾기
    dist = 40
    # 해당 물고기 위치
    target = (21, 21)
    x, y = baby_shark
    for i, j in able:
        # 거리는 bfs로 탐색
        m = bfs(baby_shark, i, j)
        if m == 0:
            continue
        if m < dist:
            dist = m
            target = (i, j)
        # 거리가 같다면 더 위, 왼쪽인지 확인
        elif m == dist:
            if i <= target[0] and j <= target[1]:
                target = (i, j)
    baby_shark = target
    answer += dist
    fish_eaten += 1
    able.remove(target)

    # 상어 크기가 커질 때
    if fish_eaten == baby_shark_size and baby_shark_size <= 6:
        able.extend(fish[baby_shark_size])
        baby_shark_size += 1
        fish_eaten = 0