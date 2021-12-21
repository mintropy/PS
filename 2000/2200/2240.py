"""
Title : 자두나무
Link : https://www.acmicpc.net/problem/2240
"""

import sys
input = sys.stdin.readline


T, W = map(int, input().split())

dp = [[0] * (W + 1) for _ in range(T + 1)]

for i in range(1, T + 1):
    n = int(input())
    for j in range(W + 1):
        if n == 1:
            if j == 0:
                dp[i][j] = dp[i - 1][j] + 1
            elif j > 0 and j % 2 == 0:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
            else:
                dp[i][j] = dp[i - 1][j]
        else:
            if j % 2 == 1:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
            else:
                dp[i][j] = dp[i - 1][j]

print(max(dp[T]))
