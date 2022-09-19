"""
Title : 벽 부수고 이동하기 3
Link : https://www.acmicpc.net/problem/16933
"""

from collections import deque
from sys import stdin

input = stdin.readline


def search():
    queue = deque([(0, 0, True, 0, 1)])
    while queue:
        x, y, day, wall, move = queue.popleft()
        if wall > K:
            continue
        if -1 != visited[wall][x][y][day] <= move:
            continue
        visited[wall][x][y][day] = move
        if x == N and y == M:
            continue
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if my_map[nx][ny]:
                    if day:
                        queue.append((nx, ny, not day, wall + 1, move + 1))
                    else:
                        queue.append((x, y, not day, wall, move + 1))
                else:
                    queue.append((nx, ny, not day, wall, move + 1))


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    my_map = [[int(x) for x in input().strip()] for _ in range(N)]
    visited = [[[[-1] * 2 for _ in range(M)] for _ in range(N)] for _ in range(K + 1)]
    delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
    search()
    possible_move = []
    for wall_count in visited:
        for x in wall_count[N - 1][M - 1]:
            if x != -1:
                possible_move.append(x)
    print(min(possible_move))
