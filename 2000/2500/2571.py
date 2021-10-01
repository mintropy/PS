"""
Title : 색종이 - 3
Link : https://www.acmicpc.net/problem/2571
"""

import sys
input = sys.stdin.readline

n = int(input())
# x축으로 연속된 길이
board_x = [[0 for _ in range(101)] for _ in range(101)]
# y축으로 연속된 길이
board_y = [[0 for _ in range(101)] for _ in range(101)]

# 기본값 설정
for _ in range(n):
    x, y = map(int, input().split())
    board_x[x][y] = 1
    board_y[x][y] = 1
    board_x[x + 10][y + 10] = 1
    board_y[x + 10][y + 10] = 1
    board_x[x + 10][y] = -1
    board_y[x + 10][y] = -1
    board_x[x][y + 10] = -1
    board_y[x][y + 10] = -1

for i in range(100):
    for j in range(100):
        board_x[i][j + 1] += board_x[i][j]
        board_y[i + 1][j] += board_y[i][j]

for i in range(100):
    for j in range(100):
        board_y[i][j + 1] += board_y[i][j]
        board_x[j + 1][i] += board_x[j][i]

# 누적합 구현
prefix_sum = [[[0, 0] for _ in range(100)] for _ in range(100)]
for i in range(100):
    for j in range(100):
        if board_x[i][j] > 0:
            if j == 0 or board_x[i][j - 1] == 0:
                prefix_sum[i][j][0] = 1
            else:
                prefix_sum[i][j][0] += prefix_sum[i][j - 1][0] + 1
        if board_y[i][j] > 0:
            if i == 0 or board_y[i - 1][j] == 0:
                prefix_sum[i][j][1] = 1
            else:
                prefix_sum[i][j][1] += prefix_sum[i - 1][j][1] + 1


max_paper = 0
for i in range(100):
    for j in range(100):
        x, y = prefix_sum[i][j]
        if x == 0 or y == 0:
            continue
        # x길이 기준으로 i가 위로 올라갔을 때, 똑같은 x길이의 개수
        heights = 1
        for k in range(i - 1, -1, - 1):
            if prefix_sum[k][j][0] == 0 or prefix_sum[k][j][0] != x:
                break
            else:
                heights += 1
        if x * heights > max_paper:
            max_paper = x * heights

print(max_paper)
