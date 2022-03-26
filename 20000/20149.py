"""
Title : 선분 교차 3
Link : https://www.acmicpc.net/problem/20149
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    x1, y1, x2, y2 = MIIS()
    x3, y3, x4, y4 = MIIS()
    
    if (
        (min(x3, x4) > x1 and min(x3, x4) > x2)
        or (max(x3, x4) < x1 and max(x3, x4) < x2)
        or (min(y3, y4) > y1 and min(y3, y4) > y2)
        or (max(y3, y4) < y1 and max(y3, y4) < y2)
    ):
        print(0)
    else:
        ccw1 = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
        ccw2 = (x2 - x1) * (y4 - y1) - (y2 - y1) * (x4 - x1)
        if ccw1 == 0 or ccw2 == 0:
            if (
                (x1 <= x3 <= x2 and y1 <= y3 <= y2)
                or (x1 <= x4 <= x2 and y1 <= y4 <= y2)
                or (x3 <= x1 <= x4 and y3 <= y1 <= y4)
                or (x3 <= x2 <= x4 and y3 <= y2 <= y4)
            ):
                print(1)
            elif x1 == x3 and y1 == y3:
                print(1)
                print(x1, y1)
            elif x1 == y4 and y1 == y4:
                print(1)
                print(x1, y1)
            elif x2 == x3 and y2 == y3:
                print(1)
                print(x2, y2)
            elif x2 == x4 and y2 == y4:
                print(1)
                print(x2, y2)
            else:
                print(0)
        elif ccw1 * ccw2 >= 0:
            print(0)
        else:
            print(1)
            if x1 == x2:
                y = (y3 - y4) / (x3 - x4) * (x1 - x3) + y3
                print(x1, y)
            elif x3 == x4:
                y = (y1 - y2) / (x1 - x2) * (x3 - x1) + y1
                print(x1, y)
            else:
                m1, m2 = (y1 - y2) / (x1 - x2), (y3 - y4) / (x3 - x4)
                x = (m1 * x1 - m2 * x3 - y1 + y3) / (m1 - m2)
                y = (y3 - y4) / (x3 - x4) * (x - x3) + y3
                print(x, y)

'''
1 6 5 5
5 5 1 1
# 1
# 5 5

0 0 0 2
0 1 0 3
# 1

0 0 1 0
0 0 2 0
# 1
'''
