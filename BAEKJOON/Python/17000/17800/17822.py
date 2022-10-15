"""
Title : 원판 돌리기
Link : https://www.acmicpc.net/problem/17822
"""

from collections import deque
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))


def rotate(N, circles, x, k):
    for i in range(x, N, x):
        circles[i].rotate(k)
    return circles


def delete_nums(N, M, circles, x):
    visited = [[False] * M for _ in range(N + 1)]
    for i in range(x, N, x):
        is_deleted = False
        for j in range(M):
            pos = []
            queue = deque((i, j))
            target = circles[i][j]
            if target == -1:
                continue
            while queue:
                i, j = queue.popleft()
                if visited[i][j] or circles[i][j] != target:
                    continue
                visited[i][j] = True
                pos.append((i, j))
                for dx, dy in delta:
                    ni, nj = i + dx, j + dy
                    if not (0 < ni < N):
                        continue
                    queue.append((ni, nj))
            if len(pos) == 1:
                continue
            is_deleted = True
            for i, j in pos:
                circles[i][j] = -1
        if not is_deleted:
            adjust_nums(circles, i)
    return circles


def adjust_nums(circles, i):
    average = sum(circles[i]) // len(circles[i])
    for j, x in enumerate(circles[i]):
        if x > average:
            circles[i][j] -= 1
        elif x < average:
            circles[i][j] += 1


if __name__ == "__main__":
    N, M, T = MIIS()
    circles = [deque()] + list(deque(MIIS()) for _ in range(N))
    for _ in range(T):
        x, d, k = MIIS()
        if not d:
            k *= -1
        circles = rotate(N, circles, x, k)
        is_deleted, circles = delete_nums(N, M, circles, x)
    print(sum([sum(line) for line in circles]))
