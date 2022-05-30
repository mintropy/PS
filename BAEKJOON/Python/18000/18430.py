"""
Title : 무기 공학
Link : https://www.acmicpc.net/problem/18430
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


def search():
    global N, M, my_map, visited
    max_points = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue
            for d in range(4):
                if not check_direction(i, j, d):
                    continue
                _point = get_points(i, j, d, True)
                _next_point = search()
                if max_points < _point + _next_point:
                    max_points = _point + _next_point
                get_points(i, j, d, False)
    return max_points


def check_direction(x: int, y: int, d: int) -> bool:
    global N, M, visited, direction
    for dx, dy in direction[d]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny]:
                return False
        else:
            return False
    return True


def get_points(x: int, y: int, d: int, mode: bool) -> bool:
    global N, M, my_map, visited, direction
    point = my_map[x][y] * 2
    visited[x][y] = mode
    for dx, dy in direction[d]:
        nx, ny = x + dx, y + dy
        point += my_map[nx][ny]
        visited[nx][ny] = mode
    return point


if __name__ == "__main__":
    N, M = MIIS()
    my_map = [list(MIIS()) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    direction = {
        0: ((-1, 0), (0, 1)),
        1: ((0, 1), (1, 0)),
        2: ((1, 0), (0, -1)),
        3: ((0, -1), (-1, 0)),
    }
    print(search())
