"""
Title : 트리플렛
Link : https://www.acmicpc.net/problem/3042
"""

import itertools
import sys
input = sys.stdin.readline

n = int(input())
grid = [input().strip() for _ in range(n)]

alphabet = [[] for _ in range(26)]
for i in range(n):
    for j in range(n):
        if grid[i][j].isalpha():
            alphabet[ord(grid[i][j]) - 65] = [i, j]

count = 0
for comb in list(itertools.combinations(alphabet, 3)):
    if all(comb):
        # 직선인지 판단
        p, q, r = comb
        dx1 = p[0] - q[0]
        dy1 = p[1] - q[1]
        dx2 = p[0] - r[0]
        dy2 = p[1] - r[1]
        if dx1 * dy2 == dx2 * dy1:
            count += 1

print(count)



'''
# WA
# 각 한 줄씩 순회하며, 한 줄에 있는 알파벳 개수찾아서 계산
count_horizontal = [0] * n
count_vertical = [0] * n
count_diagonal1 = [0] * (n * 2 - 1)
count_diagonal2 = [0] * (n * 2 - 1)

for i in range(n):
    for j in range(n):
        if grid[i][j].isalpha():
            count_horizontal[i] += 1
            count_vertical[j] += 1
            # / 대각선 위치에 더하기
            count_diagonal1[i + j] += 1
            # \ 대각선 위치에 더하기
            if i == j:
                count_diagonal2[n - 1] += 1
            elif i > j:
                count_diagonal2[n - 1 + (i - j)] += 1
            else:
                count_diagonal2[n - 1 - (j - i)] += 1

count = 0
for c in count_horizontal:
    count += (c * (c - 1) * (c - 2)) // 6
for c in count_vertical:
    count += (c * (c - 1) * (c - 2)) // 6
for c in count_diagonal1:
    count += (c * (c - 1) * (c - 2)) // 6
for c in count_diagonal2:
    count += (c * (c - 1) * (c - 2)) // 6

print(count)
'''
