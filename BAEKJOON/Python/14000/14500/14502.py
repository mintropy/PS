"""
Title : 연구소 1
Link : https://www.acmicpc.net/problem/14502
"""

from collections import deque
from itertools import combinations
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())

Map = list[list[int]]
Place = tuple[tuple[int]]


def search(
    N: int,
    M: int,
    lab_map: Map,
    places: Place,
    viruses: Place,
    delta: tuple[tuple[int]],
) -> int:
    new_lab_map = new_map(lab_map, places)
    queue: deque = deque(viruses)
    visited = [[False] * M for _ in range(N)]
    places_count = 0
    while queue:
        x, y = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        new_lab_map[x][y] = 1
        places_count += 1
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            if new_lab_map[nx][ny] == 1:
                continue
            queue.append((nx, ny))
    return places_count


def new_map(lab_map: Map, places: Place) -> Map:
    new_lab_map: Map = [line[::] for line in lab_map]
    for x, y in places:
        new_lab_map[x][y] = 1
    return new_lab_map


if __name__ == "__main__":
    N, M = MIIS()
    lab_map = [list(MIIS()) for _ in range(N)]
    blank_places = []
    viruses = []
    for i, line in enumerate(lab_map):
        for j, x in enumerate(line):
            if not x:
                blank_places.append((i, j))
            elif x == 2:
                viruses.append((i, j))
    total_places = len(blank_places)
    viruses_count = len(viruses)
    delta: tuple[tuple[int]] = ((-1, 0), (0, 1), (1, 0), (0, -1))
    ans = 0
    for comb in combinations(blank_places, 3):
        places = search(N, M, lab_map, comb, viruses, delta)
        if ans < (safe_plaecs := total_places - places - 3 + viruses_count):
            ans = safe_plaecs
    print(ans)
