"""
Title: 동혁 피자
Link : https://www.acmicpc.net/problem/6502
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


tc = 1
while True:
    pizza = tuple(MIIS())
    if len(pizza) == 1:
        break
    r, w, l = pizza
    
    if (w / 2) ** 2 + (l / 2) ** 2 <= r ** 2:
        print(f'Pizza {tc} fits on the table.')
    else:
        print(f'Pizza {tc} does not fit on the table.')
    tc += 1
