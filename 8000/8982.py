"""
Title : 수족관 1
Link : https://www.acmicpc.net/problem/8982
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N = int(input())
corners = [tuple(MIIS()) for _ in range(N)]
blocks = []
water = 0
for i in range(1, N - 2, 2):
    # depth, left, right, top
    blocks.append([corners[i][1], corners[i][0], corners[i + 1][0], 0])
    water += blocks[-1][0] * (blocks[-1][2] - blocks[-1][1])

K = int(input())
holes = [tuple(MIIS()) for _ in range(K)]
holes.sort(key=lambda x:x[1])


for hole in holes:
    for i in range(N // 2 - 1):
        d, l, r, t = blocks[i]
        if hole[0] == l and hole[1] == d:
            # search
            depth = d
            for j in range(i, -1, -1):
                if depth > blocks[j][0]:
                    depth = blocks[j][0]
                water -= (depth - blocks[j][3]) * (blocks[j][2] - blocks[j][1])
                blocks[j][3] = depth
            depth = d
            for j in range(i + 1, N // 2 - 1):
                if depth > blocks[j][0]:
                    depth = blocks[j][0]
                water -= (depth - blocks[j][3]) * (blocks[j][2] - blocks[j][1])
                blocks[j][3] = depth
            break

print(water)
