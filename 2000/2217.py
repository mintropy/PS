"""
Title : 로프
Link : https://www.acmicpc.net/problem/2217
"""

import sys
input = sys.stdin.readline

n = int(input())
rope = sorted([int(input()) for _ in range(n)], reverse = True)

max_weight = 0

for i in range(n):
    if rope[i] * (i + 1) > max_weight:
        max_weight = rope[i] * (i + 1)

print(max_weight)