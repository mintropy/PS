"""
title : 나머지 합
Link : https://www.acmicpc.net/problem/10986
"""

from math import comb
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, M = MIIS()
    seq = [0] + list(MIIS())
    mod_counts = {i: 0 for i in range(M)}
    mod_counts[0] += 1
    for i in range(N):
        seq[i + 1] += seq[i]
        seq[i + 1] %= M
        mod_counts[seq[i + 1]] += 1
    ans = 0
    for v in mod_counts.values():
        ans += comb(v, 2)
    print(ans)
