"""
Title : 스티커 정리 1
Link : https://www.acmicpc.net/problem/1101
"""

import sys, collections
input = sys.stdin.readline

n, m = map(int, input().split())

stickers = collections.defaultdict(list)
for _ in range(n):
    s, b = map(int, input().split())
    stickers[s].append(b)