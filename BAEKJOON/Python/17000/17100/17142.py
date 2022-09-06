"""
Title : 연구소 3
Link : https://www.acmicpc.net/problem/17142
"""

from collections import deque
from itertools import combinations
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())

Map = list[list[int]]
Virus = tuple[tuple[int]]


def search(N: int, lab_map: Map, virus: Virus, delta: tuple[tuple[int]]) -> tuple[int]:
    new_lab_map = new_map(lab_map, virus)
    queue: deque = deque([(x, y, 0) for x, y in virus])
    visited = [[False] * N for _ in range(N)]
    places_count = time = 0
    while queue:
        x, y, t = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        if new_lab_map[x][y] != 2:
            if time < t:
                time = t
        new_lab_map[x][y] = 3
        places_count += 1
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny]:
                continue
            if new_lab_map[nx][ny] in (1, 3):
                continue
            queue.append((nx, ny, t + 1))
    return places_count, time


def new_map(lab_map: Map, virus: Virus) -> Map:
    new_lab_map: Map = [line[::] for line in lab_map]
    for x, y in virus:
        new_lab_map[x][y] = 3
    return new_lab_map


if __name__ == "__main__":
    N, M = MIIS()
    lab_map = [list(MIIS()) for _ in range(N)]
    blank_places = 0
    viruses = []
    for i, line in enumerate(lab_map):
        for j, x in enumerate(line):
            if not x:
                blank_places += 1
            elif x == 2:
                viruses.append((i, j))
    total_places = blank_places + len(viruses)
    delta: tuple[tuple[int]] = ((-1, 0), (0, 1), (1, 0), (0, -1))
    ans = 10000
    for comb in combinations(viruses, M):
        places, time = search(N, lab_map, comb, delta)
        if places < total_places:
            continue
        if ans > time:
            ans = time
    print(-1 if ans == 10000 else ans)
