"""
Title : 구간 합 구하기 2
Link : https://www.acmicpc.net/problem/10999
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())
MIIS = lambda: map(int, input().split())


class SegmentTree:
    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    N, M, K = MIIS()
    seq = [II() for _ in range(N)]
    for _ in range(M + K):
        cmd, *nums = MIIS()
