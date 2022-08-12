"""
Title : 팰린드롬?
Link : https://www.acmicpc.net/problem/10942
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N = II()
    seq = [0] + list(MIIS())
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N):
        dp[i][i] = 1
        if seq[i] == seq[i + 1]:
            dp[i][i + 1] = 1
    else:
        dp[N][N] = 1

    for i in range(2, N):
        for j in range(1, N - i + 1):
            if dp[j + 1][i + j - 1] and seq[j] == seq[i + j]:
                dp[j][i + j] = 1

    for _ in range(II()):
        S, E = MIIS()
        print(dp[S][E])
