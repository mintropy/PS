"""
Title : 미네랄
Link : https://www.acmicpc.net/problem/2933
"""

from collections import deque
from sys import stdin

input = stdin.readline


def throw_stick(d, h) -> int:
    global C, my_map
    if d % 2:
        search_range = range(C - 1, -1, -1)
    else:
        search_range = range(C)
    for i in search_range:
        if my_map[h][i] == "x":
            my_map[h][i] = "."
            return i
    return -1


def move_cluster(st) -> None:
    global R, C, my_map
    movable = set()
    cluster_status = [True] * 4
    clusters = {x: set() for x in range(4)}
    queue = deque()
    for i, (dx, dy) in enumerate(delta):
        nx, ny = st[0] + dx, st[1] + dy
        if 0 <= nx < R and 0 <= ny < C:
            queue.append((i, nx, ny))
    while queue:
        d, x, y = queue.popleft()
        


if __name__ == "__main__":
    R, C = map(int, input().split())
    my_map = [list(x for x in input().strip()) for _ in range(R)]
    N = int(input())
    heights = list(map(int, input().split()))
    delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
    for i, h in heights:
        if throw_stick(i, h) == -1:
            continue
