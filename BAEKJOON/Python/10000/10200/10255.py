"""
Title : 교차점
Link : https://www.acmicpc.net/problem/10255
"""

from re import L
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
        tmp1 = get_ccw(X, Y, R1) * get_ccw(X, Y, R2)
        tmp2 = get_ccw(R1, R2, X) * get_ccw(R1, R2, Y)
        if not tmp1 and not tmp2:
            if X <= R2 and Y >= R1:
                if is_one_line(R1, R2, X, Y):
                    return 4
                if check_points[R2] and R2 in (X, Y):
                    continue
                if check_points[R1] and R1 in (X, Y):
                    continue
                counts += 1
        elif tmp1 <= 0 and tmp2 <= 0:
            point = get_point(X, Y, R1, R2)
            if check_points[R1] and point == R1:
                continue
            if check_points[R2] and point == R2:
                continue
            counts += 1
    return counts


def check_vertax(X, Y, C) -> bool:
    if (Y[0] - X[0]) * (C[1] - X[1]) == (Y[1] - X[1]) * (C[0] - X[0]):
        if X <= C <= Y:
            return True
    return False


def get_ccw(A, B, C) -> int:
    ccw = (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])
    return 0 if not ccw else 1 if ccw > 0 else -1


def is_one_line(A, B, X, Y) -> bool:
    if (A[1] - B[1]) * (X[0] - Y[0]) == (A[0] - B[0]) * (X[1] - Y[1]):
        if X <= A < Y <= B or A <= X < B <= Y:
            return True
    return False


def get_point(A, B, C, D) -> tuple[int]:
    x1, y2 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D
    m = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if m:
        x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / m
        y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / m
        return (x, y)
    else:
        if B == C and A <= C:
            return B
        if A == B and C <= A:
            return A


if __name__ == "__main__":
    for _ in range(int(input())):
        xmin, ymin, xmax, ymax = MIIS()
        x1, y1, x2, y2 = MIIS()
        X, Y = (x1, y1), (x2, y2)
        if X > Y:
            X, Y = Y, X
        A, B = (xmin, ymin), (xmax, ymax)
        print(line_check(X, Y, A, B))
