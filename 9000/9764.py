"""
Title : 서로 다은 자연수의 합
Link : https://www.acmicpc.net/problem/9764
"""

import sys
input = sys.stdin.readline

dp = [0] * 2001
dp[1] = dp[2] = 1
dp[3] = dp[4] = 2
for i in range(5, 2001):
    # i, (i - 1) + 1, (i - 2) + 2는 각각 한가지 방법
    dp[i] = 3
    for j in range(i - 3, i // 2, -1):
        dp[i] += dp[i - j]
    # i가 2의 배수인지 아닌지에 따라 달라짐
    if i % 2 == 0:
        dp[i] += dp[i // 2] - 1
    dp[i] %= 100999


for _ in range(int(input())):
    print(dp[int(input())])
