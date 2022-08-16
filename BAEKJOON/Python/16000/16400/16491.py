"""
Title : 대피소 찾기
Link : https://www.acmicpc.net/problem/16491
"""

from itertools import permutations
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


def is_cross(x1, y1, x2, y2, x3, y3, x4, y4) -> bool:
    ccw1 = (x1, y1, x2, y2, x3, y3)
    ccw2 = (x1, y1, x2, y2, x4, y4)


def get_ccw(x1, y1, x2, y2, a, b) -> int:
    ccw = (x2 - x1) * (b - y1) - (y2 - y1) * (a - x1)
    if ccw > 0:
        return 1
    if ccw < 0:
        return -1
    return 0


if __name__ == "__main__":
    N = int(input())
    robots = [tuple(MIIS()) for _ in range(N)]
    shelters = [tuple(MIIS()) for _ in range(N)]
    for perm in permutations(range(N), N):
        for i in range(N):
            (x1, y1), (x2, y2) = robots[i], shelters[perm[i]]
            for j in range(i + 1, N):
                (x3, y3), (x4, y4) = robots[j], shelters[perm[j]]
                if is_cross(x1, y2, x2, y2, x3, y3, x4, y4):
                    break
            else:
                continue
            break
        else:
            for x in perm:
                print(x + 1)
            break
