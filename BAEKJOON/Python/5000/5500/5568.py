'''
Title : 카드 놓기
Link : https://www.acmicpc.net/problem/5568
'''

import sys, itertools

input = sys.stdin.readline

n = int(input())
k = int(input())
cards = [str(input().strip()) for _ in range(n)]
per = list(itertools.permutations(cards, k))

num = set()
for card in per:
    n = ''
    for c in card:
        n += c
    num.add(n)
print(len(num))