"""
Title : 화학 실험
Link : https://www.acmicpc.net/problem/20311
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, K = MIIS()
colors = sorted(MIIS(), reverse=True)


if colors[0] > (N + 1) // 2:
    print(-1)
else:
    seq = [0] * N
    colors_list = []
    for i in range(K):
        colors_list += [i + 1] * colors[i]
    colors_list.reverse()
    
    for i in range(0, N, 2):
        seq[i] = colors_list.pop()
    for i in range(1, N, 2):
        seq[i] = colors_list.pop()
    
    print(*seq)
