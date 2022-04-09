"""
Title : 방탈출
Link : https://www.acmicpc.net/problem/23743
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def find_parent(parents, x):
    while x != parents[x]:
        x = parents[x]
    return x


def union_parent(parents, x, y):
    if x > y:
        x, y = y, x
    parents[y] = x
    return parents


if __name__ == "__main__":
    N, M = MIIS()
    exits = sorted([tuple(MIIS()) for _ in range(M)], key=lambda x:x[2])
    parents = list(range(N + 1))
    dist = 0
    for a, b, c in exits:
        a, b = find_parent(parents, a), find_parent(parents, b)
        if a == b:
            continue
        dist += c
        parents = union_parent(parents, a, b)
    outs = [0] + list(MIIS())
    min_outs = {}
    for i in range(N, 0, -1):
        if not parents[i]:
            continue
        min_out = outs[i]
        while i != parents[i]:
            i = parents[i]
            if min_out > outs[i]:
                min_out = outs[i]
        min_outs[i] = min(min_outs.get(i, 1000), min_out)
    print(dist + sum(min_outs.values()))
