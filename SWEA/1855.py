'''
Title : 영준이의 진짜 BFS
'''

import collections

def bfs(n: int, tree: list) -> int:
    count = 0
    queue = collections.deque([1, 0])
    visited = [False] * n
    while queue:
        p, d = queue.popleft()
        for q in tree[p][0]:
            if visited[q]:
                continue
            

    return count

t = int(input())
for i in range(t):
    n = int(input())
    # 자식 점, 트리의 깊이
    tree = [[[], 0] for _ in range(n + 1)]
    parents = list(map(int, input().split()))
    for i in range(n - 1):
        p = parents[i]
        tree[p][0].append(i + 2)
        tree[i + 2][1] = tree[p][1] + 1
    print(bfs(n, tree))