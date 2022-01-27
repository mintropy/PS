"""
Title : 화살을 쏘자!
Link : https://www.acmicpc.net/problem/20157
"""

from math import gcd
import sys
input = sys.stdin.readline


N = int(input())

bloons = {}
for _ in range(N):
    x, y = map(int, input().split())
    if x == 0:
        if 0 in bloons:
            bloons[0] += 1
        else:
            bloons[0] = 1
        continue
    g = gcd(x, y)
    x, y = x // g, y // g
    if x < 0:
        x, y = -x, -y
    if (x, y) in bloons:
        bloons[(x, y)] += 1
    else:
        bloons[(x, y)] = 1

print(max(bloons.values()))
