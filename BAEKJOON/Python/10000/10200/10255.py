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
        if (not get_ccw(X, Y, K)) and X <= K <= Y:
            counts += 1
            check_points[K] = True
    lines = ((A, C), (C, B), (D, B), (A, D))
    if counts == 2:
        for R1, R2 in lines:
            if check_points[R1] and check_points[R2]:
                return 4
        else:
            return 2
    for R1, R2 in lines:
        tmp1 = get_ccw(X, Y, R1) * get_ccw(X, Y, R2)
        tmp2 = get_ccw(R1, R2, X) * get_ccw(R1, R2, Y)
        if not tmp1 and not tmp2:
            if (R1 == X or R1 == Y) or (R2 == X or R2 == Y):
                continue
            if is_one_line(R1, R2, X, Y):
                return 4
        elif tmp1 <= 0 and tmp2 <= 0:
            if check_points[R1] or check_points[R2]:
                continue
            counts += 1
    return counts


def get_ccw(A, B, C) -> int:
    ccw = (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])
    return 0 if not ccw else 1 if ccw > 0 else -1


def is_one_line(A, B, X, Y) -> bool:
    if X <= A < Y <= B or A <= X < B <= Y or X <= A < B <= Y or A <= X < Y <= B:
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
