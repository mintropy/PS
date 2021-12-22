"""
Title : 타일링
Link : https://www.acmicpc.net/problem/1793
"""

import sys
input = sys.stdin.readline


dp = [0] * (251)
dp[0] = 1
dp[1] = 1
for i in range(2, 251):
    dp[i] = dp[i - 1] + dp[i - 2] * 2


while True:
    try:
        print(dp[int(input())])
    except:
        break
