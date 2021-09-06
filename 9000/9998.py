"""
Title : 블록 쌓기
Link : https://www.acmicpc.net/problem/9998
"""

import sys
input = sys.stdin.readline

n = int(input())
yoon = list(map(int, input().split()))
dong = list(map(int, input().split()))

left, right = yoon[n // 2], dong[n // 2]
if left > right:
    left, right = right, left






'''
Counter Example
5
3 2 5 2 3
3 2 4 2 3
ans : 7

'''