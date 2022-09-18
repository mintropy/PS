"""
Title : 미네랄
Link : https://www.acmicpc.net/problem/2933
"""

from collections import deque
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


def throw_stick(d, h) -> None:
    global C, my_map
    if d % 2:
        search_range = range(C - 1, -1, -1)
    else:
        search_range = range(C)
    for i in search_range:
        if my_map[h][i] == "x":
            my_map[h][i] = "."
            move_cluster(h, i)
            return


def move_cluster(x, y) -> None:
    global R, C, my_map, delta
    cluster_status = [True] * 4
    clusters = {x: set() for x in range(4)}
    queue = deque()
    for i, (dx, dy) in enumerate(delta):
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if my_map[nx][ny] == "x":
                queue.append((i, nx, ny))
            else:
                cluster_status[i] = False
    visited = [[False] * C for _ in range(R)]
    while queue:
        d, x, y = queue.popleft()
        if not cluster_status[d]:
            continue
        if visited[x][y]:
            continue
        visited[x][y] = True
        clusters[d].add((x, y))
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if ny < 0 or ny >= C:
                continue
            if nx == R:
                cluster_status[d] = False
            if nx < 0 or nx >= R:
                continue
            if my_map[nx][ny] == ".":
                continue
            queue.append((d, nx, ny))
    movable = set()
    for i in range(4):
        if cluster_status[i]:
            movable |= clusters[i]
    min_depth = 200
    for x, y in movable:
        my_map[x][y] = "."
        if my_map[x + 1][y] == "x":
            continue
        depth = 0
        while True:
            _x = x + 1
            if _x == R or my_map[_x][y] == "x":
                break
            depth += 1
            x = _x
        if (x + 1, y) in movable:
            continue
        if min_depth > depth:
            min_depth = depth
    for x, y in movable:
        my_map[x + min_depth][y] = "x"


if __name__ == "__main__":
    R, C = MIIS()
    my_map = [list(x for x in input().strip()) for _ in range(R)]
    N = int(input())
    heights = list(MIIS())
    delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
    for i, h in enumerate(heights):
        throw_stick(i, R - h)
    for line in my_map:
        print(*line, sep="")

"""
12 24
........................
........................
..........xxxxxxxxxxx...
..........x.........x...
..........x.........x...
..........x.........x...
..........x.........x...
..........xxxxxxxxxxx...
..............x.........
..............x.........
..............x.........
..............x.........
1
10
"""