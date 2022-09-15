"""
Title : 온풍기 안녕!
Link : https://www.acmicpc.net/problem/23289
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    R, C, K = MIIS()
    room = [list(MIIS()) for _ in range(R)]
    W = int(input())
    walls = [tuple(MIIS()) for _ in range(W)]
