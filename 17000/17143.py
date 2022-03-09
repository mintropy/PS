"""
Title : 낚시왕
Link : https://www.acmicpc.net/problem/17143
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def move_shark(r, c, s, d):
    global R, C
    _s, _d = s, d
    if d == 0 or d == 1:
        _s = s % (R * 2)
    else:
        _s = s % (C * 2)
    while _s:
        if _d == 1:
            if _s > r:
                _s -= (r - 1)
                r = 1
                _d = 2
            else:
                r -= _s
                _s = 0
        elif _d == 2:
            if _s > R - r:
                _s -= R - r
                r = R
                _d = 1
            else:
                r += _s
                _s = 0
        elif _d == 3:
            if _s > C - c:
                _s -= C - c
                c = C
                _d = 4
            else:
                c += _s
                _s = 0
        else:
            if _s > c:
                _s -= (c - 1)
                c = 1
                _d = 3
            else:
                c -= _s
                _s = 0
    return r, c, d


if __name__ == '__main__':
    R, C, M = MIIS()
    sharks = {}
    for _ in range(M):
        r, c, s, d, z = MIIS()
        sharks[(r, c)] = (s, d, z)

    ans = 0
    for idx in range(1, R + 1):
        for j in range(1, C + 1):
            if (j, idx) in sharks:
                ans += sharks[(j, idx)][2]
                sharks.pop((j, idx))
                break
        next_sharks = {}
        for (r, c), (s, d, z) in sharks.items():
            r, c, _d = move_shark(r, c, s, d)
            if (r, c) in next_sharks:
                if z > next_sharks[(r, c)][2]:
                    next_sharks[(r, c)] = (s, _d, z)
            else:
                next_sharks[(r, c)] = (s, _d, z)
        sharks = next_sharks
    print(ans)
