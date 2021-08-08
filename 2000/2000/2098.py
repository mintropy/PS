"""
Title : 외판원 순회
Link : https://www.acmicpc.net/problem/2098
"""

import sys, itertools
input = sys.stdin.readline


def tsp(city_visited: int, city_count: int, city_now: int):
    if city_count == 2:
        return adjacency_matrix[0][city_now]
    min_costs = []
    # 이미 탐색한 도시부터 되돌아가며 탐색
    for i in range(1, n):
        # 해당 도시이거나, 방문하지 않은도시이면 건너뛰기
        if i == city_now:
            continue
        if not (1 << i & city_visited):
            continue
        # i번 도시에서 city_now까지 비용
        c = adjacency_matrix[i][city_now]
        if c == 0:
            continue
        # i번 도시를 방문하지 영우
        city_not_i = (1 << n + 1) - 1
        city_not_i = city_not_i & ~(1 << i)
        cost_not_i = tsp(city_not_i, city_count - 1, i)
        min_costs.append(cost_not_i + c)
    if min_costs:
        return min(min_costs)
    else:
        return 0


n = int(input())
adjacency_matrix = [list(map(int, input().split())) for _ in range(n)]
# 마지막 도시 >> 처음도시(0)으로 돌아가는건 따로 계산
min_cost = 10 ** 8
for c in range(2, n):
    cost = tsp((1 << n + 1) - 1, n, c)
    if cost == 0:
        continue
    cost += adjacency_matrix[c][0]
    if cost < min_cost:
        min_cost = cost

print(min_cost)



'''
# 전체 탐색 : 시간 초과
def TSP(dp: list, visit: int, now: int):
    global n, w, ans
    # 모든 점을 방문 했을 때
    if visit == ((1 << n) - 1):
        weight = dp[now][-1] + w[now][0]
        if weight < ans:
            ans = weight
        return
    # 방문하지 않은 점을 찾아서 방문
    for i in range(1, n):
        if not (visit & (1 << i)):
            visit2 = visit | (1 << i)
            dp[i][visit2] = min(dp[i][visit2], dp[now][visit] + w[now][i])
            TSP(dp, visit2, i)

n = int(input())
INF = int(1e10)
w = [list(map(int, input().split())) for _ in range(n)]
dp = [[INF] * (1 << n) for _ in range(n)]
dp[0][1] = 0
ans = INF
TSP(dp, 1, 0)
print(ans)
'''