"""
Title : 2차원 배열의 합
Link : https://www.acmicpc.net/problem/2167
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, M = MIIS()
    seq = [[0] * (M + 1)] + [[0] + list(MIIS()) for _ in range(N)]
    for i in range(1, N + 1):
        for j in range(1, M):
            seq[i][j + 1] += seq[i][j]
    for i in range(1, N):
        for j in range(1, M + 1):
            seq[i + 1][j] += seq[i][j]
    K = int(input())
    for _ in range(K):
        i, j, x, y = MIIS()
        print(seq[x][y] - seq[x][j - 1] - seq[i - 1][y] + seq[i - 1][j - 1])
