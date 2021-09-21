"""
Title : 환승
Link : https://www.acmicpc.net/problem/5214
"""


import sys
import collections
input = sys.stdin.readline

n, k, m = map(int, input().split())
stations = [[] for _ in range (n + 1)]
hyper_tube = []
for i in range(m):
    tube = list(map(int, input().split()))
    hyper_tube.append(tube)
    for s in tube:
        stations[s].append(i)

visited_stations = [10 ** 7] * (n + 1)
visited_stations[1] = 1
visited_tube = [False] * m
queue = collections.deque([(1, 1)])
while queue:
    st, count = queue.popleft()
    # 방문한 역의 수가더 많으면 넘어가기
    if visited_stations[st] < count:
        continue
    # 연결된 하이퍼 튜브 >> 다음 역
    # 연결된 하이퍼 튜브
    tube = stations[st]
    for t in tube:
        if visited_tube[t]: 
            continue
        visited_tube[t] = True
        # 가능한 다음 역
        for next in hyper_tube[t]:
            if visited_stations[next] > count + 1:
                visited_stations[next] = count + 1
                queue.append((next, count + 1))

if visited_stations[n] == 10 ** 7:
    print(-1)
else:
    print(visited_stations[n])
