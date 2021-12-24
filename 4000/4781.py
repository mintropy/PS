"""
Title : 사탕 가게
Link : https://www.acmicpc.net/problem/4781
"""

import sys
input = sys.stdin.readline
ISS = lambda: input().strip().split()


def float_to_int(float_str: str) -> int:
    return int(float_str[0]) * 100 + int(float_str[2]) * 10 + int(float_str[3])


while True:
    N, M = ISS()
    if N == '0' and M == '0.00':
        break
    N = int(N)
    M = float_to_int(M)
    
    dp = [0] * (M + 1)
    for _ in range(N):
        c, p = ISS()
        c = int(c)
        p = float_to_int(p)
        for i in range(p, M + 1):
            if dp[i] < dp[i - p] + c:
                dp[i] = dp[i - p] + c
    print(dp[M])
