"""
Title : 행렬 덧셈
Link :https://www.acmicpc.net/problem/2738
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, M = MIIS()
    seq = [list(MIIS()) for _ in range(N)]
    for i in range(N):
        tmp = list(MIIS())
        for j in range(M):
            print(seq[i][j] + tmp[j], end=" ")
        print()
