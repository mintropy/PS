"""
Title : 부호
Link : https://www.acmicpc.net/problem/1247
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    for _ in range(3):
        tmp = sum(int(input()) for _ in range(int(input())))
        if tmp == 0:
            print(0)
        elif tmp > 0:
            print("+")
        else:
            print("-")
