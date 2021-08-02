"""
Title : 이친수
Link : https://www.acmicpc.net/problem/2193
"""

import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * (90 + 1)
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
for i in range(4, 90 + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])