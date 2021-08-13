"""
Title : 정육점
Link : https://www.acmicpc.net/problem/2258
"""

import sys, heapq
input = sys.stdin.readline


def check(p_before, p_after, total_weight, weights, new_weight):
    global m
    if total_weight + sum(weights) < m:
        return False

    pass



n, m = map(int, input().split())
meat = []
for _ in range(n):
    w, p = map(int, input().split())
    meat.append((p, w))

heapq.heapify(meat)

total_weight = 0
weights = []
price_now = 0
prob = [0, 0]

for _ in range(n):
    p, w = heapq.heappop(meat)
    # 가격이 달라지면, 다시 계산 시작
    if p == price_now:
        weights.append(total_weight)
    else:
        pass
    total_weight += w
    if total_weight >= m:
        print(p)
        break
else:
    print(-1)
