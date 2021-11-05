"""
Title : 누텔라 트리 (Easy)
Link : https://www.acmicpc.net/problem/23040
"""

import sys
input = sys.stdin.readline


N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

edges_color = ' ' + input().strip()
visited = [False] * (N + 1)
blacks = []
reds_parent = [range(N + 1)]
