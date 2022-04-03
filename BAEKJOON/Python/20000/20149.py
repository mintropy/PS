"""
Title : 선분 교차 3
Link : https://www.acmicpc.net/problem/20149
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def ccw(a1, b1, a2, b2, a3, b3):
    return (a2 - a1) * (b3 - b1) - (b2 - b1) * (a3 - a1)


def is_between(l, r, t):
    if l <= t <= r or r <= t <= l:
        return True
    return False


def check():
    global x1, y1, x2, y2, x3, y3, x4, y4
    if not ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4):
        if not ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2):
            if (max(x1, x2) >= min(x3, x4) and max(y1, y2) >= min(y3, y4)) or (
                min(x1, x2) >= max(x3, x4) and min(y1, y2) >= max(y3, y4)
            ):
                return True
            else:
                return False
    elif ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) < 0:
        if ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0:
            return True
    return False


if __name__ == "__main__":
    x1, y1, x2, y2 = MIIS()
    x3, y3, x4, y4 = MIIS()
    if check():
        print(1)
        try:
            print(
                ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4))
                / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)),
                ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4))
                / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)),
            )
        except ZeroDivisionError:
            if x1 > x2 or y1 > y2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            if x3 > x4 or y3 > y4:
                x3, y3, x4, y4 = x4, y4, x3, y3
            if x2 == x3 and y2 == y3:
                print(x2, y2)
            else:
                print(x1, y1)
    else:
        print(0)

"""
https://velog.io/@jini_eun/%EB%B0%B1%EC%A4%80-20149-%EC%84%A0%EB%B6%84-%EA%B5%90%EC%B0%A8-3-Java-Python

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
# 0 0
"""
