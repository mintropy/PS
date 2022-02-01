"""
Title : Gaaaaaaaaaarden
Link : https://www.acmicpc.net/problem/18809
"""

from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def make_search_garden(garden, blues, reds) -> list[list]:
    global N, M
    search_garden = [garden_line[::] for garden_line in garden]
    for x, y in blues:
        search_garden[x][y] = 3
    for x, y in reds:
        search_garden[x][y] = 4
    return search_garden


def search(search_garden: list, blues, reds) -> int:
    global N, M
    global dx, dy
    flowers = set()
    queue = deque([])
    for x, y in blues:
        queue.append((x, y, 3))
    for x, y in reds:
        queue.append((x, y, 4))
    while True:
        next_queue = deque([])
        while queue:
            x, y, c = queue.popleft()
            if search_garden[x][y] == 5:
                continue
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < M:
                    if search_garden[nx][ny] == 1 or search_garden[nx][ny] == 2:
                        next_queue.append((nx, ny, c))
        if not next_queue:
            break
        for x, y, c in next_queue:
            if search_garden[x][y] == c:
                continue
            elif search_garden[x][y] == 1 or search_garden[x][y] == 2:
                search_garden[x][y] = c
                queue.append((x, y, c))
            else:
                search_garden[x][y] = 5
                flowers.add((x, y))
    return len(list(flowers))


N, M, G, R = MIIS()
garden = [list(MIIS()) for _ in range(N)]
possible = set()
for i in range(N):
    for j in range(M):
        if garden[i][j] == 2:
            possible.add((i, j))

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
max_flower = 0
for blues in list(combinations(possible, G)):
    possible_red = possible - set(blues)
    for reds in list(combinations(possible_red, R)):
        search_garden = make_search_garden(garden, blues, reds)
        flower = search(search_garden, blues, reds)
        if max_flower < flower:
            max_flower = flower

print(max_flower)
