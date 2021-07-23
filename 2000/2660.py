'''
Title : 회장뽑기
Link : https://www.acmicpc.net/problem/2660
'''

import sys, collections

input = sys.stdin.readline
queue = collections.deque

# 친구관계 탐색 bfs
def bfs(i: int) -> int:
    global n, friendship, friend_point
    q = queue([(i, 0)])
    visited = [False] * (n + 1)
    visited[i] = True
    max_count = 0
    while q:
        x, p = q.popleft()
        for y in friendship[x]:
            if visited[y]:
                continue
            q.append((y, p + 1))
            visited[y] = True
            if p + 1 > max_count:
                max_count = p + 1
    return max_count

# 친구 관계
n = int(input())
friendship = [[] for _ in range(n + 1)]
while True:
    a, b= map(int, input().split())
    if a == -1 and b == -1:
        break
    friendship[a].append(b)
    friendship[b].append(a)

# 각 회원 점수
friend_point = [50] * (n + 1)
for i in range(1, n + 1):
    count = bfs(i)
    friend_point[i] = count

# 최소 점수와, 후보 뽑기
min_point = min(friend_point)
cadidate = []
for i in range(1, n + 1):
    if friend_point[i] == min_point:
        cadidate.append(i)

# 출력
print(min_point, len(cadidate))
for x in cadidate:
    print(x, end = ' ')