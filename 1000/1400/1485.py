"""
Title : 정사각형
Link : https://www.acmicpc.net/problem/1485
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def check_square(x1, y1, x2, y2, x3, y3):
    # x1, y1 기준으로 직각인지 확인
    d1 = (x1 - x2) ** 2 + (y1 - y2) ** 2
    d2 = (x1 - x3) ** 2 + (y1 - y3) ** 2
    d3 = (x2 - x3) ** 2 + (y2 - y3) ** 2
    if d1 + d2 == d3:
        return True
    else:
        return False


for _ in range(int(input())):
    points = [tuple(MIIS()) for _ in range(4)]
    x0, y0 = points[0]
    
    dist = []
    for i in range(1, 4):
        xt, yt = points[i]
        dist.append((x0 - xt) ** 2 + (y0 - yt) ** 2)
    
    if dist[0] == dist[1]:
        x1, y1 = points[3]
        dist1 = (x1 - points[1][0]) ** 2 + (y1 - points[1][1]) ** 2
        dist2 = (x1 - points[2][0]) ** 2 + (y1 - points[2][1]) ** 2
        if dist1 == dist2 and check_square(x0, y0, *points[1], *points[2]):
            print(1)
        else:
            print(0)
    elif dist[0] == dist[2]:
        x1, y1 = points[2]
        dist1 = (x1 - points[1][0]) ** 2 + (y1 - points[1][1]) ** 2
        dist2 = (x1 - points[3][0]) ** 2 + (y1 - points[3][1]) ** 2
        if dist1 == dist2 and check_square(x0, y0, *points[1], *points[3]):
            print(1)
        else:
            print(0)
    elif dist[1] == dist[2]:
        x1, y1 = points[1]
        dist1 = (x1 - points[2][0]) ** 2 + (y1 - points[2][1]) ** 2
        dist2 = (x1 - points[3][0]) ** 2 + (y1 - points[3][1]) ** 2
        if dist1 == dist2 and check_square(x0, y0, *points[2], *points[3]):
            print(1)
        else:
            print(0)
    else:
        print(0)


'''
Counter Example
1
0 0
4 3
0 5
4 8
ans : 0

1
0 0
3 4
-4 3
-1 7
ans : 1
'''