"""
Title : 물약
Link : https://www.acmicpc.net/problem/1050
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ingredient = {}
potion = {}

for _ in range(n):
    ing, cost = input().strip().split()
    ingredient[ing] = int(cost)

for _ in range(m):
    p, eq = input().strip().split('=')
    if p in potion:
        potion[p].append(eq)
    else:
        potion[p] = [eq]

# 각 재료를 먼저 계산
for ing in ingredient:
    for p in potion:
        for i in range(len(potion[p])):
            poly = potion[p][i]
            if ing in poly:
                potion[p][i] = poly.replace(ing, f'*{ingredient[ing]}')


tmp_potion = {}
love_cost = []
if 'LOVE' in ingredient:
    love_cost.append(ingredient['LOVE'])

if 'LOVE' in potion:
    love_poly = potion['LOVE']
    potion.pop('LOVE')

while potion:
    # 각 포션 가격을 계산 가능한지
    potion_keys = list(potion.keys())
    for p in potion_keys:
        eq_not_eval = []
        for poly in potion[p]:
            try:
                c = eval(poly)
                if p in tmp_potion:
                    tmp_potion[p].append(c)
                else:
                    tmp_potion[p] = [c]
            except:
                if p != 'LOVE':
                    eq_not_eval.append(poly)
        # 연산되지 않은 식 처리
        if not eq_not_eval:
            potion.pop(p)
        else:
            potion[p] = eq_not_eval
    
    # 가격 변화가 더 있는지
    calc = False
    for tp in tmp_potion:
        tp_value = min(tmp_potion[tp])
        for p in potion:
            for i in range(len(potion[p])):
                poly = potion[p][i]
                if tp in poly:
                    potion[p][i] = poly.replace(tp, f'*{tp_value}')
                    calc = True
    # 계산된 LOVE가 있는지
    if 'LOVE' in tmp_potion:
        love_cost.append(min(tmp_potion['LOVE']))
    # 추가적 연산이 필요없는 경우
    if not tmp_potion or not calc:
        break

# 출력
if not love_cost:
    print(-1)
else:
    min_cost = min(love_cost)
    if min_cost > 1000000000:
        print(1000000001)
    else:
        print(min_cost)
