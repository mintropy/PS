"""
Title : 카드2
Link : https://www.acmicpc.net/problem/2164
"""

import sys, collections
input = sys.stdin.readline

n = int(input())
# 가장 왼쪽이 젤 위로 가정
cards = collections.deque([i for i in range(1, n + 1)])

while True:
    if len(cards) == 1:
        break
    cards.popleft()
    l = cards.popleft()
    cards.append(l)

print(cards.pop())