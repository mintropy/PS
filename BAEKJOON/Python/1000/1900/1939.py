"""
Title : 중량제한
Link : https://www.acmicpc.net/problem/1939
"""

from collections import deque
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, M = MIIS()
    bridges = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = MIIS()
        bridges[a].append((b, c))
        bridges[b].append((a, c))
    for i in range(1, N + 1):
        bridges[i].sort(key=lambda x: -x[1])

    st, end = MIIS()
    maximum_weights = [0] * (N + 1)
    queue = deque([(st, 1_000_000_000)])
    while queue:
        pos, weight = queue.popleft()
        if maximum_weights[pos]:
            continue
        maximum_weights[pos] = weight
        for next_pos, limit in bridges[pos]:
            next_weight = min(weight, limit)
            if maximum_weights[next_pos]:
                continue
            queue.append((next_pos, next_weight))
    print(maximum_weights[end])
