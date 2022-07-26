"""
Title : 교차점
Link : https://www.acmicpc.net/problem/10255
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


def line_check(X, Y, A, B) -> int:
    counts = 0
    C, D = (A[0], B[1]), (B[0], A[1])
    check_points = {A: False, B: False, C: False, D: False}
    for K in A, B, C, D:
        if check_vertax(X, Y, K):
            counts += 1
            check_points[K] = True
    lines = ((A, C), (C, B), (D, B), (A, D))
    for R1, R2 in lines:
        if check_points[R1] and check_points[R2]:
            return 4
        if check_points[R1] or check_points[R2]:
            continue
        tmp1 = get_ccw(X, Y, R1) * get_ccw(X, Y, R2)
        tmp2 = get_ccw(R1, R2, X) * get_ccw(R1, R2, Y)
        if not tmp1 and not tmp2:
            if X <= R2 and Y >= R1:
                if is_one_line(R1, R2, X, Y):
                    return 4
                counts += 1
        elif tmp1 <= 0 and tmp2 <= 0:
            counts += 1
    return counts


def check_vertax(X, Y, C) -> bool:
    if (Y[0] - X[0]) * (C[1] - X[1]) == (Y[1] - X[1]) * (C[0] - X[0]):
        return True
    return False


def get_ccw(A, B, C) -> int:
    ccw = (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[0]) * (C[0] - A[0])
    return 0 if not ccw else 1 if ccw > 0 else -1


def is_one_line(A, B, X, Y) -> bool:
    if (A[1] - B[1]) * (X[0] - Y[0]) == (A[0] - B[0]) * (X[1] - Y[1]):
        return True
    return False


if __name__ == "__main__":
    for _ in range(int(input())):
        xmin, ymin, xmax, ymax = MIIS()
        x1, y1, x2, y2 = MIIS()
        X, Y = (x1, y1), (x2, y2)
        if X > Y:
            X, Y = Y, X
        A, B = (xmin, ymin), (xmax, ymax)
        print(line_check(X, Y, A, B))
