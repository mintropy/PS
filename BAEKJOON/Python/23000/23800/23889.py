"""
Title : 돌 굴러가유
Link : 
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M, K = MIIS()
sand_castles = list(MIIS())
stones = list(MIIS())

prefix_sum = [0] * K
for i in range(1, K):
    prefix_sum[i - 1] = sum(sand_castles[stones[i-1]-1:stones[i]-1])
else:
    prefix_sum[-1] = sum(sand_castles[stones[-1]-1:])

ans = [(idx, value) for idx, value in enumerate(prefix_sum)]
ans.sort(key=lambda x:(-x[1], x[0]))

walls = [stones[ans[i][0]] for i in range(M)]
walls.sort()
print(*walls, sep='\n')
