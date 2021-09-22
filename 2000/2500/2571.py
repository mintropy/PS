"""
Title : 색종이 - 3
Link : https://www.acmicpc.net/problem/2571
"""

import sys
input = sys.stdin.readline

n = int(input())
black_paper = [tuple(map(int, input().split())) for _ in range(n)]

board_x = [[0 for _ in range(101)] for _ in range(101)]
board_y = [[0 for _ in range(101)] for _ in range(101)]

for x, y in black_paper:
    board_x[x][y] = 1
    board_y[x][y] = 1
    board_x[x + 10][y + 10] = 1
    board_y[x + 10][y + 10] = 1
    board_x[x + 10][y] = -1
    board_y[x + 10][y] = -1
    board_x[x][y + 10] = -1
    board_y[x][y + 10] = -1

prefix_sum = [[[0, 0] for _ in range(100)] for _ in range(100)]
for i in range(100):
    for j in range(100):
        board_x[i][j + 1] += board_x[i][j]
        board_y[i + 1][j] += board_y[i][j]
        if board_x[i][j] > 0:
            if j == 0 or not prefix_sum[i][j - 1][0]:
                prefix_sum[i][j][0] = 1
            else:
                prefix_sum[i][j][0] = prefix_sum[i][j - 1][0] + 1
        if board_y[i][j] > 0:
            if i == 0 or not prefix_sum[i - 1][j][1]:
                prefix_sum[i][j][1] = 1
            else:
                prefix_sum[i][j][1] = prefix_sum[i - 1][j][1] + 1

for i in range(100):
    for j in range(100):
        board_x[i + 1][j] += board_x[i][j]
        board_y[i][j + 1] += board_y[i][j]
        if board_x[i][j] > 0:
            if i == 0 or not prefix_sum[i - 1][j][0]:
                prefix_sum[i][j][0] = 1
            else:
                prefix_sum[i][j][0] = prefix_sum[i - 1][j][0] + 1
        if board_y[i][j] > 0:
            if i == 0 or not prefix_sum[i][j - 1][1]:
                prefix_sum[i][j][1] = 1
            else:
                prefix_sum[i][j][1] = prefix_sum[i][j - 1][1] + 1


max_paper = 0
for i in range(99, -1, -1):
    for j in range(99, -1, -1):
        x, y = prefix_sum[i][j]
        if x * y > max_paper:
            max_paper = x * y

print(max_paper)
