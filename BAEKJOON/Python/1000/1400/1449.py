"""
Title : 수리공 항승
Link : https://www.acmicpc.net/problem/1449
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, L = MIIS()
    positions = sorted(MIIS()) + [5000]

    count = 0
    pos = positions[0]
    for x in positions:
        if x - pos >= L:
            count += 1
            pos = x
    print(count)
