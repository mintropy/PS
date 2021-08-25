"""
Title : 얼음깨기 팽귄
Link : https://www.acmicpc.net/problem/21738
"""

import sys
input = sys.stdin.readline


# 펭귄 위치를 루트로
n, s, p = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

parent = [0] * (n  + 1)
visited = [False] * (n + 1)

# 펭귄 위치를 루트로, 자식들만 우선 구하고 설정
# 각 자식별로 자식 번호를 키로
# 그 자식으로 따라가서, 가장 가까운 지지대 얼음까지 거리
# 자식에 있는 전체 얼음 개수를 값으로 저장
penguin_child = {i: [0, 0] for i in edges[p]}

# 펭귄의 각 자식에서 시작 탐색
# 탐색하며 가장 가까운 지지대 얼음까지 거리 저장
# 
for q in edges[p]:
    parent[q] = p
