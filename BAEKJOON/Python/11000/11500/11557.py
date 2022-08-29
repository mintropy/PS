"""
Title : Yangjogang of The Year
Link : https://www.acmicpc.net/problem/11557
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())


if __name__ == "__main__":
    for _ in range(II()):
        name, max_alcohol = "", -1
        for _ in range(II()):
            n, a = input().strip().split()
            a = int(a)
            if max_alcohol < a:
                name, max_alcohol = n, a
        print(name)
