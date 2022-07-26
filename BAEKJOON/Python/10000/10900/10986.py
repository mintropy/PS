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
    mod_counts = [0] * M
    mod_counts[0] += 1
    for i in range(N):
        seq[i + 1] += seq[i]
        seq[i + 1] %= M
        mod_counts[seq[i + 1]] += 1
    ans = sum([comb(x, 2) for x in mod_counts])
    print(ans)
