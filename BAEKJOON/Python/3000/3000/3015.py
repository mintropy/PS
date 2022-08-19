"""
Title : 오아시스 재결합
Link : https://www.acmicpc.net/problem/3015
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())


if __name__ == "__main__":
    N = II()
    stack = [II()]
    ans = 0
    for _ in range(N - 1):
        height = II()
        if stack[-1] == height:
            pass
        elif stack[-1] > height:
            pass
        elif stack[-1] < height:
            pass
