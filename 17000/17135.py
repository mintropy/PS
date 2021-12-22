"""
Title : 캐슬 디펜스
Link : https://www.acmicpc.net/problem/17135
"""

from itertools import combinations
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def simulate(x: int, y: int, z: int, grid: list) -> int:
    global N, M, D
    count = 0
    new_grid = [line[::] for line in grid]
    
    
    return count


N, M, D = MIIS()
grid = [list(MIIS()) for _ in range(N)]

max_count = 0

for x, y, z in list(combinations(range(M), 3)):
    count = simulate(x, y, z, grid)
    if max_count < count:
        max_count = count

print(max_count)
