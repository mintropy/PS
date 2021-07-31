"""
Title : 카드 놓기
Link : https://www.acmicpc.net/problem/18115
"""

import sys, collections
input = sys.stdin.readline

n = int(input())
cmd = list(map(int, input().split()))

# 가장 왼쪽이 위로
card_init = collections.deque([])

# 카드를 바닥에 놓은 작업 거꾸로 진행
for i in range(1, n + 1):
    c = cmd[-i]
    if c == 1:
        card_init.appendleft(i)
    elif c == 2:
        card_init.rotate(-1)
        card_init.appendleft(i)
        card_init.rotate(1)
    else:
        card_init.append(i)

print(*card_init)