"""
Title : 도로포장
Link : https://www.acmicpc.net/problem/1162
"""

# 29~30줄 확인 중요!!

import sys, heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())
# 도로 생성
roads = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    roads[a].append((b, c))
    roads[b].append((a, c))

INF = 10 ** 10
# i번 도시에 j개 도로를 포장했을 때
costs = [[INF] * (k + 1) for _ in range(n + 1)]
# 1번 도시의 비용은 항상 0
costs[1] = [0] * (k + 1)

# 비용, 포장한 도로 수, 도시
heap = [(0, 0, 1)]
while heap:
    cost, pavement, city = heapq.heappop(heap)
    if costs[city][pavement] < cost:
        continue
    for next_city, next_cost in roads[city]:
        # 포장한 도로 수가 k이하이면, 포장할 때, 안할 때 구분하여 이동
        # 나머지는 포장 하지 않은 경우 모두 확인
        # 포장 할 때
        if pavement < k and cost < costs[next_city][pavement + 1]:
            costs[next_city][pavement + 1] = cost
            heapq.heappush(heap, (cost, pavement + 1, next_city))
        # 포장하지 않을 때
        if cost + next_cost < costs[next_city][pavement]:
            costs[next_city][pavement] = cost + next_cost
            heapq.heappush(heap, (cost + next_cost, pavement, next_city))

print(min(costs[n]))
