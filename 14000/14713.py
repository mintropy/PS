"""
Title : 앵무새
Link : https://www.acmicpc.net/problem/14713
"""

import sys
from typing import Deque
input = sys.stdin.readline

sys.setrecursionlimit(int(1e6))

def search(parrot_idx: list, idx: int) -> bool:
    global l, m, parrots, sentence, possible
    if idx == l:
        possible = True
        return
    
    for i in range(m):
        p_idx = parrot_idx[i]
        if p_idx >= len(parrots[i]):
            continue
        if parrots[i][p_idx] == sentence[idx]:
            parrot_idx[i] += 1
            search(parrot_idx, idx + 1)
            parrot_idx[i] -= 1


n = int(input())
parrots = [list(map(str, input().split())) for _ in range(n)]
sentence = list(map(str, input().split()))

l = len(sentence)
m = len(parrots)

parrot_idx = [False] * m

possible = False

search(parrot_idx, 0)

if possible:
    print('Possible')
else:
    print('Impossible')