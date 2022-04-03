"""
Title : 카약과 강풍
Link : https://www.acmicpc.net/problem/2891
"""

import sys
input = sys.stdin.readline

n, s, r = map(int, input().split())
damaged = list(map(int, input().split()))
additional = list(map(int, input().split()))

now = [1] * (n + 2)
for d in damaged:
    now[d] -= 1
for a in additional:
    now[a] += 1
    if now[a] == 2:
        if not now[a - 1]:
            now[a] -= 1
            now[a - 1] += 1
        elif not now[a + 1]:
            now[a] -= 1
            now[a + 1] += 1

print(now.count(0))
