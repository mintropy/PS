"""
Title : 나무 탈출
Link : https://www.acmicpc.net/problem/15900
"""

import collections
import sys
input = sys.stdin.readline

n = int(input())

trees = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    trees[a].append(b)
    trees[b].append(a)

# 각 점의 깊이
depth = [0] * (n + 1)
# 잎 노드의 깊이만 저장
leaf_depth = []
queue = collections.deque([(1, 0)])

while queue:
    x, d = queue.popleft()
    # 잎 노드
    if x != 1 and len(trees[x]) == 1:
        leaf_depth.append(d)
        continue
    # 아니라면 순회
    for y in trees[x]:
        if depth[y] == 0:
            depth[y] = d + 1
            queue.append((y, d + 1))

if sum(leaf_depth) % 2 == 0:
    print('No')
else:
    print('Yes')
