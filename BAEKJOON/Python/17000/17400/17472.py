"""
Title : 다리 만들기 2
Link : https://www.acmicpc.net/problem/17472
"""

from collections import deque
from itertools import combinations
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())

Field = tuple[tuple[int]]
Islands = list[list[int]]

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))


def find_islansds(N: int, M: int, my_map: Field) -> Islands:
    islands = []
    visited = [[False] * M for _ in range(N)]
    for i, line in enumerate(my_map):
        for j, x in enumerate(line):
            if not x:
                continue
            queue = deque([(i, j)])
            tmp = []
            while queue:
                i, j = queue.popleft()
                if not my_map[i][j] or visited[i][j]:
                    continue
                visited[i][j] = True
                tmp.append((i, j))
                for dx, dy in delta:
                    ni, nj = i + dx, j + dy
                    if ni < 0 or ni >= N or nj < 0 or nj >= M:
                        continue
                    if not my_map[ni][nj]:
                        continue
                    queue.append((ni, nj))
            if not tmp:
                continue
            islands.append(tmp)
    return get_boarder(N, M, my_map, islands)


def get_boarder(N: int, M: int, my_map: Field, islands: Islands) -> Islands:
    islands_boarder = []
    for island in islands:
        tmp = []
        for x, y in island:
            zero_count = 0
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                elif not my_map[nx][ny]:
                    zero_count += 1
            if zero_count:
                tmp.append((x, y))
        islands_boarder.append(tmp)
    return islands_boarder


def search(N: int, M: int, my_map: Field, boarders: Islands) -> int:
    ans = 1000
    connections = combinations(range(len(islands_boarders)), 2)
    for comb in combinations(connections, len(islands_boarders) - 1):
        tmp = 0
        for i, j in comb:
            l = check(N, M, my_map, boarders, (i, j))
            if l == -1:
                tmp = 1000
                break
            tmp += l
        if not is_connected(len(boarders), comb):
            continue
        ans = min(ans, tmp)
    return -1 if ans == 1000 else ans


def check(
    N: int, M: int, my_map: Field, boarders: Islands, islands_nums: tuple[int]
) -> int:
    i, j = islands_nums
    min_length = 20
    for x, y in boarders[i]:
        for dx, dy in delta:
            length = 0
            nx, ny = x, y
            while True:
                nx, ny = nx + dx, ny + dy
                length += 1
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    length = 20
                    break
                if not my_map[nx][ny]:
                    continue
                if (nx, ny) not in boarders[j]:
                    length = 21
                length -= 1
                break
            if length == 1:
                length = 20
            min_length = min(min_length, length)
    return -1 if min_length == 20 else min_length


def is_connected(N: int, edges: tuple[int]) -> bool:
    visited = [False] * N
    queue = deque([0])
    while queue:
        x = queue.popleft()
        if visited[x]:
            continue
        visited[x] = True
        for i, j in edges:
            if x == i:
                queue.append(j)
            elif x == j:
                queue.append(i)
    if all(visited):
        return True
    return False


if __name__ == "__main__":
    N, M = MIIS()
    my_map = tuple(tuple(MIIS()) for _ in range(N))
    islands_boarders = find_islansds(N, M, my_map)
    print(search(N, M, my_map, islands_boarders))

"""
8 6
0 1 0 0 1 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 1 0 0 1 0
0 0 0 0 0 0
0 0 0 0 0 0
0 1 1 1 1 0
ans : 9
out : 8
# 모든 섬이 연결되지 확인하지 않음

"""
