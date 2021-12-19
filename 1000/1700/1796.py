"""
Title : 신기한 키보드
Link : https://www.acmicpc.net/problem/1796
"""

import sys
input = sys.stdin.readline


S = input().strip()
length = len(S)

alphabets = sorted(set(S))
length_alp = len(alphabets)

left = [S.find(alp) for alp in alphabets]
right = [S.rfind(alp) for alp in alphabets]

dp = [[0] * length for _ in range(length_alp)]





'''
# MLE
from itertools import permutations, product
import sys
input = sys.stdin.readline


S = input().strip()
idx = 0

alp_idxs = {}
for idx, s in enumerate(S):
    if s in alp_idxs:
        alp_idxs[s].append(idx)
    else:
        alp_idxs[s] = [idx]

if len(alp_idxs.keys()) == 1:
    print(len(S) * 2 - 1)
else:
    combs = []
    for _, idxs in sorted(alp_idxs.items()):
        combs.append(list(permutations(idxs, len(idxs))))
    
    combs = list(product(*combs))
    
    min_count = 10 ** 9
    for comb in combs:
        count = 0
        idx = 0
        for small_comb in comb:
            count += abs(small_comb[0] - idx) + 1
            for i in range(len(small_comb) - 1):
                count += abs(small_comb[i + 1] - small_comb[i]) + 1
            idx = small_comb[-1]
        if min_count > count:
            min_count = count
    
    print(min_count)
'''
