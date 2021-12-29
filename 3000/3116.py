"""
Title : 생물학자
Link : https://www.acmicpc.net/problem/3116
"""

import sys
input = sys.stdin.readline


N = int(input())
bacterias = [tuple(map(int, input().split())) for _ in range(N)]

check = [[False] * N for _ in range(N)]
max_count = 0
for i in range(N):
    if check[i]:
        continue

