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
        if not visited[q]:
            tmp.append((q, 2))
            queue.append(q)
    check = set([p] + edges[p])
    while tmp:
        q, c = tmp.popleft()
        if c == 4:
            d_count += 1
            continue
        # 탐색을 시작한 첫번째, 두번째 점으로는 되돌아가지 않게
        for r in edges[q]:
            if r not in check and not visited[r]:
                tmp.append((r, c + 1))

g_count *= 3
if d_count == g_count:
    print('DUDUDUNGA')
elif d_count > g_count:
    print('D')
else:
    print('G')


'''
14
1 2
1 3
1 4
2 5
2 6
5 7
5 8
7 9
8 10
3 11
11 12
4 13
4 14

'''