"""
title : 택배
Link : https://www.acmicpc.net/problem/1719
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def solution() -> None:
    N, M = MIIS()
    routes = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y, t = MIIS()
        routes[x].append((y, t))
        routes[x].append((x, y))
    


solution()
