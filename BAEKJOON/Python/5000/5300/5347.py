"""
Title : LCM
Link : https://www.acmicpc.net/problem/5347
"""

import math
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(math.lcm(a, b))
