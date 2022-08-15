"""
Title : 종이자르기
Link : https://www.acmicpc.net/problem/2628
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    w, h = MIIS()
    n = int(input())
    cuts = [[h], [w]]
    for _ in range(n):
        cmd, pos = MIIS()
        cuts[cmd].append(pos)
    cuts[0].sort()
    cuts[1].sort()
    max_h = max_w = 0
    pos = 0
    for _h in cuts[0]:
        diff = _h - pos
        if max_h < diff:
            max_h = diff
        pos = _h
    pos = 0
    for _w in cuts[1]:
        diff = _w - pos
        if max_w < diff:
            max_w = diff
        pos = _w
    print(max_h * max_w)
