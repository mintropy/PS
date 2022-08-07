"""
Title : ACM Craft
Link : https://www.acmicpc.net/problem/1005
"""

from collections import deque
from sys import stdin

input = stdin.readline
II = lambda: int(input())
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    for _ in range(II()):
        N, K = MIIS()
        buildings = [0] + list(MIIS())
        before_count = [0] * (N + 1)
        next_building = [[] for _ in range(N + 1)]
        for _ in range(K):
            x, y = MIIS()
            next_building[x].append(y)
            before_count[y] += 1
        build_times = [0] * (N + 1)
        queue = deque([])
        W = II()
        for i in range(1, N + 1):
            if not before_count[i]:
                if i == W:
                    print(buildings[i])
                    break
                build_times[i] = buildings[i]
                queue.append((i, buildings[i]))
        else:
            while queue:
                x, t = queue.popleft()
                for y in next_building[x]:
                    if build_times[y] < t + buildings[y]:
                        build_times[y] = t + buildings[y]
                    before_count[y] -= 1
                    if not before_count[y]:
                        queue.append((y, build_times[y]))
                        if y == W:
                            print(build_times[W])
                            break
                else:
                    continue
                break
