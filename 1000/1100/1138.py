"""
Title : 한 줄로 서기
Link : https://www.acmicpc.net/problem/1138
"""

import sys
input = sys.stdin.readline


N = int(input())
heights = list(map(int, input().split()))

line = [0] * N
for i in range(N):
    count = heights[i]
    idx = 0
    while True:
        if count == 0:
            if line[idx] == 0:
                line[idx] = i + 1
                break
            else:
                idx += 1
        elif line[idx] == 0:
            count -= 1
            idx += 1
        else:
            idx += 1

print(*line)
