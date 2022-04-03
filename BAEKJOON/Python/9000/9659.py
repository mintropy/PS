"""
Title : 돌 게임 5
Link : https://www.acmicpc.net/problem/9659
"""

import sys
input = sys.stdin.readline


N = int(input())
if N % 2:
    print('SK')
else:
    print('CY')
