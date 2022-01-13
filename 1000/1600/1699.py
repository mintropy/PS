"""
Title : 제곱수의 합
Link : https://www.acmicpc.net/problem/1699
"""

import sys
input = sys.stdin.readline


N = int(input())
dp = [N] * (N + 1)
for i in range(1, int(N ** 0.5) + 1):
    dp[i * i] = 1

squares = []
for i in range(1, N + 1):
    if dp[i] == 1:
        squares.append(i)
        continue
    dp[i] = min([dp[squares[j]] + dp[i - squares[j]] for j in range(len(squares))])

print(dp[N])
