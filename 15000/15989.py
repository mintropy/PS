"""
Title : 1, 2, 3 더하기 4
Link : https://www.acmicpc.net/problem/15989
"""

dp = [[0] * 4 for _ in range(10001)]
dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, 10001):
    dp[i][1] = 1
    dp[i][2] = dp[i - 2][1] + dp[i - 2][2]
    dp[i][3] = sum(dp[i - 3])

for _ in range(int(input())):
    print(sum(dp[int(input())]))
