"""
Title : 실 전화기
Link : https://www.acmicpc.net/problem/23039
"""

import sys
input = sys.stdin.readline


def is_planar_graph(graph: list) -> bool:
    if 5 in graph[2] and (3 in graph[1] or 5 in graph[1]):
        return False
    if 4 in graph[2] and (1 in graph[3] or 5 in graph[3]):
        return False
    if 3 in graph[2] and (1 in graph[4] or 2 in graph[4]):
        return False
    return True


N = int(input())
graph = [[] for _ in range(6)]
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


if N == 10:
    print(-1)
# 이미 평면 그래프일 때
elif N == 1 or is_planar_graph(graph):
    print(0)
# 한마리 옮겨서 가능


# 두마리 올겨서 가능


