"""
Title : 전구를 켜라
Link : https://www.acmicpc.net/problem/2423
"""

from collections import deque
from re import I
from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    lines = [list(x for x in input().strip()) for _ in range(N)]
    if (N + M) % 2:
        print("NO SOLUTION")
    else:
        count_map = [[[N * M] * 2 for _ in range(M)] for _ in range(N)]
        queue = deque([(0, 0, 0, 0, 0, 1 if lines[0][0] == "\\" else 0)])
        while queue:
            lx, ly, x, y, count, changed = queue.popleft()
            if count_map[x][y][changed] < count:
                continue
            count_map[x][y][changed] = count
            now = lines[x][y]
            if changed:
                if now == "\\":
                    now = "/"
                else:
                    now = "\\"
            if now == "\\":
                pass
                if x < N - 1:
                    if lines[x + 1][y] == "\\":
                        queue.append((x, y, x + 1, y, count + 1, 1))
                    else:
                        queue.append((x, y, x + 1, y, count, 0))
                if y < M - 1:
                    if lines[x + 1][y] == "\\":
                        queue.append((x, y, x, y + 1, count + 1, 1))
                    else:
                        queue.append((x, y, x, y + 1, count, 0))
                if x < N - 1 and y < M - 1:
                    if lines[x + 1][y + 1] == "\\":
                        queue.append((x, y, x + 1, y + 1, count, 0))
                    else:
                        queue.append((x, y, x + 1, y + 1, count + 1, 1))
            else:
                if lx == x - 1:
                    if x >= N - 1:
                        continue
                    if lines[x + 1][y] == "\\":
                        queue.append((x, y, x + 1, y, count, 0))
                    else:
                        queue.append((x, y, x + 1, y, count + 1, 1))
                elif ly == y - 1:
                    if y >= N - 1:
                        continue
                    if lines[x][y + 1] == "\\":
                        queue.append((x, y, x, y + 1, count, 0))
                    else:
                        queue.append((x, y, x, y + 1, count + 1, 1))
        print(count_map[N - 1][M - 1])
