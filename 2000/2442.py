"""
Title : 2*n 타일링 2
Link : https://www.acmicpc.net/problem/2442
"""

import sys

input = sys.stdin.readline

n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))