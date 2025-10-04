"""
Title : 수학은 비대면강의입니다
Link : https://www.acmicpc.net/problem/19532
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    a, b, c, d, e, f = map(int, input().split())
    x = (c * e - b * f) / (a * e - b * d)
    y = (a * f - c * d) / (a * e - b * d)
    print(int(x), int(y))
