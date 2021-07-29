"""
Title : 격자상의 경로
Link : https://www.acmicpc.net/problem/10164
"""

import sys, math
input = sys.stdin.readline

n, m, k = map(int, input().split())

if k == 0:
    print(math.factorial(n + m - 2) // (math.factorial(n - 1) * math.factorial(m - 1)))
else:
    kx, ky = k // m + 1, k % m
    result = 1
    result *= math.factorial(kx + ky - 2) // (math.factorial(kx - 1) * math.factorial(ky - 1))
    result *= math.factorial(n - kx + m - ky) // (math.factorial(n - kx) * math.factorial(m - ky))
    print(result)