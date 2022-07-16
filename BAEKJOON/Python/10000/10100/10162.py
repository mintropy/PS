"""
Title : 전자레인지
Link : https://www.acmicpc.net/problem/10162
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    T = int(input())
    if T % 10:
        print(-1)
    else:
        a, b, c = T // 300, (T % 300) // 60, (T % 60) // 10
        print(a, b, c)
