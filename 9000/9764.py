"""
Title : 서로 다은 자연수의 합
Link : https://www.acmicpc.net/problem/9764
"""

import sys
input = sys.stdin.readline

dp = [[0] * 2001 for _ in range(2001)]

for i in range(1, 2001):
    dp[i][i] = 1
    
for i in range(1, 2001):
    for j in range(1, i):
        # 범위 확인
        pass
