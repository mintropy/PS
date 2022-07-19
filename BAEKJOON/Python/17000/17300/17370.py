"""
Title : 육삭형 우리 속의 개미
Link : https://www.acmicpc.net/problem/17370
"""

import sys
input = sys.stdin.readline


def search(count, last, now, turn):
    global N, dx, dy, ans
    x, y = now
    if my_map[x][y]:
        if count == N:
            return 1
        return 0
    if count == N:
        return 0
    tmp = 0
    my_map[x][y] = True
    for d in range(3):
        _x, _y = x + dx[turn][d], y + dy[turn][d]
        if last == (_x, _y):
            continue
        tmp += search(count + 1, now, (_x, _y), (turn + 1) % 2)
    my_map[x][y] = False
    return tmp


if __name__ == "__main__":
    N = int(input())
    my_map = [[False] * 1000 for _ in range(1000)]
    dx, dy = ((-1, -1, 1), (-1, 1, 1)), ((-1, 1, 0), (0, -1, 1))
    x, y = 0, 0
    print(search(0, (x, y), (x, y), 0))
