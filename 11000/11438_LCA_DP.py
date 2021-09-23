"""
Title : LCA 2
Link : https://www.acmicpc.net/problem/11438
"""

import sys
import collections
input = sys.stdin.readline


def find_parent():
    global graph, parent, depth
    queue = collections.deque([(1, 1)])
    while queue:
        p, d = queue.popleft()
        if depth[p]:
            continue
        depth[p] = d
        # 인접한 점을 자식으로 설정
        for q in graph[p]:
            if not depth[q]:
                queue.append((q, d + 1))
                parent[q].append(p)
                # 각 점에서 2 ^ i번째 부모 설정
                i = 0
                while (d + 1) - (2 ** i) > 0:
                    if parent[q][-1] == 1:
                        break
                    try:
                        parent[q].append(parent[parent[q][i]][i])
                        i += 1
                    except:
                        break


def LCA(a, b):
    # b 깊이가 더 깊거나 같도록
    if depth[a] > depth[b]:
        a, b = b, a
    # 높이 맞춰주기
    while depth[a] < depth[b]:
        for b_ in parent[b][::-1]:
            if depth[b_] == depth[a]:
                b = b_
                break
            elif depth[b_] > depth[a]:
                b = b_
                break
    if a == b:
        return a
    # 공통 조상 찾아가기
    while a != b:
        for i in range(len(parent[a]) - 1, 0, -1):
            if parent[a][i] != parent[b][i]:
                a, b = parent[a][i], parent[b][i]
                break
        else:
            a, b = parent[a][0], parent[b][0]
    return a


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 2^i 번째 부모
parent = [[] for _ in range(n + 1)]
# 깊이
depth = [0] * (n + 1)

find_parent()

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(LCA(a, b))
