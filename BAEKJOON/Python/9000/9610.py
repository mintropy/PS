"""
Title : 사분면
Link : https://www.acmicpc.net/problem/9610
"""

import sys
input = sys.stdin.readline


points = [0] * 5

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        points[0] += 1
    elif x > 0 and y > 0:
        points[1] += 1
    elif x < 0 and y > 0:
        points[2] += 1
    elif x < 0 and y < 0:
        points[3] += 1
    else:
        points[4] += 1

for i in range(1, 5):
    print(f'Q{i}: {points[i]}')
print(f'AXIS: {points[0]}')
