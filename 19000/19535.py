"""
Title : ㄷㄷㄷㅈ
Link : https://www.acmicpc.net/problem/19535
"""

import sys, collections, math
input = sys.stdin.readline

n = int(input())
edges = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

# ㅈ개수
g_count = 0
# leaf저장 큐
queue = collections.deque([])
for i in range(1, n + 1):
    l = len(edges[i])
    if l == 1:
        queue.append(i)
    elif l >= 3:
        g_count += math.factorial(l) // (6 * math.factorial(l - 3))

# ㄷ개수 구하기
d_count = 0
visited = [False] * (n + 1)
while queue:
    p = queue.popleft()
    visited[p] = True
    # ㄷ확인
    tmp = collections.deque([])
    for q in edges[p]:
        if not visited[q]:
            tmp.append((q, 2))
            queue.append(q)
    check = set([p] + edges[p])
    while tmp:
        q, c = tmp.popleft()
        if c == 5:
            break
        if c == 4:
            d_count += 1
        for r in edges[q]:
            if r not in check and not visited[r]:
                tmp.append((r, c + 1))

if d_count == g_count * 3:
    print('DUDUDUNGA')
elif d_count > g_count * 3:
    print('D')
elif d_count * 3 < g_count:
    print('G')
