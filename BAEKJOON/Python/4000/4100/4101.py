"""
Title : 크냐
Link : https://www.acmicpc.net/problem/4101
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    while True:
        x, y = map(int, input().split())
        if x == y == 0:
            break
        if x > y:
            print("Yes")
        else:
            print("No")
