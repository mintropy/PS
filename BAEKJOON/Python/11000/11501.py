"""
Title : 주식
Link : https://www.acmicpc.net/problem/11501
"""

import sys
input = sys.stdin.readline


for _ in range(int(input())):
    input()
    prices = list(map(int, input().split()))
    price_now = prices.pop()
    total = 0
    while prices:
        if price_now > prices[-1]:
            total += price_now - prices.pop()
        else:
            price_now = prices.pop()
    print(total)
