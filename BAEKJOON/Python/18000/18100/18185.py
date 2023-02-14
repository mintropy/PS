"""
Title : 라면 사기 (Small)
Link : https://www.acmicpc.net/problem/18185
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    seq = [0] * 2 + list(map(int, input().split()))

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
    print(sum(dp[0]) * 3 + sum(dp[1]) * 5 + sum(dp[2]) * 7)
