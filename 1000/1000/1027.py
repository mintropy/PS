"""
Title : 고층 건물
Link : https://www.acmicpc.net/problem/1027
"""

# 기울기를 나누어서 구하는 것 보다, 곱하는 방식으로 계산하자
# 나누어서 계산하면 부동소수점 문제로, 정확한 값을 찾기 힘들다

import sys

input = sys.stdin.readline

n = int(input())
buildings = list(map(int ,input().split()))

max_count = 0

for i in range(n):
    height = buildings[i]
    # 왼쪽으로 확인
