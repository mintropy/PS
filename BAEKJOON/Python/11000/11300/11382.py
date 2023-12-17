"""
Title : 꼬마 정민
Link : https://www.acmicpc.net/problem/11382
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(a + b + c)
