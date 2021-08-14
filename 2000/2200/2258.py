"""
Title : 정육점
Link : https://www.acmicpc.net/problem/2258
"""

import sys, heapq
input = sys.stdin.readline


n, m = map(int, input().split())
meat = []
total_weight = 0
for _ in range(n):
    w, p = map(int, input().split())
    total_weight += w
    meat.append((-p, p, w))

heapq.heapify(meat)

min_cost = 3 * 10 ** 8

while meat:
    _, p, w = heapq.heappop(meat)
    # 종료조건
    if p > min_cost:
        break
    if total_weight < m:
        break
    weights = [w]
    weights_same_price = w
    while True:
        if not meat and meat[0][1] == p:
            weights.append(w)
            weights_same_price += w
        else:
            break
    
    # 전체 무게에서 지금 가격 전체 무게 뺐을때
    # m을 넘어가는 경우과, 넘지않는 경우로 구분
    if total_weight - weights_same_price >= m:
        # 해당 가격으로 최소가격 저장
        min_cost = p
    else:
        # 해당 가격 일부만 구매해서 원하는 무게를 넘는 수 찾기
        weight_diff = total_weight - m
        # 해당 무게로 필요한 개수
        meat_count = weight_diff // w + 1
        p2 = p * meat_count
        # 가격 확인
        if p2 < min_cost:
            min_cost = p2
    # 무게 최신화
    total_weight -= weights_same_price

if min_cost == 3 * 10 ** 8:
    print(-1)
else:
    print(min_cost)
