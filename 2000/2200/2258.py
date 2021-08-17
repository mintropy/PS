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


# 불가능한 경우 == 전체 무게가 원하는 무게보다 낮음
if total_weight < m:
    print(-1)
# 가능한 경우 >> 탐색
else:
    # 최저 금액
    min_cost = 3 * 10 ** 8
    
    while meat:
        _, p, w = heapq.heappop(meat)
        # 종료조건 : 남은 전체 무게가 필요 무게보다 낮을 때
        if total_weight < m:
            break
        # p금액의 모든 고기 무게
        weights = [w]
        # p금액 모든 고기 무게 합
        weights_same_price = w
        while True:
            if meat and meat[0][1] == p:
                _, p, w = heapq.heappop(meat)
                weights.append(w)
                weights_same_price += w
            else:
                break
        
        # 전체 무게에서 지금 가격 전체 무게 뺐을때
        # m을 넘어가는 경우과, 넘지않는 경우로 구분
        # 전체 무게를 빼도 가능하면, 해당 무게 고기 하나만 사도 가능
        if total_weight - weights_same_price >= m:
            # 해당 가격으로 최소가격 저장
            if p < min_cost:
                min_cost = p
        # 만약 불가능하면, p가격 고기 일부만 구매해서 가능한 경우
        else:
            # p가격에서 필요한 무게
            weight_diff = m - (total_weight - weights_same_price)
            # 해당 무게로 필요한 개수를 확인
            # 같은 무게 고기 내림차순 정렬하여 확인
            # 무거운거부터 담아서 최대한 적게 구매하도록
            weights.sort(reverse= True)
            weights_now = 0
            meat_count = 0
            for w in weights:
                weights_now += w
                meat_count += 1
                if weights_now >= weight_diff:
                    break
            # 가격 확인, 최신화
            cost_now = p * meat_count
            if cost_now < min_cost:
                min_cost = cost_now
        # 무게 최신화
        total_weight -= weights_same_price
    print(min_cost)



'''
Counter Example
10 10
2 3
2 4
2 5
3 1
1 3
7 9
7 3
8 4
10 3
3 10
ans : 3
output : 4

'''