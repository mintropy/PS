"""
Title : N과 M (6)
Link : https://www.acmicpc.net/problem/15655
"""

import itertools

n, m = map(int, input().split())

comb = itertools.combinations(sorted(list(map(int, input().split()))), m)

for c in comb:
    print(*c)