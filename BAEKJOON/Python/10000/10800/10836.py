"""
Title : 여왕벌
Link : https://www.acmicpc.net/problem/10836
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


M, N = MIIS()


grid_length = M * 2
growth = [0] * (grid_length)
for _ in range(N):
    zero, one, _ = MIIS()
    growth[zero] += 1
    growth[zero + one] += 1

growth[0] += 1
for i in range(grid_length - 1):
    growth[i + 1] += growth[i]

for i in range(M):
    output_line = [growth[M - 1 - i]] + growth[M:-1]
    print(*output_line)



'''
M, N = MIIS()

hive = [[1] * M for _ in range(M)]

growth = [0] * (M + M - 1)
for _ in range(N):
    new_growth = tuple(MIIS())
    idx = g = 0
    
    for ng in new_growth:
        for _ in range(ng):
            growth[idx] += g
            idx += 1
        g += 1

growth_map = [[0] * M for _ in range(M)]
for i in range(M):
    growth_map[M - 1 - i][0] = growth[i]
for i in range(1, M):
    growth_map[0][i] = growth[M - 1 + i]

for i in range(M):
    for j in range(M):
        if i == 0 or j == 0:
            hive[i][j] += growth_map[i][j]
        else:
            max_growth = max(
                growth_map[i - 1][j], growth_map[i - 1][j - 1], growth_map[i][j - 1]
            )
            growth_map[i][j] = max_growth
            hive[i][j] += max_growth


for line in hive:
    print(*line)
'''
