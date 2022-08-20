"""
Title : 정렬 게임
Link : https://www.acmicpc.net/problem/13415
"""

from collections import deque
from sys import stdin

input = stdin.readline

II = lambda: int(input())
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N = II()
    seq = list(MIIS())
    stack = []
    for _ in range(II()):
        A, B = MIIS()
