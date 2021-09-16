"""
Title : 문자열 폭발
Link : https://www.acmicpc.net/problem/9935
"""

import sys
input = sys.stdin.readline

string = input().strip()
explode = input().strip()

# 출력이 담기는 리스트
stack = []
# 폭발 가능성이 있는 문자열
danger = []
# 폭발 문자열의 시작 문자열이 있다면, 해당 인덱스
last_st = []

# 폭발 문자열 길이
l = len(explode)
# 폭발 문자열이 의심될 때, 추적하는 인덱스
idx = 0
# 지난 문자열 확인할 때
check = 0

for s in string:
    # 폭발 문자열인지 확인
    if idx:
        # 폭발 문자열
        if idx == l:
            # 이전에 지나친 폭발 문자열 있는지 확인
            pass
        # 계속 폭발 문자열이 이어지는지
        elif explode[idx] == s:
            idx += 1
            danger.append(s)
        # 폭발 문자열이 아니게 되면
        else:
            idx = 0
            stack += danger
            danger = []
    else:
        # 새로운 폭발 문자열이 시작되면
        if explode[idx] == s:
            last_st.append(len(stack) - 1)
            idx += 1
            danger.append(s)
        else:
            stack.append(s)

if stack:
    print(*stack, sep='')
else:
    print('FRULA')
