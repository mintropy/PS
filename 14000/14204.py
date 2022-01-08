"""
Title : 표 정렬
Link : https://www.acmicpc.net/problem/14204
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def check(grid, horizontal_order, vertical_order) -> int:
    global N, M
    for i in range(1, N):
        for j in range(1, M):
            if grid[i][horizontal_order[j][0]] < grid[i][horizontal_order[j - 1][0]]:
                return 0
    for j in range(1, M):
        for i in range(1, N):
            if grid[vertical_order[i][0]][j] < grid[vertical_order[i - 1][0]][j]:
                return 0
    return 1


N, M = MIIS()
grid = [list(MIIS()) for _ in range(N)]

horizontal_order = [(i, grid[0][i]) for i in range(M)]
vertical_order = [(j, grid[j][0]) for j in range(N)]
horizontal_order.sort(key=lambda x:x[1])
vertical_order.sort(key=lambda x:x[1])

print(check(grid, horizontal_order, vertical_order))


'''
2 3
2 6 4
1 5 3
'''