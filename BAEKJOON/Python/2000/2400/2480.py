"""
Title : 주사위 세개
Link : https://www.acmicpc.net/problem/2480
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    X, Y, Z = map(int, input().split())
    if X == Y == Z:
        print(10000 + X * 1000)
    elif X == Y:
        print(1000 + X * 100)
    elif Y == Z:
        print(1000 + Y * 100)
    elif Z == X:
        print(1000 + Z * 100)
    else:
        print(max(X, Y, Z) * 100)
