"""
Title : 비트코인은 신이고 나는 무적이다
Link : https://www.acmicpc.net/problem/23257
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


n, m = MIIS()
montly_bong = list(MIIS())
for i in range(n):
    montly_bong[i] = abs(montly_bong[i])

dp = montly_bong[::]
# 2개에서 n개 선택
for _ in range(2, m + 1):
    for i in range(n):
        price_now = dp[i]
        price_next = 0
        for j in range(i + 1):
            if price_next < price_now ^ montly_bong[j]:
                price_next = price_now ^ montly_bong[j]
        dp[i] = price_next

print(max(dp))
