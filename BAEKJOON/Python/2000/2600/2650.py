"""
Title : 교차점개수
Link : https://www.acmicpc.net/problem/2650
"""

from sys import stdin

input = stdin.readline


def transform_coordinate(x, y) -> tuple:
    if x == 1:
        return y, 51
    elif x == 2:
        return y, 0
    elif x == 3:
        return 0, 50 - y
    elif x == 4:
        return 51, 50 - y


def get_ccw(x1, y1, x2, y2, a, b) -> bool:
    ccw = (x2 - x1) * (b - y1) - (y2 - y1) * (a - x1)
    if not ccw:
        return 0
    if ccw > 0:
        return 1
    return -1


if __name__ == "__main__":
    N = int(input())
    points = []
    for _ in range(N // 2):
        x1, y1, x2, y2 = map(int, input().split())
        (x1, y1), (x2, y2) = transform_coordinate(x1, y1), transform_coordinate(x2, y2)
        if (x1, y1) > (x2, y2):
            x1, y1, x2, y2 = x2, y2, x1, y1
        points.append((x1, y1, x2, y2))
    check = [0] * (N // 2)
    for i, (x1, y1, x2, y2) in enumerate(points):
        for j, (x3, y3, x4, y4) in enumerate(points):
            if i >= j:
                continue
            ccw1 = get_ccw(x1, y1, x2, y2, x3, y3)
            ccw2 = get_ccw(x1, y1, x2, y2, x4, y4)
            if not ccw1 and not ccw2:
                if (x1, y1) < (x3, y3) < (x2, y2) and (x1, y1) < (x4, y4) < (x2, y2):
                    continue
                if (x3, y3) < (x1, y1) < (x4, y4) and (x3, y3) < (x2, y2) < (x4, y4):
                    continue
                check[i] += 1
                check[j] += 1
                continue
            if ccw1 * ccw2 <= 0:
                check[i] += 1
                check[j] += 1
    print(sum(check) // 2)
    print(max(check))

"""
4
1 3 1 6
1 4 1 5

4
1 3 1 6
1 4 1 7
"""
