"""
Title : 흙길 보수하기
Link : https://www.acmicpc.net/problem/1911
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())

if __name__ == "__main__":
    N, L = MIIS()
    holes = [tuple(map(int, input().split())) for _ in range(N)]
    holes.sort()
    count = 0
    pos = holes[0][0]
    for x, y in holes:
        if pos <= x:
            pos = x
        else:
            x = pos
        diff = y - x
        if diff % L:
            diff_count = diff // L + 1
        else:
            diff_count = diff // L
        count += diff_count
        pos += diff_count * L
    print(count)
