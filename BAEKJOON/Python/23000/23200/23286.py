"""
Title : 허들 넘기
Link : https://www.acmicpc.net/problem/23286
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, M, T = MIIS()
    hurdles = [[-1] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        u, v, h = MIIS()
        hurdles[u][v] = h
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if hurdles[i][k] == -1 or hurdles[k][j] == -1:
                    continue
                max_hurdle = max(hurdles[i][k], hurdles[k][j])
                if hurdles[i][j] == -1 or hurdles[i][j] > max_hurdle:
                    hurdles[i][j] = max_hurdle
    for _ in range(T):
        s, e = MIIS()
        print(hurdles[s][e])
