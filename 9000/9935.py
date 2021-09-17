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

# 문자열 길이
l = len(string)
# 폭발 문자열 길이
l_d = len(explode)
# 지금 추적하고 있는 문자열 인덱스
idx = 0
# 폭발 문자열이 의심될 때, 추적하는 인덱스
danger_idx = 0
# 지난 문자열 확인할 때
check = 0

while idx < l:
    s = string[idx]
    # 폭발 문자열인지 확인
    if danger_idx:
        # 폭발 문자열
        if danger_idx == l_d:
            danger = []
            # 이전에 지나친 폭발 문자열 있는지 확인
            while last_st:
                last_idx = last_st[-1]
                idx_now = 0
                # 위 인덱스부터 stack마지막까지 가능한지 확인
                for _ in range(last_idx, len(stack)):
                    if stack[last_idx + idx_now] != explode[idx_now]:
                        break
                    idx_now += 1
                # stack마지막까지 확인했으면 
                # 추가적으로 문자열 돌면서 확인
                # 더 확인해야할 문자열 길이
                check_len = l_d - idx_now - 1
                if idx + check_len > l_d:
                    break
                for _ in range(check_len):
                    if stack[last_idx + idx_now] != explode[idx_now]:
                        break
                    idx_now += 1
                # 모든 과정을 통과했으면 폭발 문자열
                # stack의 last_idx까지 pop
                while len(stack) > last_idx:
                    stack.pop()
        # 계속 폭발 문자열이 이어지는지
        elif explode[danger_idx] == s:
            danger_idx += 1
            danger.append(s)
        # 폭발 문자열이 아니게 되면
        else:
            danger_idx = 0
            stack += danger
            danger = []
    else:
        # 새로운 폭발 문자열이 시작되면
        if explode[danger_idx] == s:
            last_st.append(len(stack) - 1)
            danger_idx += 1
            danger.append(s)
        else:
            stack.append(s)
    idx += 1

if stack:
    print(*stack, sep='')
else:
    print('FRULA')
