"""
Title : 거울 설치
Link : https://www.acmicpc.net/problem/2151
"""

from collections import deque
from sys import stdin

input = stdin.readline


def search(N: int, house: list[str]) -> int:
    st, end = find_enterences(house)
    if st[0] == 0:
        st += [2, 0]
        st[0] += 1
    elif st[0] == N - 1:
        st += [0, 0]
        st[0] -= 1
    elif st[1] == 0:
        st += [1, 0]
        st[1] += 1
    elif st[1] == N - 1:
        st += [3, 0]
        st[1] -= 1
    queue = deque([st])

    visited = [[[N * N] * 4 for _ in range(N)] for _ in range(N)]
    while queue:
        x, y, d, mirror = queue.popleft()
        if visited[x][y][d] <= mirror:
            continue
        visited[x][y][d] = mirror
        if house[x][y] in "*#":
            continue
        nx, ny = next_node(x, y, d)
        if 0 <= nx < N and 0 <= ny < N:
            queue.append((nx, ny, d, mirror))
        if house[x][y] in ".":
            continue
        nx, ny = next_node(x, y, (d + 1) % 4)
        if 0 <= nx < N and 0 <= ny < N:
            queue.append((nx, ny, (d + 1) % 4, mirror + 1))
        nx, ny = next_node(x, y, (d - 1) % 4)
        if 0 <= nx < N and 0 <= ny < N:
            queue.append((nx, ny, (d - 1) % 4, mirror + 1))
    return min([x for x in visited[end[0]][end[1]] if x != N * N])


def find_enterences(house: list[str]) -> list[list[int]]:
    enterences = []
    for i, line in enumerate(house):
        for j, x in enumerate(line):
            if x == "#":
                enterences.append([i, j])
    return enterences


def next_node(x: int, y: int, d: int) -> tuple[int]:
    if d == 0:
        return x - 1, y
    if d == 1:
        return x, y + 1
    if d == 2:
        return x + 1, y
    if d == 3:
        return x, y - 1


if __name__ == "__main__":
    N = int(input())
    house = [input().strip() for _ in range(N)]
    print(search(N, house))
