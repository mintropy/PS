"""
title : 택배
Link : https://www.acmicpc.net/problem/1719
"""

import heapq
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def search(dist: list, routes: list, x: int) -> list:
    heap = [(t, x, x) for x, t in routes[x]]
    heapq.heapify(heap)
    while heap:
        t, y, pos = heapq.heappop(heap)
        if x != y:
            if dist[x][y] > 0:
                continue
            dist[x][y] = pos
        for z, et in routes[y]:
            if dist[x][z] == -1:
                heap.append((t + et, z, pos))
        heapq.heapify(heap)
    return dist


def solution() -> None:
    N, M = MIIS()
    routes = [[] for _ in range(N)]
    for _ in range(M):
        x, y, t = MIIS()
        routes[x - 1].append((y - 1, t))
        routes[y - 1].append((x - 1, t))

    dist = [[-1] * N for _ in range(N)]
    for i in range(N):
        dist = search(dist, routes, i)

    for i in range(N):
        for j in range(N):
            if i == j:
                print('-', end=' ')
            else:
                print(dist[i][j] + 1, end=' ')
        print()


solution()
