"""
Title : 달이 차오른다, 가자.
Link : https://www.acmicpc.net/problem/1194
"""

from collections import deque
from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    maze = [input().strip() for _ in range(N)]
    st = []
    doors = {chr(65 + i): [False, []] for i in range(6)}
    for i, line in enumerate(maze):
        for j, x in enumerate(line):
            if x == "0":
                st = [i, j]
            elif 65 <= ord(x) <= 70:
                doors[x][1].append((i, j))
    ans = -1
    queue = deque([(*st, 0)])
    dist = [[0] * M for _ in range(N)]
    delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
    while queue:
        x, y, c = queue.popleft()
        if maze[x][y] == "1":
            ans = c
            break
        if dist[x][y] <= c:
            continue
        dist[x][y] = c
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if x < 0 or x >= N or y < 0 or y >= M:
                continue
            s = maze[nx][ny]
            if s == "1":
                queue.append((nx, ny, c + 1))
            elif s == "#":
                continue
            elif 97 <= ord(s) <= 102:
                s = s.upper()
                doors[s][0] = True
                queue.append((nx, ny, c + 1))
            elif 65 <= ord(x) <= 70:
                if doors[x][0]:
                    pass
                else:
                    pass
