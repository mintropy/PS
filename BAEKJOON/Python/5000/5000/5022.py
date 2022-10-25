"""
Title : 연결
Link : https://www.acmicpc.net/problem/5022
"""

from collections import deque
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, M = MIIS()
    ax1, ay1 = MIIS()
    ax2, ay2 = MIIS()
    bx1, by1 = MIIS()
    bx2, by2 = MIIS()

    if (
        min(ax1, ax2) < max(bx1, bx2)
        or max(ax1, ax2) > min(bx1, bx2)
        or min(ay1, ay2) < max(by1, by2)
        or max(ay1, ay2) > min(by1, by2)
    ):
        print(abs(ax1 - ax2) + abs(ay1 - ay2) + abs(bx1 - bx2) + abs(by1 - by2))
        exit()
    ans = 0

    delta = ((-1, 0, 1, 0), (0, 1, 0, -1))
    for _ in range(2):
        base_length = abs(ax1 - ax2) + abs(ay1 + ay2)
        visited = [[10000] * N for _ in range(M)]
        queue = deque([(bx1, by1, 0)])
        while queue:
            x, y, c = queue.popleft()
            if visited[x][y] <= c:
                continue
            visited[x][y] = c

        ax1, ay1, bx1, by1 = bx1, by1, ax1, ay1
        ax2, ay2, bx2, by2 = bx2, by2, ax2, ay2
    print(ans)
