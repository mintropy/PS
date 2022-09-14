"""
Title : 버스 노선
Link : https://www.acmicpc.net/problem/10165
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())


if __name__ == "__main__":
    N, M = II(), II()
    buses = []
    for _ in range(M):
        a, b = map(int, input().split())
        if a > b:
            b = N + b
        buses.append((a, b))
    buses.sort()
