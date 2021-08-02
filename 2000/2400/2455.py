"""
Title : 초콜릿 자르기
Link : https://www.acmicpc.net/problem/2163
"""

import sys
input = sys.stdin.readline

max_count = 0
now = 0

for _ in range(4):
    o, i = map(int, input().split())
    now -= o
    now += i
    max_count = max(now, max_count)

print(max_count)