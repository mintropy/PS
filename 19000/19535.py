"""
Title : ㄷㄷㄷㅈ
Link : https://www.acmicpc.net/problem/19535
"""

import sys, collections
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
    # 인접 간선이 3개 이상일 때 선택
    # 간선이 1, 2면 값이 0이됨
    g_count += (l * (l - 1) * (l - 2)) // 6

# ㄷ개수 구하기
# leaf에서 시작
d_count = 0
visited = [False] * (n + 1)
while queue:
    p = queue.popleft()
    if visited[p]:
        continue
    visited[p] = True
    # ㄷ확인
    # 하나 인접한 점에 이동해서 시작
    # 하나 인접한 점은 queue에도 추가
    tmp = collections.deque([])
    for q in edges[p]:
        tmp.append((p, q, 2))
        queue.append(q)
    while tmp:
        prev, q, c = tmp.popleft()
        if c == 4:
            if not visited[q]:
                d_count += 1
            continue
        # 이전 점이나 방문한 점으로는 가지 않게
        for r in edges[q]:
            if r != prev:
                tmp.append((q, r, c + 1))

g_count *= 3
if d_count == g_count:
    print('DUDUDUNGA')
elif d_count > g_count:
    print('D')
else:
    print('G')


'''
12
1 2
2 3
3 4
2 5
5 6
2 7
2 8
7 9
9 10
8 11
11 12

'''