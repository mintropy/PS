"""
Title : 분산처리
Link : https://www.acmicpc.net/problem/1009
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    mods = {
        0: (10,),
        1: (1,),
        2: (2, 4, 8, 6),
        3: (3, 9, 7, 1),
        4: (4, 6),
        5: (5,),
        6: (6,),
        7: (7, 9, 3, 1),
        8: (8, 4, 2, 6),
        9: (9, 1),
    }
    for _ in range(int(input())):
        a, b = map(int, input().split())
        print(mods[a % 10][(b - 1) % len(mods[a % 10])])
