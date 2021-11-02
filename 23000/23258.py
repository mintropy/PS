"""
Title : 밤편지
Link : https://www.acmicpc.net/problem/23258
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def Floyd_Warshall(N: int, roads: list) -> tuple:
    dist = [[-1] * (N + 1) for _ in range(N + 1)]
    pass_through = [[500] * (N + 1) for _ in range(N + 1)]
    # 거쳐 가는 점
    for k in range(1, N + 1):
        # 출발 점
        for i in range(1, N + 1):
            # i >> k 로 가는 길이 없을 때
            if not roads[i][k]:
                continue
            # 도착 점
            for j in range(1, N + 1):
                # k >> j로 가는 길이 없을 때
                if not roads[k][j]:
                    continue
                # 돌아가더라도 이슬 먹는 양이 줄어들거나 같을 때
                if pass_through[i][j] >= k:
                    # i >> j 길보다 i >> k >> j 길이 더 짧을 때
                    if dist[i][j] == -1 or roads[i][k] + roads[k][j] < dist[i][j]:
                        dist[i][j] = roads[i][k] + roads[k][j]
                        pass_through[i][j] = k
    return dist, pass_through


N, Q = MIIS()
roads = [[0] * (N + 1)] + list([0] + list(MIIS()) for _ in range(N))
dist, pass_through = Floyd_Warshall(N, roads)

for _ in range(Q):
    C, s, e = MIIS()
    if dist[s][e] == -1 or pass_through[s][e] >= C:
        print(-1)
    else:
        print(dist[s][e])
