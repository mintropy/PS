"""
Title : 사탕 가게
Link : https://www.acmicpc.net/problem/4781
"""

import sys
input = sys.stdin.readline
ISS = lambda: input().strip().split()


while True:
    N, M = ISS()
    if N == '0' and M == '0.00':
        break
    N = int(N)
    M = int(M.replace('.', ''))
    
    dp = [0] * (M + 1)
    for _ in range(N):
        c, p = ISS()
        c = int(c)
        p = int(p.replace('.', ''))
        for i in range(p, M + 1):
            if dp[i] < dp[i - p] + c:
                dp[i] = dp[i - p] + c
    print(dp[M])
