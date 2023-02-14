"""
Title : 라면 사기 (Large)
Link : https://www.acmicpc.net/problem/18186
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, B, C = MIIS()
    seq = [0] * 2 + list(MIIS())

    if C >= B:
        print(sum(seq) * B)
    else:
        dp = [[0] * (N + 2) for _ in range(3)]
        for i in range(2, N + 2):
            x = seq[i]
            dp[1][i] = min(x, dp[0][i - 1])
            x -= dp[1][i]
            dp[0][i - 1] -= dp[1][i]
            dp[2][i] = min(x, dp[1][i - 1])
            x -= dp[2][i]
            dp[1][i - 1] -= dp[2][i]
            dp[0][i] = x
        print(sum(dp[0]) * B + sum(dp[1]) * (B + C) + sum(dp[2]) * (B + C * 2))
