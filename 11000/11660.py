"""
Title : 구간 합 구하기 5
Link : https://www.acmicpc.net/problem/11660
"""

import sys
input = sys.stdin.readline


n, m = map(int ,input().split())
seq = [list(map(int, input().split())) for _ in range(n)]

# 누적합 구하기, 행별로
for i in range(n):
    for j in range(n - 1):
        if i == n - 1 and j == n - 1:
            break
        elif j == n - 1:
            seq[i + 1][j] += seq[i][j]
        else:
            seq[i][j + 1] += seq[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    