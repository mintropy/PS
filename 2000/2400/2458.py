"""
Title : 키 순서
Link : https://www.acmicpc.net/problem/2458
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M = MIIS()

# i번이 j번보다 키가 작으면 1
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = MIIS()
    graph[a][b] = 1

# Flyod Warshall
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

answer = 0
for i in range(1, N + 1):
    count_realations = 0
    for j in range(1, N + 1):
        if graph[i][j] or graph[j][i]:
            count_realations += 1
    if count_realations == N - 1:
        answer += 1

print(answer)
