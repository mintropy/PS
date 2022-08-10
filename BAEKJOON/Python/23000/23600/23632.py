"""
Title : 쿠키런 킹덤
Link : https://www.acmicpc.net/problem/23632
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, M, T = MIIS()
    buildings_num = list(MIIS())
    resources = [tuple(MIIS()) for _ in range(N)]
    buildings_resouces = [tuple(MIIS()) for _ in range(N - M)]

    resources_available = [False] * (N + 1)
    for x in buildings_num:
        for _, *resource in resources[x]:
            for r in resource:
                resources_available[r] = True
    resources_to_buildings = [set() for _ in range(N + 1)]
    resources_need = [0] * (N + 1)
    for x, _, *resource in buildings_resouces:
        for r in resource:
            if resources_available[r]:
                continue
            resources_to_buildings[r].add(x)
            resources_need += 1
