"""
Title : 도전 숫자왕
Link : https://www.acmicpc.net/problem/23057
"""

import sys
input = sys.stdin.readline

n = int(input())
cards = sorted(list(map(int, input().split())))

perfix = cards[::]
for i in range(n - 1):
    perfix[i + 1] += perfix[i]

m = perfix[-1]