"""
Title : 색칠 1
Link : https://www.acmicpc.net/problem/1117
"""

from sys import stdin

input = stdin.readline


def search(W, H, f, c, x1, y1, x2, y2):
    ans = (x2 - x1) * (y2 - y1) * (c + 1)


if __name__ == "__main__":
    W, H, f, c, x1, y1, x2, y2 = map(int, input().split())
