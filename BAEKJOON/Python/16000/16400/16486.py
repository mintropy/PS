"""
Title : 운동장 한 바퀴
Link : https://www.acmicpc.net/problem/16486
"""

import sys

input = sys.stdin.readline

d1 = int(input())
d2 = int(input())

ans = (d1 * 2) + (2 * 3.141592 * d2)
print(ans)