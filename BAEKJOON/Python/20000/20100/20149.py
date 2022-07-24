"""
Title : 선분 교차 3
Link : https://www.acmicpc.net/problem/20149
"""

import sys

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def ccw(a1, b1, a2, b2, a3, b3):
    tmp = (a2 - a1) * (b3 - b1) - (b2 - b1) * (a3 - a1)
    return 0 if not tmp else 1 if tmp > 0 else -1


def get_point(A: tuple, B: tuple, C: tuple, D: tuple):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D
    m = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if m:
        x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / m
        y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / m
        print(x, y)
    else:
        if B == C and A <= C:
            print(*B)
        elif A == D and C <= A:
            print(*A)


if __name__ == "__main__":
    x1, y1, x2, y2 = MIIS()
    x3, y3, x4, y4 = MIIS()
    ccw1 = ccw(x1, y1, x2, y2, x3, y3)
    ccw2 = ccw(x1, y1, x2, y2, x4, y4)
    ccw3 = ccw(x3, y3, x4, y4, x1, y1)
    ccw4 = ccw(x3, y3, x4, y4, x2, y2)

    tmp1, tmp2 = ccw1 * ccw2, ccw3 * ccw4
    if not tmp1 and not tmp2:
        if (x1, y1) > (x2, y2):
            x1, y1, x2, y2 = x2, y2, x1, y1
        if (x3, y3) > (x4, y4):
            x3, y3, x4, y4 = x4, y4, x3, y3
        if (x1, y1) <= (x4, y4) and (x2, y2) >= (x3, y3):
            print(1)
            get_point((x1, y1), (x2, y2), (x3, y3), (x4, y4))
        else:
            print(0)
    else:
        if tmp1 <= 0 and tmp2 <= 0:
            print(1)
            get_point((x1, y1), (x2, y2), (x3, y3), (x4, y4))
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
"""
