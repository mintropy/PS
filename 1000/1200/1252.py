"""
Title : 이진수 덧셈
Link : https://www.acmicpc.net/problem/1252
"""

import sys
input = sys.stdin.readline

a, b = map(str, input().split())

a2 = int(a, 2)
b2 = int(b, 2)
result = bin(a2 + b2)
print(str(result)[2:])