"""
Title : 자원 캐기
Link : https://www.acmicpc.net/problem/14430
"""

import sys
n, m = map(int, input().split())
mine = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            if mine[0][0] == 1:
                dp[0][0] = 1
        elif i == 0:
            dp[0][j] = dp[0][j - 1] + mine[0][j]
        elif j == 0:
            dp[i][0] = dp[i - 1][0] + mine[i][0]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + mine[i][j]

print(dp[-1][-1])