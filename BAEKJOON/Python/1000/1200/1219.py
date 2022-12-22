"""
Title : 오민식의 고민
Link : https://www.acmicpc.net/problem/1219
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, st, end, M = MIIS()
    transfers = [[] for _ in range(N)]
    for _ in range(M):
        s, e, p = MIIS()
        transfers[s].append((e, p))
    cities = list(MIIS())
