"""
Title : 치즈
Link : https://www.acmicpc.net/problem/2638
"""

import sys
import collections
input = sys.stdin.readline


def bfs(grid: list, cheese: list) -> tuple:
    global dx, dy
    next_cheese = []
    melt_cheese = []
    # 각 치즈가 공기와 2공간 이상 접촉하면 녹음
    # 아니라면 next_cheese에 저장
    for x, y in cheese:
        is_melt = 0
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if grid[nx][ny] == 2:
                is_melt  += 1
        if is_melt < 2:
            next_cheese.append((x, y))
        else:
            melt_cheese.append((x, y))
    return next_cheese, melt_cheese


def find_inner_area(grid: list, inner_area: list, first=False) -> list:
    global dx, dy, n, m
    # first=True이면 처음 내부 공간 탐색하여 반환
    # False이면 기존 내부공간 활용하여 탐색
    area = []
    if first:
        # 외부 한 공간에서 외부 공간 전체 탐색
        # 외부 공기는 2로 바꾸기
        queue = collections.deque([(0, 0)])
        while queue:
            x, y = queue.popleft()
            if grid[x][y] == 2:
                continue
            grid[x][y] = 2
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if not grid[nx][ny]:
                    queue.append((nx, ny))
        # 내부 공간 탐색
        for i in range(n):
            for j in range(m):
                if not grid[i][j]:
                    area.append((i, j))
    else:
        # 내부 각 공간에서 외부 공기 공간으로 이어지는지 탐색
        # 만약 이어진다면, 주변 내부 공기 모두 바꾸기
        # 모든 공간에서부터 탐색할 필요 없음
        # 모든 내부 공간에서 이웃한 외부 공기 있으면 모두 변경
        for x, y in inner_area:
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if grid[nx][ny] == 2:
                    grid[x][y] = 2
                    queue = collections.deque([(x, y)])
                    while queue:
                        a, b = queue.popleft()
                        for d in range(4):
                            na, nb = a + dx[d], b + dy[d]
                            if not grid[na][nb]:
                                grid[na][nb] = 2
                                queue.append((na, nb))
                    break
        # 다시 한 번 더 탐색하며 내부공기만 담아서 리턴
        for x, y in inner_area:
            if not grid[x][y]:
                area.append((x, y))
    return area


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

cheese = []
for i in range(n):
    for j in range(m):
        if grid[i][j]:
            cheese.append((i, j))

inner_area = find_inner_area(grid, [], True)
# 소모된 시간
time = 0
# 치즈가 없을때 까지
while cheese:
    # 지금 치즈에서 녹을 수 있는 치즈 탐색
    next_cheese, melt_cheese = bfs(grid, cheese)
    # 녹은 치즈 반영
    for x, y in melt_cheese:
        grid[x][y] = 2
    # 다음 치즈 반영
    cheese = next_cheese
    # 내부 치즈 갱신
    inner_area = find_inner_area(grid, inner_area)
    # 시간 증가
    time += 1

print(time)

'''
7 7
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 1 0 1 0 1 0
0 1 1 1 0 1 0
0 0 1 0 0 1 0
0 0 1 1 1 1 0
0 0 0 0 0 0 0

'''