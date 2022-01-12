"""
Title : 달려달려
Link : https://www.acmicpc.net/problem/1757
"""

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
dist = [int(input()) for _ in range(N)]

dp = [[10 ** 8] * (M + 1) for _ in range(N)]
dp[0][1] = dist[0]
for i, n in enumerate(dist[1: ]):
    dp[i + 1][0] = dp[i][1]
    dp[i + 1][-1] = dp[i][-2]
    for j in range(1, M):
        dp[i + 1][j] = min(dp[i][j - 1], dp)


print(max(dp[N]))
