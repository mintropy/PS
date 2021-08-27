"""
Title : 알약
Link : https://www.acmicpc.net/problem/4811
"""

import sys
input = sys.stdin.readline

dp = [[0] * (31) for _ in range(31)]
dp[1][1] = 1
for i in range(2, 31):
    # W i개에 H 1개 추가하는 경우의 수
    dp[i][1] = i
    # W i개에 H j개 추가하는 경우의 수
    for j in range(2, i):
        # j - 1개 >> j개
        # i - (j - 1)번 탐색
        # 처음 마지막은 그대로, 중간은 + 1
        dp[i][j] += dp[i - (j - 1)][j - 1] + 1
        for k in range(1, i - (j - 1)):
            dp[i][j] += dp[k][j - 1] + 1
    dp[i][i] = dp[i][i - 1]


for _ in range(int(input())):
    n = int(input())
    print(dp[n][n])
    pass