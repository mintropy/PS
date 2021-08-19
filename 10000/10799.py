"""
Title : 쇠막대기
Link : https://www.acmicpc.net/problem/10799
"""

import sys
input = sys.stdin.readline


blueprint = input().strip()

iron_stick = 0
laser_count = 0
stick_start = 0
# 다른 레이저에 의해 한 번 잘렸던 쇠막대기
# 레이저 나올 때, 닫는 괄호에서 확인해야 함
stick_cut = 0
idx = 0
while idx < len(blueprint):
    # 레이저 발견
    if idx < len(blueprint) - 1 and blueprint[idx:idx+2] == '()':
        laser_count = 1
        if stick_start:
            iron_stick += stick_start - stick_cut
            stick_cut = 0
        idx += 1
    # 열는 괄호
    elif blueprint[idx] == '(':
        stick_start += 1
        if stick_start == 1:
            stick_cut = 0
    # 닫는 괄호 : 레이저 초기화 / 막대 추가
    elif blueprint[idx] == ')':
        if laser_count:
            iron_stick += stick_start
            laser_count = 0
            stick_cut = stick_start - 1
        else:
            stick_cut -= 1
        stick_start -= 1
    idx += 1

print(iron_stick)
