"""
Title : 공주님의 정원
Link : https://www.acmicpc.net/problem/2457
"""

import sys
input = sys.stdin.readline


def check(m1, d1, m2, d2):
    # 비교 기준으로 할 날짜 m1, d1
    # 가능한지 확인할 날짜 m2, d2
    # m1, d1이 더 빠르거나 같은지 확인
    # 가능한 경우만 고르고, 아니면 False
    if m1 < m2:
        return True
    elif m1 == m2 and d1 <= d2:
        return True
    return False



n = int(input())
flowers = [tuple(map(int, input().split())) for _ in range(n)]

flowers.sort(key = lambda x:(-x[2], -x[3], x[0], x[1]))

# 가장 늦게 지는 꽃이 11월 30일까지 펴있는지 확인
if flowers[0][2] <= 11:
    print(0)
# 꽃을 모두 꺼내며 확인
else:
    flower_count = 1
    m1, d1, m2, d2 = flowers[0]
    # 마지막에 지는 꽃이 피는 날짜
    blossom = [m1, d1]
    # 그 전에 선택할 꽃 예비 명단
    prob = []
    for i in range(1, n):
        # 12월에 지는 꽃일때 확인 필요
        
        m1, d1, m2, d2 = flowers[i]
        # 만약 예비꽃이 3월 1일 이전에 핀다면 종료
        if prob and check(*prob, 3, 1):
            print(flower_count + 1)
            break
        # 해당 꽃이 가능하면 예비명단과 비교 최신화
        if check(*blossom, m2, d2):
            if not prob:
                prob = [m1, d1]
            # 예비 명단의 꽃보다 더 빨피 피는지 확인
            elif check(m1, d1, *prob):
                prob = [m1, d1]
            else:
                continue
        # 불가능하면, 예비명단 꽃을 최신꽃으로
        else:
            flower_count += 1
            blossom = prob
            # 바뀐 꽃과 비교해서 가능한지 다시 확인
            if check(*blossom, m2, d2):
                prob = [m1, d1]
            else:
                print(0)
                break
    else:
        # 모든 꽃을 확인한 경우, 예비꽃을 확인
        if check(*prob, 3, 1):
            print(flower_count + 1)
        else:
            print(0)
