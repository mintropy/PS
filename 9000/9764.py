"""
Title : 서로 다은 자연수의 합
Link : https://www.acmicpc.net/problem/9764
"""

import sys
input = sys.stdin.readline

dp = [[0] * 2001 for _ in range(2001)]
dp[1][1] = 1
dp[2][1] = dp[2][2] = 1

for i in range(3, 2001):
    dp[i][i] = 1
    for j in range(i - 1, 0, - 1):
        if (j * (j + 1)) // 2 < i:
            dp[i][j] = dp[i][j + 1]
        elif j > i - j:
            dp[i][j] = (dp[i][j + 1] + dp[i - j][1]) % 100999
        else:
            dp[i][j] = (dp[i][j + 1] + (dp[j][1] - dp[j][j])) % 100999

for _ in range(int(input())):
    print(dp[int(input())][1])
